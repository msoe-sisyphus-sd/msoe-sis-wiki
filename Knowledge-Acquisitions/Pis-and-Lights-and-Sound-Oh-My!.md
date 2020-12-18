# Goal
The goal of this knowledge acquisition was to understand how audio input and output works on Raspberry Pis and what limitations exist to using the onboard audio interface when also using GPIO to drive the NeoPixel light strip. More specifically, the team wants to understand how the lights can interact with internal audio sources (e.g. a music stream from the internet) and external audio sources (e.g. a USB microphone monitoring the noise level in a given room).

# Background

## Sisyphus Industries
Sisyphus Industries (in particular Matt) have investigated this in the past but have not made any great strides in producing features. From what the team can tell there are no fragments in the codebase that enable any such feature so our investigation started from scratch.

We did _not_ reach out to Matt for assistance as we were able to get things working fine on our side.

# Outcomes

## External Audio

We were able to get lights to respond to external nose levels in a basic sense where the noise level correlated to the brightness of the lights. A video of this in action may be found here: https://msoe365-my.sharepoint.com/personal/burkhardtr_msoe_edu/Documents/Microsoft%20Teams%20Chat%20Files/video-20201217-065613-437cccaa.mp4

### Materials Used
* Insignia USB Recording Microphone

### Process

The first thing I did was 
