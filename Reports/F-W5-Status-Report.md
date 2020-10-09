# Sprint Goal

Finish off any zero-day items for setup and develop simple yet creative light sequences to demonstrate setup completion.

# Burndown Chart

![image](uploads/a3f56d4cda8ed9186dc50b76acdff29d/image.png)

# Team Commitment

## Burkhardt, Robert

###### Hours: 8

###### Rating (0-10): 8

###### Summary:

* Set up 2 Pis with Raspbian
* Set up Light strip on Pi with new library
* Got the full code base running (sisproxy, sisbot, siscloud)
* Began writing Python module to change lights based on time of day (immediate switch)

## Casper, Joseph

###### Hours: 6

###### Rating (0-10): 5

###### Summary: 

I finally received my SD card and light strip. However, I learned that I need more materials in order to connect the lights to the pi (power stepping chip, breadboard, jumper cables, power source). I'm not familiar with connecting things to Pis, so I have been researching how to do this while I wait for my new materials. I would have tested my light code on the coffee table, but the lights are still out so I was still unable to test my code. Since the lights will be repaired tomorrow, I'll hopefully be able to use the table at MSOE next week.

## Enters, Stuart

###### Hours: 6

###### Rating (0-10): 4

###### Summary:
* Participated in team meetings
* Worked on installing hardware
* Looked into seting up testing framework for node

## Fleming, Grace

###### Hours: 9

###### Rating (0-10): 8

###### Summary:
* Ran circles around myself with SD card and networking issues.
* Wired neopixels!
* Got neopixels lighting up and working with officially supported neopixel library
* Struggled with getting neopixels working with the sisyphus neopixel code.
* Scraped an SD image from the production version of the table, and used this image to boot my pi 3.
* Determined how to make backups from an SD card, and wrote instructions into the README.md.

Hours: 9
Rating: 8/10

## Wojciechowski, Andrew

###### Hours: 11.07

###### Rating (0-10): 7

###### Summary:
This week I spent a lot of time working on setting up my local Raspberry PI for development. A lot of time I spent debugging issue with installing Raspbian with NOOBS but I was eventually able to get Raspbian installed. I also spent time get node and python installed and I was able to successfully run the sisproxy project locally on my PI.

Insert Summary Here

# Discussion

## Key Meetings

* Standup (2020-10-05)
* Status Report and Tech Report Draft Overview (2020-10-08)

## Findings

* The README is woefully incomplete and very much outdated
* _Do not_ use a Pi 3 SD card on a Pi 4 - it will break the 4
* EE peers were usefully in setting up integrated LED strips (some soldering was required)
* How to run the application and electrical requirements for the Pi
* The code base uses an outdated, open source, "frakenstein-ed" Python 2 library for driving the LEDs which makes it extremely hard to get up and started right now

## Successes

* Some members of the team have their Lights running!
* New lights were shipped and received by MSOE for the Senior Design Table
* A draft of the Tech Report was created
* Pulled a "production" image of the Pi (Dr. Taylor's table) for use on Pis or diagnosing issues
* The code base is closer to having a testing framework and workflow set up

## Risk Updates

* Some members of the team are still waiting on electronics to ship
* The burn down is not looking great

# Questions

* Review our Status Report?
    * Since we aren't introducing new technologies can the prototype section address upgrading technologies (e.g. Python 2 => Python 3)?


# Conclusion

Some of the team is still running into hardware issues (either in shipping or in setting up the environment) which is halting development on PBIs. The burn down doesn't look amazing due to this issue and it's probably very worrying being that we are nearing the end of the 1st sprint - but a lot of learning has been done about the code base, Pis and NeoPixel LED strips. The team chooses to look at this predicament as an investment into more speedy and effective development in the future.