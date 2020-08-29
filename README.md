# frame-extractor
[![CircleCI](https://circleci.com/gh/FirmaTechnologies/framextract.svg?style=shield)](https://circleci.com/gh/FirmaTechnologies/framextract)
![PyPI](https://img.shields.io/pypi/v/frame-extractor)

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

## [Development](https://realpython.com/certificates/b677c954-49fe-495b-963c-a05f39b6725a/)
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

## [Tests](https://test.pypi.org/project/frame-extractor/)
```zsh
pytest --durations=3 --cov-report=html --cov=framextract
```
