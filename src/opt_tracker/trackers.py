from pathlib import Path
from typing import Dict, Optional
from datetime import datetime
import os
import json

from opt_tracker import indexes

LOG_SEP = '##'


def jsonize(dictionary: Optional[Dict] = None, **kwargs) -> str:
    if dictionary is None:
        logganda = dict()
    logganda.update(**kwargs)
    return json.dumps(logganda)


class FileTracker:

    def __init__(self, log_file: Union[str, Path]):
        self.log_file = Path(log_file)
        self.log_file.parent().mkdir(parents=True, exist_ok=True)
        with open(self.log_file, 'a') as log:
            log.write('-- START -- ')

    def _write_log_line(self, index_str: str, json_str: str) -> None:
        log_datetime = datetime.now().strftime()
        with open(self.log_file, 'a+') as log:
            log.write(LOG_SEP.join([log_datetime, index_str, json_str]))

    def log_params(dictionary: Optional[Dict] = None, **kwargs):
        index_str = indexes.index_to_str(indexes.Index.BEGIN)
        params_str = jsonize(dictionary, **kwargs)
        self._write_log_line(index_str, params_str)
        
        
    def log_event(index: Union[int, datetime], dictionary: Optional[Dict] = None, **kwargs):
        index_str = indexes.index_to_str(index)
        params_str = jsonize(dictionary, **kwargs)
        self._write_log_line(index_str, params_str)

    def log_results(dictionary: Optional[Dict] = None, **kwargs):
        index_str = indexes.index_to_str(indexes.Index.END)
        params_str = jsonize(dictionary, **kwargs)
        self._write_log_line(index_str, params_str)
