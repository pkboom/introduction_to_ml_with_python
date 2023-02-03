## mglearn

If you get `ImportError: No module named mglearn` you can try to install mglearn into your python environment using
the command `pip install mglearn` in your terminal or `!pip install mglearn` in Jupyter Notebook.

## Errata

Please note that the first print of the book is missing the following line when listing the assumed imports:

```python
from IPython.display import display
```

Please add this line if you see an error involving `display`.

The first print of the book used a function called `plot_group_kfold`.
This has been renamed to `plot_label_kfold` because of a rename in
scikit-learn.

## Setup

To run the code, you need the packages `numpy`, `scipy`, `scikit-learn`, `matplotlib`, `pandas` and `pillow`.
Some of the visualizations of decision trees and neural networks structures also require `graphviz`. The chapter
on text processing also requires `nltk` and `spacy`.

The easiest way to set up an environment is by installing [Anaconda](https://www.continuum.io/downloads).

### Installing packages with conda:

If you already have a Python environment set up, and you are using the `conda` package manager, you can get all packages by running

    conda install numpy scipy scikit-learn matplotlib pandas pillow graphviz python-graphviz

For the chapter on text processing you also need to install `nltk` and `spacy`:

    conda install nltk spacy

### [Writing mathematical expressions &rarr;](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions)

Math markdown: https://en.wikibooks.org/wiki/LaTeX/Mathematics
