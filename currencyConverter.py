from tabulate import tabulate
from currency_converter import CurrencyConverter


class Currency_converter(object):
    def __init__(self, amount, current, converted):
        self.amount = amount
        self.current = current
        self.converted = converted

        self.parser = CurrencyConverter()

    def values(self):
        try:
            result = round(self.parser.convert(self.amount, self.current, self.converted), 2)
            data = {
                "Current Currency": [str(f"{self.amount} {self.current}")],
                "Converted Currency": [str(f"{result} {self.converted}")]
            }
            return data

        except:
            print("Need currency amount, current currency & conversion currency")

    def __repr__(self):
        values = self.values()
        return tabulate(values, headers="keys", tablefmt="pretty")


if __name__ == "__main__":
    currency = Currency_converter(1, "USD", "INR")
    print(currency)
