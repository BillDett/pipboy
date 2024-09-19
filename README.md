pipboy
======

This is my local copy that I can hack on to minimize the codebase and simplify it.

The 'pypboy' directory contains the original that we know works (for reference)

## Installation

### HyperPixel
Follow [the instructions](https://shop.pimoroni.com/products/hyperpixel-4?variant=12569485443155) at Pimoroni's site for enabling the HyperPixel display in the kernel.

NOTE: enable the screen with the following line in `/boot/firmware/config.txt`
```
dtoverlay=vc4-kms-dpi-hyperpixel4sq
```

### Libraries
```
$ sudo apt-get update
$ sudo apt-get install git python3-dev libsdl2-dev libsdl2-image-2.0-0 libsdl2-ttf-2.0-0 libopenblas-dev libopenjp2-7-dev
```

### Packages

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
