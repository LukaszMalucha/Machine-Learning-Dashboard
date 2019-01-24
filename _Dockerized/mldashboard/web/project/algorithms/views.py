from flask import render_template, redirect, url_for, Blueprint, session

## BLUEPRINT INIT

algorithms_blueprint = Blueprint(
    'algorithms', __name__,
    template_folder="templates"
)

from .ml_algorithms import *


## User Login
@algorithms_blueprint.context_processor
def context_processor():
    current_user = session.get('current_user') or 'Guest'
    return dict(current_user=current_user)


#################################################################### ML ESTIMATOR TYPES SUMMARY #####################################################################################################################


## ML TYPE CHOICE HANDLING ##########################################################     

@algorithms_blueprint.route('/summary/<type_id>')
def summary(type_id):
    if type_id == "Regression":
        return redirect(url_for("algorithms.regression"))
    elif type_id == "Classification":
        return redirect(url_for("algorithms.classification"))
    else:
        return redirect(url_for("algorithms.clustering"))


## REGRESSION INITIATION ############################################################

@algorithms_blueprint.route('/regression')
def regression():
    ## Decribe ml type
    algorithm_preprocessors, algorithm_issues = algorithm_characteristics("Regression")

    ## Describe dataset
    dataset, X, y, describe, rows, columns = regression_dataset()

    single_prediction = ''

    return render_template('regression.html', data=dataset.to_html(),
                           describe=describe.to_html(), single_prediction=single_prediction, rows=rows,
                           columns=columns, algorithm_preprocessors=algorithm_preprocessors,
                           algorithm_issues=algorithm_issues)


## REGRESSION ALGORITHM CHOICE HANDLING #############################################

@algorithms_blueprint.route('/regressor/<regressor_id>')
def regressor(regressor_id):
    choice = regressor_id

    ## Describe ML type
    algorithm_preprocessors, algorithm_issues = algorithm_characteristics("Regression")

    ## Describe dataset
    dataset, X, y, describe, rows, columns = regression_dataset()

    ## Apply Chosen Algrotihm
    if choice == 'polynomial_regression':
        X_grid, plot_prediction, single_prediction = polynomial_regression(X, y)
    elif choice == 'svr':
        X_grid, plot_prediction, single_prediction = svr(X, y)
    else:
        X_grid, plot_prediction, single_prediction = randomforest(X, y)

    ## Visualize Dataset
    regression_plot(choice, X, y, X_grid, plot_prediction)

    return render_template('regression.html', data=dataset.to_html(),
                           describe=describe.to_html(), single_prediction=single_prediction, choice=choice,
                           rows=rows, columns=columns, algorithm_preprocessors=algorithm_preprocessors,
                           algorithm_issues=algorithm_issues,
                           )


## CLASSIFICATION INITIATION ########################################################

@algorithms_blueprint.route('/classification')
def classification():
    ## Decribe ml type
    algorithm_preprocessors, algorithm_issues = algorithm_characteristics("Classification")

    ## Describe dataset
    dataset, X, y, describe, rows, columns, dataset_head = classification_dataset()

    single_prediction = ''

    return render_template('classification.html', data=dataset_head.to_html(),
                           describe=describe.to_html(), single_prediction=single_prediction,
                           rows=rows, columns=columns, algorithm_preprocessors=algorithm_preprocessors,
                           algorithm_issues=algorithm_issues)


## CLASSIFICATION ALGORITHM CHOICE HANDLING #########################################

