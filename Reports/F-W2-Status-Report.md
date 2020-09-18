# *Pre-*Sprint Goal

The team will learn how to develop on the Sisyphus Table and understand the current state and limitations of the code base.

# Burndown Chart

N/A

The team was able to complete one 0-day task:
* #5 - Investigate Python Light Library Testing

Since we are not in a sprint, this PBI was not story pointed and thus cannot contribute to a burndown.

# Team Commitment

## Burkhardt, Robert
###### Hours: 5.5
###### Rating (0-10): 6
###### Summary: 
* Team Meetings
* Cleaned up GitLab wiki
* Established Git flow process
* Investigated current platform dependencies of the Sisyphus Table & Raspberry Pi

## Casper, Joseph
###### Hours: 6
###### Rating (0-10): 5
###### Summary:
I started getting familiar with the code in the repo, and I investigated tests for the code. There aren't any tests written for the code that we'll be using (specifically, the files led_main.py, led_startup.py, colorFunctions.py, and sisbot.js.) I suggested that we write tests for these files, though this may be difficult because these files cannot be run unless they're being run on a pi. Also, I talked with the team about our git and development flow. I'll be able to log more hours once we finally get code to start running on the table. I plan on connecting to the table on Monday. 

Insert Summary Here

## Enters, Stuart
###### Hours: 6
###### Rating (0-10): 4
###### Summary:

I participated in team meetings planning how to begin working on the project. I spent a good amount of time trying to get the server running locally so I could see exactly what it did. I am blocked in documenting the existing code until we get access to the remainder of the code (we have 1 of 3 repos)

## Fleming, Grace
###### Hours: 6.33
###### Rating (0-10): 4
###### Summary:
This week, I worked on learning about how development is currently performed on the table.
Learning about the current devenv required getting in touch with Bruce Shapiro, who put us in touch with Matt Klundt, the lead (and only?) developer. I communicated over email with Matt to learn about the current dev process, discovered that there were more repositories we did not have access to, and obtained SSH credentials for the pi.
I also participated in team meetings, and worked on building the codebase on a linux VM (problematic).

## Wojciechowski, Andrew
###### Hours: 8.03h
###### Rating (0-10): 7
###### Summary:

This week I spent some time looking ways we could test the Python lights module. I found a complication related to one of the libraries that the Python lights module uses which will make testing the module difficult where the library can only be imported on a Raspberry PI. I also spent a lot of time reading through the codebase and I put together a architecture document in the wiki for the Python lights module here: https://gitlab.com/msoe.edu/sdl/sd21/sisyphus/msoe-sisbot/-/wikis/Architecture/Python-Lights-Module-Architecture

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