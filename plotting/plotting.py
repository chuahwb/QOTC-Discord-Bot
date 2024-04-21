import matplotlib.pyplot as plt
from io import BytesIO
import numpy as np
from scipy.stats import gaussian_kde


def plot_data(data, title, color):
    """
    Generates a histogram with a density plot and a vertical mean line for the given data.

    Args:
        data (dict): A dictionary with prices as keys and quantities as values.
        title (str): The title of the plot.
        color (str): The color for the histogram bars.

    Returns:
        BytesIO: An in-memory binary stream containing the plot image.
    """
    if not data:
        return None

    prices = np.array(list(data.keys()))
    quantities = np.array(list(data.values()))

    fig, ax = plt.subplots(figsize=(10, 5))

    # Create histogram
    hist, bins, _ = ax.hist(prices, weights=quantities, bins=len(
        prices), alpha=0.75, color=color, label='Histogram')

    # Calculate the density adjusted for the logarithmic scale
    density = gaussian_kde(prices, weights=quantities)
    xs = np.linspace(prices.min(), prices.max(), 200)
    density_values = density(xs) * sum(quantities) / \
        density.integrate_box_1d(prices.min(), prices.max())
    ax.plot(xs, density_values, 'r--', label='Density Curve')

    # Calculate and plot the mean price
    mean_price = np.average(prices, weights=quantities)
    ax.axvline(mean_price, color='k', linestyle='dashed',
               linewidth=1, label=f'Mean: {mean_price:.2f}')
    ax.text(mean_price, max(density_values),
            f'Mean: {mean_price:.2f}', fontsize=12, ha='right', va='top')

    # Set logarithmic scale and labels
    ax.set_yscale('log')
    ax.set_xlabel('Price ($)')
    ax.set_ylabel('Quantity (Log Scale)')
    ax.set_title(title)
    ax.legend()
    ax.grid(True)

    # Save the plot to a BytesIO buffer
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close(fig)
    return buf

