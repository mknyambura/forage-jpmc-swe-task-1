import unittest
from client3 import getDataPoint

class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        result = getDataPoint(quotes[0])
        self.assertEqual(result, ('ABC', {'bid_price': 120.48, 'ask_price': 121.2, 'price_ratio': 0.9968316831683168}))

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        result = getDataPoint(quotes[1])
        self.assertEqual(result, ('DEF', {'bid_price': 117.87, 'ask_price': 121.68, 'price_ratio': 0.9678081407619582}))

    def test_getDataPoint_emptyQuote(self):
        # Test when an empty quote is passed
        empty_quote = {}
        result = getDataPoint(empty_quote)
        self.assertEqual(result, (None, None, None, None))  # Adjust based on the expected behavior

    def test_getDataPoint_invalidQuoteStructure(self):
        # Test when the quote structure is invalid
        invalid_quote = {'invalid_key': 'invalid_value'}
        result = getDataPoint(invalid_quote)
        self.assertEqual(result, (None, None, None, None))  # Adjust based on the expected behavior

if __name__ == '__main__':
    unittest.main()
