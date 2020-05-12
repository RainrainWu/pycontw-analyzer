# pycontw-inspector

pycontw-inspector is an integrated analyzer that can extract various types of raw data (e.g. attendee, programs, checkins), and inspect some valuable information via customized strtegies construct by each team with their different domain knowledge.

# Getting Started
## Prerequisites
- Python 3.8

## Run Analyzer
An example program `analyzer/app.py` would be a great choice for the first try, run it by
```
pipenv run python analyzer/app.py
```

## Configuration
You can set up configs in `analyzer/config.py` easily, please refer to the code for advanced instructions.

# Development
## Architecture
pycontw-inspector currently construct by three layers:
- extractor:
    extract raw data from file.
- provider:
    collect data form all extractor and provide more explainable data for inspecting.
- inspector:
    inspect valuable information via implementing strategies.

## Default Raw Data Tree
```
data
├── attendee
│   ├── discount.csv
│   ├── reserved.csv
│   └── standard.csv
└── programs
    └── program_2019.csv
```

## Execute Task
[invoke](https://pypi.org/project/invoke/) is used for the tasks management, some available tasks list below:

### For Environment
- inv env.clean
- inv env.init

### For Style
- inv style.pylint
- inv style.flake8
- inv style.blackcheck
- inv style.black

### For Test
- inv test.pytest

# Contributors
- [Rain Wu](https://github.com/RainrainWu)