from typing import Any, Callable, TypeVar, Tuple

T = TypeVar('T')

def is_reflexive(a:T, t_function:Callable[[T], T]) -> bool:
    return a == t_function(a)

def is_symmetric(a:T, b:T, t_function:Callable[[T,T], T]) -> bool:
    return t_function(a,b) == t_function(b,a)

def is_transitive(a:T,b:T,c:T, t_function:Callable[[T,T,T], T]) -> tuple:
    ...