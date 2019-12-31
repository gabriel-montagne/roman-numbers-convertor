import json
from unittest.mock import Mock

import pytest

from main import handler

test_data = [
    (1111, 'MCXI'), (2222, 'MMCCXXII'), (3333, 'MMMCCCXXXIII'), (444, 'CDXLIV'), (555, 'DLV'),
    (666, 'DCLXVI'), (777, 'DCCLXXVII'), (888, 'DCCCLXXXVIII'), (999, 'CMXCIX')
]


@pytest.mark.parametrize('n, expected', test_data)
def test_1(n, expected):
    data = {'number': n}
    req = Mock(get_json=Mock(return_value=data), args=data)
    actual_result = handler(req)
    expected_result = json.dumps({'result': expected})
    assert actual_result == expected_result


def test_str():
    data = {'number': '122'}
    req = Mock(get_json=Mock(return_value=data), args=data)
    actual_result = handler(req)
    expected_result = ('key "number" must be integer!', 500)
    assert actual_result == expected_result


def test_too_big():
    data = {'number': 4422}
    req = Mock(get_json=Mock(return_value=data), args=data)
    actual_result = handler(req)
    expected_result = ('Input must be <= 3999]', 500)
    assert actual_result, expected_result


def test_missing_key():
    data = {'some-key': '4422'}
    req = Mock(get_json=Mock(return_value=data), args=data)
    actual_result = handler(req)
    expected_result = ('There is no "number" key in payload', 500)
    assert actual_result == expected_result


if __name__ == '__main__':
    unittest.main()
