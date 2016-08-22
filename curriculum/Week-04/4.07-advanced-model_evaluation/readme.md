
# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Advanced Model Evaluation

### LEARNING OBJECTIVES
*After this lesson, you will be able to:*
- Learn about and use sklearn functions to help perform different kinds of model evaluation
- Demonstrate how to use sklearn GridSearch to autotune models

<a name="introduction"></a>
## Introduction to gridsearch 

A correlation matrix is used to investigate the dependence between multiple variables at the same time. The result is a table containing the correlation coefficients between each variable and the others. This is ideal for feature selection when deciding which features to use in a predictive model.		 

NumPy has an easy to use method perform to perform matrix correlations called ‘corrcoef’. [Review the code](./code/starter-code/week4-4.1-breast-cancer-coefficients.ipynb) for performing a Pearson correlation coefficient matrix on the Breast Cancer Dataset.

What is "gridsearch"? Gridsearch is the process of searching for the optimal set of tuning parameters for a model. It searches across values of parameters and uses cross-validation to evaluate the effect. It's called gridsearch because the idea is that there is a "grid" of parameters that are iteratively searched.

What kind of "tuning parameters" would we use this to search for?

<a name="demo"></a>
## Demo: Grid Search (15 mins)

For regularization like Ridge or Lasso, the optimal tuning parameters cannot be formulated automatically. We iteratively search for the best parameter for our problem.

sklearn's LogisticRegression class can accept an "l2" or "l1" **penalty** keyword argument, for Ridge and the Lasso, respectively. The **C** parameter indicates the inverse of the regularization strength. A small value for C will make the shrinkage (Ridge) or sparsity (Lasso) penalty larger, whereas larger values will decrease the effect of the penalty term.

```python
from sklearn.linear_model import LogisticRegression


# Logistic regression with a strong Lasso penalty:
sparse_logreg = LogisticRegression(penalty='l1', C=0.0001)

# Logistic regression with a weak Ridge penalty:
shrunk_logreg = LogsiticRegression(penalty='l2', C=1000.0)
```


<a name="demo"></a>
## Demo: Multinomial logistic regression (15 mins)

Review [GridSearch Example](./code/starter-code/week4-4.1-search-grid.ipynb) and [Classification Report](./code/starter-code/week4-4.1-classification-report.ipynb) techniques for use in independent practice and project work.


<a name="guided-practice"></a>
## Guided Practice: Gridsearch with multinomial logistic modeling on crime data 

So far, we have been using logistic regression for binary problems where there are only two class labels. As you might have suspected or read in the documentation, logistic regression can be extended to dependent variables with multiple classes.

We are using the gridsearch in conjunction with multinomial logistic to optimize a model that predicts the category (type) of crime based on various features captured by San Francisco police departments.

<a name="ind-practice"></a>
## Independent Practice: Classification Metrics (25 minutes)

Use your Project 4 classification model and the classification report utility to output the classification metrics of your model. Hint: use the additional resource notebooks below to analyze your project data.

<a name="conclusion"></a>
## Conclusion (5 mins)
- Review independent practice deliverable(s)
- Recap topic(s) covered
- Review logit coefficients

***

### ADDITIONAL RESOURCES
- Python [Lesson Correlation Matrix Example](./code/starter-code/week4-4.1-breast-cancer-coefficients.ipynb)
- Python [Lesson GridSearch Example](./code/starter-code/week4-4.1-search-grid.ipynb)
- Python [Lesson Classification Report Example](./code/starter-code/week4-4.1-classification-report.ipynb)