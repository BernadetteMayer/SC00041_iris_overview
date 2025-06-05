# python read iris dataset and do stuff
# import seaborn package 
import seaborn as sns

# load the iris dataset
iris = sns.load_dataset("iris")

# TODO: Import datetime and create timestamp for plot file

g = sns.PairGrid(iris, hue="species")
g.map_diag(sns.histplot)
g.map_offdiag(sns.scatterplot)
g.add_legend()

# save plot
g.figure.savefig("../output/output_250530_12.53.png")
