from typing import Tuple, Union, Dict, Any, List
from pathlib import Path
from datetime import datetime
import json

from opt_tracker.trackers import LOG_SEP, LOG_DATE_FORMAT
from opt_tracker.indexes import str_to_index, Index

Record = Tuple[datetime, Union[Index, datetime, int], Dict[str, Any]]


def parse_row(row: str) -> Record:
    log_date_str, index, payload = row.split(LOG_SEP)
    log_datetime = datetime.strptime(log_date_str, LOG_DATE_FORMAT)
    return log_datetime, str_to_index(index), json.loads(payload)


def parse_log_file(log_file_path: Union[str, Path]) -> List[List[Record]]:
    log_file_path = Path(log_file_path)
    with open(log_file_path, 'r') as log_file:
        rows = log_file.readlines()

    records = list(map(parse_row, rows))

    reports: List = []
    for rec in records:
        if rec[1] == Index.HEADER:
            reports.append([])
        reports[-1].append(rec)

    return reports
