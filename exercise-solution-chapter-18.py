from dataclasses import dataclass

@dataclass(frozen=True)
class Money:
    amount: float
    currency: str

def add_money(a: Money, b: Money) -> Money:
    if a.currency != b.currency:
        raise ValueError("The currencies must be equal.")

    return Money(
        amount=a.amount + b.amount,
        currency=a.currency
    )

# Correct case
money1 = Money(10, "USD")
money2 = Money(5, "USD")
result = add_money(money1, money2)
print(result) # Money(amount=15, currency='USD')

# Incorrect case
money3 = Money(5, "EUR")
try:
    result = add_money(money1, money3)
    print(result)
except ValueError as e:
    print(e)
