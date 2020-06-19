import argparse
import logging as log

from src.bar.cash_desk import CashDesk
from src.utils.config import Config, args_to_conf_dict, merge_configuration
from src.utils.logger import configure_logging
from src.utils.tracing import configure_jaeger_span_exporter


def main():
    APP_NAME = 'The Cashdesk'

    parser = argparse.ArgumentParser(description='The Cashdesk v0.0.1')
    parser.add_argument('-H', '--host', type=str, help='HTTP Server Host')
    parser.add_argument('-P', '--port', type=int, help='HTTP Server Port')
    parser.add_argument('-S', '--connection-string', type=str, help='Storage Connection String')
    parser.add_argument('-c', '--config', type=str, help='Config file path')
    parser.add_argument('-ah', '--agent-host', type=str, help='Tracing Agent Host')
    parser.add_argument('-ap', '--agent-port', type=str, help='Tracing Agent Port')
    parser.add_argument('-sn', '--service-name', type=str, help='Service Name', default='the-cashdesk')
    parser.add_argument('-l', '--log-level', type=str, help='Application log level', default='info')
    args = parser.parse_args()

    configure_logging(args.log_level)

    if args.config:
        config = Config(config_path=args.config)
        conf_file = config.get_the_cashdesk_config()
        conf_args = args_to_conf_dict(args=args)
        configuration = merge_configuration(from_file=conf_file, from_args=conf_args)
    else:
        configuration = args_to_conf_dict(args=args)

    configure_jaeger_span_exporter(configuration)

    log.info('********** Starting %s **********', APP_NAME)
    log.info('Configuration: %s', configuration)

    cashdesk = CashDesk(name=APP_NAME, host=configuration['host'], port=configuration['port'],
                        connection_string=configuration['connection_string'])

    cashdesk.run()


main()
