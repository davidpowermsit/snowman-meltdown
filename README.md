# snowman-meltdown

[![Release](https://img.shields.io/github/v/release/davidpowermsit/snowman-meltdown)](https://img.shields.io/github/v/release/davidpowermsit/snowman-meltdown)
[![Build status](https://img.shields.io/github/actions/workflow/status/davidpowermsit/snowman-meltdown/main.yml?branch=main)](https://github.com/davidpowermsit/snowman-meltdown/actions/workflows/main.yml?query=branch%3Amain)
[![codecov](https://codecov.io/gh/davidpowermsit/snowman-meltdown/branch/main/graph/badge.svg)](https://codecov.io/gh/davidpowermsit/snowman-meltdown)
[![Commit activity](https://img.shields.io/github/commit-activity/m/davidpowermsit/snowman-meltdown)](https://img.shields.io/github/commit-activity/m/davidpowermsit/snowman-meltdown)
[![License](https://img.shields.io/github/license/davidpowermsit/snowman-meltdown)](https://img.shields.io/github/license/davidpowermsit/snowman-meltdown)

Command-line Snowman game, a hangman variant where each wrong guess melts part of the snowman. Written in Python.

- **Github repository**: <https://github.com/davidpowermsit/snowman-meltdown/>
- **Documentation** <https://davidpowermsit.github.io/snowman-meltdown/>

## Getting started with your project

### 1. Create a New Repository

First, create a repository on GitHub with the same name as this project, and then run the following commands:

```bash
git init -b main
git add .
git commit -m "init commit"
git remote add origin git@github.com:davidpowermsit/snowman-meltdown.git
git push -u origin main
```

### 2. Set Up Your Development Environment

Then, install the environment and the pre-commit hooks with

```bash
make install
```

This will also generate your `uv.lock` file

### 3. Run the pre-commit hooks

Initially, the CI/CD pipeline might be failing due to formatting issues. To resolve those run:

```bash
uv run pre-commit run -a
```

### 4. Commit the changes

Lastly, commit the changes made by the two steps above to your repository.

```bash
git add .
git commit -m 'Fix formatting issues'
git push origin main
```

You are now ready to start development on your project!
The CI/CD pipeline will be triggered when you open a pull request, merge to main, or when you create a new release.

To finalize the set-up for publishing to PyPI, see [here](https://fpgmaas.github.io/cookiecutter-uv/features/publishing/#set-up-for-pypi).
For activating the automatic documentation with MkDocs/Zensical, see [here](https://fpgmaas.github.io/cookiecutter-uv/features/docs_tool/#deploying-to-github-pages).
To enable the code coverage reports, see [here](https://fpgmaas.github.io/cookiecutter-uv/features/codecov/).

## Releasing a new version



---

Repository initiated with [osprey-oss/cookiecutter-uv](https://github.com/osprey-oss/cookiecutter-uv).
