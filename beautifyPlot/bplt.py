import matplotlib.pyplot as plt
def beautifyPlot(kwargs):
    '''
    Run at end of matplotlib plotting routine.
    '''
    pltFunctions = {
        "acorr":plt.acorr, 
        "angle_spectrum":plt.angle_spectrum, 
        "annotate":plt.annotate, 
        "arrow":plt.arrow, 
        "autoscale":plt.autoscale, 
        "autumn":plt.autumn, 
        "axes":plt.axes, 
        "axhline":plt.axhline, 
        "axhspan":plt.axhspan, 
        "axis":plt.axis, 
        "axline":plt.axline, 
        "axvline":plt.axvline, 
        "axvspan":plt.axvspan, 
        "bar":plt.bar, 
        "bar_label":plt.bar_label, 
        "barbs":plt.barbs, 
        "barh":plt.barh, 
        "bone":plt.bone, 
        "box":plt.box, 
        "boxplot":plt.boxplot, 
        "broken_barh":plt.broken_barh, 
        "cbook":plt.cbook, 
        "cla":plt.cla, 
        "clabel":plt.clabel, 
        "clf":plt.clf, 
        "clim":plt.clim, 
        "close":plt.close, 
        "cm":plt.cm, 
        "cohere":plt.cohere, 
        "color_sequences":plt.color_sequences, 
        "colorbar":plt.colorbar, 
        "colormaps":plt.colormaps, 
        "connect":plt.connect, 
        "contour":plt.contour, 
        "contourf":plt.contourf, 
        "cool":plt.cool, 
        "copper":plt.copper, 
        "csd":plt.csd, 
        "cycler":plt.cycler, 
        "delaxes":plt.delaxes, 
        "disconnect":plt.disconnect, 
        "draw":plt.draw, 
        "draw_all":plt.draw_all, 
        "draw_if_interactive":plt.draw_if_interactive, 
        "errorbar":plt.errorbar, 
        "eventplot":plt.eventplot, 
        "figaspect":plt.figaspect, 
        "figimage":plt.figimage, 
        "figlegend":plt.figlegend, 
        "fignum_exists":plt.fignum_exists, 
        "figtext":plt.figtext, 
        "figure":plt.figure, 
        "fill":plt.fill, 
        "fill_between":plt.fill_between, 
        "fill_betweenx":plt.fill_betweenx, 
        "findobj":plt.findobj, 
        "flag":plt.flag, 
        "functools":plt.functools, 
        "gca":plt.gca, 
        "gcf":plt.gcf, 
        "gci":plt.gci, 
        "get":plt.get, 
        "get_backend":plt.get_backend, 
        "get_cmap":plt.get_cmap, 
        "get_current_fig_manager":plt.get_current_fig_manager, 
        "get_figlabels":plt.get_figlabels, 
        "get_fignums":plt.get_fignums, 
        "get_plot_commands":plt.get_plot_commands, 
        "get_scale_names":plt.get_scale_names, 
        "getp":plt.getp, 
        "ginput":plt.ginput, 
        "gray":plt.gray, 
        "grid":plt.grid, 
        "hexbin":plt.hexbin, 
        "hist":plt.hist, 
        "hist2d":plt.hist2d, 
        "hlines":plt.hlines, 
        "hot":plt.hot, 
        "hsv":plt.hsv, 
        "importlib":plt.importlib, 
        "imread":plt.imread, 
        "imsave":plt.imsave, 
        "imshow":plt.imshow, 
        "inferno":plt.inferno, 
        "inspect":plt.inspect, 
        "install_repl_displayhook":plt.install_repl_displayhook, 
        "interactive":plt.interactive, 
        "ioff":plt.ioff, 
        "ion":plt.ion, 
        "isinteractive":plt.isinteractive, 
        "jet":plt.jet, 
        "legend":plt.legend, 
        "locator_params":plt.locator_params, 
        "logging":plt.logging, 
        "loglog":plt.loglog, 
        "magma":plt.magma, 
        "magnitude_spectrum":plt.magnitude_spectrum, 
        "margins":plt.margins, 
        "matplotlib":plt.matplotlib, 
        "matshow":plt.matshow, 
        "minorticks_off":plt.minorticks_off, 
        "minorticks_on":plt.minorticks_on, 
        "mlab":plt.mlab, 
        "new_figure_manager":plt.new_figure_manager, 
        "nipy_spectral":plt.nipy_spectral, 
        "np":plt.np, 
        "pause":plt.pause, 
        "pcolor":plt.pcolor, 
        "pcolormesh":plt.pcolormesh, 
        "phase_spectrum":plt.phase_spectrum, 
        "pie":plt.pie, 
        "pink":plt.pink, 
        "plasma":plt.plasma, 
        "plot":plt.plot, 
        "plot_date":plt.plot_date, 
        "polar":plt.polar, 
        "prism":plt.prism, 
        "psd":plt.psd, 
        "quiver":plt.quiver, 
        "quiverkey":plt.quiverkey, 
        "rc":plt.rc, 
        "rcParams":plt.rcParams, 
        "rcParamsDefault":plt.rcParamsDefault, 
        "rcParamsOrig":plt.rcParamsOrig, 
        "rc_context":plt.rc_context, 
        "rcdefaults":plt.rcdefaults, 
        "rcsetup":plt.rcsetup, 
        "re":plt.re, 
        "register_cmap":plt.register_cmap, 
        "rgrids":plt.rgrids, 
        "savefig":plt.savefig, 
        "sca":plt.sca, 
        "scatter":plt.scatter, 
        "sci":plt.sci, 
        "semilogx":plt.semilogx, 
        "semilogy":plt.semilogy, 
        "set_cmap":plt.set_cmap, 
        "set_loglevel":plt.set_loglevel, 
        "setp":plt.setp, 
        "show":plt.show, 
        "specgram":plt.specgram, 
        "spring":plt.spring, 
        "spy":plt.spy, 
        "stackplot":plt.stackplot, 
        "stairs":plt.stairs, 
        "stem":plt.stem, 
        "step":plt.step, 
        "streamplot":plt.streamplot, 
        "style":plt.style, 
        "subplot":plt.subplot, 
        "subplot2grid":plt.subplot2grid, 
        "subplot_mosaic":plt.subplot_mosaic, 
        "subplot_tool":plt.subplot_tool, 
        "subplots":plt.subplots, 
        "subplots_adjust":plt.subplots_adjust, 
        "summer":plt.summer, 
        "suptitle":plt.suptitle, 
        "switch_backend":plt.switch_backend, 
        "sys":plt.sys, 
        "table":plt.table, 
        "text":plt.text, 
        "thetagrids":plt.thetagrids, 
        "threading":plt.threading, 
        "tick_params":plt.tick_params, 
        "ticklabel_format":plt.ticklabel_format, 
        "tight_layout":plt.tight_layout, 
        "time":plt.time, 
        "title":plt.title, 
        "tricontour":plt.tricontour, 
        "tricontourf":plt.tricontourf, 
        "tripcolor":plt.tripcolor, 
        "triplot":plt.triplot, 
        "twinx":plt.twinx, 
        "twiny":plt.twiny, 
        "uninstall_repl_displayhook":plt.uninstall_repl_displayhook, 
        "violinplot":plt.violinplot, 
        "viridis":plt.viridis, 
        "vlines":plt.vlines, 
        "waitforbuttonpress":plt.waitforbuttonpress, 
        "winter":plt.winter, 
        "xcorr":plt.xcorr, 
        "xkcd":plt.xkcd, 
        "xlabel":plt.xlabel, 
        "xlim":plt.xlim, 
        "xscale":plt.xscale, 
        "xticks":plt.xticks, 
        "ylabel":plt.ylabel, 
        "ylim":plt.ylim, 
        "yscale":plt.yscale, 
        "yticks":plt.yticks, 
    }

    for key, arguments in kwargs.items():
        function = pltFunctions.get(key, False)
        if function:
            if(isinstance(arguments,dict)):
                function(**arguments)
                
            if(isinstance(arguments,list)):
                function(*arguments)
        else:
            print(f"Function {key} is not supported!")
