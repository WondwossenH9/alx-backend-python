#!/usr/bin/env python3
from typing import Any, Dict, Optional

def safely_get_value(dct: Dict[Any, Any], key: Any, default: Optional[Any] = None) -> Optional[Any]:
    """
    Safely retrieves a value from a dictionary, returning a default value if the key is not present.
    """
    if key in dct:
        return dct[key]
    else:
        return default
