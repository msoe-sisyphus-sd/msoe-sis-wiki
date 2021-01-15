# Possible Interfaces

## C-Libraries
* Open Sound System - https://en.wikipedia.org/wiki/Open_Sound_System
    * Seems to be deprecated / dis-included from the latest Raspbian image
* Advance Linux Sound Architecture - https://www.alsa-project.org/wiki/Main_Page
    * Comes with Debian and is the de-facto replacement for OSS
* Pulse Audio - https://www.freedesktop.org/wiki/Software/PulseAudio/
    * 
* Port Audio - http://www.portaudio.com/

## Python Interfaces
* `ossaudiodev` - https://docs.python.org/3/library/ossaudiodev.html
* `pyaudio` - http://people.csail.mit.edu/hubert/pyaudio/
* `sounddevice` - https://python-sounddevice.readthedocs.io/en/0.4.1/
* `pyalsaaudio` - http://larsimmisch.github.io/pyalsaaudio/index.html#
* `pulsectl` - https://pypi.org/project/pulsectl/

# Pro-Con Lists

## `ossaudiodev`
* Interfaces with the OSS library/driver

### Pro
* Native support in Python

### Con
* "Deprecated" in modern Linux distributions

# Evaluation Chart

## Criteria

# Hardware

## USB Microphone

### Pro
* Better audio quality at low range entry

### Con

## USB Sound Card and 3.5mm Microphone

### Pro
* Low entry cost
* Modular
* Non-intrusive integration with table (small and won't be a visual blight)
* Native audio pass through with ALSA
    * In testing if I had my headphones and a mic. plugged into the sound card I would hear the mic. input live - possibility to easily redirect input to another process.

### Con
* Increased failure risk (more parts means more opportunity for failure)
* Reduced audio quality at low range entry

# Testing and Code

## Verify Microphone Input
* List all input audio devices
```
arecord -l
```

* Record sound
```
arecord -f S16_SE -d 10 -r 16000 --device=<use attributes from arecord -l output> recording.wav [-c <# of channels (stereo or mono>]
```