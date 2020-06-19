import logging as log

from src.bar.storage import Storage
from src.common.http_server import HttpServer


def get_amount_of_product(data):
    return data['amount']


class CashDesk(HttpServer):

    def __init__(self, connection_string: str, name: str = 'Cash Desk', host: str = 'localhost', port: int = 8084):
        super().__init__(name, host, port)
        print(connection_string)
        self.db = Storage(connection_string=connection_string)
        self.pay_in()

    def pay_in(self):
        self.add_endpoint(endpoint='/pay_in', endpoint_name='pay_in', handler=self.payment)

    def payment(self, data):
        log.info('Payment in progress: %s', data)

        price = self.get_product_price(data=data)
        items_sold = self.get_items_sold(data=data)
        amount = get_amount_of_product(data=data)

        total_price = amount * price

        payout = data['bill'] - total_price

        if payout < 0:
            log.error('Not enough money')
            return ValueError('Not enough money')
        else:
            total_items = items_sold + amount
            self.db.update_items((total_items, data['product']))
            return {'payout': payout}

    def get_product_price(self, data):
        product = self.db.get_price_of_product(product_name=data['product'])
        return product['price']

    def get_items_sold(self, data):
        product = self.db.get_items_sold(product_name=data['product'])
        return product['items_sold']
