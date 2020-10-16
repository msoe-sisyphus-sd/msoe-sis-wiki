# Sprint Goal

Finish off any zero-day items for setup and develop simple yet creative light sequences to demonstrate setup completion.

# Burndown Chart

Link Chart Here

# Team Commitment

## Burkhardt, Robert
###### Hours: X
###### Rating (0-10): X
###### Summary:

Insert Summary Here

## Casper, Joseph
###### Hours: 9.75 + today
###### Rating (0-10): 8
###### Summary:

- 10/09 - 45m - Meeting with Dr. Taylor
- 10/12 - 1h - Weekly team standup
- 10/13 - 4h - Spent time deploying code to the table and learning how to push new light modes to it. Running into a bug where its not recognizing the new light mode
- 10/15 - 4h - Implemented a spinning light pattern. A lot of the time taken today was figuring out how to reliably push and test new light code to the table, which Grace helped with.
- 10/15 - tbd h - Wrapped up the week by reviewing PRs, writing the deliverables, planning the next sprint, etc.

This week was more successful than previous weeks. Since the lights are up and running on the table, I was able to finish the spin light pattern. I also know how to get new light patterns to run on the table, which was more confusing than it looked

## Enters, Stuart
###### Hours: 15
###### Rating (0-10): 8
###### Summary:

Completed setting up the automated tests as well as documenting the setup process. Nearly completed setting up the lights

## Fleming, Grace
###### Hours: 9.5
###### Rating (0-10): 9.2
###### Summary:
* Met with Dr. Taylor & discussed sprint endgame. Also invited Bruce to our next meeting on Friday. Also learned about ABET supervision of university programs (not sure if should log time for that, so didn't). 
* set up twitch stream on a raspberry pi with a Logitech webcam that was given to me as 'celebratory desk junk for your departure' when I left Direct Supply (courtesy of Addam Wierich). Stream is configured as a linux service (called stream). Credentials for the pi are available upon request.
* Met with team for weekly meeting -- sprint plan, next sprint, etc. Much paperwork. (also sorry for logging this 2 days late, somehow I never remember to log group meetings).* WOO! Made the lights turn into a clock. Colors currently are thus-- second hand - pink minutes hand - orange hour hand - light blue
  * NOTE that the background color of the table is a dark blue, so the hour hand is not particularly visible. I will fix this when I go in tomorrow to shift the lights such that the 12 is opposite the webcam (currently the clock is 'upside down'). I also need to make the code less gross. BUT IT WORKS!
* Spent time looking at the difference between RGB and RGBW strips and whether or not that was affecting our ability to develop locally (with George).
* Looked at the RGBW vs RGB issue on neopixel strips with George
* finished setting up my local setup (yay, it works now!)
* PR's and end-of-sprint stuff.

## Wojciechowski, Andrew
###### Hours: 8.67
###### Rating (0-10): 8
###### Summary:
Comments made to issues in GitLab

* Added README instructions to Grace's PR explaining how to create a whichcson.js file
* Spent some time looking at the pipeline for the test project. The GitLab CI file looks correct but it looks like there is an issue with our Raspberry PI runner.
* Started looking at hooking up the lights and I got very confused by the electronics. I'm going to ask if any of my group members can help me.
* Meeting with the team to start the sprint 2 plan and to plan out finishing out PBIs for the sprint.
* Got the node testing framework setup with some basic tests added and I added a new node stage to the GitLab CI file.
* Made some progress with figuring out how to wire the lights but I'm still really confused. I reached out to George for some help.
* George guided me through setting up the lights circuit. Unfortunately it's still not working. I'll investigate more later.
* Brief investigation individually to see why the node pipeline was failing. Then I talked with Stuart later and he was able to fix the node pipeline.

# Discussion

Insert Discussion Points here

# Questions

Insert Questions here

# Conclusion

Insert Conclusion here