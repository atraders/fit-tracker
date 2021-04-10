from pathlib import Path
from typing import Dict, Optional, Union, Any
from datetime import datetime
import json

from opt_tracker import indexes

LOG_SEP = ' - '
LOG_DATE_FORMAT = r'%Y-%m-%d-%H:%M'


def unite_kwargs(dictionary: Optional[Dict] = None, **kwargs) -> Dict[str, Any]:
    if dictionary is None:
        logganda: Dict[Any, Any] = dict()
    logganda.update(**kwargs)
    return logganda


class FileTracker:

    def __init__(self, log_file: Union[str, Path]):
        self.log_file = Path(log_file)
        self.log_file.parent.mkdir(parents=True, exist_ok=True)
        self.write_log_line(
            indexes.index_to_str(indexes.Index.BEGIN),
            {'init': self.__class__.__name__}
        )

    def write_log_line(self, index_str: str, params: Dict[str, Any]) -> None:
        log_datetime = datetime.now().strftime(LOG_DATE_FORMAT)
        with open(self.log_file, 'a+') as log:
            log.write(LOG_SEP.join([log_datetime, index_str, json.dumps(params)]))
            log.write('\n')

    def log_params(self, dictionary: Optional[Dict] = None, **kwargs):
        index_str = indexes.index_to_str(indexes.Index.BEGIN)
        params = unite_kwargs(dictionary, **kwargs)
        self.write_log_line(index_str, params)

    def log_event(self, index: Union[int, datetime], dictionary: Optional[Dict] = None, **kwargs):
        index_str = indexes.index_to_str(index)
        params = unite_kwargs(dictionary, **kwargs)
        self.write_log_line(index_str, params)

    def log_results(self, dictionary: Optional[Dict] = None, **kwargs):
        index_str = indexes.index_to_str(indexes.Index.END)
        params = unite_kwargs(dictionary, **kwargs)
        self.write_log_line(index_str, params)
