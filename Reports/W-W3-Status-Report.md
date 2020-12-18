# Sprint Goal
Finish off carryover from sprint 2, and explore methods of input for lighting dependent on physical environment.

# Burndown Chart
![image](uploads/41eb594d485dc8eec6ab78d5bee2c52a/image.png)

_Image taken at 2020-12-17 7:02_

# Team Commitment

## Burkhardt, Robert
**Hours**: X

**Rating (0-10)**: X

**Summary**:

Insert Summary Here

## Casper, Joseph
**Hours**: 8.5

**Rating (0-10)**: 6

**Summary**:

| Date | User | Hours Spent | Description | Issue/MR | Repository |
|------|------|-------------|-------------|----------|------------|
| 2020-12-11 | @casperjm | .5h | Meeting with Dr. Taylor | #7 | msoe-sisbot |
| 2020-12-14 | @casperjm | .5h | Weekly team stand up; began sprint planning | #7 | msoe-sisbot |
| 2020-12-14 | @casperjm | 3h | Began fixing eslint errors in the siscloud repo | #34 | msoe-siscloud |
| 2020-12-16 | @casperjm | 3h | Continued fixing eslint errors, almost finished | #34 | msoe-siscloud |
| 2020-12-17 | @casperjm | 1.5h | Team meeting to write sprint report and status report | #7 | msoe-sisbot |

This week I started fixing the eslint errors in the siscloud repo. The first day, I did work setting up eslint and got some initial fixes down, the second day I went more in depth and fixed more errors. There are about a quarter of the initial errors remaining. 


## Enters, Stuart
**Hours**: 10

**Rating (0-10)**: 7

**Summary**:
| Date | User | Hours Spent | Description | Issue/MR | Repository |
|------|------|-------------|-------------|----------|------------|
|2020-12-11|@enterss|2.67h|Looked at Andy's merged in code for a scaffold. Began working on converting the maths into code|#19|msoe-sisbot|
|2020-12-11|@enterss|1.25h|Met with team and did status report|#7|msoe-sisbot|
|2020-12-11|@enterss|0.50h|Met with Dr. Taylor|#7|msoe-sisbot|
|2020-12-14|@enterss|0.50h|Team sync meeting & initial sprint 4 planning|#7|msoe-sisbot|
|2020-12-16|@enterss|1h|translated math into pseudocode|#19|msoe-sisbot|
|2020-12-16|@enterss|0.50h|Helped Grace debug light issue|#7|msoe-sisbot|
|2020-12-17|@enterss|2h|Meeting with team for end of sprint ceremonies|#7|msoe-sisbot|
|2020-12-17|@enterss|0.50h|Worked with George to implement pseudo code|#19|msoe-sisbot|
|2020-12-17|@enterss|1h|Manual testing of the pattern|#19|msoe-sisbot|

## Fleming, Grace
**Hours**: X

**Rating (0-10)**: X

**Summary**:

Insert Summary Here

## Wojciechowski, Andrew
**Hours**: 12h

**Rating (0-10)**: 8

**Summary**:

| Date | User | Hours Spent | Description | Issue/MR | Repository |
|------|------|-------------|-------------|----------|------------|
| 2020-12-11 | @wojciechowskia | 30m | Meeting with Dr. Taylor | #7 | msoe-sisbot |
| 2020-12-13 | @wojciechowskia | 4h 30m | Merged in sisbot updates from the GitHub upstream. This was very tedious since the eslint change caused a ton of merge conflicts. Since we didn't make any changes other than linting I accepted all of Matt's changes, fixed eslint errors again, and reran prettier formatting on all of the JS files. Sisproxy and Siscloud also had updates so I merged those into new dev branches in our repo to correspond with our sisbot dev branch. Those were easy fast-forward merges. Finally, I verified that we were able to run these changes on the table. Ran into some issues with the lights module not being installed on the table so I installed pip on the Coffee table and I was able to verify the LED lights were still working with these changes. | #38 | msoe-sisbot |
| 2020-12-14 | @wojciechowskia | 30m | Met with the team and created the initial sprint plan for sprint 4 | #7 | msoe-sisbot |
| 2020-12-15 | @wojciechowskia | 30m | Created a new PI 4 image from my local PI setup for Grace to use. | #7 | msoe-sisbot |
| 2020-12-15 | @wojciechowskia | 30m | Wrote up a new wiki article for local setup instructions | #7 | msoe-sisbot |
| 2020-12-17 | @wojciechowskia | 30m | Re-added eslint to the updated sisproxy code pulled from the upstream repo | #38 | msoe-sisbot |
| 2020-12-17 | @wojciechowskia | 2h | Setup Grace's demo on my setup just in case we need to use my light strip for that demo. I plan to add the extra libraries that I installed in the demo repo and Grace is planning on getting the code updated to work with the lights. | #15 | msoe-sisbot |
| 2020-12-17 | @wojciechowskia | 1h 40m | Meeting with team, standup, wrote status report, modified the sprint 3 and 4 plans, and discussed sprint review tomorrow. | #7 | msoe-sisbot |
| 2020-12-17 | @wojciechowskia | 1h 20m | Helped Grace resolve some issues with installing the LED library using python3. Also, looked at trying different wav files to try and change the color. | #15 | msoe-sisbot |

# Discussion

## Key Meetings

* 2020-12-11 - Met with Dr. Taylor to discuss sprint progress
* 2020-12-14 - Weekly Team Meeting for sprint update and Sprint 4 planning
* 2020-12-17 - Team meeting to finish sprint 3 documentation

## Findings
* Bruce gave the team a list of potential long-term projects 
    * HomeKit Integration / Android Home Automation Integration
    * Better Ambient Lighting
        * The team is a bit warry of this project since it seems to lack the depth of a long term project.
            * Machine learning to select lighting curve
            * Use camera instead of photo-resistor
            * External lighting module
* Audio input and output is possible with the lights running

## Successes
* Audio input can be used to adjust the brightness of the LEDs
* Implemented ML algorithm to generate colors based off WAV file
* The upstream was merged into our working repository

## Risk Updates
* Batteries can catch fire :fire:
    * Grace is cursed and therefore banned from the Cybersecurity lab (2 Yays, 1 Nay, 2 Abstains) /s

# Questions
* When should our technology report be due?
* Add Bruce and Matt as guests to team chat?

## Really Important Questions
* How are you (like really)?
* Which freshman SE do you hate the most?
* Which freshman SE do you like the most?
* Which major do you hate the most and why is it CE?

## Really Really Important Questions
* What is the meaning of life, the universe, and everything?

# Conclusion
All in all the team feels it has been a really good sprint. In addition to completing outstanding sprint work the team was able to investigate audio input and output while running the lights. Furthermore, the team was able to tackle DX (developer experience) debt with merging upstream changes into our working repository and clearing up `eslint` errors in `siscloud` and `sisproxy`.

Happy New Year :tada: 