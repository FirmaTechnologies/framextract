# Frame Extractor
A CLI library to extract frames from a video

## Installation
PyPI
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
pip install wheel -r requirements.txt
bumpversion [major][minor][patch]
python setup.py sdist bdist_wheel
twine check dist/*
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
twine upload dist/*
```
