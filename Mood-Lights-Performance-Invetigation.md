# Running the sound-output-to-color-spike on my laptop

The following was the CPU utilization running on my Windows 10 laptop without the lights averaged over 5 trials.

| Trial       | CPU Utilization (%) |
| ----------- | ----------- |
| Trial 1     | 24.6%       |
| Trial 2     | 27.5%       |
| Trial 3     | 27.2%       |
| Trial 4     | 26.5%       |
| Trial 5     | 26.1%       |

Average: 26.38%

# Running the sound-output-to-color-spike on my PI

The following was the CPU utilization running on my Raspberry PI without the lights averaged over 5 trials.

| Trial       | CPU Utilization (%) |
| ----------- | ----------- |
| Trial 1     | 100%       |
| Trial 2     | 100%       |
| Trial 3     | 100%       |
| Trial 4     | 100%       |
| Trial 5     | 100%       |

Average: 100%

# Running the sound-output-to-color-spike on my PI

The following was the CPU utilization running on my Raspberry PI with the lights averaged over 5 trials.

| Trial       | CPU Utilization (%) |
| ----------- | ----------- |
| Trial 1     | 100%       |
| Trial 2     | 100%       |
| Trial 3     | 100%       |
| Trial 4     | 100.3%       |
| Trial 5     | 100%       |

Average: 100.06%

# Running the sound-output-to-color-spike on my PI measuring temperature
| Trial       | Temperature (Celsisus) |
| ----------- | ----------- |
| Trial 1     | 46       |
| Trial 2     | 45       |
| Trial 3     | 47       |
| Trial 4     | 46       |
| Trial 5     | 47       |

Average: 46.2 degrees celsisus


# Running led_startup using PWM

The following is the CPU utilization with running led_startup in the sisbot repo using PWM averaged over 5 trials.

| Trial       | CPU Utilization (%) |
| ----------- | ----------- |
| Trial 1     | 25.8%       |
| Trial 2     | 28.2%       |
| Trial 3     | 27.8%       |
| Trial 4     | 27.4%       |
| Trial 5     | 27.8%       |

Average: 27%

# Running led_startup using SPI

The following is the CPU utilization with running led_startup in the sisbot repo using SPI averaged over 5 trials.

| Trial       | CPU Utilization (%) |
| ----------- | ----------- |
| Trial 1     | 15.5%       |
| Trial 2     | 15.9%       |
| Trial 3     | 14.2%       |
| Trial 4     | 14.9%       |
| Trial 5     | 15.2%       |

Average: 16.04%

# Quick Win Optimizations for ML algorithm

Removing OpenCV helped the performance of the algorithm especially on the Raspberry PI. When the ML is run on a Raspberry PI without OpenCV the CPU utilization wasn't constantly at 100% and that cut CPU utilization by about half. However when run on Windows there was no change in the CPU utilization.

# Audio Input Investigation

For investigating the performance of listening for audio input I wrote a simple script to continuously record audio data from a microphone on a Raspberry PI in 5 second intervals using the PyAudio library. Then that script sent that data to a python server running on my MSOE laptop. This went really well and the PI and both the server were not overwhelmed with performance issues and there was very little delay in getting the data to the server. With the success I was able to add the ML algorithm to the server which also did not have any significant performance issues as well.

# Conclusions
If we use Python for audio input PyAudio will be a great library to use maximize performance. We should have many options if we use PyAudio including listening for audio directly on the PI. For the ML if we use the current solution the performance will be maximized if we remove OpenCV and don't run the ML code directly on the Raspberry PI. 