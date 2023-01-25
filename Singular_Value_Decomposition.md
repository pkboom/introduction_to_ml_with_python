Math markdown: https://en.wikibooks.org/wiki/LaTeX/Mathematics

We can think of a matrix A as a _transformation_ that acts on a vector x by multiplication to produce a new vector Ax.

For a matrix A, only some of the vectors change the magnitude of a vector without changing its direction. These special vectors are called the _eigenvectors_ of A and their corresponding scalar quantity λ is called an _eigenvalue_ of A for that eigenvector. So the eigenvector of an n×n matrix A is defined as a nonzero vector u such that:
$$Au =\lambda u $$

```py
from numpy import linalg
linalg.eig(a)

# example
# lam= [-1. -2.]
# u= [[ 1.     -0.7071]
#     [ 0.      0.7071]]
# LA.eig() returns the normalized eigenvector.
# A normalized vector is a unit vector whose length is 1.
```

Multiply matrices

```py
a @ b
```

dot matrices

```py
np.dot(a, b) # if both are 1-d arrays
a.T @ b
```

A symmetric matrix transforms a vector by stretching or shrinking it along its eigenvectors.

Eigenvectors can form a basis for a vector space.

An important property of the symmetric matrices is that an n×n symmetric matrix has n linearly independent and orthogonal eigenvectors, and it has n real eigenvalues corresponding to those eigenvectors.

Eigendecomposition

If we have an n×n symmetric matrix A, we can decompose it as

$$A = PDP^T$$

D is an n×n diagonal matrix comprised of the n eigenvalues of A. P is also an n×n matrix, and the columns of P are the n linearly independent eigenvectors of A that correspond to those eigenvalues in D respectively.

<image src="Eigendecomposition.webp" width="400">

Now in each term of the eigendecomposition equation $$u_iu_i^Tx$$ gives a new vector which is the orthogonal projection of x onto ui. Then this vector is multiplied by λi. Since λi is a scalar, multiplying it by a vector, only changes the magnitude of that vector, not its direction.

Now we go back to the eigendecomposition equation again
