## mglearn

If you get `ImportError: No module named mglearn` you can try to install mglearn into your python environment using the command `pip install mglearn` in your terminal or `!pip install mglearn` in Jupyter Notebook.

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
