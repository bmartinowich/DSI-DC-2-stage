## PPT

## Code

## Conclusion

We've discussed overfitting in the context of bias and variance, and we've seen some techniques like regularization that are used to avoid overfitting. In this lesson we'll discuss another method for avoid overfitting that is commonly referred to a the train/test split. The idea is very similar to cross-validation (indeed it is a type of cross-validation) in that we split the dataset into two subsets:

- a subset to train our model on, and
- a subset to test our model's predictions on

This serves two useful purposes:

- We prevent overfitting by not using all the data, and
- we have some remaining data to evaluate our model.

While it may seem like a relatively simple idea, there are some caveats to putting it into practice. For example, if you are not careful it is easy to take a non-random split. Suppose we have salary data on technical professionals that is composed 80% of data from California and 20% elsewhere and is sorted by state. If we split our data into 80% training data and 20% testing data we ight inadvertantly select all the California data to train and all the non-California data to test. In this case we've still overfit on our data set because we did not sufficiently randomize the data.
In a situation like this we can use k-fold cross validation, which is the same idea applied to more than two subsets. In particular, we partition our data into k subsets and train on k−1 one of them. holding the last slice for testing. We can do this for each of the possible k−1 subsets.
