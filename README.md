[![assnatouverte](./website/logo.svg)](https://assnatouverte.ca/)

[![CircleCI](https://circleci.com/gh/emgre/assnatouverte.svg?style=svg)](https://circleci.com/gh/emgre/assnatouverte)
[![codecov](https://codecov.io/gh/emgre/assnatouverte/branch/master/graph/badge.svg)](https://codecov.io/gh/emgre/assnatouverte)

# Installation

You'll need:
- [Python 3.8+](https://www.python.org/)
- [poetry](https://python-poetry.org/)

Clone the repository then run `poetry install --with dev`.

# Usage

All the commands should be executed through poetry like so:
`poetry run assnatouverte [command]`.

To get usage details, run `poetry run assnatouverte -h`.

## Database management

The crawling data is stored in a [SQLite](https://www.sqlite.org/index.html) database.
To create the database, run `poetry run assnatouverte init_db`. It will create a file in
the current working directory named `assnatouverte.sqlite` with the appropriate tables.

On all commands, you can specify the database file with the `-db` parameter. It should
appear **before** the command and should specify a complete SQLite URL as defined by
SQLAlchemy (see [here](https://docs.sqlalchemy.org/en/13/core/engines.html#sqlite) for
more details). Example: `poetry run assnatouverte -db sqlite:///my_database.db init_db`.

By default, the `init_db` command won't delete any table or content. You can however
ask the program to completely overwrite the database with the `-x` option. Example: 
`poetry run assnatouverte init_db -x`.

## Crawling

To run a crawler, simply run `poetry run assnatouverte crawl [...]` with a list of
crawlers. The crawlers will be executed sequentially.

# Quality

## Unit tests

To run the unit test, run `poetry run python -m unittest`.

## Coverage

For coverage results, run `poetry run coverage run -m unittest`. To get a report, run
`poetry run coverage report`.

## Linting

To run the linter ([pylint](https://www.pylint.org/)), run
`poetry run pylint assnatouverte tests`.

## Static typing

To run the static type analyzer ([mypy](http://mypy-lang.org/)), run
`poetry run mypy assnatouverte`.

# License

assnatouverte
Copyright (C) 2019 - 2021 Émile Grégoire

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
