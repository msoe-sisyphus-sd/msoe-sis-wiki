# Possible Interfaces

## C-Libraries
* Open Sound System - https://en.wikipedia.org/wiki/Open_Sound_System
    * Seems to be deprecated / dis-included from the latest Raspbian image
* Advance Linux Sound Architecture - https://www.alsa-project.org/wiki/Main_Page
    * Comes with Debian and is the de-facto replacement for OSS
* Pulse Audio - https://www.freedesktop.org/wiki/Software/PulseAudio/
    * Audio server - lots of features but a bit more complex then we probably need
    * Not evaluated
* Port Audio - http://www.portaudio.com/
    * Cross platform Audio API 

## Python Interfaces
* `ossaudiodev` - https://docs.python.org/3/library/ossaudiodev.html
* `pyaudio` - http://people.csail.mit.edu/hubert/pyaudio/
* `sounddevice` - https://python-sounddevice.readthedocs.io/en/0.4.1/
* `pyalsaaudio` - http://larsimmisch.github.io/pyalsaaudio/index.html#
* `pulsectl` - https://pypi.org/project/pulsectl/
    * Wrapper for Pulse Audio which wasn't evaluated - noted as an alternative in the worst case scenario

# Pro-Con Lists

## `ossaudiodev`
* Interfaces with the OSS library/driver

### Pro
* Native support in Python

### Con
* "Deprecated" in modern Linux distributions

## `pyAudio`
* Interfaces with PortAudio

### Pro
* Supports blocking and callback streaming
* Used in the spikes and ML project being currently used (2021-01-21)
* Supports OSS, ALSA under the hood

### Con
* Requires PortAudio

### Note
* The current ML spike/solution uses an additional package called `pyAudioAnalysis` but to the Team's current understanding - `pyAudio` is not required to use this package.

## `sounddevice`
* Interfaces with PortAudio
* Was used in a spike/demo for setting the light's brightness based on audio levels
* Uses `numpy` to handle data

### Pro
* Support 
* Smaller API foot print than `pyAudio`
* Supports blocking and callback streaming

### Con
* Requires PortAudio

## `pyalsaaudio`
* Low level wrapper on the ALSA interface

### Pro
* Specific to Linux environment without the need for a Sound API
* Forces use of the PCM

### Con
* Extremely low level API leaves too much control to the developer

# Hardware

## USB Microphone

### Pro
* Better audio quality at low range entry

### Con
* Bulky 
* Hard to fit into the current table aesthetic (color, form, distraction)

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

# Decisions

* A USB microphone should be used to provide the ML model the cleanest data (due to the "garbage in, garbage out" principle)

* `pyAudio` and `PortAudio` are the sound APIs of choice