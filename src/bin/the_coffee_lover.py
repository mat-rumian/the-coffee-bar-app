import argparse
import requests
import json
import logging as log
from random import randint
from time import sleep

from src.utils.config import Config, args_to_conf_dict, merge_configuration
from src.utils.logger import configure_logging
from src.utils.tracing import configure_jaeger_span_exporter_with_manual_requests


def main():
    APP_NAME = 'The Coffee Lover'

    parser = argparse.ArgumentParser(description='The Coffee Lover v0.0.1')
    parser.add_argument('-H', '--host', type=str, help='The Coffee Bar Server Host')
    parser.add_argument('-P', '--port', type=int, help='The Coffe Bar Server Port')
    parser.add_argument('-c', '--config', type=str, help='Configuration file path')
    parser.add_argument('-ah', '--agent-host', type=str, help='Tracing Agent Host')
    parser.add_argument('-ap', '--agent-port', type=str, help='Tracing Agent Port')
    parser.add_argument('-sn', '--service-name', type=str, help='Service Name', default='the-coffee-lover')
    parser.add_argument('-l', '--log-level', type=str, help='Application log level', default='info')
    args = parser.parse_args()

    configure_logging(args.log_level)

    if args.config:
        config = Config(config_path=args.config)
        conf_file = config.get_the_coffee_lover_config()
        conf_args = args_to_conf_dict(args=args)
        configuration = merge_configuration(from_file=conf_file, from_args=conf_args)
    else:
        configuration = args_to_conf_dict(args=args)

    configure_jaeger_span_exporter_with_manual_requests(configuration)

    log.info('********** Starting %s **********', APP_NAME)
    log.info('Configuration: %s', configuration)

    url = 'http://{}:{}/do_espresso'.format(configuration['host'], configuration['port'])

    log.info('The Coffee Bar URL: %s', url)

    while True:
        espresso_order = {
            'amount': randint(1, 10),
            'product': 'espresso',
            'bill': randint(1, 20)
        }
        data = json.dumps(espresso_order)

        sleep(5)
        log.info('Ordering %s', espresso_order)
        res = requests.post(url=url, json=data)
        log.info('Order result: %s', res.text)


main()
