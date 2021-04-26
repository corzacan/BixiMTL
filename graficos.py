import matplotlib.pyplot as plt


def histograma(dfDuration, ptitle, pxlbl, pylbl):
    plt.hist(dfDuration, bins=50)
    #plt.title(ptitle)
    plt.get_current_fig_manager().set_window_title(ptitle)
    plt.xlabel(pxlbl)
    plt.ylabel(pylbl)
    plt.show()

