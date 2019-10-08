# PYTHON_ARGCOMPLETE_OK
import logging

from arghandler import ArgumentHandler, subcmd

from assnatouverte.crawling.crawler_service_factory import CrawlerServiceFactory
from assnatouverte.crawling.defaults import DEFAULT_DB_STR
from assnatouverte.database.database_service_factory import DatabaseServiceFactory


def set_verbose_logging():
    logging.basicConfig(level=logging.DEBUG)


@subcmd('crawl', help='Execute a crawler')
def crawl(parser, context, args):
    parser.add_argument('crawlers', metavar='crawler', type=str, nargs='+', help='crawlers to execute')
    parser.add_argument('--print-sql', action='store_true', help='print SQL requests')
    args = parser.parse_args(args)

    if context.v:
        set_verbose_logging()

    crawler_service_factory = CrawlerServiceFactory().with_db_str(context.db)
    if args.print_sql:
        crawler_service_factory.echo_sql()
    crawler_service = crawler_service_factory.build()

    for crawler in args.crawlers:
        crawler_service.execute_crawler(crawler)


@subcmd('init_db', help='Create the database')
def init_db(parser, context, args):
    parser.add_argument('-x', '--overwrite', action='store_true', help='overwrite existing database')
    args = parser.parse_args(args)

    if context.v:
        set_verbose_logging()

    database_service = DatabaseServiceFactory().with_db_str(context.db).build()
    database_service.init_db(args.overwrite)


def main():
    handler = ArgumentHandler(prog='assnatouverte', enable_autocompletion=True, use_subcommand_help=True)
    handler.add_argument('-db', metavar='database', type=str, default=DEFAULT_DB_STR,
                         help='database connection string (default: "%(default)s")')
    handler.add_argument('-v', action='store_true', help='verbose mode')
    handler.run()


if __name__ == "__main__":
    main()
