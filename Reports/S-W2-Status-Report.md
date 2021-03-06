# Sprint Goal

A user will be able to enable mood lighting and see its effects on the lab Sisyphus table.

# Burndown Chart

![image](uploads/c19488ddf806375b9f69c750a8113f60/image.png)

# Team Commitment

## Burkhardt, Robert
* Hours: 6
* Rating (0-10): 7.23
* Summary:

|       Date | Hours Spent | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Issue | Repository  |
|------------|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|-------------|
| 2021-03-12 | 1h          | Met with Dr. Taylor to discuss week outcomes and potential changes to process. It was decided to move to two week sprints (after the current one closes out) and reduce the amount of documentation put into status reports.                                                                                                                                                                                                                                           | #59   | msoe-sisbot |
| 2021-03-16 | 1h          | Met with team to do weekly standup and discuss issues with our current architecture (consideration was made to adjust to C++ rather than python - but this still requires further discussion). The team has decided to stay the course with Python for the remainder of this sprint                                                                                                                                                                                    | #59   | msoe-sisbot |
| 2021-03-16 | 1h30m       | Continued to map music to colors to get a baseline understanding of variance and how the colors are being generated.                                                                                                                                                                                                                                                                                                                                                   | #58   | msoe-sisbot |
| 2021-03-17 | 1h          | Began considering how to best implement color smoothing as it relates to the coordinate system. My initial thought is to change the continuous color spectrum to a more discrete spectrum and force similar colors to default into a certain bucket (thus mitigating drastic changes). This also has the benefit of allowing the algorithm to easily switch to a different color when a completely different type of song begins to play. Code is still forthcoming... | #58   | msoe-sisbot |
| 2021-03-18 | 1h30m       | Weekly status report meeting, merge request review, and standup.                                                                                                                                                                                                                                                                                                                                                                                                       | #59   | msoe-sisbot |

## Casper, Joseph
* Hours: 6.5
* Rating (0-10): 5
* Summary:

| Date | User |	Hours Spent | Description | Issue | Repository |
| ------ | ------ | ------ | ------ | ------ | ------ |
| 2021-03-12 | casperjm | 1h | Weekly meeting with Dr. Taylor | #59 | msoe-sisbot |
| 2021-03-12 | casperjm | 1h | Met with Stuart to try to diagnose why sisproxy wasn't running on his Pi. We managed to fix some of the issues, but he ended up running into an issue with his Python distribution. | #41 | msoe-sisbot |
| 2021-03-17 | casperjm | 2h | Reviewed the code that I'll be modifying in the smoothing PBI, began working on an implementation | #58 | msoe-sisbot |
| 2021-03-17 | casperjm | 1h | Weekly stand up | #59 | msoe-sisbot |
| 2021-03-18 | casperjm | 1.5h | Met with team to do merge request reviews and to write the status report | #59 | msoe-sisbot |

This week I started work on the smoothing PBI. At first I was unsure of exactly what was supposed to be accomplished by this ticket, but I have a much clearer idea of what to do after talking about it with the team.

## Enters, Stuart
* Hours: 6.5
* Rating (0-10): 4
* Summary:

| Date | User |	Hours Spent | Description | Issue | Repository |
| ------ | ------ | ------ | ------ | ------ | ------ |
| 2021-03-12 | enterss | 1h | Weekly meeting with Dr. Taylor | #59 | msoe-sisbot |
| 2021-03-12 | enterss | 4h | Worked on getting the server running locally, had to deal with a bunch of install issues. I think I'm just going to flash a new image and start over | #61 | msoe-sisbot |
| 2021-03-18 | enterss | 1.5h | Met with team to review merge request, standup, and status report | #59 | msoe-sisbot |

I unfortunately had a lot going on this week personally and with other classes, so I could not perform as well as I wanted to. Hopefully I can get my Pi imaged tomorrow, then complete the endpoint PBI, which shouldn't take too long. Depending on the response we get from Matt, I may or may not make good headway on that PBI.

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