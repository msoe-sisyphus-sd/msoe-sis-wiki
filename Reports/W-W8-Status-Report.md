# Sprint Goal

Determine where the modified (volume-sensitive) algorithm for translating audio to color will run.

# Burndown Chart

![image](uploads/3baa765b0ecd711033ce22ae922aa043/image.png)

Recorded at 2021-02-04 08:37 so there might be a dip by 2021-02-05 morning

# Team Commitment

## Burkhardt, Robert
* Hours: X
* Rating (0-10): X
* Summary:

Insert Summary Here

## Casper, Joseph
* Hours: 8.75
* Rating (0-10): 7
* Summary: 


| Date | User |	Hours Spent | Description | Issue | Repository |
| ------ | ------ | ------ | ------ | ------ | ------ |
| 2021-01-20 | casperjm | 15m | Met with Dr. Taylor  | #7 | msoe-sisbot |
| 2021-02-01 | casperjm | 30m | Weekly stand up with team | #7 | msoe-sisbot |
| 2021-02-01 | casperjm | 2h | Started to investigate eslint bug. I did this by individually linting files one by one to see when it breaks | #34 | msoe-sisbot |
| 2021-02-01 | casperjm | 5h | Finished eslint PBI | #34 | msoe-sisbot |
| 2021-02-01 | casperjm | 1h | Met with team to write status report | #7 | msoe-sisbot |

I was able to finally finish fixing the broken eslint code (there was one issue in one file where a variable was declared twice, and that broke the entire app). Now that the eslint ticket is finished, I'll be able to start working on adding the new buttons to the app. 	

## Enters, Stuart
* Hours: X
* Rating (0-10): X
* Summary:

Insert Summary Here

## Fleming, Grace
* Hours: X
* Rating (0-10): X
* Summary:

Insert Summary Here

## Wojciechowski, Andrew
* Hours: 8h
* Rating (0-10): 8
* Summary:

| Date | User | Hours Spent | Description | Issue/MR | Repository |
|------|------|-------------|-------------|----------|------------|
| 2021-01-31 | @wojciechowskia | 2h | Researched what features the pyAudioAnalysis library extracts. Found this wiki article here written by the author describing each of the features: https://github.com/tyiannak/pyAudioAnalysis/wiki/3.-Feature-Extraction. I also dumped the raw feature names using the current demo and I found out that the mean, standard deviation, and deltas are calculated for each feature and I uploaded those names to the wiki. Finally, I found that the features are mainly calculated in the source file in the library here: https://github.com/tyiannak/pyAudioAnalysis/blob/master/pyAudioAnalysis/ShortTermFeatures.py | #45 | msoe-sisbot |
| 2021-02-01 | @wojciechowskia | 0.33h | Standup with the team, discussion on the usability outcome assessment, and the tech report due in a few weeks. | #7 | msoe-sisbot |
| 2021-02-01 | @wojciechowskia | 2h | Chatted with Grace a bit about what features are extracted with pyAudioAnalysis. Looked into the different visualization options provided by pyAudioAnalysis to try and determine the dimensions of each of the different features. Realized that none of these worked since the visualization for the features performs something called a dimensional reduction. So, I started looking into writing my own plotting code to get this better visualization. | #45 | msoe-sisbot |
| 2021-02-02 | @wojciechowskia | 1.17h | Extracted sample feature values using the chopin_waltz.wav in pyAudioAnalysis. Also, looked into how the number of samples pyAudioAnalysis is determined and figured out it's based on the number of audio samples detected. | #45 | msoe-sisbot |
| 2021-02-03 | @wojciechowskia | 0.5h | Discussions with Grace throughout today about the Android demo. Discussed some of the things we need to do with multithreading in the Android demo to have one thread listen for audio and have another process the data. Also, discussed difficulties with using JLibrosa and did some more research into this and figured instead of a byte[] we might be able to read in the samples as a float[] and pass it into JLibrosa without needing to read in a file. | #45 | msoe-sisbot |
| 2021-02-03 | @wojciechowskia | 0.5h | Spent some time researching about extracting audio features in Swift for potentially exploring doing that in iOS. Found a few possibilities and threw them in the wiki. Apple provides there own ML library which can do this called Core ML 3, and I found a few repos in which people did the audio analysis themselves. | #45 | msoe-sisbot |
| 2021-02-04 | @wojciechowskia | 0.5h | Put together a JSON schema for streaming features to the server. Looked also a bit into how the samples in jlibrosa are collected. I'm thinking we can collect raw samples in the app and then on the server calculate the mean, standard deviation, and delta values. | #45 | msoe-sisbot |
| 2021-02-01 | @wojciechowskia | 1h | Standup with the team, discussion about usability testing results and wrote status report | #7 | msoe-sisbot |


# Discussion

## Key Meetings
* Meeting with Dr. Taylor 2021-01-29 to discuss first week
* Team meeting (stand up and check in) on 2021-02-01 - tasked out Usability testing
* Team meeting (status report and finalize Usability testing results) on 2021-02-04

## Findings
* Usability testing was planned and executed during this week. The team built out a series of mocks that extend the app's current functionality. Testing revealed weaknesses in the workflow and copy (verbiage). The team hopes to iterate on the design if it is going to be implemented. See https://gitlab.com/msoe.edu/sdl/sd21/sisyphus/msoe-sisbot/-/wikis/UX/Usability-Testing for more details

## Successes
* Integrating volume as a feature appears to be relatively trivial and should require minimum integration with the current implementation via RMS

## Risk Updates
* Audio capture on Android is really "fricken-chicken" hard
    * Biggest issues are memory allocation and junky audio buffer data (lots of 0s)
* Might need to remove the AI Service PBI (#49) with how work is being completed

# Questions
* Mind looking over a draft of our tech report (outside of Sprint Review) next week? We will send it out Monday night 2020-02-08 
* Do you like snow? :snowflake: 

# Conclusion
The team feels engaged with the sprint, and despite having a heavy week coming up is ready to take on any challenges!