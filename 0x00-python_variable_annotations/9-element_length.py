#!/usr/bin/env python3
'''task 9 module
'''
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''Compute length of list of sequences
    '''
    return [(i, len(i)) for i in lst]
