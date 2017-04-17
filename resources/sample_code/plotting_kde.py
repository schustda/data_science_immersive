def plot_kde(df, col):
    """Fit a Gaussian KDE to input data, plot fit over histogram of the data.
    Parameters
    ----------
    df: Pandas DataFrame
    col: str
        Column from df with numeric data to be plotted
    Returns
    -------
    ax: Matplotlib axis object
    """
    ax = plot_hist_basic(df, col)
    data = df[col]
    density = stats.kde.gaussian_kde(data)
    x_vals = np.linspace(data.min(), data.max(), 100)
    kde_vals = density(x_vals)

    ax.plot(x_vals, kde_vals, 'b-')

    return ax