@algorithms_blueprint.route('/classifier/<classifier_id>')
def classifier(classifier_id):
    ## Decribe ml type
    algorithm_preprocessors, algorithm_issues = algorithm_characteristics("Classification")

    ## Describe dataset
    dataset, X, y, describe, rows, columns, dataset_head = classification_dataset()

    # Splitting the dataset into the Training set and Test set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

    # Feature Scaling
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)

    # Choose classifier to fit the Training set
    classifier = GaussianNB() if classifier_id == 'naive_bayes' \
        else KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2) if classifier_id == 'k-nearest_neighbors' \
        else SVC(kernel='rbf', random_state=0)
    classifier.fit(X_train, y_train)

    # Predicting the Test set results
    y_pred = classifier.predict(X_test)

    # Making the Confusion Matrix
    from sklearn.metrics import confusion_matrix
    cm = confusion_matrix(y_test, y_pred)
    df = pd.DataFrame(cm, index=['Bought: Yes', 'Bought: No'], columns=['Predicted: Yes', 'Predicted: No'])
    accuracy = (df.iloc[0, 0] + df.iloc[1, 1])
    accuracy = "{}%".format(float(accuracy))

    # Visualising the Test set results with the heatmap
    classification_plot(classifier_id, X_test, y_test, classifier)

    return render_template('classification.html', data=dataset_head.to_html(),
                           describe=describe.to_html(), cma=df.to_html(),
                           rows=rows, columns=columns, acc=accuracy, classifier_id=classifier_id,
                           algorithm_preprocessors=algorithm_preprocessors,
                           algorithm_issues=algorithm_issues)


## CLUSTERING INITIATION ############################################################

@algorithms_blueprint.route('/clustering')
def clustering():
    ## Decribe ml type
    algorithm_preprocessors, algorithm_issues = algorithm_characteristics("Clustering")

    ## Describe dataset
    dataset, X, describe, rows, columns, dataset_head = clustering_dataset()

    return render_template('clustering.html', data=dataset_head.to_html(),
                           describe=describe.to_html(), rows=rows, columns=columns,
                           algorithm_preprocessors=algorithm_preprocessors, algorithm_issues=algorithm_issues)


## CLUSTERING ALGORITHM CHOICE HANDLING #############################################  

@algorithms_blueprint.route('/clusterer/<clusterer_id>')
def clusterer(clusterer_id):
    ## Decribe ml type
    algorithm_preprocessors, algorithm_issues = algorithm_characteristics("Clustering")

    ## Describe dataset
    dataset, X, describe, rows, columns, dataset_head = clustering_dataset()

    choice = clusterer_id

    if choice == 'hierarchical_clustering':
        ## Using the dendogram to find the optimal number of clusters
        dendrogram_plot(choice, X)
        ## Result = 5

        ## Fitting Hierarchical Clustering to the dataset (optimal clusters = 5)
        hc = AgglomerativeClustering(n_clusters=5, affinity='euclidean', linkage='ward')
        y_pred = hc.fit_predict(X)

        ## Visualising the clusters 

    if choice == 'k-means_clustering':

        ## Using the elbow method to find the optimal number of clusters
        wcss = []  ## initialize the list
        for i in range(1, 11):
            kmeans = KMeans(n_clusters=i,  ## from 1 to 10
                            init='k-means++',  ## k-means++ to avoid random initialziation trap
                            max_iter=300,  ## 300 is deafault
                            n_init=10,  ## algorithm runs with different initial centroids
                            random_state=0)
            kmeans.fit(X)
            wcss.append(kmeans.inertia_)  ## to compute wcss
        ## Result = 5    

        ## Visualising Elbow Method
        elbow_plot(choice, wcss)

        ## Applying k-means to the mall dataset - from the plot we can see that optimum is 5 clusters.
        kmeans = KMeans(n_clusters=5,
                        init='k-means++',  ## k-means++ to avoid random initialziation trap
                        max_iter=300,  ## 300 is deafault
                        n_init=10,  ## algorithm runs with different initial centroids
                        random_state=0)
        y_pred = kmeans.fit_predict(X)  ## fit_predict returns a cluster for each observation

    ## Visualising the clusters
    clustering_plot(choice, X, y_pred)

    return render_template('clustering.html', data=dataset_head.to_html(),
                           describe=describe.to_html(), rows=rows, columns=columns,
                           choice=choice, algorithm_preprocessors=algorithm_preprocessors,
                           algorithm_issues=algorithm_issues)
