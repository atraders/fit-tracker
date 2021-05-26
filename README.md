# Fit Tracker

A lightweight package to track training of statistical/ML models. Inspired by MLFlow tracking, but
with a simpler implementation.


# Quickstart

Fit tracker provides a transparent and simple way to log the results of experiments such as
training a ML/statistical models, or running a numerical simulation where events might be indexed
by integers or dates.

The only tracker implemented so far is the `FileTracker`, that writes a log file on your disk.
``` python
tracker = FileTracker('path/to/logfile.log')
```

Three logging methods are available:
- `.log_params(dictionary: Optional[Dict] = None, **kwargs)` that can be used at the beginning of
  the training to log initial parameters (anything that can be converted to string), either as a
  `dict` argument or as keyword arguments (or both);
- `.log_event(index: Union[int, datetime], dictionary: Optional[Dict] = None, **kwargs)`, 
  typically used multiple times to log various events of a simulation; for instance performance
  metrics for each folds, or for each time-series split in a time-series setting;
- `.log_results(dictionary: Optional[Dict] = None, **kwargs)`, similar to `.log_params` but to be
  called at the end of the script.

The function `fit_tracker.parsers.parse_log_file(log_file_path: Union[str, Path])` can be used to
recover the logged experiments, split by run.

# Example with scikit-learn