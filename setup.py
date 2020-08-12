import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE/'README.md').read_text()

# This call to setup() does all the work
setup(
    name='frame-extractor',
    version='0.2.1',
    description='Extract frames from a video',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/FirmaTechnologies/framextract',
    author='ngchanway',
    author_email='chan_way@firma-tech.com',
    license='GPL-3.0',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Topic :: Multimedia :: Video'
    ],
    packages=['framextract'],
    include_package_data=True,
    install_requires=[
        'numpy',
        'opencv-python'
    ],
    entry_points={
        'console_scripts': [
            'framextract=framextract.__main__:main'
        ]
    }
)
