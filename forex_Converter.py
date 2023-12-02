from forex_python.converter import CurrencyRates

c = CurrencyRates()

amount = float(input("Enter the amount: "))
from_currency, to_currency = input("From Currency: ").upper(), input("To Currency: ").upper()

result = c.convert(from_currency, to_currency, amount)
print(f" {amount} {from_currency} to {to_currency} : {result}")
