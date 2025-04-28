# CyberBook

CyberBook is a collection of open-source extensions for building interactive educational books. It is built on top of Teachbooks, which itself extends Jupyter Book.

This repository serves as an example book for a [Maglev](https://github.com/Hansolini/Take-home-Maglev-lab) assignment, demonstrating how to build and customize interactive books.

## Features

### Interactive content
This book uses the `sphinx-thebe` extension created by TeachBooks to embed live Python code, executed entirely in-browser. This extension makes code cells in the `.ipynb` files of the book executable in the browser. The Python backend kernel will be initialized when the rocket ship icon is clicked.

TeachBooks has developed several metadata tags that you can decorate Jupyter Notebook cells with, to alter their behavior. 
Some tags that prove useful includes:
- `auto-execute-page`: Automatically initializes Thebe live-code on page loaded.
- `thebe-remove-input-init`: Hides the Python code cell, while still running the cell when live coding is started and showing the output of the execution on the page.

For further details on live-coding, see [the Teachbooks manual](https://teachbooks.io/manual/features/live_code.html).

### Self-Assessment Quizzes
Create interactive quizzes with the `ipyquizjb` toolkit, rendered via IPyWidgets. See [ipyquizjb](https://github.com/ForceoftheCyber/ipyquiz) for more details on usage.

### Dynamic simulations
Add dynamic simulations with `ipysim`, allowing readers to adjust parameters of the simulation and receive feedback through animations, rendered via IPyWidgets. See [ipysim](https://github.com/ForceoftheCyber/ipysim) for more details on usage.

For more details towards expanding upon this book, please refer to the [TeachBooks manual](https://teachbooks.io/manual/intro.html).

## Building instructions

### Initial setup
Make a Python virtual environment:

Windows:
```bash
python -m venv ".venv"
.\.venv\Scripts\activate
python -m pip install -r requirements.txt
```

For Linux, replace `.\.venv\Scripts\activate` with `source .venv/Scripts/activate`.

### Building the book

This book uses the `teachbooks` package to build and serve the book. This package is a wrapper around Jupyter Book, with some [additional features](https://teachbooks.io/manual/features/overview.html). To build the book, use

```bash
teachbooks build book
```
from the root directory.

### Launch locally
```bash
teachbooks serve
```
This will provide you with a link to open up the built book in a browser.

### Publish your book online (GitHub Pages)

This repository uses the TeachBooks Github workflow which builds and releases the book online via GitHub Pages. When you push changes to the branch, the corresponding website on GitHub will be automatically updated aswell. For more details, see the [Teachbooks manual](https://teachbooks.io/manual/external/deploy-book-workflow/README.html#gh-workflow-settings)

## Running tests

These tests test using ipyquiz in the context of the book, and they do not have to be run when changing the content of just the book.

### Install extra requirements

```bash
python -m pip install -r devreq.txt
```

### Run tests
```bash
python -m pytest .\PlayWrightTest\
```
