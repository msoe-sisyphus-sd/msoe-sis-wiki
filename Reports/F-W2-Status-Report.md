# *Pre-*Sprint Goal

The team will learn how to develop on the Sisyphus Table and understand the current state and limitations of the code base.

# Burndown Chart

N/A

The team was able to complete one 0-day task:
* #5 - Investigate Python Light Library Testing

Since we are not in a sprint, this PBI was not story pointed and thus cannot contribute to a burndown.

# Team Commitment

## Burkhardt, Robert
###### Hours: 4.5
###### Rating (0-10): 6
###### Summary: 
* Team Meetings
* Cleaned up GitLab wiki
* Established Git flow process
* Investigated current platform dependencies of the Sisyphus Table & Raspberry Pi

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
###### Hours: X
###### Rating (0-10): X
###### Summary:

Insert Summary Here

## Wojciechowski, Andrew
###### Hours: X
###### Rating (0-10): X
###### Summary:

Insert Summary Here

# Discussion

## Key Meetings

The team held two meetings - once at the beginning of the week and once before the Friday Advisor meeting. During the first meeting the team identified "0-day" tasks required to get the team up to speed on the Sisyphus table code-base and clarified the timeline for PBIs, sprint planning, and senior design deliverables. During the second meeting the team finalized the Project Proposal and modified 0-day PBIs.

The team also made contact with the lead developer Matt Klundt.

## Findings

* Andy Wojciechowski discovered that the Python lighting library (Neopixel) requires a Raspberry Pi environment to run and test. This is important because the team now knows that any interactions with the lighting library will require interfacing with a Pi. Additionally, Andy documented the Python Lights Module Architecture in the project wiki.

* George Burkhardt & Grace Fleming identified that the current state of the code base prevents it from being build on any Windows-like system (due to an `epoll` dependency). This was confirmed by Stuart Enters at a later date, when attempting to build on the WSL and identified another incompatible platform dependency - `webshot`.

* Grace Fleming made contact with the lead developer Matt Klundt and was given SSH access credentials, a Postman API collection, and cursory knowledge about additional repos.

## Successes

* Grace Fleming made contact with lead developer Matt Klundt and was able to understand their development process.

* George Burkhardt was able to "fork" the `sisbot` GitHub repository into GitLab.

## Risk Updates

* Joe Casper identified a critical lack of tests for both Javascript and Python code. Tests may only be developed on the Pi itself due to the Neopixel library.

# Questions

* How can the team access and track the table remotely?

* How can the team develop on the table locally in the Senior Design Lab?

* Is it worth investing in some type of emulator/virtualization of the Pi and accessories?

* If we determine each developer should have access to a physical Pi - how do we go about getting funding?

* What do you need from us next week?

* What areas do you think we could improve in?

# Conclusion

The team feels like they've learned a lot and have a better understanding of table and the technologies that drive it. The team is not feeling super confident (~6/10) in getting up and running. The platform issues and remote nature of the school year makes it hard to engage with the table and each other. Regardless, the team will work hard to gain a better understanding before Sprint 1 begins. We are all excited to work on this project and discover how to combine art and technology.