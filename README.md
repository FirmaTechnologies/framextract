# Frame Extractor
A CLI library to extract frames from a video

## Installation
PyPI
```
$ pip install frame-extractor
```

## Usage
CLI
```
$ framextract <inputfile> -o <outputfolder> -f <framerate>
```

## Development
```
bumpversion [major][minor][patch]
python setup.py sdist bdist_wheel
twine check dist/*
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
twine upload dist/*
```
