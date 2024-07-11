#!/usr/bin/env python3
'''task 7 module
'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''Convert key and value to a tuple
    '''
    return (k, float(v**2))
