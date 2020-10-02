# Sprint Goal

Finish off any zero-day items for setup and develop simple yet creative light sequences to demonstrate setup completion.

# Burndown Chart

![image](uploads/4c84f232020b04e300efef536b7e5cf0/image.png)
[Chart](https://gitlab.com/groups/msoe.edu/sdl/sd21/sisyphus/-/milestones/1)

# Team Commitment

## Burkhardt, Robert

###### Hours: 6

###### Rating (0-10): 5

###### Summary:

* Began to read and understand the current state of the lights code base and APIs
* Attempted to set up Sisyphus Web App locally (and failed)
* Set up a Raspberry Pi environment (still waiting on strip)
* Ordered materials for local development

Insert Summary Here

## Casper, Joseph

###### Hours: 5.5

###### Rating (0-10): 6

###### Summary:

I wasn't able to contribute much because 1) I am waiting on the postal office to deliver my light strip and SD card, and 2) the lights on the table are out, so I'm not really able to work on adding my light pattern. I still made some progress on implementing lights, and I have something that _should_ work, but I need to wait until the light strip is fixed to test it. 

## Enters, Stuart

###### Hours: X

###### Rating (0-10): X

###### Summary:

Insert Summary Here

## Fleming, Grace

###### Hours: X

###### Rating (0-10): X

###### Summary:

Insert Summary Here

## Wojciechowski, Andrew

Hours: 9h

Rating: 7

This week I worked on setting up linting in the sisbot project using eslint and pylint. I was able to get the pylint checked hooked up GitLab CI but we wrote up a different PBI to handle eslint since we were not working in the JavaScript module this sprint and there were 78 eslint warnings in the current JavaScript code. Also, this week Grace guided me through setting up the Coffee table to have a static IP. Finally, I discovered that the LED issue got worse on the Coffee table with most of the LEDs not lighting up now and I communicated that issue to Matt.

# Discussion

## Key Meetings

* Monday 2020-09-28 - Standup
* Thursday 2020-10-01 - Draft Status Report

## Findings

* Matt K. informed us that when an LED burns out it can cascade down the strip resulting in the flickering lights we've encountered over the past week. Sisyphus Industries will be sending replacement LED strips.

## Successes

* Andy and Grace assigned a static IP to the table in preparation to make it available for remote login via the MSOE VPN.
* Andy configured `pylint` to ensure good Python practices
* Stuart configured `pytest` as scaffolding to start writing out a testing suite for the team's changes.
* A majority of the team has received their SD cards and NeoPixel LED strips to enable local development.

## Risk Updates

* MSOE IT has yet to tunnel the table to be accessible over MSOE VPN.
* More hardware is needed to run the strips than initially thought which means safe local development is delayed still.

# Questions

* How uncouth is it to refactor parts of the code base with better practices and patterns?

# Conclusion

The team feels demotivated because they don't have the materials to begin working on PBIs (and it's Week 4!), but are looking forward to jumping into things once everything is delivered. The team does not like to be  beholden to MSOE IT or UPS/USPS. We are trying to make the most of this week by expanding our knowledge and completing tasks that don't require Pis and LED strips.