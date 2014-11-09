def cross_validation(clf, X, Y, num_folds):
    """
    :param clf: a classifier to use for training (eg. SVM / MultinomialNaiveBayes ...)
    :param X: vectors
    :param Y: labels
    :param num_folds: number of folds
    :return: accuracy as the average of k-fold cross-validation.
    """
    X = X.todense()
    fold_size = len(X) / num_folds
    i = 0
    accs = []
    for fold in xrange(num_folds):
        test_mat = X[i*fold_size : (i+1)*fold_size]
        test_labels = Y[i*fold_size : (i+1)*fold_size]

        train_mat = X[0:i*fold_size].tolist() + X[(i+1)*fold_size::].tolist()
        train_labels = Y[0:i*fold_size] + Y[(i+1)*fold_size::]
        clf.fit(train_mat, train_labels)
        predicted_labels = clf.predict(test_mat)

        # finding accuracy:
        correct = 0
        for predicted, true in zip(predicted_labels, test_labels):
            if predicted == true:
                correct += 1
        acc = float(correct) / float(len(predicted_labels))
        accs.append(acc)

    return np.mean(accs)
