from typing import Tuple, Union, Dict, Any
from pathlib import Path
from datetime import datetime
import json

from .trackers import LOG_SEP, LOG_DATE_FORMAT
from .indexes import str_to_index, Index


def parse_row(row: str) -> Tuple[datetime, Union[Index, datetime, int], Dict[str, Any]]:
    log_date_str, index, payload = row.split(LOG_SEP)
    log_datetime = datetime.strptime(log_date_str, LOG_DATE_FORMAT)
    return log_datetime, str_to_index(index), json.loads(payload)


def parse_log_file(log_file_path: Union[str, Path]):
    log_file_path = Path(log_file_path)
    with open(log_file_path, 'r') as log_file:
        rows = log_file.readlines()

    records = list(map(parse_row, rows))

    reports = []
    for rec in records:
        if rec[1] == Index.HEADER:
            reports.append([])
        reports[-1].append(rec)

    return reports
