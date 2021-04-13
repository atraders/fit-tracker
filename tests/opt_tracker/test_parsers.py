import datetime
from pathlib import Path

from opt_tracker import parsers
from opt_tracker.indexes import Index


def test_parse_log_file():
    desired = [
        [
            (
                datetime.datetime(2021, 4, 12, 18, 22),
                Index.HEADER,
                {"init": "FileTracker"},
            ),
            (
                datetime.datetime(2021, 4, 12, 18, 22),
                Index.BEGIN,
                {"input": "dictionary", "welwala": 1},
            ),
            (
                datetime.datetime(2021, 4, 12, 18, 22),
                Index.BEGIN,
                {"keywordargument": 1.1},
            ),
            (
                datetime.datetime(2021, 4, 12, 18, 23),
                0,
                {"first_event": "test", "otherkey": True},
            ),
            (
                datetime.datetime(2021, 4, 12, 18, 23),
                1,
                {"second_event": "test2", "otherkey": False},
            ),
            (datetime.datetime(2021, 4, 12, 18, 24), Index.END, {"allgood": True}),
        ]
    ]
    assert parsers.parse_log_file(Path(__file__).parent / "test.log") == desired
