from project.algorithms.models import AlgorithmModel

## PREPROCESSING
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

## CLASSIFICATION
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

## REGRESSION
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor

## CLUSTERING
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import KMeans

## PLOTS
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import ListedColormap

## DATASETS
import os.path

my_path = os.path.abspath(os.path.dirname(__file__))
position_salaries = os.path.join(my_path, "../../static/datasets/Position_Salaries.csv")
social_network_ads = os.path.join(my_path, "../../static/datasets/Social_Network_Ads.csv")
mall_customers = os.path.join(my_path, "../../static/datasets/Mall_Customers.csv")


########################## ALGORITHM CHARACTERISTICS ###################################################################

def algorithm_characteristics(type):
    algorithm = AlgorithmModel.query.filter_by(algorithm_type=type).first()
    algorithm_preprocessors = algorithm.algorithm_preprocessors
    algorithm_preprocessors = algorithm_preprocessors.split(',')
    algorithm_issues = algorithm.algorithm_issues
    algorithm_issues = algorithm_issues.split(',')
    return (algorithm_preprocessors, algorithm_issues)


########################## REGRESSION ##################################################################################

def regression_dataset():
    dataset = pd.read_csv(position_salaries)
    X = dataset.iloc[:, 1:2].values
    y = dataset.iloc[:, 2:3].values
    describe = dataset.describe()
    rows = len(dataset.index)
    columns = len(dataset.columns)
    return (dataset, X, y, describe, rows, columns)


### ALGORTIHMS

def polynomial_regression(X, y):
    poly_reg = PolynomialFeatures(degree=4)
    X_poly = poly_reg.fit_transform(X)
    lin_reg = LinearRegression()
    lin_reg.fit(X_poly, y)
    X_grid = np.arange(min(X), max(X), 0.1)
    X_grid = X_grid.reshape(len(X_grid), 1)
    plot_prediction = lin_reg.predict(poly_reg.fit_transform(X_grid))
    single_prediction = lin_reg.predict(poly_reg.fit_transform(6.5))
    single_prediction = single_prediction.flat[0]
    single_prediction = ('%.2f' % (single_prediction,)).rstrip('0').rstrip('.')
    return (X_grid, plot_prediction, single_prediction)


def svr(X, y):
    sc_X = StandardScaler()
    X = sc_X.fit_transform(X)
    sc_y = StandardScaler()
    y = sc_y.fit_transform(y)
    regressor = SVR(kernel='rbf')  ## Kernel choice - linear, poly or gaussian(rbf)
    regressor.fit(X, y)
    X_grid = np.arange(min(X), max(X), 0.1)
    X_grid = X_grid.reshape(len(X_grid), 1)
    plot_prediction = regressor.predict(X_grid)
    single_prediction = sc_y.inverse_transform(
        regressor.predict(sc_X.transform(np.array([[6.5]]))))  ## transform value into array with numpy.array
    single_prediction = single_prediction.flat[0]
    single_prediction = ('%.2f' % (single_prediction,)).rstrip('0').rstrip('.')  ## for better display
    return (X_grid, plot_prediction, single_prediction)


def randomforest(X, y):
    regressor = RandomForestRegressor(n_estimators=600, random_state=0)
    regressor.fit(X, y)
    X_grid = np.arange(min(X), max(X), 0.01)  ## increase the resolution
    X_grid = X_grid.reshape((len(X_grid), 1))
    plot_prediction = regressor.predict(X_grid)
    single_prediction = regressor.predict(6.5)
    single_prediction = single_prediction.flat[0]
    single_prediction = ('%.2f' % (single_prediction,)).rstrip('0').rstrip('.')
    return (X_grid, plot_prediction, single_prediction)


### PLOT

def regression_plot(algorithm, X, y, X_grid, plot_prediction):
    figure = plt.figure()
    sns.set_style("darkgrid", {"axes.facecolor": ".9"})
    plt.scatter(X, y, color='red')
    plt.plot(X_grid, plot_prediction, color='darkblue')
    plt.ylim(ymin=0)
    plt.title('Salary Estimate - {}'.format(algorithm))
    plt.xlabel('Position Level')
    plt.ylabel('Salary', fontsize=12)
    plt.yticks(fontsize=10)
    figure.savefig('static/img/{}.svg'.format(algorithm))


