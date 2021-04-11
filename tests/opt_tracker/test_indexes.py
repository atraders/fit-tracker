from datetime import datetime, timezone

import pytest

from opt_tracker import indexes


def test_int_index_to_str():
    for malformed_index in [1.1, 'wrong', False, datetime.now()]:
        with pytest.raises(TypeError):
            indexes.int_index_to_str(malformed_index)

    assert indexes.int_index_to_str(-10) == 'int-10'
    assert indexes.int_index_to_str(1) == 'int1'


def test_str_to_int_index():
    assert indexes.str_to_int_index('int0') == 0
    assert indexes.str_to_int_index('int1') == 1
    assert indexes.str_to_int_index('int-1') == -1
    with pytest.raises(AssertionError):
        indexes.str_to_int_index('float101010.0')
    with pytest.raises(AssertionError):
        indexes.str_to_int_index('int-10.0')
    with pytest.raises(AssertionError):
        indexes.str_to_int_index('int1e10')


def test_datetime_index_to_str():
    for malformed_index in [1.1, 'wrong', False, 10]:
        with pytest.raises(TypeError):
            indexes.datetime_index_to_str(malformed_index)

    date = datetime.fromtimestamp(1607727600.0, tz=timezone.utc)
    assert indexes.datetime_index_to_str(date) == 'ts1607727600.0'


def test_str_to_datetime_index():
    assert indexes.str_to_datetime_index('ts1607727600.0') == datetime.fromtimestamp(1607727600.0, tz=timezone.utc)
    with pytest.raises(AssertionError):
        indexes.str_to_int_index('dt101010.0')
    with pytest.raises(AssertionError):
        indexes.str_to_int_index('ts1io')

def test_index_to_str():
    pass


def test_str_to_index():
    pass
