import logging as log
from time import sleep
from random import random, randint

from src.common.http_server import HttpServer

COFFEES = {
    'espresso': '/espresso',
    'cappuccino': '/cappuccino',
    'americano': '/americano'
}


class CoffeeMachine(HttpServer):

    water_status = 1000
    coffee_status = 1000

    def __init__(self, name: str = 'The Coffee Machine', host: str = 'localhost', port: int = 8084):
        super().__init__(name, host, port)
        self.add_all_endpoints()

    def update_water(self, needed_amount: int):
        if (self.water_status - needed_amount) >= 0:
            self.water_status -= needed_amount
            sleep(random())
            return True
        else:
            # Everybody know that filling the coffee is taking time and sometimes there can be no coffee
            if randint(1, 100) % 2 == 0:
                sleep(random())
                self.water_status = 1000
                self.update_water(needed_amount)
            else:
                return False

    def update_coffee(self, needed_amount: int):
        if (self.coffee_status - needed_amount) >= 0:
            self.coffee_status -= needed_amount
            sleep(random())
            return True
        else:
            # Everybody know that filling the coffee is taking time and sometimes there can be no coffee
            if randint(1, 100) % 2 == 0:
                sleep(random())
                self.coffee_status = 1000
                self.update_coffee(needed_amount)
            else:
                return False

    def add_all_endpoints(self):
        self.add_endpoint(endpoint=COFFEES['espresso'], endpoint_name='espresso', handler=self.prepare_espresso)

    def prepare_espresso(self, data):
        WATER = 37
        COFFEE = 8

        amount = data['amount']
        log.info('Preparing espresso coffee')
        water_needed = amount * WATER
        coffee_needed = amount * COFFEE

        if all([self.update_water(needed_amount=water_needed), self.update_coffee(needed_amount=coffee_needed)]):
            log.info('Coffee done in number of: %s', amount)
            return {'status': 'done'}
        else:
            log.error('Missing some ingredients')
            return ValueError('Missing some ingredients')
