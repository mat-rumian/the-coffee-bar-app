import argparse
import logging as log

from src.bar.bar import Bar
from src.utils.config import Config, args_to_conf_dict, merge_configuration
from src.utils.logger import configure_logging
from src.utils.tracing import configure_jaeger_span_exporter


def main():
    APP_NAME = 'The Coffee Bar'

    parser = argparse.ArgumentParser(description='The Coffee Bar v0.0.1')
    parser.add_argument('-H', '--host', type=str, help='HTTP Server Host')
    parser.add_argument('-P', '--port', type=int, help='HTTP Server Port')
    parser.add_argument('-ch', '--coffeemachine-host', type=str, help='Coffe Machine Host')
    parser.add_argument('-cp', '--coffeemachine-port', type=int, help='Coffee Machine Port')
    parser.add_argument('-mh', '--cashdesk-host', type=str, help='Cashdesk Host')
    parser.add_argument('-mp', '--cashdesk-port', type=int, help='Cashdeks Port')
    parser.add_argument('-c', '--config', type=str, help='Configuration file path')
    parser.add_argument('-ah', '--agent-host', type=str, help='Tracing Agent Host')
    parser.add_argument('-ap', '--agent-port', type=str, help='Tracing Agent Port')
    parser.add_argument('-sn', '--service-name', type=str, help='Service Name', default='the-coffee-bar')
    parser.add_argument('-l', '--log-level', type=str, help='Application log level', default='info')
    args = parser.parse_args()

    configure_logging(args.log_level)

    if args.config:
        config = Config(config_path=args.config)
        conf_file = config.get_the_coffee_bar_config()
        conf_args = args_to_conf_dict(args=args)
        configuration = merge_configuration(from_file=conf_file, from_args=conf_args)
    else:
        configuration = args_to_conf_dict(args=args)

    configure_jaeger_span_exporter(configuration)

    log.info('********** Starting %s **********', APP_NAME)
    log.info('Configuration: %s', configuration)
    the_bar = Bar(name=APP_NAME, host=configuration['host'], port=configuration['port'],
                  coffee_machine_host=configuration['coffeemachine_host'],
                  coffee_machine_port=configuration['coffeemachine_port'],
                  cashdesk_host=configuration['cashdesk_host'],
                  cashdesk_port=configuration['cashdesk_port'])

    the_bar.run()


main()
