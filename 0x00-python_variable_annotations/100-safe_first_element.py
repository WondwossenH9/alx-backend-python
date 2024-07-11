# The types of the elements of the input are not know
from typing import Any, List, Optional

def safe_first_element(lst: List[Any]) -> Optional[Any]:
    if lst:
        return lst[0]
    else:
        return None
