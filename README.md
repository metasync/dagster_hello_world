# Dagster Hello World

This is simple "Hello World!" sample for Dagster.

Welcome to Dagster!

# Prerequsites

This project uses uv for package dependency management:

  https://docs.astral.sh/uv/

Please install uv first.

# Basic usage

First, clone this repository by git.

Then, setup project environment:

```
uv sync
```

Last, run for development locally:

```
uv run dagster dev
```

Now you can go visit the dagster web portal for the project in your favorite browser:

  http://localhost:3000

To run test cases in this project:

```
uv run pytest
```
