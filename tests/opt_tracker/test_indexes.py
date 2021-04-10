import pytest
from datetime import datetime

from opt_tracker import indexes


def test_int_index_to_str():
    for malformed_index in [1.1, 'wrong', False, datetime.now()]:
        with pytest.raises(AssertionError):
            indexes.int_index_to_str(malformed_index)
    
    assert indexes.int_index_to_str(1) == 'int1'
    assert indexes.int_index_to_str(-10) == 'int-10'
