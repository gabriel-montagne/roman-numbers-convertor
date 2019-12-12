from re import match

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
    if not match(r'^[0-9]+$', string):
        raise Exception('Input must be integer in interval [1 ... 3999]')
    digit_number = int(string)
    if digit_number < 0 or digit_number > 3999:
        raise Exception('Input must be <= 3999]')
    return digit_number


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


def convert_number(digit_string):
    digit_numeral = validate_input(digit_string)
    roman_numeral = ''
    for i in range(4):
        digit = digit_numeral % 10
        roman_numeral = convert_digit(digit, i) + roman_numeral
        digit_numeral = digit_numeral // 10
    return roman_numeral


if __name__ == '__main__':
    number = validate_input('12')
    print(convert_number(number))
