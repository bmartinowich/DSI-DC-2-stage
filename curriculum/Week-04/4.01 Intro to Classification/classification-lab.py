# read the iris data into a DataFrame
import pandas as pd
url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
col_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
iris = pd.read_csv(url, header=None, names=col_names)

iris.head()

# allow plots to appear in the notebook
%matplotlib inline
import matplotlib.pyplot as plt

# increase default figure and font sizes for easier viewing
plt.rcParams['figure.figsize'] = (6, 4)
plt.rcParams['font.size'] = 14

# create a custom colormap
from matplotlib.colors import ListedColormap
cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

# map each iris species to a number
# let's use Iris-setosa':0, 'Iris-versicolor':1, 'Iris-virginica':2 and create a column caled 'species_num'

# create a scatter plot of PETAL LENGTH versus PETAL WIDTH and color by SPECIES

# create a scatter plot of SEPAL LENGTH versus SEPAL WIDTH and color by SPECIES


'''
KNN Modeling
'''

# store feature matrix in "X"

# store response vector in "y"

# Make use of train, test, split

# import KNN from SKLearn, instatiate a model with one neighbor

# check the accuracy

# create a model with 5 neighbors. Did it improve?

# bonus: create a looped function that will check all levels of various neighbors. Implement it.

# also bonus: according to SKLearn documentation, what is 'knn.predict_proba(X_new)' going to do?
