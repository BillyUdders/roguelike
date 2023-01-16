# roguelike

[Repo that follows this TCOD V2 tutorial.](https://www.rogueliketutorials.com/tutorials/tcod/v2)

It's not a carbon copy, I've reorganized and modernized code where appropriate, using `@dataclass` heavily
and running `pyupgrade` in `pre-commit` to force any old style syntax to use newer features, such as `yield from` etc.

### Setup:

##### Python 3.11 required!

Assumes MacOSX.

```shell
brew install python # install python 3.11 with pyenv, brew, asdf etc.
python -m venv /path/to/new/virtual/environment # wherever your virtualenv is
pip install -r requirements.txt # install TCOD and friends
pre-commit install --install-hooks # for static analysis and code coverage
```
