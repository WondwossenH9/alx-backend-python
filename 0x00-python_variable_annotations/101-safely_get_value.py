#!/usr/bin/env python3
from typing import Any, Dict, Optional, TypeVar

T = TypeVar('T')

def safely_get_value(dct: Dict[Any, T], key: Any, default: Optional[T] = None) -> Optional[T]:
    """
    Safely retrieves a value from a dictionary, returning a default value if the key is not present.
    """
    if key in dct:
        return dct[key]
    else:
        return default
