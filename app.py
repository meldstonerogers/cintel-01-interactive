import matplotlib.pyplot as plt
import numpy as np
from shiny.express import ui, input, render
import shinyswatch
from shinyswatch import theme


# Add page title
ui.page_opts(
    title="Plotting with PyShiny", theme=shinyswatch.theme.minty, fillable=True
)

# Create sidebar with slider input
with ui.sidebar():
    ui.input_slider("selected_number_of_bins", "Number of Bins", 0, 100, 20)


# Create histogram
@render.plot(alt="A histogram")
def histogram():
    np.random.seed(19680801)
    x = 100 + 15 * np.random.randn(437)
    plt.hist(
        x,
        input.selected_number_of_bins(),
        color="#CBC3E3",
        density=True,
        edgecolor="#98FF98",
    )
