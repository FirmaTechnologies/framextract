# frame-extractor
[![CircleCI](https://circleci.com/gh/FirmaTechnologies/framextract.svg?style=shield)](https://circleci.com/gh/FirmaTechnologies/framextract)

A CLI library to extract frames from a video

## Installation
[PyPI](https://pypi.org/project/frame-extractor/)
```zsh
pip install frame-extractor
```

## Usage
CLI
```zsh
framextract <inputfile> --get-info-only -o <outputfolder> -f <framerate>
```

## Development
MacOS
```zsh
python -m venv venv
source venv/bin/activate
pip install [wheel] -r requirements.txt
bumpversion [--tag] [--commit] [major|minor|patch]
python setup.py sdist [bdist_wheel]
twine check dist/*
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
twine upload dist/*
```

## Tests
```zsh
pytest --durations=3 --cov-report=html --cov=framextract
```
