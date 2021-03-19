# Sprint Goal

A user will be able to enable mood lighting and see its effects on the lab Sisyphus table.

# Burndown Chart

![image](uploads/c19488ddf806375b9f69c750a8113f60/image.png)

# Team Commitment

## Burkhardt, Robert
* Hours: X
* Rating (0-10): X
* Summary:

Insert Summary Here

## Casper, Joseph
* Hours: X
* Rating (0-10): X
* Summary:

Insert Summary Here

## Enters, Stuart
* Hours: X
* Rating (0-10): X
* Summary:

Insert Summary Here

## Fleming, Grace
* Hours: 9.5
* Rating (0-10): 8
* Summary: I got some stuff done this week finally, but I wasn't super focused and wasted some time on configuring my environment.

| Date       | User          | Hours Spent | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Issue/MR                                       | Repository  |
|------------|---------------|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------|-------------|
| 2021-03-12 | Grace Fleming | 2h          | Specked out code, but was unable to test because I couldn't connect to VPN using George's instructions. Since I have a different distro, I tried using the Ubuntu 20.04 recommended VPN instructions, but those haven't worked for me either yet :(                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Handle Sisyphus Table Audio Streaming Response | msoe-sisbot |
| 2021-03-12 | Grace Fleming | 1h          | Status report & reviewed Andy's PR for #56                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Q3 Ceremonies                                  | msoe-sisbot |
| 2021-03-15 | Grace Fleming | 1h          | Filled in the translator() and communicator() methods (see architecture diagram). Still need manual/unit testing.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Handle Sisyphus Table Audio Streaming Response | msoe-sisbot |
| 2021-03-16 | Grace Fleming | 1h          | Argue with myself about whether or not global variables are OK here because of the multi-threading approach. Looked into Celery (multithreading library for Python). Come to the conclusion that Python is not the language for doing real-time audio processing. Discuss feasibility of switching languages with Andy. Agree to bring concerns up to team during weekly Tuesday meeting.                                                                                                                                                                                                                                                                                                                                                                                                 | Handle Sisyphus Table Audio Streaming Response | msoe-sisbot |
| 2021-03-17 | Grace Fleming | 3.50h       | Spent a looooong time trying to get Pyaudio for windows working. Tried installing the VSBuild tools (since that is what the error said to do). That didn't work, so I eventually ended up crying to Andy about it who gave me a link to a whl file for installing it. The reaadme.md has been updated with info on how to install pyadudio. Then my windows machine had some issues with pytest :cry: , basically my machine would hang indefinitely while trying to run tests. I eventually solved this by clapping 6 times, turning in a circle while singing "Ring around the Rosie", and running pytest from inside the test directory. It worked this time! I was then able to find errors in my test/code, and get those pushed into a branch. There is currently a PR out for #57. | Handle Sisyphus Table Audio Streaming Response | msoe-sisbot |
| 2021-03-17 | Grace Fleming | 1h          | Standup with team & grooming. Also did some team bonding, which was surprisingly not that bad.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Q3 Ceremonies                                  | msoe-sisbot |

## Wojciechowski, Andrew
* Hours: 9.16
* Rating (0-10): 7
* Summary:

| Date | User | Hours Spent | Description | Issue/MR | Repository |
|------|------|-------------|-------------|----------|------------|
| 2021-03-15 | @wojciechowskia | 0.33h | Filled in some details in some of the future PBIs in the backlog | #59 | msoe-sisbot |
| 2021-03-16 | @wojciechowskia | 2h | Setup siscloud on my local setup and started looking into the issue with the checkbox. I think there is an issue with how the model is instantiated. I'm going to continue looking into the issue. | #41 | msoe-sisbot |
| 2021-03-16 | @wojciechowskia | 1h | Standup with the team and did a little bit of grooming with the team. | #59 | msoe-sisbot |
| 2021-03-17 | @wojciechowskia | 3h | Looked into issues with setting up the checkbox in siscloud. I think I understand what the issue where the change event for the mood lighting toggle is not working properly. I'm not sure why but if I can't figure it out soon we should email Matt | #41 | msoe-sisbot |
| 2021-03-09 | @wojciechowskia | 1h | Discussed designs for sislisten with the team and came up with an architecture diagram with the team. | #55 | msoe-sisbot |
| 2021-03-18 | @wojciechowskia | 0.5h | Looked into this and I am completely stumped. I am going to ask the team if we ever emailed Matt about this issue | #41 | msoe-sisbot |
| 2021-03-18 | @wojciechowskia | 1.33h | Standup with the team, reviewed Grace's MR, and wrote status report with the team. | #59 | msoe-sisbot |

# Discussion

## Key Meetings
* Meeting with Dr. Taylor (3/12), discussed admin information related to senior design show, poster competition, and paperwork plan
* Tuesday team sync (3/15) standup, brief grooming, team bonding

## Findings
* Team discussed languages appropriate for this problem (namely python vs c++) and chose to stick with python _for now_.
* Python's 'periodic tasks' are basically just while loops, so the thread pool pattern might make more sense.

## Successes
* Merged #57

## Risk Updates
* Siscloud is still cantankerous; everyone on the team has looked at it but we still can't determine why the change implementation isn't effective (we will be getting in touch with Matt).

# Questions
* Were we switching paperwork after this sprint, or right now? (this only matters for next week at this point)

# Conclusion
The team made some progress with issues, but does have concerns about whether there will be time to integrate siscloud into the setup. The team theorizes that if this part of left out of the sprint goal we have a decent shot at meeting the goal. Bigger picture, the team has some apprehension about accomplishing everything they want to (particularly beat detection and user settings) by the end of the quarter, but is committed to giving it their best shot.