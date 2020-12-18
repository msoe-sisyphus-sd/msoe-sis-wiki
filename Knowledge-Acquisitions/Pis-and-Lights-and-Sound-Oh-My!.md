# Goal
The goal of this knowledge acquisition was to understand how audio input and output works on Raspberry Pis and what limitations exist to using the onboard audio interface when also using GPIO to drive the NeoPixel light strip. More specifically, the team wants to understand how the lights can interact with internal audio sources (e.g. a music stream from the internet) and external audio sources (e.g. a USB microphone monitoring the noise level in a given room).

# Background

## Sisyphus Industries
Sisyphus Industries (in particular Matt) have investigated this in the past but have not made any great strides in producing features. From what the team can tell there are no fragments in the codebase that enable any such feature so our investigation started from scratch.

We did reach out to Matt for assistance (only over email), but did not end up using much of his research, as we were able to get things working fine on our side, and his own observations were identical to our initial ones.

# Outcomes

## Internal Audio

One way that the table could be controlled via sound is having the Pi output an audio signal (to speakers perhaps) and have a Python process "hook into" this stream and changes the lights based off different qualities of the audio (e.g. volume, timbre, energy, etc.). However, an issue posed by the current setup is that the NeoPixel LED strip is controlled off GPIO Pin 18 which uses the 1 channel of the Pis PWM. This prevents stereo audio output and makes it challenging to use mono output. Additionally, it was discovered that even just plugging in a 3.5mm audio jack into the Pi would cause the LEDs to cease functioning. A workaround needed to be found.

### Solution

According to the [rpi_ws281x](https://github.com/jgarff/rpi_ws281x) library - different GPIO use different control chips (PWM for pin 18, PCM for pin 21, and SPI for pin 10) which all require different level of system configuration to use. Since we know PWM is a no go from the start, the next appropriate control to test was PCM. Switching the circuit and changing some Python variables to use pin 21 allowed the lights to run the same but also allowed simultaneous audio output via the analog jack when using `omxplayer`.

@burkhardtr did not test SPI as it required more config changes but would probably work just as fine. One issue in using PCM is that even though analog output is enabled, output over USB is still disabled which means external sound cards cannot be used in this setup (@burkhardtr naively attempted to use an external USB sound card when the LEDs were still driven off pin 18 to no avail). Additionally, during testing @burkhardtr was playing with `alsa` configs and seems to have disabled `alsa` from detecting the analog jack as an interface - yet `omxplayer` still output sound fine. @flemingg was able to get `alsa` to detect the analog jack interface but used SPI as the control (GPIO pin 10). More investigation is needed to determine if PCM is suitable for enabling output or what configs need to be adjusted so that the Linux environment can hook into the audio streams.

## External Audio - Audio Input
 
We were able to get lights to respond to external noise levels in a basic sense where the noise level correlated to the brightness of the lights. A video of this in action may be found here: https://msoe365-my.sharepoint.com/personal/burkhardtr_msoe_edu/Documents/Microsoft%20Teams%20Chat%20Files/video-20201217-065613-437cccaa.mp4

### Materials Used
* Insignia USB Recording Microphone

### Process

The first thing @burkhardtr did was plug in the microphone. Upon doing this the Raspbian environment should detect the interface and load any necessary drivers automagically.

To test that the microphone is recognized try the command: 
```bash
aplay -l
```
and the microphone should show up in the output.

Next, a library to interface with the streams is needed. For the sake of simplicity @burkhardtr decided on using [PortAudio](http://www.portaudio.com/) for it's simple build process and multitude of languages interfaces (specifically in Python). Either follow the build instructions on PortAudio's site or use `apt-get install` to install and load the library (this might require a restart if done manually).

Since the lights are controlled using Python, @burkhardtr kept in the spirit of simplicity and decided to use a Python library to interface with PortAudio - he selected [Sound Device](https://python-sounddevice.readthedocs.io/en/0.4.1/) which has a good mixture of low level access and high level constructs that make it easy to hook in and out of streams without too much configuration or magic numbers for defining the audio stream.

After that, following and tweaking a bit of sample code from Sound Devices website yielded a script that allows for audio input volume levels to determine the brightness of the LED strip - link to code is below.

### Notes

Since audio input does not rely on the PWM or PCM it is not necessary to switch the LEDs off pin 18 although this is untested. @burkhardtr conducted this knowledge acquisition and spike after investigating audio input and switched his LED light strip to use pin 21 with the PCM controlling it.

Python3 was used for simplicity and to ensure any future code uses up-to-date languages and libraries.

### Code

https://gitlab.com/msoe.edu/sdl/sd21/sisyphus/lights-audio-input/-/blob/audio-input-lights/content/lights/audio.py

## External Audio - Audio Output
We were able to show that simultaneous playing of audio and control of the lights is possible by having audio use the PWM channel on the raspberry pi and the lights utilize SPI (GPIO pin 10). At this point we are unsure of the level of real-time communication permitted between the lights and the audio output stream.

### Materials Used
* 3.5mm jack headphones

### Process
SPI was enabled by editing both the SPI interface (via `sudo raspi-config`) and by editing the `/boot/config.txt` and adding the following lines:
````
# for using SPI
core_freq=500
core_freq_min=500
````
After making these changes, we sought to determine whether or not the sound could be enabled simultaneously. A long and irksome process of attempting to determine how audio drivers were loaded ensued. @flemingg got her setup working by editing the `/boot/config.txt` and adding the following:
````
# Enable audio (loads snd_bcm2835)
dtparam=audio=on
````
In addition to this, the `blacklist snd_bcm2835` had to be removed from `/etc/modprobe/snd-blacklist.conf`. The system was then rebooted. The package `alsa-base` also had to be installed via `apt`. After this, the audio card would show up without issue in the ALSA listing (found by running `aplay -l`). 

Initially the thought was to have a machine learning algorithm analyze an audio file and then generate colored output to match the given audio file, as @flemingg (found a library for this)[https://github.com/tyiannak/color_your_music_mood?ref=hackernoon.com] and believed that it was possible to get it working. The library was written in python 3. In the interest of simplicity, python 3 was used for the remainder of the spike.

In order to facilitate the use of this library, many additional packages were required: 
* opencv (not downloaded via pip3, rather pulled from apt)
* scikit-learn
* PyAudio (which had to be built from scratch)

The algorithm was able to perform and the lights responded to the selected song file's generated color; however, the algorithm errantly selected the same color for each song played. Unfortunately, this issue went unsolved, believed to be an issue with the adaption of the machine learning algorithm, the sampling rate applied, or perhaps both.

Finally, an attempt was made to use an approach similar to @burkhardtr's, in which a `stream` object monitors a system channel and reports data on the channel, using the `sounddevice` library. The only difference was that an `OutputStream` was used instead of an `InputStream.`

````
def start_monitoring():
    with sd.OutputStream(callback=update_lights, device=0):
        while True:
            pass
````

For reasons unsolved, however, the Outputstream always reported an empty `outdata` to the callback function.


### Code
The machine learning attempt is located (here)[https://gitlab.com/msoe.edu/sdl/sd21/sisyphus/sound-output-to-color-spike].
