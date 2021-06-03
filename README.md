# ScreenBrightnessControl
Brightness Control App based on QT and screen_brightness_control. Creates a tray icon with a slider where you can change the brightness

I made this because some OS's don't want to natively support this feature unless it is an integrated display (laptop for example)

## Requirements

* Python 3.8
* PyQT5
* screen_brightness_control
* pyinstaller (used for creating an executable)

## Installation

A build for Windows can be found in the releases section, though it can be built using pyinstaller using the install script.

```shell script
pyinstaller brightnesscontol.spec
```