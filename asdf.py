def nested_cv(X, y, inner_cv, outer_cv, Classifier, parameter_grid):
  outer_scores = []
# for each split of the data in the outer cross-validation
# (split method returns indices)
for training_samples, test_samples in outer_cv.split(X, y):
# find best parameter using inner cross-validation
best_parms = {}
best_score = -np.inf
# iterate over parameters
for parameters in parameter_grid:
# accumulate score over inner splits
cv_scores = []
# iterate over inner cross-validation
for inner_train, inner_test in inner_cv.split(
X[training_samples], y[training_samples]):
# build classifier given parameters and training data
clf = Classifier(**parameters)
clf.fit(X[inner_train], y[inner_train])
# evaluate on inner test set
score = clf.score(X[inner_test], y[inner_test])
cv_scores.append(score)
# compute mean score over inner folds
mean_score = np.mean(cv_scores)
if mean_score > best_score:
# if better than so far, remember parameters
best_score = mean_score
best_params = parameters
# build classifier on best parameters using outer training set
clf = Classifier(**best_params)
clf.fit(X[training_samples], y[training_samples])
# evaluate
outer_scores.append(clf.score(X[test_samples], y[test_samples]))
return np.array(outer_scores)