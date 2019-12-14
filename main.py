import json
import re

ROMAN_SYMBOLS = {
    0: {
        '1': 'I',
        '5': 'V',
    },
    1: {
        '1': 'X',
        '5': 'L',
    },
    2: {
        '1': 'C',
        '5': 'D',
    },
    3: {
        '1': 'M'
    }
}


def validate_input(string):
    if not re.match(r'^[0-9]+$', string):
        return None, 'Input must be integer in interval [1 ... 3999]'
    digit_number = int(string)
    if digit_number < 0 or digit_number > 3999:
        return None, 'Input must be <= 3999]'
    return digit_number, None


def convert_digit(digit, power):
    result = ''
    if digit < 5:
        if digit < 4:
            result = ROMAN_SYMBOLS[power]['1'] * digit
        else:
            result = ROMAN_SYMBOLS[power]['1'] + ROMAN_SYMBOLS[power]['5']
    else:
        if digit < 9:
            result = ROMAN_SYMBOLS[power]['5'] + (digit - 5) * ROMAN_SYMBOLS[power]['1']
        else:
            result = (digit - 8) * ROMAN_SYMBOLS[power]['1'] + ROMAN_SYMBOLS[power + 1]['1']
    return result


def convert_number(digit_numeral):
    roman_numeral = ''
    for i in range(4):
        digit = digit_numeral % 10
        roman_numeral = convert_digit(digit, i) + roman_numeral
        digit_numeral = digit_numeral // 10
    return roman_numeral


def handler(request):
    request_json = request.get_json()
    if request_json and 'digits_string' in request_json:
        digits_string = request_json['digits_string']
        digit_numeral, error_message = validate_input(digits_string)
        if error_message:
            return error_message, 500
        return json.dumps({'result': convert_number(digit_numeral)})
    else:
        return 'There is no digits_string key in payload', 500


if __name__ == "__main__":
    from flask import Flask, request
    app = Flask(__name__)

    @app.route('/handler')
    def index():
        return handler(request)

    app.run('0.0.0.0', 5000, debug=True)