########################## CLASSIFICATION ##############################################################################

def classification_dataset():
    dataset = pd.read_csv(social_network_ads)
    X = dataset.iloc[:, [2, 3]].values
    y = dataset.iloc[:, 4].values
    dataset_head = dataset.head(10)
    stats_data = dataset.iloc[:, 2:4]
    describe = stats_data.describe()
    rows = len(dataset.index)
    columns = len(dataset.columns)
    return (dataset, X, y, describe, rows, columns, dataset_head)


def classification_plot(algorithm, X_test, y_test, classifier):
    figure = plt.figure()

    X_set, y_set = X_test, y_test
    X1, X2 = np.meshgrid(np.arange(start=X_set[:, 0].min() - 1, stop=X_set[:, 0].max() + 1, step=0.01),
                         np.arange(start=X_set[:, 1].min() - 1, stop=X_set[:, 1].max() + 1, step=0.01))
    plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
                 alpha=0.85, cmap=ListedColormap(('darkred', 'darkgreen')))
    plt.xlim(X1.min(), X1.max())
    plt.ylim(X2.min(), X2.max())
    for i, j in enumerate(np.unique(y_set)):
        plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
                    c=ListedColormap(('red', 'green'))(i), label=j)
    plt.title('Test Set Results')
    plt.xlabel('Age')
    plt.ylabel('Estimated Salary')
    plt.legend()
    figure.savefig('static/img/{}.svg'.format(algorithm))


########################## CLUSTERING ##################################################################################


def clustering_dataset():
    dataset = pd.read_csv(mall_customers)
    X = dataset.iloc[:, [3, 4]].values
    dataset_head = dataset.head(10)
    stats_data = dataset.iloc[:, 2:5]
    describe = stats_data.describe()
    rows = len(dataset.index)
    columns = len(dataset.columns)
    return (dataset, X, describe, rows, columns, dataset_head)


def dendrogram_plot(algorithm, X):
    figure = plt.figure()
    sch.dendrogram(sch.linkage(X, method='ward'))
    sns.set_style("darkgrid", {"axes.facecolor": ".9"})
    plt.title("Dendrogram")
    plt.xlabel('Customers')
    plt.ylabel('Euclidean distances')
    figure.savefig('static/img/{}-determine.svg'.format(algorithm))


def elbow_plot(algorithm, wcss):
    figure = plt.figure()
    sns.set_style("darkgrid", {"axes.facecolor": ".9"})
    plt.plot(range(1, 11), wcss)
    plt.title('The Elbow Method')
    plt.xlabel('Number of clusters')
    plt.ylabel('WCSS')

    figure.savefig('static/img/{}-determine.svg'.format(algorithm))


def clustering_plot(algorithm, X, y_pred):
    figure = plt.figure()
    plt.scatter(X[y_pred == 0, 0], X[y_pred == 0, 1],
                ## specify that we want first cluster + first column vs second column for 'y'
                s=100, c='red', label='Savers')  ## size for datapoints/color
    plt.scatter(X[y_pred == 1, 0], X[y_pred == 1, 1], s=100, c='blue', label='Average')
    plt.scatter(X[y_pred == 2, 0], X[y_pred == 2, 1], s=100, c='green', label='Target Group')
    plt.scatter(X[y_pred == 3, 0], X[y_pred == 3, 1], s=100, c='orange', label='Overspenders')
    plt.scatter(X[y_pred == 4, 0], X[y_pred == 4, 1], s=100, c='magenta', label='Careful')
    sns.set_style("darkgrid", {"axes.facecolor": ".9"})
    plt.title('Suggested Clusters')
    plt.xlabel('Annual income (k$)')
    plt.ylabel('Spending Score (1-100)', fontsize=12)
    plt.ylim(ymin=0)
    plt.legend(fontsize=9)
    figure.savefig('static/img/{}.svg'.format(algorithm))
