from pathlib import Path
from uuid import uuid4

from fit_tracker.trackers import FileTracker


def remove_log_time(log_content: str) -> str:
    rows = log_content.split("\n")
    log_with_no_timestamps = "\n".join(
        [" - ".join(row.split(" - ")[1:]) for row in rows]
    )
    return log_with_no_timestamps


def assert_log_equality(log_content1: str, log_content2: str):
    log1_with_no_timestamps = remove_log_time(log_content1)
    log2_with_no_timestamps = remove_log_time(log_content2)
    assert log1_with_no_timestamps == log2_with_no_timestamps


def test_file_tracker():
    temp_log_file_name = f"{uuid4()}test.log"
    ft = FileTracker(Path.home() / temp_log_file_name)
    ft.log_params({"input": "dictionary", "welwala": 1})
    ft.log_params(keywordargument=1.1)
    ft.log_event(index=0, dictionary={"first_event": "test"}, otherkey=True)
    ft.log_event(index=1, dictionary={"second_event": "test2"}, otherkey=False)
    ft.log_results(allgood=True)

    with open(Path(__file__).parent / "test.log", "r") as test_log_file:
        desired_log_result = test_log_file.read()

    with open(Path.home() / temp_log_file_name, "r") as this_log_file:
        written_log_result = this_log_file.read()

    assert_log_equality(desired_log_result, written_log_result)
