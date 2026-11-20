# snowman-meltdown

[![Commit activity](https://img.shields.io/github/commit-activity/m/davidpowermsit/snowman-meltdown)](https://img.shields.io/github/commit-activity/m/davidpowermsit/snowman-meltdown)
[![License](https://img.shields.io/github/license/davidpowermsit/snowman-meltdown)](https://img.shields.io/github/license/davidpowermsit/snowman-meltdown)

Command-line Snowman game, a hangman variant where each wrong guess melts part of the snowman. Written in Python.

## Getting started

You need [Git](https://git-scm.com/), [uv](https://docs.astral.sh/uv/getting-started/installation/) and `make`. uv installs the right Python version for you.

```bash
git clone git@github.com:davidpowermsit/snowman-meltdown.git
cd snowman-meltdown
make install
```

`make install` creates the virtual environment, installs the dependencies and sets up the pre-commit hooks.

## Play the game

```bash
uv run snowman
```

Guess one letter at a time. Each wrong guess melts the snowman a little more, and you lose when it has completely melted.

## Run the tests

```bash
make test
```

This runs the whole suite with pytest. To run a single file or test, use pytest directly:

```bash
uv run pytest tests/test_game_logic.py
uv run pytest -k test_player_wins
```

## Contributing

1. Create a branch: `git checkout -b my-change`
2. Make your change and add or update tests in `tests/`.
3. Check that formatting, linting and type checks pass: `make check`
4. Check that the tests pass: `make test`
5. Commit, push your branch and open a pull request on GitHub.

Found a bug or have an idea? [Open an issue](https://github.com/davidpowermsit/snowman-meltdown/issues). For bugs, include your operating system and the steps to reproduce it.

---

Repository initiated with [osprey-oss/cookiecutter-uv](https://github.com/osprey-oss/cookiecutter-uv).
