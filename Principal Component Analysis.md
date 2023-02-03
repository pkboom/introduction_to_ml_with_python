### Dimensionality reduction

First, we need to define a new coordinate system (by rotating the original one) in which the transformed features are independent.

Then we need to sort these features based on the amount of information that they hold and eliminate one or more features that are ranked lower than the others.

PCA roughly follows the same procedure. The only difference is that it finds a coordinate system in which the features are uncorrelated.

### Random variable

Discrete random variable

Continuous random variable

If X is a continuous random variable, the probability that X takes a value in the interval [a, b] can be written as

![Alt text](https://miro.medium.com/v2/resize%3Afit%3A1296/format%3Awebp/1%2A3yom45JYC4tcIAMISq3SKQ%402x.png)

where f(x) is called the probability density function (PDF) of X. We know that

![Alt text](https://miro.medium.com/v2/resize%3Afit%3A776/format%3Awebp/1%2ACGrDP9Ovg3q_2dR61cAiLA%402x.png)

So the integral of a PDF over the entire space must be equal to 1

![Alt text](https://miro.medium.com/v2/resize%3Afit%3A556/format%3Awebp/1%2AqH6ICR_STiNdsmkLo0HLXw%402x.png)

### Covariance

![Alt text](https://miro.medium.com/v2/resize%3Afit%3A1400/format%3Awebp/1%2AoRLLnCztNOQikEstGtJrjw%402x.png)

The covariance of X and Y provides a measure of the association between X and Y. A positive covariance indicates that the deviations of X and Y from their respective means tend to have the same sign. So when one of them (X or Y) is high, the other one tends to be high, and when one of them is low the other one tends to be low. It also means that they tend to increase or decrease together or move in the same direction. On the other hand, a negative covariance indicates that the deviations of X and Y from their respective means tend to have opposite signs. When one of them is high, the other one tends to be low, and when one of them increases, the other one tends to decrease. So they tend to move in the opposite direction.

### Correlation

![Alt text](https://miro.medium.com/v2/resize%3Afit%3A1128/format%3Awebp/1%2AQvy6R3mB3ZRmcMW1b1E-ZQ%402x.png)

Based on Eq. 16, the correlation and covariance have the same sign (since standard deviation is always positive). When ρ(X, Y)>0, X and Y are positively correlated and tend to move together, and when ρ(X, Y)<0, they are negatively correlated and tend to move in the opposite direction. If ρ(X, Y)=0, X and Y are said to be uncorrelated.

In summary, the value of ρ(X, Y) provides a measure of the extent to which two random variables X and Y are linearly related. If the values that X and Y take are relatively concentrated around a straight line with a positive slope, then ρ(X, Y) will be close to 1. On the other hand, if these values are relatively concentrated around a straight line with a negative slope, then ρ(X, Y) will be close to −1.

### covariance

the covariance of a random vector along two arbitrary vectors doesn’t change by changing the coordinate system.

a random variable with a normal distribution is just a linear function of another random variable with a standard normal distribution.

PCA is based on two assumptions. The random vector X that represents our data set is a continuous random vector. there are no missing values in the dataset.

However, as we mentioned before, what we are looking for is the independent features of the dataset. So we want the uncorrelated features to be independent too. This only happens if the dataset has an MVN distribution.

PCA never fails to give an uncorrelated orthogonal basis for our data set. However the random variables represented by this basis are not necessarily independent. If the dataset is sampled from an MVN distribution, the uncorrelated random variable are independent too.

### Multivariate normal distribution (MVN).

µ and Σ are the parameters of the MVN distribution. We can generate some possible values of X using NumPy’s function random.multivariate_normal().
