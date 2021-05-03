#! /bin/bash
isort src
pylint src
mypy src
pytest tests
