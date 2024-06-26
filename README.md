pipboy
======

This is my local copy that I can hack on to minimize the codebase and simplify it.

The 'pypboy' directory contains the original that we know works (for reference)

## Installation

### Libraries
```
$ sudo apt-get update
$ sudo apt-get install libsdl2-dev libsdl2-image-2.0-0 libsdl2-ttf-2.0-0 libopenblas-dev libopenjp2-7-dev
```

### Packages

Make a Virtual Environment

```
$ python -m venv ./.venv
$ source ./.venv/bin/activate
$ python3 setup.py install
$ pip install -r requirements.txt
```


## Run it
```
$ python3 main.py
```
