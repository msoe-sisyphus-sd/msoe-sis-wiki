# Sprint Goal
Investigate mapping audio to colors and how to integrate a Python ML model with the existing code base.

# Burndown Chart
![image](uploads/1553f6cf15ca89b057cfeea42d462af1/image.png)

# Team Commitment

## Burkhardt, Robert
* Hours: 6.75h
* Rating (0-10): 7.99
* Summary:

| Date | Hours Spent | Description | Issue / MR | Repository | 
| --- | --- | --- | --- | --- |
| 2021-01-08 | 0.5h | Met with Dr. Taylor to discuss sprint plans and other outcomes. | #7 | msoe-sisbot |
| 2021-01-11 | 0.25h | Weekly standup with Grace and Andy | #7 | msoe-sisbot |
| 2021-01-14 | 1h | Weekly meeting with team to discuss status report and do standup. Came away with a possible demo for next week - having the ML run on a PI that changes the color of the Table in the lab over HTTP | #7 | msoe-sisbot |
| 2021-01-12 | 2h | Investigated OSS, ALSA, Port Audio, and Pulse Audio as hardware audio interfaces/driver in Linux. OSS was found to be "deprecated" and no longer included in standard Raspbian distributions. Additionally, Port Audio and Pulse Audio are cross platform interfaces but may be overly complex for what is actually needed (passing an audio stream to a Python process). ALSA is the de-facto replacement for OSS but has minimal Python interface support when compared to Port Audio or Pulse Audio. | #44 | msoe-sisbot |
| 2021-01-13 | 1.5h | Investigated ALSA, pyaudio, sounddevice, and other possible python interfaces for using audio. I was also able to play around with using USB mics and USB sound cards for determining audio quality. I made two different recordings using `arecord` and evaluated found that (unironically) the USB microphone sounded better. However, the USB microphone is bulky and might not be a detriment to the table's design and aesthetic so this will have to be considered when choosing the best hardware. Additionally, it seems that pyaudio and sounddevice are similar in capabilities but pyaudio is used by the ML model and is claimed to be faster than sounddevice. Futher testing is required in a full setup. I plan to spend a hot second looking of the ML model code to see if pyaudio is needed or if it can be cut for an ALSA python library to pass audio around.
| msoe-sisbot |
| 2020-01-14 | 1.5h | Began drafting spike report with decision matrices for determining which is the best library to use according to different criterion. This will hopefully prove out what is the way to move forward and helps feed technology justification for the tech. report. Spike report may be seen here: https://gitlab.com/msoe.edu/sdl/sd21/sisyphus/msoe-sisbot/-/wikis/Spikes:-Audio-Interfaces Please note that this document is currently a draft and a work in progress so there may be missing items. I plan to complete the doc and detail a full decision matrix. Hopefully after that is completed I can begin scaffolding and integrating audio input with the ML models for a demo at the end of the sprint (which may take the form of a separate app that runs over the network). | #44 |

## Casper, Joseph
* Hours: 8+
* Rating (0-10): 6
* Summary:

| Date | User |	Hours Spent | Description | Issue | Repository |
| ------ | ------ | ------ | ------ | ------ | ------ |
| 2021-01-12 | casperjm | 2h | Tried to get the app running locally so that I can add in a new button | #41 | msoe-sisbot |
| 2021-01-13 | casperjm | 5h | Spent more time trying to get the app to run. I got closer, but not there yet. | #41 | msoe-sisbot |
| 2021-01-14 | casperjm | 1h | Status report meeting with team | #7 | msoe-sisbot |
| 2021-01-14 | casperjm | xh | Prepared demo for Dr. Taylor | #7 | msoe-sisbot |

I spent a lot of time trying to get the app running locally on my windows machine. In the meeting on Thursday, someone brought up that the app needs to be run on the Pi :facepalm:. I'll hopefully be able to get the app running now. I also spent time preparing a demo for the meeting on Friday.

## Enters, Stuart
* Hours: 8
* Rating (0-10): 6
* Summary:

| Date | Hours Spent | Description | Issue | Repository |
| --- | --- | --- | --- | --- |
| 2020-1-8 | 20m | Met with Taylor for weekly meetup | #7 | msoe-sisbot |
| 2020-1-13 | 2h | Discussed direction of issue w/ Grace and decided to split out issue into sub-issues | #43 | msoe-sisbot |
| 2020-1-14 | 4h | Figured out how to connect to table and tested light pattern | #19 | msoe-sisbot |
| 2020-1-14 | 40m | Wrote documentation for testing patterns on the table via Postman & ssh | #7 | msoe-sisbot |
| 2020-1-14 | 1h | Met w/ team for standup & status report | #7 | msoe-sisbot |

## Fleming, Grace
* Hours: 9.75
* Rating (0-10): 8.5
* Summary:

