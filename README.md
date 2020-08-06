# imgextract
[![CircleCI](https://circleci.com/gh/FirmaTechnologies/framextract.svg?style=shield)](https://circleci.com/gh/FirmaTechnologies/framextract)

A CLI library to extract frames from a video

## Installation
[PyPI](https://pypi.org/project/frame-extractor/)
```bash
pip install frame-extractor
```

## Usage
CLI
```bash
framextract <inputfile> -o <outputfolder> -f <framerate>
```

## Development
MacOS
```bash
python -m venv venv
source venv/bin/activate
pip install [wheel] -r requirements.txt
bumpversion [--tag] [--commit] [major|minor|patch]
python setup.py sdist [bdist_wheel]
twine check dist/*
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
twine upload dist/*
```
