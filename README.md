# Voce Browser
![GPL License](https://img.shields.io/badge/license-GPLv3-green) ![Platforms](https://img.shields.io/powershellgallery/p/DNS.1.1.1.1)
![Python v3.7](https://img.shields.io/github/pipenv/locked/python-version/metabolize/rq-dashboard-on-heroku) ![Build passing](https://img.shields.io/github/workflow/status/actions/toolkit/Main%20workflow) ![Speech Recognition](https://img.shields.io/badge/speech-recognition-important) ![gTTS](https://img.shields.io/badge/gTTS-2.1.1-blueviolet) ![PyQt5](https://img.shields.io/badge/PyQt5-5.12.3-red)


Voce Browser is a chromium based voice controlled browser using PyQtWebEngine. It has all the basic browser features like Chrome or Firefox and in addition it can be controlled with voice commands.

![Voce Browser](https://github.com/trabdlkarim/voce-browser/blob/master/screenshots/VoceScreenshot3.png)

![Voce Browser](https://github.com/trabdlkarim/voce-browser/blob/master/screenshots/VoceScreenshot6.png)

## Table of contents
* [Description](#description)
* [Features](#features)
* [Technologies](#technologies)
* [Setup](#setup)
* [License](#license)

## Description
This project uses the Qt GUI library Python binding as user interface. Voce Browser can be given voice commands which are translated and then exceuted using google speech recognition API. Its web engine is PyQtWebEngine, a chromium based engine.

## Features
Voce has all standard browser features and voice commands capabilities

## Technologies
This project is created with:
* PyQt5 5.12.3
* PyQtWebEngine 5.12.1
* SpeechRecognition: 3.8.1
* gTTS 2.1.1
* pydub
	
## Setup
To run the browser, first download or git clone this project and then install it locally in your Python environment as described below.

Supposing that you have already **Python3** and **pip3** installed on your system, from the terminal change the current directory to the project root directory. Proceed then as follows:

```
$ python3 setup.py build
$ python3 setup.py install
$ vocebrowser
```

or install a wheel distribution

```
$ python3 setup.py bdist_wheel
$ pip3 ./dist/*.whl install
$ ./bin/startbrowser
```
Note:
> If you want the **commands** in the **project bin** directory to be system wide, just create a bin directory (if does not exist) in your **home directory**. And copy the scripts in your home bin dir.
Finally add it to the **path** env variable and your  done.

## License ![GPL License](https://img.shields.io/badge/license-GPLv3-green)
Project under GPL-3.0 License