| Date | User | Hours Spent | Description | Issue/MR | Repository |
|------|------|-------------|-------------|----------|------------|
|2021-01-11 | Grace Fleming | 2h | Spent time today looking at how to make a mood classification based off of specific music physical attributes, instead of valence/arousal. This would be considered a non-ML approach, and we could use pitch, tempo, intensity and timbre to create a projection into 3D space. This might not relate directly to mood, but we could probably end up with chromatic similarities between similar mood samples. I dug around for libraries to assess each of these features, and determined off-the-shelf libraries that could likely pitch, tempo and intensity, but struggled to find something to classify timbre. Will discuss with Stuart whether or not we can potentially build a chromatic model using only pitch, rhythm and intensity. | Spike: Mood Lighting & Alternative Algorithms	| msoe-sisbot|
|2021-01-11 | Grace Fleming | 15m | Standup with Andy/George | Group Meetings Time Log | msoe-sisbot |
| 2021-01-12 | Grace Fleming | 2h | Worked on designing an approach to do audio track projection into 2-space using pitch and tempo. Met with rather limited success. Nothing is interesting enough to generate a color yet I don't think, but I am making progress. | Spike: Mood Lighting & Alternative Algorithms| msoe-sisbot |
| 2021-01-13 | Grace Fleming | 2h | Switched the non-ML approach to Stuart. I switched back to the ML-model. The owner of the old demo piece did us all a solid by publishing an updated model trained with a newer version of sklearn, so the codebase ran no problem on Linux. I tried out the model using a few songs, both with lyrics and without, The model worked really well this time, generating a large spectrum of colors for varied music, and I think using native audio input is the key here (versus output like in my demo). Once I had that working, I looked into performing a web request to the server to change the color of the lights. Also, this is not explicitly related to my PBI, but I had the idea of using a phone's microphone to capture/record audio. This would make it super SUPER easy to integrate into the Sisyphus workflow, so I spent some time talking with Joe about the idea. | Spike: Mood Lighting & Alternative Algorithms| msoe-sisbot | 
| 2021-01-14 | Grace Fleming| 2h | Worked on making the ML demo into an actually functioning piece of code that can make an API call to the table. Realistically this shouldn't have taken as long as it did, but it ended up taking awhile because the JSON format is "double-wrapped." | Spike: Mood Lighting & Alternative Algorithms | msoe-sisbot |
| 2021-01-14 | Grace Fleming |30m | assisted Stuart with development on the table (provided networking help, helped him set up Postman and manipulate the table via API, corrected CURL requests, etc) | Spike: Mood Lighting & Alternative Algorithms | msoe-sisbot |
| 2021-01-14 | Grace Fleming | 1h | Status report with team & groomed a new ticket | Group Meetings Time Log | msoe-sisbot |

## Wojciechowski, Andrew
* Hours: 5.39
* Rating (0-10): 6
* Summary:

| Date | User | Hours Spent | Description | Issue/MR | Repository |
|------|------|-------------|-------------|----------|------------|
| 2021-01-08 | @wojciechowskia | 0.25h | Standup with the team. Also, discussed checking with Dr. Taylor when the tech report is due as well as the sprint review. | #7 | msoe-sisbot |
| 2021-01-11 | @wojciechowskia | 1h | Investigated CPU utilization and temperature of the sound output to color spike. Determined that CPU utilization was about at 100% with the lights and the temperature was about 46 degrees celsius after running the algorithm. | #40 | msoe-sisbot |
| 2021-01-12 | @wojciechowskia | 0.17h | Purchased a USB microphone to use for testing performance. | #40 | msoe-sisbot |
| 2021-01-12 | @wojciechowskia | 1.5h | Wrote code to test the performance of recording 5 seconds of audio from a microphone continuously and sending it to a server to do the machine learning. Awaiting a microphone for testing.| #40 | msoe-sisbot |
| 2021-01-13 | @wojciechowskia | 0.5h | Read up on SPI vs. PWM vs PCM a bit. Nothing was mentioned about performance concerns between the methods but I am going to compare the performance with the LED library next and eventually audio when I get my USB microphone| #40 | msoe-sisbot |
| 2021-01-14 | @wojciechowskia | 1h | Spent some time looking into the performance implications of PWM vs. SPI for the lights. Found that SPI took less CPU utilization so then I ran the ML spike on the PI without the lights and the CPU utilization was still at 100%| #40 | msoe-sisbot |
| 2021-01-14 | @wojciechowskia | 1h | Standup and wrote status report with the team | #7 | msoe-sisbot |

# Discussion

## Key Meetings
* Friday 1/8: Met with Dr. Taylor to discuss project and risks associated with with the new direction. We also developed a new format for weekly sync meetings between the team and Dr. Taylor.
* Monday 1/11: sync meeting (missed by 2/5 of the team for various life issues). 
* Thursday 1/14: Status report meeting

## Findings
* Sisyphus app code is difficult to run.
* Documentation for team development process is poor.
* Physical audio features extracted from audio can be used to describe the mood of an audio/musical segment.

## Successes
* ML algorithm developed from demo works on Ubuntu 20.04 to effectively colorize music mood.
* Stuart got his light pattern working.

## Risk Updates
* Dr. Schilling performed a firmware upgrade to the lab topology. No abnormalities have been identified in network access, but it's something to be aware of.
* The ML algorithm being used is CPU-intensive and eats up 100% of a raspberry pi  4B+'s cpu.

# Questions
* Specific timeline for tech report?
* Is the due date for the self-guided learning in canvas actually accurate? (the 28th)

# Conclusion
The team remains excited about the project direction, and is currently considering multiple methods of implementation (pi vs. phone vs. external hardware under the table). The team plans to have a fully functioning demo as well as decision matrices for design decisions surrounding software/hardware considerations prepared for next week's sprint review.