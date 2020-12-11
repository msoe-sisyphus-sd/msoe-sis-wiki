# Sprint Goal

Finish off carryover from sprint 2, and explore methods of input for lighting dependent on physical environment.

# Burndown Chart

Link Chart Here

# Team Commitment

## Burkhardt, Robert
###### Hours: 7.75
###### Rating (0-10): 7.22222
###### Summary:

| Date | User | Hours Spent | Description | Issue/MR | Repository |
|------|------|-------------|-------------|----------|------------|
| 2020-12-04 | @burkhardtr | 15m | Met with Dr. Taylor | #7 | msoe-sisbot |
| 2020-12-07 | @burkhardtr| 30m | Team meeting to write status report | #7 | msoe-sisbot |
| 2020-12-03 | @burkhardtr | 1h+ | Prep for meeting with Dr. Taylor W2 status report. Plus looked over some merge requests as well as discussed some of the student outcomes (what is uability testing? etc.) | #7 | msoe-sisbot |
| 2020-12-10 | @burkhardtr | 2h | Tested using a USB audio card to output sound while the lights are running and failed miserably. Using an external audio card requires re-configuring the alsa which will disable GPIO output. I haven't tested input but I have a hunch that it won't be much better than output (using the same USB audio card). It remains to be seen whether a stand alone USB microphone might be able to circumvent the alsa requirements (especially since audio input isn't native to the Pi). It seems that since the Pi is limited in which I/O interface has control over the PWM we might need to use GPIO to generate or accept audio signals - will investigate further based on @flemingg's research. | #15 | msoe-sisbot |
| 2020-12-10 | @burkhardtr | 1.5h | Attempted to switch the output of the PINs to use PCM vs PWM which would enable analog output. I was able to get the LEDs to run on new Pins and then run audio through the jack (without lights running) but afterwards I couldn't get the lights working again (even reverting to old pins). Most likely I messed up some config thing that I can't remember changing - will investigate further since according to the underlying PWM/PCM library it is possible to run GPIO with analog audio output (or I2C audio for input) by using different pins. https://github.com/jgarff/rpi_ws281x | #15 | msoe-sisbot |
| 2020-12-10 | @burkhardtr | 2.5h | Enabled audio output while lights are running! I was able to switch the GPIO pin from 18 to 21 which uses the PCM rather than the PWM which frees it for audio output. I am planning on developing a script that will monitor audio output and change the lights accordingly as a small spike. I also have a USB soundcard and USB mic which can be used to test lights responding to ambient audio (it would require switching the GPIO to use SPI rather than PCM which requires for Pi configuration than I currently understand) | #15 | msoe-sisbot | 

## Casper, Joseph
###### Hours: 5 + today
###### Rating (0-10): 5
###### Summary:

| Date | User | Hours Spent | Description | Issue/MR | Repository |
|------|------|-------------|-------------|----------|------------|
| 2020-12-07 | @casperjm | 1h | Weekly team stand up | #7 | msoe-sisbot |
| 2020-12-09 | @casperjm | 2h | Finshed holidays and put up for review | #13 | msoe-sisbot |
| 2020-12-10 | @casperjm | 1h | Fixed some issues found in review | #13 | msoe-sisbot |
| 2020-12-10 | @casperjm | 1h | Met with team to do reviews and to do the status report | #7 | msoe-sisbot |


This week I finished up the holiday light pattern. I submitted my merge request and got a lot of feedback, so I spent some time polishing my code up before it was approved and merged. I will be picking up some tickets to work on that are outside of the sprint as I have nothing to work on at the moment

## Enters, Stuart
###### Hours: X
###### Rating (0-10): X
###### Summary:

## Fleming, Grace
###### Hours: 13
###### Rating (0-10): 5
###### Summary: I felt very useless this week after the lights got fixed. I spent a lot of time researching for our spike PBI but without axilliary hardware I wasn't able to implement anything useful.
| Date         |      User    | Hours Spent | Description | Issue/MR | Repository |
|--------------|--------------|-------------|-------------|----------|------------|
| 2020-12-04	|Grace Fleming|	0.25h	| Meeting with Dr. Taylor (logged in retro) |Group Meetings Time Log| msoe-sisbot| 
| 2020-12-07	| Grace Fleming| 1.25h	| Weekly meeting with the team. Worked on standup and sprint planning. |Group Meetings Time Log	|msoe-sisbot|
|2020-12-07	|Grace Fleming|	1.50h	| Emailed with Matt & tried a few things (reinstalling python). Scheduled a meeting for 12/08 to walk through the light issue in real-time. Tried a GPIO utility called pigpio as a last-ditch effort to find a way to "see" what's happening on each GPIO. After trying this GPIO utility, reattaching the hat and rebooting the pi the lights WORKED :) Will continue monitoring to future issues.| 	Table Issue: Lights are not turning on on the coffee table| msoe-sisbot |
| 2020-12-07	|Grace Fleming| 1.50h	| Researched the audio issue further. I am unsure of whether we can use GPIO's as audio input due to the fact the pi hat is currently covering up all of the GPIO's. I think I need to interface with Matt about this, though, since at least in code, the raspberry pi only dedicates 1 GPIO to the lights. I ensured HDMI was not an option for audio input (Pi does not support ARC). Furthermore, the audio jack on the pi can only be used for audio OUTPUT (which we are currently using the DMA channel for anyway) and not input. Next plan: get in touch with Matt about GPIO usage, and try to locate a relatively inexpensive USB microphone to test with. | Knowledge Acquisition: Sync Table Lights with Audio Track|msoe-sisbot|
| 2020-12-10 | Grace Fleming | 1.5h 	| Researched USB/pi configurations a bit more. Looked into how one might use GPIO's for input along with the i2c codec. Realized that because the pi doesn't have analog GPIO's, using the GPIO pins may not be possible anymore, and USB may be our only option :( Finally emailed Matt to ask for his thoughts and opinions on how he'd go about adding audio input. Matt threw out the idea of using a USB hub, which might be possible except that currently USB's can't do sound input while we have the GPIO's active. | Knowledge Acquisition: Sync Table Lights with Audio Track |msoe-sisbot|
| 2020-12-10 | Grace Fleming | 0.5h 	| Theorized a new PBI idea for remote control of a Sisyphus table. This could be useful for troubleshooting, or maybe even for people who want to have monitoring and control over their tables from a distance. Also, this would help us conduct remote and asynchronous usability studies. | Group Meetings Time Log | msoe-sisbot |

Insert Summary Here

## Wojciechowski, Andrew
###### Hours: X
###### Rating (0-10): X
###### Summary:

Insert Summary Here

# Discussion


## Key Meetings
* 2020-12-07: We met as a team for sprint planning

## Findings
* We are capable of playing audio while using GPIO lights (using PCM for GPIO control, and PWM for audio output)

## Successes
* We finished 2 new light patterns and got the code reviewed
* Grace got the lights working again

## Risk Updates
* None here

# Questions

Is the usability testing student outcome assessment a team activity?

# Conclusion

Over the course of this week, we groomed our backlog after being away from this project for a while, we fixed issues we were having with the table, completed a knowledge acquisition and discussed next steps, completed two new light patterns, and planned a possible usability experiment to discover new potential features.