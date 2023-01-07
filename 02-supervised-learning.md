# Estimators

All machine learning models in scikit-learn are implemented in their own classes, which are called Estimator classes.

# Parameters

The majority of them are either speed optimizations or for very special use cases.

$$
ŷ= w[0] * x[0] + w[1] * x[1] + ... + w[p] * x[p] + b
$$

# Supervised Machine Learning Algorithms

## Linear Models

### Linear Regression

- LinearRegression
- Ridge
- Lasso

Alpha: regularization parameter
higher alpha, lower coefficients, higher regularization

### Linear Classification

- LogisticRegression
- LinearSVC

C: strenth of regularization
lower C, lower coefficients, higher regularization

L2 regularization. Try this first.
L1 regularization. Some coefficients are zero.

## Naive Bayes Classifiers

- GaussianNB: applied to any continuous data
- BernoulliNB: binary data
- MultinomialNB: count data
  > BernoulliNB and MultinomialNB are mostly used in text data classification.

## Decision Tress

DecisionTreeRegressor
DecisionTreeClassifier

## Ensemble

### bagging

random forests

### Boosting

grandient boosting(GBM)
XGBoost
Light GBM

## Support Vector Machines

lower gamma, lower complexity
smaller C, more restricted model
