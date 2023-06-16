import unittest

from client3 import getDataPoint
from client3 import getRatio


class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            
            # assertions to verify the correctness of the output
            self.assertEqual(stock, quote['stock'])
            self.assertEqual(bid_price, float(quote['top_bid']['price']))
            self.assertEqual(ask_price, float(quote['top_ask']['price']))
            self.assertEqual(price, (bid_price + ask_price) / 2)

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
        stock, bid_price, ask_price, price = getDataPoint(quote)
        
        # Add assertions to verify the correctness of the output
        self.assertEqual(stock, quote['stock'])
        self.assertEqual(bid_price, float(quote['top_bid']['price']))
        self.assertEqual(ask_price, float(quote['top_ask']['price']))
        self.assertGreater(bid_price, ask_price)  # Assert that bid_price is greater than ask_price
        self.assertEqual(price, (bid_price + ask_price) / 2)


  """ ------------ Add more unit tests ------------ """

  def test_getRatio(self):
        # Test case when price_b is non-zero
        price_a = 10
        price_b = 5
        expected_ratio = 2.0
        actual_ratio = getRatio(price_a, price_b)
        self.assertEqual(actual_ratio, expected_ratio)
        
        # Test case when price_b is zero
        price_a = 10
        price_b = 0
        expected_ratio = None
        actual_ratio = getRatio(price_a, price_b)
        self.assertEqual(actual_ratio, expected_ratio)

if __name__ == '__main__':
    unittest.main()
