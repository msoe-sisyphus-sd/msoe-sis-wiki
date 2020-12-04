# Sprint Goal

Finish off carryover from sprint 2, and explore methods of input for lighting dependent on physical environment.

# Burndown Chart

![image](uploads/3d6c26dc7433821aec4074360f1b58be/image.png)

# Team Commitment

## Burkhardt, Robert
###### Hours: ~1h (Thursday meeting with team)
###### Rating (0-10): -2 (at least I'm doing better than our initial pylint score!)
###### Summary:

I have not made any notable progress on any assigned PBIs. I might argue that I spent this week adjusting to the new quarter and I spent the break decompressing from last quarter but these are just excuses and do not justify my behavior. This is completely unprofessional and inconsiderate to my teammates. I promise to both Dr. Taylor and my team to make up this weeks work and more in the coming days so that I am making contributions to the team and helping complete this sprints work.

## Casper, Joseph
###### Hours: X
###### Rating (0-10): X
###### Summary:

Insert Summary Here

## Enters, Stuart
###### Hours: X
###### Rating (0-10): X
###### Summary:

Insert Summary Here

## Fleming, Grace
###### Hours: 9.5
###### Rating (0-10): 7
###### Summary:
This week I worked mostly on troubleshooting the table's lack of lights. My major mistake this week was not putting enough time into my actual sprintwork and more time playing lab tech.
| Date       | User          | Hours     | Desc            | Issue | Repository |
|------------|---------------|-----------|-----------------|--------|-------------|
| 2020-12-01 | Grace Fleming | 2 	| Looked for a list of which DMA channels the Raspberry pi with Raspbian running on it would use regularly. Basically--no such list exists (https://www.raspberrypi.org/forums/viewtopic.php?t=246305). Raspbian used to ship with a file telling the user which channels the OS needed but this is no longer available (https://www.raspberrypi.org/forums/viewtopic.php?p=1027708#p615725). I did locate the DMA address map on the official website (https://www.raspberrypi.org/app/uploads/2012/02/BCM2835-ARM-Peripherals.pdf) but this does not elaborate for which DMA channels are used for what since it is a chip spec and not related to the OS running on the chip. At the very least, it should be possible to use GPIO to control sound (http://blog.koalo.de/2013/05/i2s-support-for-raspberry-pi.html), as some indie hacker dude accomplished it, and he isn't the only one (his article was just the most explanatory, so I'm dropping it here for future reference). | Knowledge Acquisition: Sync Table Lights with Audio Track |msoe-sisbot |
| 2020-11-30 | Grace Fleming | 1.5 | Discovered the issue with the lights upon return to school, and initially tried to restart node, retart the table, restart the python process, manipulate LED's individually. Upon these steps failing I attempted to physically access the lab to physically unplug/replug in the table, but found my access revoked to DH329. Put in an IT ticket for access to the lab. | Table Issue: Lights are not turning on on the coffee table | msoe-sisbot |
| 2020-12-01 | Grace Fleming | 1.0 | Gained physical access to the lab. Manually tried turning the table off/on again. To my shock and disappointment this did not fix the lights. Repeated the software-controllable steps from yesterday as a sanity check. Informed team of the issue, then coordinated to meet up physically with Andy later in the day to test the table with his pi. | Table Issue: Lights are not turning on on the coffee table | msoe-sisbot |
| 2020-12-02 | Grace Fleming | 1.5 | Met with Andy at 6PM in the Cyber lab. We attempted to wire the table's lights to his pi, but were stopped by a concern about grounding the lights correctly. The table's lights have a 3-wire pow/gnd/data line at one end and a 2-wire pow/gnd data line at the other. Andy's local setup was configured to use a 2-wire pow/gnd input for the power supply and then another 2-wire gnd/data for his pi. We weren't sure on the exact steps required to translate the table's wiring to the pi's, because I was concerned that if we grounded the lights to the power supply, we would cause issues by not using the ground from the pi. At the same time, I was hesitant to ground both to the power supply and the pi because we would've had to also connect power to the pi. Andy and I called George in hopes of resolving the issue, but were unable to reach a resolution. George suggested wiring Andy's pi to the table's hat directly which seemed like a great idea, until we realized that Andy's model 4 uses a USB-C power supply and the table uses a micro-USB power supply. Without having a properly rated adapter, I didn't want to risk frying either device. Finally, I attempted to swap the lights on the table from the existing light strip to the older, mostly burnt-out strip. This effort was unsuccessful, and the old strip didn't illuminate. | Table Issue: Lights are not turning on on the coffee table | msoe-sisbot |
| 2020-12-03 | Grace Fleming | 1.5 | Having a rough idea that the lights were not the issue with the setup, I decided to verify by using the LED strip from Dr. Taylor's table with the lab table. I had some concerns about hooking up the lights, since the wiring for the smaller strip varies from that of the larger strip. I successfully manipulated the whichcsons config file to ensure we weren't trying to access LED's that didn't exist, however, and then wired the lights as normal. There was no visible illumination, even with explicit python manipulation. After this failure, I touched base with the team over MSTeams and we decided reflashing the table's SD card was worth a shot, so I created a backup of the table's existing SD card image, before flashing a copy of the image from Dr. Taylor's table onto the lab table. This required re-setting the static IP and re-configuring the whichcsons file again. After doing all this, reattaching the original light strip and doing a hard reboot (power supply on/off), the lights still failed to illuminate. Discouraged, I informed the team and we brainstormed next steps, including 1) informing Dr. Taylor and 2) Getting in touch with Bruce/Matt. | Table Issue: Lights are not turning on on the coffee table | msoe-sisbot |
| 2020-12-04 | Grace Fleming | 2 | Frustrated with the ambiguity surrounding the table's issues, I decided this morning to transport the table's strips (both the old burnt one and the new one) to my apartment for reverse testing with Dr. Taylor's mini table. To my surprise, both light strips illuminated with the mini table (although the burnt one was...well, mostly burnt). This confirmed my suspicion that the LED lights are not to blame for the lab table's lack of illumination. The team theorized that there must be an issue with the Pi hat on the table or the wiring in between. Visual inspection on my part showed no issues with the wiring under the lab table, but I'm not an EE. I could've missed something. | Table Issue: Lights are not turning on on the coffee table | msoe-sisbot |


## Wojciechowski, Andrew
###### Hours: 8
###### Rating (0-10): 6
###### Summary:

| 2020-11-09 | @wojciechowskia | 2h | Tried using my RGB strip using Stuart's setup which involved plugging the LED strip directly into the power supply but I still ran into problems with my black wire getting bent and being difficult plug in. I'm going to try it on my RGBW strip that I ordered which should arrive tomorrow and if that doesn't work I'll take the RGB strip down to campus on Wednesday and have one of my team members with the proper tools help me. | #25 | msoe-sisbot |
| 2020-11-10 | @wojciechowskia | 0.5h | Got the lights working on a new RGBW strip that I received by directly plugging into the power supply | #25 | msoe-sisbot
| 2020-12-01 | @wojciechowskia | 1.50h | Spent some time troubleshooting with Grace. Tried to use the table's lights on my local setup but we didn't given we didn't want to break the strip since my local setup could only power 60 LEDs instead of the entire strip. Also, we looked into trying to run the table using my Raspberry PI but there were compatibility issues between my PI 4 and the PI 3 that the table used. | #37 | msoe-sisbot |
| 2020-12-03 | @wojciechowskia | 1h | Spent some time looking into this. I don't think it will be possible to implement this pattern since you can only set the brightness for the entire light strip instead of individual LEDs making it impossible to make one side of the strip dimmer than the other. | #30 | msoe-sisbot |
| 2020-12-03 | @wojciechowskia | 2h | Came up with an idea to use the white pixel to control whether the lights become dimmer or not. Implemented the initial light pattern based on this idea, still need to test it in which I'm probably going to mock out theta and rho values until we figure out why the lights on the Coffee table won't turn on. | #30 | msoe-sisbot |
| 2020-12-03 | @wojciechowskia | 0.5h | Added some code comments explaining the math behind the magnetic pattern, fixed an issue with indexes, refactored variable names to be clearer, and added a missing import in the magnetic pattern file. | #30 | msoe-sisbot |
| 2020-12-03 | @wojciechowskia | 0.5h | Spent some time reading through the ball plotter code and led_main to learn more about the theta and rho values that are given to the lights module. I also read through a few of the .thr files where some of them has negative theta values so I added handling for that in the magnetic light pattern. | #30 | msoe-sisbot |

# Discussion

* Since the table seems to have continuous issues - the team created a PBI to track time spent debugging the table that will exist across sprints (similar to how the Ceremonies PBI exists).

## Key Meetings

* Andy and Grace met Tuesday (2020-12-01) to debug the lights in lab (George briefly joined via Teams to give his 2 cents).

## Findings

* GPIO can be used for audio input!!
* Productivity really suffers during term breaks and week 1 of new terms.

## Successes

* Grace was able to use Dr. Taylor's table setup to test the large table's light strip and isolate the issues to the table hardware and not the lights (which still work).

## Risk Updates

* The table lights aren't working again (uh oh) - but the motors still run and the server is still accessible so it's more likely a hardware issue (probably the Pi Hat or wiring between the Pi and the strip).

# Questions

* How does Dr. Taylor feel about re-locating the mini table to the lab?
* How should we proceed with fixing the table? We promise we aren't incompetent!
    * Should we reach out to Bruce and Matt?
* Can you grant us access to a Pi 3 Model A from EECS to both help debug the table and to switch out Grace's Pi (which is currently running the stream)?

# Conclusion

The team is disheartened by the electronic issues and doesn't feel great about our "contributions" for the first couple weeks. However, we are rearing to tackle the remaining work in the coming weeks and hunt down all the electronics gremlins (see below).

(We might get in contact with some of our EE/CE peers to see if they have any insights)

![image](uploads/58adcaff33fd81ba69336e7b4628db4b/image.png)