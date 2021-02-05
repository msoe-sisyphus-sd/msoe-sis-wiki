# Sprint Goal

Determine where the modified (volume-sensitive) algorithm for translating audio to color will run.

# Burndown Chart

![image](uploads/3baa765b0ecd711033ce22ae922aa043/image.png)

Recorded at 2021-02-04 08:37 so there might be a dip by 2021-02-05 morning

# Team Commitment

## Burkhardt, Robert
* Hours: 7.5
* Rating (0-10): 8
* Summary:

| Date | Hours Spent | Description | Issue / MR | Repository |
| --- | --- | --- | --- | --- |
| 2021-01-29 | 0.25h | Weekly status report with Dr. Taylor | #7 | msoe-sisbot | 
| 2021-02-01 | 0.25h | Standup with the team, discussion on the usability outcome assessment, and the tech report due in a few weeks. | #7 | msoe-sisbot | 
| 2021-02-04 | 1h | Standup with the team, discussion about usability testing results and wrote status report | #7 | msoe-sisbot |
| 2021-02-01 | 2h | Wrote out basic persona, workflow, and user testing document for the Usability test. The team decided to re-orient the UX test to be around the new audio-lights mode. The plan is that I would write out the tests and build a quick prototype that the rest of the team could review and use to conduct the test. I ran into some weird Adobe Cloud issues on my computer (couldn't log in since MSOE disabled my access and that broke everything) so I was only able to create a first pass of the mocks (seen in the Wiki history) Acessible here: https://gitlab.com/msoe.edu/sdl/sd21/sisyphus/msoe-sisbot/-/wikis/UX/Usability-Testing| #7 | msoe-sisbot |
| 2021-02-02 | 2h | Finished the usability prototype with revisions from the team. The prototype is published in Adobe XD and can be accessed online via: https://xd.adobe.com/view/c5914d8a-b905-46e8-be44-17fd03f059f3-90c2/?fullscreen&hints=off The goal of the prototype is to see if users are able to turn on and off the lighting controls and change colors and feature axis | #7 | msoe-sisbot |
| 2021-02-03 | 1h | Worked on getting volume feature data to determine colors to be displayed on the table. I had to correct a couple of library things on my Pi as I shuffled configs around but the main chunk of this time was figuring out what pyAudioAnalysis could offer interms of juding volume. I went a foot deep in the rabbit hole of singal process and found to naive metrics RMS (root mean square) and peak. I think these are a good start and python provides a built-in module to calculate them (via audioop). The issue is that these are boundless metrics ranging from 0 to Inf. so normalization is an issue when plotting it along 0-255 for alpha values. There are a couple different ways to correct for this - the first being normalize as more measurements are taken, the second is to have a preset value to normalize against (hopefully generated from measurements) | #48 | msoe-sisbot |
| 2021-02-04 | 1+h | Began implementing the volume metric via RMS (root mean square) - I decided that for now the best way to normalize the audio is to normalize as values are taken since I don't have a good base line measurment. I hope to perform some manual testing by sending the new colors to the Sisyphus table. Please note I continued to work on this after filling out the report so the times might be a little bit off... | #49 | msoe-sisbot | 

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
* Hours: 8.5
* Rating (0-10): 5
* Summary:

| Date | User | Hours Spent | Description | Issue/MR | Repository |
|------|------|-------------|-------------|----------|------------|
| 2020-02-1 | @enterss | 30m | Standup w/ Team | #7 | msoe-sisbot |
| 2020-02-1 | @enterss | 2h | Working on various dev environment issues | #48 | msoe-sisbot |
| 2020-02-4 | @enterss | 2h | Looked into existing algorithm and determined how to change the brightness based on the audio input | #48 | msoe-sisbot |
| 2020-02-4 | @enterss | 2h | Wrote out rough draft of section of Tech Report | #46 | msoe-sisbot |
| 2020-02-4 | @enterss | 2h | Standup w/ Team | #7 | msoe-sisbot |

## Fleming, Grace
* Hours: 12.25
* Rating (0-10): 2
* Summary: Everything takes me too long.



<table>
  <tr>
   <td><strong>Date</strong>
   </td>
   <td><strong>User</strong>
   </td>
   <td><strong>Hours Spent</strong>
   </td>
   <td><strong>Description</strong>
   </td>
   <td><strong>Issue/MR</strong>
   </td>
   <td><strong>Repository</strong>
   </td>
  </tr>
  <tr>
   <td>2021-01-29
   </td>
   <td>Grace Fleming
   </td>
   <td>0.25h
   </td>
   <td>Sync with Dr. Taylor
   </td>
   <td><a href="https://gitlab.com/msoe.edu/sdl/sd21/sisyphus/msoe-sisbot/issues/7">Group Meetings Time Log</a>
   </td>
   <td>msoe-sisbot
   </td>
  </tr>
  <tr>
   <td>2021-01-29
   </td>
   <td>Grace Fleming
   </td>
   <td>1h
   </td>
   <td>Researched more into the porting of sklearn into C. Explored<a href="https://github.com/nok/sklearn-porter"> https://github.com/nok/sklearn-porter</a>. Finally, emailed the professor in charge of the machine learning algorithm we are currently using requesting the dataset he used to train his algorithm and thanking him fro his work.
   </td>
   <td><a href="https://gitlab.com/msoe.edu/sdl/sd21/sisyphus/msoe-sisbot/issues/45">Spike: Mood lighting & Mobile as a Artificial Intelligence Computation Platform</a>
   </td>
   <td>msoe-sisbot
   </td>
  </tr>
  <tr>
   <td>2021-01-29
   </td>
   <td>Grace Fleming
   </td>
   <td>0.75h
   </td>
   <td>Got set up for android development (again, this time on linux). No surprises, setup went smoother on linux. Can now run an app on my emulator. Will be pushing shortly to a new spike demo repository.
   </td>
   <td><a href="https://gitlab.com/msoe.edu/sdl/sd21/sisyphus/msoe-sisbot/issues/45">Spike: Mood lighting & Mobile as a Artificial Intelligence Computation Platform</a>
   </td>
   <td>msoe-sisbot
   </td>
  </tr>
  <tr>
   <td>2021-01-29
   </td>
   <td>Grace Fleming
   </td>
   <td>0.75h
   </td>
   <td>Figuring out with Andy how to best divide this after some research, since it's obvious there isn't a 'quick and easy' solution. Re-wrote subtasks.
   </td>
   <td><a href="https://gitlab.com/msoe.edu/sdl/sd21/sisyphus/msoe-sisbot/issues/45">Spike: Mood lighting & Mobile as a Artificial Intelligence Computation Platform</a>
   </td>
   <td>msoe-sisbot
   </td>
  </tr>
  <tr>
   <td>2021-01-29
   </td>
   <td>Grace Fleming
   </td>
   <td>1h
   </td>
   <td>Researched PyAudioAnalysis alternatives in java. Found (this)<a href="https://about-time-too.netlify.app/msoe.edu%2Fsdl%2Fsd21%2Fsisyphus">https://github.com/Subtitle-Synchronizer/jlibrosa</a> for pulling zero-crossing rate and (this)<a href="https://about-time-too.netlify.app/msoe.edu%2Fsdl%2Fsd21%2Fsisyphus">https://github.com/mileshenrichs/QuiFFT</a> for doing fast Fourier transforms, both of which PyAudioAnalysis does.
   </td>
   <td><a href="https://gitlab.com/msoe.edu/sdl/sd21/sisyphus/msoe-sisbot/issues/45">Spike: Mood lighting & Mobile as a Artificial Intelligence Computation Platform</a>
   </td>
   <td>msoe-sisbot
   </td>
  </tr>
  <tr>
   <td>2021-02-01
   </td>
   <td>Grace Fleming
   </td>
   <td>2h
   </td>
   <td>Spent two hours trying to figure out how to record audio in android. went down the wrong track trying to record audio using the Android media recorder, since apparently we want <em>raw</em> audio, which is found under the AudioRecord() class, and not the MediaRecorder() class. Right now the MediaRecorder() version that records audio and saves it to a file is pushed to origin. tomorrow I'll want to update this to use the AudioRecorder class instead. I found two different examples of how to do this, one<a href="https://github.com/Piasy/RxAndroidAudio"> here</a> and one<a href="https://github.com/aahlenst/android-audiorecord-sample/blob/master/src/main/java/com/example/audiorecord/AudioRecordActivity.java"> here</a>. Finally, I also looked into what MFCC values are, since they are a feature of the existing algorithm I don't understand. Read<a href="https://medium.com/prathena/the-dummys-guide-to-mfcc-aceab2450fd"> this article here</a>. As far as calculating those values go, JLibrosa does support the MFCC stuff which is great. Looking through the other features Andy had laid out in his feature wiki, I'm not so sure about how I'm going to calculate some of the other values in that list, like spectral energy, for example. I think that is going to need more research, or maybe we'll just have to implement it on our own.
   </td>
   <td><a href="https://gitlab.com/msoe.edu/sdl/sd21/sisyphus/msoe-sisbot/issues/45">Spike: Mood lighting & Mobile as a Artificial Intelligence Computation Platform</a>
   </td>
   <td>msoe-sisbot
   </td>
  </tr>
  <tr>
   <td>2021-02-02
   </td>
   <td>Grace Fleming
   </td>
   <td>1.50h
   </td>
   <td>Spent a ton of time looking through siscloud to see how it loads up the frontend, as I figure this will help us make changes to it. I learned about how it sets up, initializes, looks for sisyphus tables (or fails to). Once a sisyphus table is setup, the app moves into the 'manipulation mode' where the user can actually control the sisyphus table. In hindsight this information is very useful for determining why our table from the lab's remote web interface is broken.
   </td>
   <td><a href="https://gitlab.com/msoe.edu/sdl/sd21/sisyphus/msoe-sisbot/issues/46">Create First-Pass Architecture Draft</a>
   </td>
   <td>msoe-sisbot
   </td>
  </tr>
  <tr>
   <td>2021-02-02
   </td>
   <td>Grace Fleming
   </td>
   <td>0.50h
   </td>
   <td>Spent some time implementing raw audio capture. Right now it saves to a file on the SD card on a phone, but I will be changing that to save to a AtomicIntegerArray, which is the Java thread-safe version of an array. This should be able to hold the raw audio values and then we can hopefully play around with them.
   </td>
   <td><a href="https://gitlab.com/msoe.edu/sdl/sd21/sisyphus/msoe-sisbot/issues/45">Spike: Mood lighting & Mobile as a Artificial Intelligence Computation Platform</a>
   </td>
   <td>msoe-sisbot
   </td>
  </tr>
  <tr>
   <td>2021-02-03
   </td>
   <td>Grace Fleming
   </td>
   <td>0.75h
   </td>
   <td>JLibrosa apparently does not support raw audio data, as our algorithm requires (only accepts wav files). Read through JLibrosa and tried to weight the pros and cons of modifying the library vs. just writing my own dang library in Java. Honestly, we'd really only have to transition over<a href="https://github.com/tyiannak/pyAudioAnalysis/blob/b27644a3d9351733693c79718441430619d6141f/pyAudioAnalysis/ShortTermFeatures.py#L543"> https://github.com/tyiannak/pyAudioAnalysis/blob/b27644a3d9351733693c79718441430619d6141f/pyAudioAnalysis/ShortTermFeatures.py#L543</a>. In some ways, I feel like converting PyAuduioAnalysis directly makes more sense at this point. And yes, I really wish that I knew why everything on this PBI was so difficult and/or took so long. Good thing I wasn't burned out before this sprint because I will be afterwards.
   </td>
   <td><a href="https://gitlab.com/msoe.edu/sdl/sd21/sisyphus/msoe-sisbot/issues/45">Spike: Mood lighting & Mobile as a Artificial Intelligence Computation Platform</a>
   </td>
   <td>msoe-sisbot
   </td>
  </tr>
  <tr>
   <td>2021-02-03
   </td>
   <td>Grace Fleming
   </td>
   <td>2h
   </td>
   <td>Worked on implementing audio data capture and storage into a queue. This shouldn't have taken me 2 hours, but it did, because I had some confusion about how and why multiple threads were needed. Figured it out, and finally hopped on a call with Andy to explain (he was curious). Demo has been pushed. Next step is figuring out how to take the captured audio data and feed it to librosa.
   </td>
   <td><a href="https://gitlab.com/msoe.edu/sdl/sd21/sisyphus/msoe-sisbot/issues/45">Spike: Mood lighting & Mobile as a Artificial Intelligence Computation Platform</a>
   </td>
   <td>msoe-sisbot
   </td>
  </tr>
  <tr>
   <td>2021-02-04
   </td>
   <td>Grace Fleming
   </td>
   <td>1h45m
   </td>
   <td>Changed to a periodic task to process audio. Integrated JLibrosa and used FLOAT_PCM to collect audio values so they could be fed to Librosa. Ran into some significant memory issues.
   </td>
   <td><a href="https://gitlab.com/msoe.edu/sdl/sd21/sisyphus/msoe-sisbot/issues/45">Spike: Mood lighting & Mobile as a Artificial Intelligence Computation Platform</a>
   </td>
   <td>msoe-sisbot
   </td>
  </tr>
</table>



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
* We got a response from the creator of the original algorithm we adapted with directions on how to recreate his dataset!

## Risk Updates
* Audio capture on Android is really "fricken-chicken" hard
    * Biggest issues are memory allocation and junky audio buffer data (lots of 0s)
* Might need to remove the AI Service PBI (#49) with how work is being completed

# Questions
* Mind looking over a draft of our tech report (outside of Sprint Review) next week? We will send it out Monday night 2020-02-08 
* Do you like snow? :snowflake: 

# Conclusion
The team feels engaged with the sprint, and despite having a heavy week coming up is ready to take on any challenges!