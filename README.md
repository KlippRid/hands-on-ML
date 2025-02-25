# Hands-on Machine Learning with Scikit-Learn, Keras and TensorFlow

Library containing different ml tools and examples based on examples in Hands-on Machine Learning with Scikit-Learn, 
Keras and TensorFlow by Aurelien Geron.

## Setup

### Step 1
Install uv
```
brew install uv
```

### Step 2
Create and activate a virtual env
```
uv venv .venv
```

### Step 3
Install the proprietary python package `mltools` and open source required packages by running 

```
uv pip install -e .
```

### Step 4
Run main to activate jupiter notebook

```
python main.py
```

## Add packages 
Run
```
uv pip install <python package name>
```
this will add your package to the `pyproject.toml` file.

## Linting
The toml file installs ruff which is a linting tool to help keep standardised format of code.
Check code errors or format issues
```
ruff check .
```
Automatically fix linting issues
```
ruff check --fix .
```
Format code
```
ruff format .
```
Alternative add this to a pre-commit hook, add ruff to .pre-commit-config.yaml:

```
repos:
- repo: https://github.com/astral-sh/ruff-pre-commit
  rev: "latest"
  hooks:
    - id: ruff
    - id: ruff-format
```
Then install pre-commit hooks:
```
pre-commit install
```
Now, ruff will run automatically when you commit code.

