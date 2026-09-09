from typing import Callable, TypeVar
from typing_extensions import ParamSpec
from functools import wraps

P = ParamSpec("P")
R = TypeVar("R")

def logged(func: Callable[P, R]) -> Callable[P, R]:
    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        return func(*args, **kwargs)
    return wrapper

@logged
def greet(name: str, times: int) -> str:
    return (name + " ") * times

print(greet("Ana", 3))
print(greet("Bob", "3"))
