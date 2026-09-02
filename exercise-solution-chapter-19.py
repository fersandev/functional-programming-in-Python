from dataclasses import dataclass
from typing import Union

@dataclass(frozen=True)
class Ok:
    value: object

    def map(self, func):
        return Ok(func(self.value))

@dataclass(frozen=True)
class Err:
    error: str

    def map(self, func):
        return self

Result = Union[Ok, Err]

def safe_divide(a, b) -> Result:
    if b == 0:
        return Err("you cannot divide by zero")
    return Ok(a / b)

resultado = (
    safe_divide(20, 4)
    .map(lambda x: x + 1)
    .map(lambda x: x * 10)
)

print(resultado)  # Ok(value=60.0)
