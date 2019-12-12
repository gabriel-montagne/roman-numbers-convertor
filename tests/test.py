import unittest
from unittest.mock import Mock
from main import handler


class ConvertNumberToRomanNumeralCase(unittest.TestCase):
    def test_1(self):
        data = {'digits_string': '12'}
        req = Mock(get_json=Mock(return_value=data), args=data)
        actual_result = handler(req)
        expected_result = 'XII'
        self.assertEqual(actual_result, expected_result)

    def test_2(self):
        data = {'digits_string': '79'}
        req = Mock(get_json=Mock(return_value=data), args=data)
        actual_result = handler(req)
        expected_result = 'LXXIX'
        self.assertEqual(actual_result, expected_result)

    def test_3(self):
        data = {'digits_string': '225'}
        req = Mock(get_json=Mock(return_value=data), args=data)
        actual_result = handler(req)
        expected_result = 'CCXXV'
        self.assertEqual(actual_result, expected_result)

    def test_4(self):
        data = {'digits_string': '2922'}
        req = Mock(get_json=Mock(return_value=data), args=data)
        actual_result = handler(req)
        expected_result = 'MMCMXXII'
        self.assertEqual(actual_result, expected_result)

    def test_chars(self):
        data = {'digits_string': 'a022'}
        req = Mock(get_json=Mock(return_value=data), args=data)
        actual_result = handler(req)
        expected_result = ('Input must be integer in interval [1 ... 3999]', 500)
        self.assertEqual(actual_result, expected_result)

    def test_too_big(self):
        data = {'digits_string': '4422'}
        req = Mock(get_json=Mock(return_value=data), args=data)
        actual_result = handler(req)
        expected_result = ('Input must be <= 3999]', 500)
        self.assertEqual(actual_result, expected_result)

    def test_missing_key(self):
        data = {'digit_string': '4422'}
        req = Mock(get_json=Mock(return_value=data), args=data)
        actual_result = handler(req)
        expected_result = ('There is no digits_string key in payload', 500)
        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()
