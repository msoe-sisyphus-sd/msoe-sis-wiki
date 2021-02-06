# Mobile as a Artificial Intelligence Computation Platform: A Cautionary Tale

During the course of the 5th sprint, the team investigated the feasibility of placing the burden of audio processing and machine learning onto a mobile phone.

The motivation for this method was simple: most consumers own smartphones, all smartphones have microphones, and all smartphones with microphones can capture audio. Furthermore, if an app were developed to listen to music and process the audio into audio features, these features could be passed to a web server that would perform the final analysis, return a color, and then the web server on the table could be used to change the color.

The issue for this spike was #45.

After 2 weeks, the PBI was canned and the team moved onto other areas of investigation.


## Python Mobile Frameworks for Machine Learning

Python mobile frameworks for Android exist, but most [do not support the porting of "binary" libraries including sklearn and scikit-learn) to mobile](https://stackoverflow.com/questions/42620871/building-python-packages-succeeds-but-scikit-learn-is-improperly-built). Kivy, a mobile framework for python, [supports running numpy on android](https://stackoverflow.com/questions/39533680/can-i-run-numpy-or-other-python-packages-on-android), but as of right now this isn't useful unless there's a machine learning library to support. Java libraries for machine learning exist, but none of them are able to load in the existing machine learning model, and at the time of writing, the team does not have a suitable dataset to train a new algorithm (although instructions for creating one were obtained).


## Compromise: Machine Learning in Python; Audio on Android

Due to the difficulty with running machine learning algorithms on a mobile device directly, the team chose next to investigate doing audio processing on android and simply sending the resulting feature array to a web server, which would in turn output the color from the machine learning model and make the appropriate request to the table's web server to change the lights.


Unfortunately, implementation of this failed. Android is short on audio-processing libraries. While it supports raw audio capture with the `MediaRecord` object, the format of the data that is returned is not easily integrated with existing audio processing libraries, particularly [jlibrosa](https://github.com/Subtitle-Synchronizer/jlibrosa), which is the a rough sibling to `PyAudioAnalysis.` The possibility of porting `PyAudioAnalysis` directly to Java was considered, but deemed too-time consuming.


Nevertheless, an audio spike was produced that recorded audio and obtains MFCC's from raw audio in android, stored [here](https://gitlab.com/msoe.edu/sdl/sd21/sisyphus/phone-ml-demo). Problematically, the MFCC values generated using `JLibrosa` on the same `.wav` file as MFCC values generated using `PyAudioAnalysis` do not match, even after performing a normalization. Attempts to troubleshoot the different between the MFCC values in python vs Java brought no resolution. 


Furthermore, the latency involved with computing MFCC's was high, and this was only 1 of 20 different features that would've had to be stripped from the collected audio.


Given the complexity and lack of support for general linear algebra options in Java proved to be another issue (despite the existence of `ejml` and `org.apache.math3.Vector..`, neither library worked well with integration of raw `float[]` or `short[]` arrays, and were impossible to convert into one another without an O(n*m) complexity). 

## Ultimately, Moving On Was the Best Option

After two weeks of battling the issues, the team decided that on measures of performance, maintainability and code quality, the idea should be scrapped and streaming raw audio data pursued instead, or at the very least, audio processing in C or Python should be considered.

