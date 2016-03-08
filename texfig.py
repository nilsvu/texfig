"""
Utility to generate PGF vector files from Python's Matplotlib plots to use in LaTeX documents.

Read more at https://github.com/knly/texfig
"""

import matplotlib as mpl
mpl.use('pgf')

from math import sqrt
default_width = 5.78853 # in inches
default_ratio = (sqrt(5.0) - 1.0) / 2.0 # golden mean
 
mpl.rcParams.update({
    "text.usetex": True,
    "pgf.texsystem": "xelatex",
    "pgf.rcfonts": False,
    "font.family": "serif",
    "font.serif": [],
    "font.sans-serif": [],
    "font.monospace": [],
    "figure.figsize": [default_width, default_width * default_ratio],
    "pgf.preamble": [
        # put LaTeX preamble declarations here
        r"\usepackage[utf8x]{inputenc}",
        r"\usepackage[T1]{fontenc}",
        # macros defined here will be available in plots, e.g.:
        # r"\newcommand{\vect}[1]{#1}",
        # You can use dummy implementations, since you LaTeX document
        # will render these properly, anyway.
    ],
})

import matplotlib.pyplot as plt


"""
Returns a figure with an appropriate size and tight layout.
"""
def figure(width=default_width, ratio=default_ratio, pad=0, *args, **kwargs):
    fig = plt.figure(figsize=(width, width * ratio), *args, **kwargs)
    fig.set_tight_layout({
        'pad': pad
    })
    return fig


"""
Returns subplots with an appropriate figure size and tight layout.
"""
def subplots(width=default_width, ratio=default_ratio, *args, **kwargs):
    fig, axes = plt.subplots(figsize=(width, width * ratio), *args, **kwargs)
    fig.set_tight_layout({
        'pad': 0
    })
    return fig, axes


"""
Save both a PDF and a PGF file with the given filename.
"""
def savefig(filename, *args, **kwargs):
    plt.savefig(filename + '.pdf', *args, **kwargs)
    plt.savefig(filename + '.pgf', *args, **kwargs)
