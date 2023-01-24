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

Now we plot the eigenvectors on top of the transformed vectors:
