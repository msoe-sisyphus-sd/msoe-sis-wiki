# Pre-Sprint Goal

The team will further investigate the table's setup (networking, code, dependencies, etc.) and plan PBIs for Sprint 1.

# Burndown Chart

N/A

## PBIs Completed (0-day tasks)
* #3 - Team feels that the setup of the wiki is decent for now.
* #1 - Team has opted to purchase SD cards and LED strips for local development.

## PBIs Refined for Sprint 1
* #4 - Team is planning on setting up Testing in first sprint.

## Blocked 
* #10 - Team moved table into Cybersecurity Lab for easy `ssh` access. Waiting on MSOE IT for VPN configuration.

# Team Commitment

## Burkhardt, Robert

###### Hours: 8

###### Rating (0-10): 7

###### Summary:

* Team Meetings
* Note-taker for meetings and Reports/Plans
* Worked on "debugging" lighting issue on table
* Worked on identifying platform specific code in order to see if we could develop on non-Pi environments
* Worked on adding tasks and acceptance criteria for 2 potential Sprint 1 PBIs
* "Forked" additional code bases into GitLab

## Casper, Joseph

###### Hours: 9

###### Rating (0-10): 7

###### Summary:

- 5.5h in team meetings
- 3h in the senior design lab working with the table/reviewing code
- .5h on student outcome assignments

During team meetings, we wrote PBIs, and for those PBIs, we wrote tasks and acceptance criteria for those PBIs. I learned how to ssh into the table Pi (with the help of Grace). I reviewed the code in the code base to become more comfortable with it. I am feeling confident that with the start of the sprint I will be able to start contributing more. 

## Enters, Stuart

###### Hours: 10

###### Rating (0-10): 3

###### Summary:

I spent my time outside the group continuing to document the existing code. In the group, I discussed the project proposal with Dr. Taylor, helped create a definition of done, created PBIs, and task out #25 and #22, and story pointed PBIs

## Fleming, Grace

###### Hours: 9.5

###### Rating (0-10): 8/10

###### Summary:
This week, I spent time in Networking heaven. I thought it was a pretty good week for me. I started off over the weekend by designing a laboratory lab setup that enabled people to remote into the table while preserving wifi access for onsite development (previously impossible).
During the week I was able to help another member with the same setup, then chat with Jared about how to make this table externally accessible from outside of campus. Finally, I was able to play a role in implementing that solution by actually moving the table (compounded with some LED troubleshooting).
I also spent time in meetings/working on PBIs with the rest of the team, and creating an initial sprint plan outline.

If I could do this week again, I would try and spend more time in the codebase. I pretty much just learned how the lights worked, and didn't learn a ton about the JS stuff.

## Wojciechowski, Andrew

###### Hours: 10.38

###### Rating (0-10): 7

###### Summary:

This week I spent time looking at buying materials to build the code to build on my Real Time systems Raspberry PI. I also spent time reading through the source code of the 2 new git repositories we got access to (sisproxy and siscloud) and getting a understanding for those. I also setup the ability to SSH into the coffee table and I discovered a way to restart the lights without rebooting the table. Finally, I also contributed in team meetings with planning out PBIs for the sprint and I tasked out and wrote acceptance criteria for a few of the PBIs.

# Discussion

## Key Meetings

The team had 3 meetings - once after Week 2 Friday's advisor meeting, once on Monday drafting the initial set of PBIs, and once on Thursday to finalize the Sprint 1 plan and write up the Status Report.

## Findings

* Grace and George discovered that moving the code base to a non-Pi environment is not possible without a concerted effort. The team has moved forward with purchasing appropriate materials for developing on our personal Pis.

* Grace met Jared a MSOE Network Administrator and devised a network topology to allow remote access to the table's Pi while remaining visible to other devices on the network.

* Andy discovered a way to restart the lights without rebooting the whole table via the `restart.sh` script

* Grace and George spent time "debugging" the flashing lights on the table - it is still unknown if the issue is of software or hardware origin.

## Successes

* The team created a signup sheet for access (physical and digital) to the table and respect social distancing protocols.

* The team has figured out how to SSH into the Pi and make changes while IT deploys our plan.

## Risk Updates

* The team is still somewhat unfamiliar with the code base and APIs used on the table. However, the team feels this will be quickly mitigated once Sprint 1 begins.

* The table's lights have begun to flash with out any obvious explanation or source of impetus (no one has made drastic code changes). See question below... 

# Questions

* When can we submit a _draft_ of the Technical Report for overview?
    * Should we submit the report to you (Dr. Taylor) or should we seek an outsider's opinion (i.e. another Senior Design Advisor)
* Lights are flashing and we don't know what's going on?
    * This is more a question for Bruce and Matt


# Conclusion

The team feels like they've learned a lot and have a better understanding of table and how to communicate with it. The team is feeling more confident (\~7.5/10 up from 6) in getting up and running. The team is optimistic about soon being able to access the table from a remote environment. The team is excited for Sprint 1 to begin although weary of some hardware challenges ahead (setting up development environments and the table's lighting issue).

