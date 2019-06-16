# Installation

You'll need:
- [Python 3.7](https://www.python.org/)
- [pipenv](https://pypi.org/project/pipenv/)

Clone the repository then run `pipenv install`.

# Usage

All the commands should be executed in the virtualenv created by pipenv.
Simply type `pipenv shell` to activate the virtualenv. The commands should
then be executed with `python -m assnatouverte [command]`.

To get usage details, run `python -m assnatouverte -h`.

## Database management

The crawling data is stored in a [SQLite](https://www.sqlite.org/index.html) database.
To create the database, run `python -m assnatouverte init_db`. It will create a file in
the current working directory named `assnatouverte.sqlite` with the appropriate tables.

On all commands, you can specify the database file with the `-db` parameter. It should
appear **before** the command and should specify a complete SQLite URL as defined by
SQLAlchemy (see [here](https://docs.sqlalchemy.org/en/13/core/engines.html#sqlite) for
more details). Example: `python -m assnatouverte -db sqlite:///my_database.db init_db`.

By default, the `init_db` command won't delete any table or content. You can however
ask the program to completely overwrite the database with the `-x` option. Example: 
`python -m assnatouverte init_db -x`.

## Crawling

To run a crawler, simply run `python -m assnatouverte crawl [...]` with a list of
crawlers. The crawlers will be executed sequentially.

# Unit tests

To run the unit test, run `python -m unittest`.

For coverage results, be sure to install the develop dependencies with
`pipenv install --dev`, then run `coverage run -m unittest`. To get a report,
run `coverage report`.

# License

assnatouverte
Copyright (C) 2019  Émile Grégoire

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
