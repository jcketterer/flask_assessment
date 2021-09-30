from forex_python.converter import (
    CurrencyRates,
    CurrencyCodes,
    Decimal,
    RatesNotAvailableError,
)

currency_rate = CurrencyRates(force_decimal=True)
currency_code = CurrencyCodes()


def final_amount(conv_from, conv_to, amount):
    entered_amount = Decimal(amount)
    final_amount = round(
        currency_rate.convert(conv_from.upper(), conv_to.upper(), entered_amount), 2
    )

    code_symbol = currency_code.get_symbol(conv_to)
    output = f"{code_symbol} {final_amount}"
    return output


def correct_curr_code(code):
    try:
        if not type(code) == str:
            return False
        amount = currency_rate.convert(code.upper(), "USD", Decimal(10.00))
        return True

    except RatesNotAvailableError:
        return False


def valid_number(number):
    try:
        num = float(number)

        if num <= 0:
            return False
        return True

    except ValueError:
        return False
