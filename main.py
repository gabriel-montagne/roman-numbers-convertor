import json
import re

ROMAN_MAP = {
    0: {'1': 'I', '2': 'II', '3': 'III', '4': 'IV', '5': 'V', '6': 'VI', '7': 'VII', '8': 'VIII', '9': 'IX'},
    1: {'1': 'X', '2': 'XX', '3': 'XXX', '4': 'XL', '5': 'L', '6': 'LX', '7': 'LXX', '8': 'LXXX', '9': 'XC'},
    2: {'1': 'C', '2': 'CC', '3': 'CCC', '4': 'CD', '5': 'D', '6': 'DC', '7': 'DCC', '8': 'DCCC', '9': 'CM'},
    3: {'1': 'M', '2': 'MM', '3': 'MMM'}
}


def convert_digit(power, digit):
    """
    Converts a digit in roman numeral system for the given power of ten
    :param power:
    :param digit:
    :return:
    """
    return ROMAN_MAP[power][digit]


def convert_number(number: int):
    """
    Converts a digit number into a roman numeral
    :param number:
    :return:
    """
    return ''.join([convert_digit(i, n) for i, n in enumerate(list(str(number))[::-1])][::-1])


def validate_input(number):
    if type(number) is int:
        if number < 0 or number > 3999:
            return None, 'Input must be integer in interval [1 ... 3999]'
    else:
        return None, 'key "number" must be integer!'

    return number, None


def handler(request):
    request_json = request.get_json()
    if request_json and 'number' in request_json:
        number = request_json['number']
        digit_numeral, error_message = validate_input(number)
        if error_message:
            return error_message, 500
        return json.dumps({'result': convert_number(digit_numeral)})
    else:
        return 'There is no "number" key in payload', 500


if __name__ == "__main__":
    from flask import Flask, request

    app = Flask(__name__)


    @app.route('/handler', methods=['POST'])
    def index():
        return handler(request)


    app.run('0.0.0.0', 5000, debug=True)
