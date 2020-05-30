# pycontw-inspector

pycontw-inspector is an integrated analyzer that can extract various types of raw data (e.g. attendee, programs, checkins), and inspect some valuable information via customized strategies construct by each team with their different domain knowledge.

# Getting Started
## Prerequisites
- Python 3.8

## Obtain data
Analyzer will use mock_data with directory `./mock_data/` by default, you can refresh it via run `pipenv run python analyzer/utils/mock_data.py`. For real data, please contact conributors listed below.

## Run Analyzer
An example program `analyzer/app.py` would be a great choice for the first try, run it by
```
pipenv run python analyzer/app.py
```

## Configuration
You can set up configs in `analyzer/config.py` easily, please refer to the code for advanced instructions.

# Development
## Architecture
pycontw-inspector currently construct by four layers:
- extractor:
    extract raw data from file.
- provider:
    collect data form all extractor and provide more explainable data for inspecting.
- inspector:
    inspect valuable information via implementing strategies.
- visualizer:
    visualize the results data.

## Default Raw Data File Tree
```
data
├── attendee
│   ├── discount_2019.csv
│   ├── reserved_2019.csv
│   └── standard_2019.csv
├── programs
│   └── program_2019.csv
└── vacancies
    ├── cake_resume.csv
    └── linked_in.csv
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

### For Test
- inv test.pytest

# Contributors
- [Rain Wu](https://github.com/RainrainWu)