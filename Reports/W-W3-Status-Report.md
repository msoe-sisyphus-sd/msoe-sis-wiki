# Sprint Goal
Finish off carryover from sprint 2, and explore methods of input for lighting dependent on physical environment.

# Burndown Chart
![image](uploads/41eb594d485dc8eec6ab78d5bee2c52a/image.png)

_Image taken at 2020-12-17 7:02_

# Team Commitment

## Burkhardt, Robert
**Hours**: 10.5

**Rating (0-10)**: 10

**Summary**:

| Date | User | Hours Spent | Description | Issue/MR | Repository |
|------|------|-------------|-------------|----------|------------|
| 2020-12-11 | @burkhardtr | 0.5h | Meeting with Dr. Taylor | #7 | msoe-sisbot |
| 2020-12-17 | @burkhardtr | 1.75h | Met with team for end of sprint activities and pre-made reports and reviews for faster fill out. | #7 | msoe-sisbot |
| 2020-12-17 | @burkhardtr | 0.5h | Assisted Stuart with validating pseudo code | #19 | msoe-sisbot |
| 2020-12-15 | @burkhardtr | 3h | Explored the use of PortAudio and `sounddevice` which is a Python interface for the underlying library. Could not get the library to detect the analog jack for input but this may be due to my mucking about in the audio config files. I will see what I can undo/reset because I hope I don't have to set up the Pi from scratch again. Playing audio seems to still work fine through when using `omxplayer` which is weird since it doesn't seem to use `alsa` under the hood since `alsa` isn't detecting the sound card. I may need to move the LEDs to SPI rather than PCM and use a USB audio interface to play and record sounds. Will investigate further. | #15 | msoe-sisbot |
| 2020-12-16 | @burkhardtr | 2h | Got audio input to work! I used a USB microphone that was immediately recognized by the PortAudio library which means I can access it from Python! Played around with the API a bit to get a feel for how it works and ported one of the light scripts to Python3 so that I can use `sounddevice` to control the lights. | #15 | msoe-sisbot |
| 2020-12-16 | @burkhardtr | 1h | Integrated the `sounddevice` library with controlling strip brightness! I had to play around a bit with some of the math that normalizes the volume (weird linear algebra type stuff) and tried to use different channels to control different parts of the strip (didn't work out perfectly - would need to open a new spike for further analysis since this PBI is limited to understanding how audio works on the Pi and how it can be used with LEDs). | #15 | msoe-sisbot |
| 2020-12-17 | @burkhardtr | 1.75h | Wrote up process and findings in wiki as to share findings with team and Sisyphus Industries. | #15 | msoe-sisbot |


## Casper, Joseph
**Hours**: 8.5

**Rating (0-10)**: 6

**Summary**:

| Date | User | Hours Spent | Description | Issue/MR | Repository |
|------|------|-------------|-------------|----------|------------|
| 2020-12-11 | @casperjm | .5h | Meeting with Dr. Taylor | #7 | msoe-sisbot |
| 2020-12-14 | @casperjm | .5h | Weekly team stand up; began sprint planning | #7 | msoe-sisbot |
| 2020-12-14 | @casperjm | 3h | Began fixing eslint errors in the siscloud repo | #34 | msoe-siscloud |
| 2020-12-16 | @casperjm | 3h | Continued fixing eslint errors, almost finished | #34 | msoe-siscloud |
| 2020-12-17 | @casperjm | 1.5h | Team meeting to write sprint report and status report | #7 | msoe-sisbot |

This week I started fixing the eslint errors in the siscloud repo. The first day, I did work setting up eslint and got some initial fixes down, the second day I went more in depth and fixed more errors. There are about a quarter of the initial errors remaining. 


## Enters, Stuart
**Hours**: 10

**Rating (0-10)**: 7

**Summary**:
| Date | User | Hours Spent | Description | Issue/MR | Repository |
|------|------|-------------|-------------|----------|------------|
|2020-12-11|@enterss|2.67h|Looked at Andy's merged in code for a scaffold. Began working on converting the maths into code|#19|msoe-sisbot|
|2020-12-11|@enterss|1.25h|Met with team and did status report|#7|msoe-sisbot|
|2020-12-11|@enterss|0.50h|Met with Dr. Taylor|#7|msoe-sisbot|
|2020-12-14|@enterss|0.50h|Team sync meeting & initial sprint 4 planning|#7|msoe-sisbot|
|2020-12-16|@enterss|1h|translated math into pseudocode|#19|msoe-sisbot|
|2020-12-16|@enterss|0.50h|Helped Grace debug light issue|#7|msoe-sisbot|
|2020-12-17|@enterss|2h|Meeting with team for end of sprint ceremonies|#7|msoe-sisbot|
|2020-12-17|@enterss|0.50h|Worked with George to implement pseudo code|#19|msoe-sisbot|
|2020-12-17|@enterss|1h|Manual testing of the pattern|#19|msoe-sisbot|

## Fleming, Grace
**Hours**: 18ish

**Rating**: 7

**Summary**:

I tried to implement an audio spike that was overambitious. Despite good effort and a TON of time slogged into the issue _and_ a prototype, the prototype is uninteresting and does not function as I would've hoped. 
| date | User | Hours Spent | Description | Issue/MR | Repo |
|--|--|--|--|--|--|
|2020-12-13 | Grace Fleming |0.50h | Reviewed PR | Integrate Upstream with Fork	| msoe-sisbot|
|2020-12-14 | Grace Fleming |0.50h | Standup & end-of-sprint plan. Revised sprint 3 plan and created a sprint 4 plan. |Group Meetings Time Log	| msoe-sisbot |
|2020-12-14 | Grace Fleming |1.50h | Synchronized with George about what's left to work on. Made plans to implement a spike showcasing simultaneous audio output and light manipulation. Researched audio libraries for audio output capable of analyzing music. Found this which may be a cool area of exploration for audio INPUT. Continued researching audio output manipulation libraries.|Knowledge Acquisition: Sync Table Lights with Audio Track |msoe-sisbot |
|2020-12-15 | Grace Fleming |1.50h | Attempted to assemble local dev environment to begin working on spike. Hit with a wall when tried to boot pi 3 image on pi 4 image. Contacted Andy about stealing a pi 4 dev image. Assisted Andy in building the image. While waiting for image to transfer/upload, researched more ways of manipulating and controlling sound. Found librosa, a python library for doing audio output analysis. I am unsure of whether there will be time to implement a suitable demo using librosa, as it seems quite complicated.  | Knowledge Acquisition: Sync Table Lights with Audio Track | msoe-sisbot |
|2020-12-15 | Grace Fleming |2.50h | Set up dev pi, which took unfortunate amount of time (bad batteries). Then found out how to switch GPIO and lights to SPI. Required some digging but found this. After applying the accepted fix, the lights worked just fine :) I attempted to get the audio part working, but my pi wouldn't recognize my headphones in the 3.5mm jack. I tried updating the kernel via rpi-update as this was a suggestion on a Raspbian forum. No changes, and sudo raspi-config doesn't show anything either. Tomorrow I will see if I have a different headphone pair I can try. | Knowledge Acquisition: Sync Table Lights with Audio Track	| msoe-sisbot |
|2020-12-16 | Grace Fleming | 3h | Got ALSA to finally recognize my audio card after a ton of digging my editing the boot/config.txt and then running a sudo modprobe snd_bcm2835. Not sure why I have to do both :shrug:. Integrated with lights, and started setting up development environment to pull together 3 different repos for a spike: a machine learning algorithm, a supporting audio analysis library, and a library for splitting wav files. | Knowledge Acquisition: Sync Table Lights with Audio Track	 | msoe-sisbot | 
|2020-12-16 | Grace Fleming | 2h | Worked on trying to install the openCV library to my pi since that package is required for the machine learning algorithm to measure the mood of my music. This was completely unsuccessful after trying several articles and in some cases waiting like 4 hours to install stuff--in all cases it would take forever to compile, and then error out on something. At this rate I will need to shift to a different spike idea, depressing as it is. Right now I think the easiest thing to do is detect the sound level of a track and change the brightness of the lights based on that :(. It is not the most glamorous but I don't want to sit on trying to install a single dependency. ALSO--I spent some of my time handling my local dev env. Unfortunately for me, the batteries I was using to power my LED's caught fire today (it is my theory that something in the box caused a full circuit and ground was shorted to power). The pi and the neopixels are both fine, but unfortunately the batteries are most definitely not, and the battery terminal holder is ruined as well. I am just grateful I was home when the smoking and burning started, or otherwise my apartment might've burned to the ground 🤞 Thankfully the majority of work left over in this sprint is going to be pure coding and will not sure a lab. | Knowledge Acquisition: Sync Table Lights with Audio Track | msoe-sisbot |
| 2020-12-17 | Grace Fleming| 5h| Worked pretty much all day on trying to get my spike working. In the end I got it all hooked up. opencv was able to be installed from an official raspbian repo. Setting up the python repos themselves was a complete mess, and I had audio library issues with installing PyAudio, which I found out later had to be installed from source on the raspberry pi. I then had to convert the implementation piece of my spike from some dude's github project (using audio input) to my own implementation using audio output. In the end the algorithm compiles and can manipulate lights, but is basically useless because for some unforseen reason, the color spectrum generated is always blue no matter what. I troubleshot this with both Andy and George but we couldn't figure it out :( | Knowledge Acquisition: Sync Table Lights with Audio Track | msoe-sisbot |
| 2020-12-17 | Grace Fleming| 1h40m| Retro, sprint finalization, status report. | Group Meetings Time Log | msoe-sisbot |

## Wojciechowski, Andrew
**Hours**: 12h

**Rating (0-10)**: 8

**Summary**:

| Date | User | Hours Spent | Description | Issue/MR | Repository |
|------|------|-------------|-------------|----------|------------|
| 2020-12-11 | @wojciechowskia | 30m | Meeting with Dr. Taylor | #7 | msoe-sisbot |
| 2020-12-13 | @wojciechowskia | 4h 30m | Merged in sisbot updates from the GitHub upstream. This was very tedious since the eslint change caused a ton of merge conflicts. Since we didn't make any changes other than linting I accepted all of Matt's changes, fixed eslint errors again, and reran prettier formatting on all of the JS files. Sisproxy and Siscloud also had updates so I merged those into new dev branches in our repo to correspond with our sisbot dev branch. Those were easy fast-forward merges. Finally, I verified that we were able to run these changes on the table. Ran into some issues with the lights module not being installed on the table so I installed pip on the Coffee table and I was able to verify the LED lights were still working with these changes. | #38 | msoe-sisbot |
| 2020-12-14 | @wojciechowskia | 30m | Met with the team and created the initial sprint plan for sprint 4 | #7 | msoe-sisbot |
| 2020-12-15 | @wojciechowskia | 30m | Created a new PI 4 image from my local PI setup for Grace to use. | #7 | msoe-sisbot |
| 2020-12-15 | @wojciechowskia | 30m | Wrote up a new wiki article for local setup instructions | #7 | msoe-sisbot |
| 2020-12-17 | @wojciechowskia | 30m | Re-added eslint to the updated sisproxy code pulled from the upstream repo | #38 | msoe-sisbot |
| 2020-12-17 | @wojciechowskia | 2h | Setup Grace's demo on my setup just in case we need to use my light strip for that demo. I plan to add the extra libraries that I installed in the demo repo and Grace is planning on getting the code updated to work with the lights. | #15 | msoe-sisbot |
| 2020-12-17 | @wojciechowskia | 1h 40m | Meeting with team, standup, wrote status report, modified the sprint 3 and 4 plans, and discussed sprint review tomorrow. | #7 | msoe-sisbot |
| 2020-12-17 | @wojciechowskia | 1h 20m | Helped Grace resolve some issues with installing the LED library using python3. Also, looked at trying different wav files to try and change the color. | #15 | msoe-sisbot |

# Discussion

## Key Meetings

* 2020-12-11 - Met with Dr. Taylor to discuss sprint progress
* 2020-12-14 - Weekly Team Meeting for sprint update and Sprint 4 planning
* 2020-12-17 - Team meeting to finish sprint 3 documentation

## Findings
* Bruce gave the team a list of potential long-term projects 
    * HomeKit Integration / Android Home Automation Integration
    * Better Ambient Lighting
        * The team is a bit warry of this project since it seems to lack the depth of a long term project.
            * Machine learning to select lighting curve
            * Use camera instead of photo-resistor
            * External lighting module
* Audio input and output is possible with the lights running

## Successes
* Audio input can be used to adjust the brightness of the LEDs
* Implemented ML algorithm to generate colors based off WAV file
* The upstream was merged into our working repository

## Risk Updates
* Batteries can catch fire :fire:
    * Grace is cursed and therefore banned from the Cybersecurity lab (2 Yays, 1 Nay, 2 Abstains) /s

# Questions
* When should our technology report be due?
* Add Bruce and Matt as guests to team chat?

## Really Important Questions
* How are you (like really)?
* Which freshman SE do you hate the most?
* Which freshman SE do you like the most?
* Which major do you hate the most and why is it CE?

## Really Really Important Questions
* What is the meaning of life, the universe, and everything?

# Conclusion
All in all the team feels it has been a really good sprint. In addition to completing outstanding sprint work the team was able to investigate audio input and output while running the lights. Furthermore, the team was able to tackle DX (developer experience) debt with merging upstream changes into our working repository and clearing up `eslint` errors in `siscloud` and `sisproxy`.

Happy New Year :tada: 