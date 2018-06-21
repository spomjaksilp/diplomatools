# -*- coding: utf-8 -*-
import os

import matplotlib as mpl
# mpl.verbose.level = 'debug-annoying'
# mpl.use("Qt5Agg")
# mpl.use("pgf")
from matplotlib.backends.backend_pgf import FigureCanvasPgf
import matplotlib.pyplot as plt

# use pgf for creating pdf
mpl.backend_bases.register_backend('pdf', FigureCanvasPgf)

# axiomatic definitions
# Convert pt to inch
inches_per_pt = 1.0/72.27 
inch_per_cm = 0.393700787

# get these values from latex document using "\the\textwidth" and "\the\columnwidth"
textwidth_pt_default = 510
textwidth_cm_default = textwidth_pt_default*inches_per_pt/inch_per_cm

columnwidth_pt_default = 246
columnwidth_cm_default = columnwidth_pt_default*inches_per_pt/inch_per_cm

textwidth_pt_thesis = 455.24417
textwidth_cm_thesis = textwidth_pt_thesis*inches_per_pt/inch_per_cm


plotwidth_thesis_full = textwidth_cm_thesis*.8
plotwidth_thesis_half = textwidth_cm_thesis*.49

golden_mean = (5**.5-1.0)/2.0

fonts = {
    "latin":
        {
            "fontsSerif":   ["Latin Modern Math", ],
            "fontsSans":    ["Latin Modern Sans", ],
        },
    "tufonts":
        {
            "fontsSerif":   ["PT Serif", ],
            "fontsSans":    ["PT Sans", ],
        },
    "xkcd":
        {
            "fontsSerif":   ["xkcd Script", ],
            "fontsSans":    ["xkcd Script", ],
        },
}


# font and size functions
def setFigSize(textwidth_cm, aspect=golden_mean, title=False):
    # update mpl defauls
    fig_width = textwidth_cm * inch_per_cm
    fig_height = fig_width * aspect
    params_resize = {
                     'figure.figsize': (fig_width, fig_height),
                     'figure.subplot.left': 0.175,
                     'figure.subplot.bottom': 0.2,
                     'figure.subplot.right': 0.95,
                     'figure.subplot.top': 0.95
                     }
    if title:
        params_resize['figure.subplot.top'] = 0.88
    plt.rcParams.update(params_resize)
    
def setFigSizePt(textwidth_pt, aspect=golden_mean, title=False):
    setFigSize(textwidth_pt*inches_per_pt/inch_per_cm, aspect=aspect, title=title)

def setFont(size=12., scale=10/12., sans=False, style="latin"):
    fontsSerif = fonts[style]["fontsSerif"]
    fontsSans = fonts[style]["fontsSans"]

    # size
    params_text = {
                   'axes.labelsize': size,
                   'font.size': size*scale,
                   'legend.fontsize': size*scale,
                   'xtick.labelsize': size*scale,
                   'ytick.labelsize': size*scale,
                   'axes.titlesize': size,
                   }
    plt.rcParams.update(params_text)

    # font
    plt.rcParams["font.serif"] = fontsSerif
    plt.rcParams["font.sans-serif"] = fontsSans

    # pgf system for pdf generation
    pgf_with_pdflatex = {
        "pgf.texsystem": "lualatex",
        "pgf.preamble": [
            r"\usepackage{fontspec}",
            r"\usepackage{siunitx}",
            r"\sisetup{detect-all}",
            r"\usepackage{braket}",
            r"\DeclareSIUnit\BohrRadii{a_0}"
        ]
    }
    mpl.rcParams.update(pgf_with_pdflatex)

    # matplotlib tex system
    plt.rcParams["text.usetex"] = True
    plt.rcParams["text.latex.unicode"] = True
    plt.rcParams['text.latex.preamble'] = "\\usepackage{amsmath},\\usepackage{siunitx},\\sisetup{detect-all},\\usepackage{braket},\\DeclareSIUnit\\BohrRadii{a_0}"

    if sans:
        plt.rcParams["font.family"] = "sans-serif"

    else:
        plt.rcParams["font.family"] = "serif"


