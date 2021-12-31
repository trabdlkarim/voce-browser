# Voce Browser

![GPL License](https://img.shields.io/badge/license-GPLv3-green) ![Platforms](https://img.shields.io/powershellgallery/p/DNS.1.1.1.1)
![Python v3.7](https://img.shields.io/github/pipenv/locked/python-version/metabolize/rq-dashboard-on-heroku) ![Build passing](https://img.shields.io/github/workflow/status/actions/toolkit/Main%20workflow) ![Speech Recognition](https://img.shields.io/badge/speech-recognition-important) ![gTTS](https://img.shields.io/badge/gTTS-2.1.1-blueviolet) ![PyQt5](https://img.shields.io/badge/PyQt5-5.12.3-red)


Voce Browser is a chromium based voice controlled browser using PyQtWebEngine. It has all the basic browser features like Chrome or Firefox and in addition it can be controlled with voice commands.

![Voce Browser](https://github.com/trabdlkarim/voce-browser/blob/master/screenshots/VoceScreenshot3.png)

![Voce Browser](https://github.com/trabdlkarim/voce-browser/blob/master/screenshots/VoceScreenshot6.png)

## Table of contents

* [Description](#description)
* [Features](#features)
* [Dependencies](#dependencies)
* [Setup](#setup)
* [License](#license)

## Description

This project uses the Qt GUI library Python binding as user interface. Voce Browser can be given voice commands which are translated and then exceuted using google speech recognition API. Its web engine is PyQtWebEngine, a chromium based engine.

## Features

Voce has all standard browser features, and plus voice commands capabilities.

### Supported Voice Commands

- Open tab: Open a new tab.
- Close tab: close current tab
- Open window: Open a new window.
- Close window: close current window
- Search: Search for a keyword. This command should be followed by a keyword.
- Go back: go back to the previous page if any
- Go forward: go to the next page if any
- Go home: go to the default homepage
- Reload page: Reload the current page
- Exit, bye and quit: Close all windows and exit the browser

## Dependencies

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
python3 setup.py build
python3 setup.py install
vocebrowser
```

or install a wheel distribution

```
python3 setup.py bdist_wheel
pip3 ./dist/*.whl install
./bin/startbrowser
```

## Notes:

### Running Commands System-wide

> If you want the **commands** in the **project bin** directory to be system wide, just create a bin directory (if does not exist) in your **home directory**. And copy the scripts in your home bin dir.
Finally add it to the **path** env variable and you're  done.

### Pydub Module

> The **pydub** module depends on **FFmpeg** package to render audio files so make sure it is installed on your system. For example, on Ubuntu you can install it with the following command: ***sudo apt install ffmpeg***. For more information go to: https://ffmpeg.org/  

### PyAudio Module

> If having troubles on installing PyAudio with Python higher than 3.7, then you should first try to the install the following packages as follows:

For Linux (Ubuntu)

```
sudo apt-get install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0
pip install pyaudio
```

For Wındows
```
pip install pipwin
pipwin install pyaudio
```



## License 

![GPL License](https://img.shields.io/badge/license-GPLv3-green)

This is an open-source project under the GPL-3.0 License
