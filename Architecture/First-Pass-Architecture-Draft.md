# Current Architecture Understanding

## Role of Siscloud

## Role of Sisproxy

## Role of Sisbot

# Integration of New Features
We anticipate the following modules, or areas of functionality:
\[Sisyphus App\]

* Settings to switch on
* Settings to adjust colors per axis

\[Input Stream\]

* Takes in audio
* Possibly parses

\[Setup for External Module\]

* Start up scripts
* Configure ALSA, etc.
* Install python, load modules, etc.

\[Alogrithm\]

* What are the featrures
* Agnostic to colors
* Take input stream
* Output vector

\[Mapping Module\]

* Takes in output vector
* Translates to color
* Recieves changes from app

\[Communication Layer\]

* Take color from mapping
* Send to table (supra fast)