# color functions
# define costum colors
colorTUBlue = (0./255., 95./255., 140./255.)
colorTUBlue80 = (51./255., 127./255., 163./255.)
colorTUBlue60 = (102./255., 159./255., 186./255.)
colorTUBlue40 = (153./255., 191./255., 209./255.)
colorTUBlue20 = (204./255., 223./255., 232./255.)
colorTURed = (185./255., 40./255., 25./255.)
colorTURed80 = (199./255., 83./255., 71./255.)
colorTURed60 = (213./255., 126./255., 117./255.)
colorTURed40 = (227./255., 169./255., 163./255.)
colorTURed20 = (241./255., 212./255., 209./255.)
colorTUPurple = (126./255., 35./255., 89/255.)
colorTUColdGray = (130./255., 140./255., 150/255.)
colorTUWarmGray = (130./255., 125./255., 120/255.)
colorState = (0/255., 102/255., 153/255.)
colorPotential = (255./255., 165./255., 0./255.)

cdict1 = {'red': ((0.0, 0.0, 0.1),
                  (0.5, 0.0, 0.5),
                  (1.0, 1.0, 1.0)),

          'green': ((0.0, 0.0, 0.7),
                    (0.0, 0.3, 0.3),
                    (1.0, 0.4, 0.0)),

          'blue': ((0.0, 0.0, 1.0),
                   (0.5, 0.3, 0.0),
                   (1.0, 0.0, 0.0))
          }

plt.register_cmap(name='BlueRed', data=cdict1)

# define custom colormaps
def getColor(descr):
    if isinstance(descr,str):
        if descr in ["pot", "potential"]:
            return "orange"
        if descr in ["state", "wf", "wavefunction"]:
            return colorTUBlue
            #return plt.get_cmap("ocean")(.6)
        if descr in ["light"]:
            return colorTUPurple#"#9467bd"

def colorMapWizard(colorList,name):
    cdict = {'red':[], 'green':[], 'blue':[]}
    for i,c in enumerate(colorList):
        cdict['red'].append((i/(len(colorList)-1),c[0],c[0]))
        cdict['green'].append((i/(len(colorList)-1),c[1],c[1]))
        cdict['blue'].append((i/(len(colorList)-1),c[2],c[2]))
    plt.register_cmap(name=name, data=cdict)


# useful functions
def makeInset(ax,scale=0.7):
    for item in ([ax.title, ax.xaxis.label, ax.yaxis.label] +
             ax.get_xticklabels() + ax.get_yticklabels()):
        item.set_fontsize(item.get_fontsize()*scale)
        ax.xaxis.labelpad *= scale
        ax.yaxis.labelpad *= scale

def max_ticks(ax=None, nx=5, ny=None):
    ax = plt.gca() if ax is None else ax
    ax.xaxis.set_major_locator(mpl.ticker.MaxNLocator(nx))
    ax.yaxis.set_major_locator(mpl.ticker.MaxNLocator(nx if not ny else ny))

def set_locator_dx(dx, ax=None):
    ax = plt.gca() if ax is None else ax
    ax.xaxis.set_major_locator(mpl.ticker.MultipleLocator(dx))

def set_locator_dy(dy, ax=None):
    ax = plt.gca() if ax is None else ax
    ax.yaxis.set_major_locator(mpl.ticker.MultipleLocator(dy))

def savepdf(name=None, fig=None):
    import sys, os
    if fig is not None:
        assert name is not None, "if figure is given, name has to be given!"
    fname = "../img/%s.pdf" % (((os.path.basename(sys.argv[0])).split(".")[0]) if name is None else name)
    fname_pdf = fname if fname.lower().endswith(".pdf") else fname+".pdf"
    fname_eps = os.path.splitext(fname_pdf)[0]+".eps"
    if fig is None:
        plt.tight_layout(.5)
        # plt.tight_layout(.5)
        plt.savefig(fname_pdf)
    else:
        # fig.tight_layout(.5)  # does not work with fig bc of python bug
        fig.tight_layout(pad=1/2)
        fig.savefig(fname_pdf)
    #plt.savefig(fname_eps)
    #os.system("epstopdf '{0}' && rm '{0}'".format(fname_eps))


# now set things
setFigSize(plotwidth_thesis_full, golden_mean)
setFont()

params_lines = {
               "lines.markersize": 4
               }

plt.rcParams.update(params_lines)

params_legend = {
                 "legend.numpoints": 1,
                 "legend.fancybox":True
                 }

plt.rcParams.update(params_legend)

params_figure = {
                 "figure.dpi": 300,
                 "savefig.dpi": 300
                 }

plt.rcParams.update(params_figure)
