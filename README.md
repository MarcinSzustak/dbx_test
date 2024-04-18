# pyspark-project-template

PySpark project template for new projects

## Repository information

| Property      | Value            |
|---------------|------------------|
| Owner         | Michał Misiewicz |
| Documentation | TBA              |


## Used tools

- [GitHub Actions](https://docs.github.com/en/actions/quickstart) - CI/CD tool
- [PyTest](https://docs.pytest.org/en/7.2.x/) - Testing framework
- [Poetry](https://python-poetry.org/docs/) - Dependency manager
- [pre-commit](https://pre-commit.com) - pre-commit GitHub hooks manager
- [black](https://black.readthedocs.io) - Linter
- [flake8](https://flake8.pycqa.org) - Linter

## Poetry

Poetry helps you declare, manage and install dependencies of Python projects, ensuring you have the right stack
everywhere. Poetry uses the `pyproject.toml` file to orchestrate the project and its dependencies.

### basic commands:

- `poetry install` - Install dependencies from `pyproject.toml` file.
- `poetry add name_of_package` - Adds required packages to your `pyproject.toml` and installs them.
- `poetry remove name_of_package` - Removes a package from the current list of installed packages.
- `poetry lock` - To pin manually added dependencies from your `pyproject.toml` file to `poetry.lock`.
- `poetry env info` - Displays information about the current environment.

[more commands](https://python-poetry.org/docs/cli/#install)

## pre-commit

Python package which allows you to create and execute hooks before every commit. All hooks are defined in the `.pre-commit-config.yaml` file.

### quick start:

- `pre-commit install` to initialize the git hooks.
- `pre-commit run --all-files` runs all hooks manually.
