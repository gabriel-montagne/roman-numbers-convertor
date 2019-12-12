import unittest
import pytest
from main import convert_number


class ConvertNumberToRomanNumeralCase(unittest.TestCase):
    def test_1(self):
        actual_result = convert_number('12')
        expected_result = 'XII'
        self.assertEqual(actual_result, expected_result)

    def test_2(self):
        actual_result = convert_number('79')
        expected_result = 'LXXIX'
        self.assertEqual(actual_result, expected_result)

    def test_3(self):
        actual_result = convert_number('225')
        expected_result = 'CCXXV'
        self.assertEqual(actual_result, expected_result)

    def test_4(self):
        actual_result = convert_number('2922')
        expected_result = 'MMCMXXII'
        self.assertEqual(actual_result, expected_result)

    def test_chars(self):
        with pytest.raises(Exception) as e_info:
            assert convert_number('a022')
        assert str(e_info.value) == 'Input must be integer in interval [1 ... 3999]'

    def test_too_big(self):
        with pytest.raises(Exception) as e_info:
            assert convert_number('4422')
        assert str(e_info.value) == 'Input must be <= 3999]'


if __name__ == '__main__':
    unittest.main()
