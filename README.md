pipboy
======

This is my local copy that I can hack on to minimize the codebase and simplify it.

The 'pypboy' directory contains the original that we know works (for reference)

## Installation

### HyperPixel
Follow [the instructions](https://github.com/pimoroni/hyperpixel4/issues/177) at Pimoroni's github site for enabling the HyperPixel display in the kernel.

TL;DR: enable the screen with the following line in `/boot/firmware/config.txt`
```
dtoverlay=vc4-kms-dpi-hyperpixel4sq
```

### Libraries
```
$ sudo apt-get update
$ sudo apt-get install git python3-dev libsdl2-dev libsdl2-image-2.0-0 libsdl2-ttf-2.0-0 libopenblas-dev libopenjp2-7-dev
```

### Packages

(NOTE: On the pi zero 2 w with Bookworm I found that I needed to use the system-installed python/SDL intead of making a virtual environment. Using the latest versions of both in the virtual environment didn't work- the screen doesn't get initialized properly by pygame). This is the configuration that worked for me.

```
bill@pipboy:~/dev/pipboy $ python
Python 3.11.2 (main, May  2 2024, 11:59:08) [GCC 12.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import pygame
pygame 2.1.2 (SDL 2.26.5, Python 3.11.2)
Hello from the pygame community. https://www.pygame.org/contribute.html
>>>
```

To override a system package (since python now yells at you when you try it):

```
$ pip install --break-system-packages xmldict
```



(Original instructions with venv)

Make a Virtual Environment

```
$ git clone https://github.com/BillDett/pipboy.git
$ cd pipboy
$ python -m venv ./.venv
$ source ./.venv/bin/activate
$ python3 setup.py install
$ pip install -r requirements.txt
```

Set up the [alternate i2c interface](https://learn.pimoroni.com/article/getting-started-with-hyperpixel-4#using-the-alternate-i2c-interface-on-hyperpixel-4-0-for-advanced-users) for the Hyperpixel display since we need GPIO pins for the rotary switch.

```
$ sudo ln -s /dev/i2c-3 /dev/i2c-1
```


## Run it
```
$ python3 main.py
```
