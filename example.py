# import texfig first to configure Matplotlib's backend
import texfig
# then, import PyPlot
import matplotlib.pyplot as plt

# obtain a nicely configured figure from texfig (or make your own)
fig = texfig.figure()
# plot as usual
plt.title(r'Title with $\vect{x}$')
plt.plot(range(10))
# save your plot as both a PDF and a PGF file with texfig (or save a '.pfg' file on your own)
texfig.savefig("example_plot")
# Now \usepackage{pgf} and \input the .pgf file in your LaTeX document. Admire the beauty of LaTeX vector plots.
