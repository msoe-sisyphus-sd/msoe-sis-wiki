# Sprint Goal

Continue exploring different light patterns and being investigating additional inputs to affect lighting schemes.

# Burndown Chart

![image](uploads/6ea3370eaac1bf86387d99a9f320f5ef/image.png)
_As a reminder - we forgot to start the milestone on time so we adjusted the start date to give a more representative burn down chart._

# Team Commitment

## Burkhardt, Robert
###### Hours: ~5h + Thursday Meeting
###### Rating (0-10): 7.5
###### Summary:

| Date | User | Hours Spent | Description | Issue/MR | Repository |
|------|------|-------------|-------------|----------|------------|
| 2020-10-23 | burkhardtr | 30m | Met with Dr. Taylor for weekly advisor meeting. In this meeting we discussed the sprint review, the status of the sprint, student outcomes due the following week, and briefly touched the software components report and improvements that could be made to it. We also discussed the macro schedule of the project and the micro schedule of the next couple weeks (with Dr. Taylor's availability). | #7 | msoe-sisbot |
| 2020-10-26 | burkhardtr | 20m | Met with team to perform standup - not a lot went on. Briefly touched on Stuart's PR. | #7 | msoe-sisbot | 
| 2020-10-26 | burkhardr | 1h | Finished drafting the file and attempted to run it on the table but to no avail (I was remote). I think what was going wrong was I didn't have the right endpoint and I might need to build an object in the runtime to reference the file (or find the right schema). My plan is to tackle this with the table in person. | #23 | msoe-sisbot | 
| 2020-10-21 | burkhardtr | 2h | Fixed more ESLint errors. Again, I am spending a bit of time ensuring that the functionality is preserved. The code uses a lot of pre ES6 patterns (no classes), with `var` and `this` embedded in anonymous functions - this means that the functions can change at runtime so I need to trace the objects and ensure something like an unused variable isn't being called with from different calling context | #28 | msoe-sisbot
| 2020-10-29 | burkhardtr | 45m | Tried to put `eslint` in the test runner but due to some issues it was reset and was not live. I also spent time re-familiarizing myself with the gitlab-ci yml format and options for efficient execution (caching and such). | #28 | msoe-sisbot
| 2020-10-29 | burkhardtr | 30m | Was inspired by Bruce's comment about printing the time on the table with the track so I spent some time "sprint planning" and coming up with circular designs for printing time. I plan on refining the designs and uploading them to a new PBI for grooming. | #23 | msoe-sisbot

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
###### Hours: 9.08
###### Rating (0-10): 7
###### Summary:

| Date | User | Hours Spent | Description | Issue/MR | Repository |
|------|------|-------------|-------------|----------|------------|
| 2020-10-23 | Andrew Wojciechowski | 1h | Met with Dr. Taylor to discuss the state of the project and the schedule for the rest of the quarter | 7 | msoe-sisbot |
| 2020-10-26 | Andrew Wojciechowski | 0.50h | Tried a few more things on my local light setup. The wire connections on the power supply feel secure so I'm starting to think it's a problem with the red and black wires having too small connections on them. Reached out to George for help on this | 9 | msoe-sisbot |
| 2020-10-26 | Andrew Wojciechowski | 0.25h | Noticed some things we need to resolve with our automated testing repo. Our install scripts are currently pointing to clone the repo to a branch that has not been merged yet and I have a few questions for the team about what we want our process to be for making changes to that repo. I wrote down some questions in preparation for that later today. | 17 | msoe-sisbot |
| 2020-10-26 | Andrew Wojciechowski | 0.33h | Standup, and talked about merging one of Stuart's old automated testing branches into dev in order for us to add new automated tests | 7 | msoe-sisbot |
| 2020-10-27 | Andrew Wojciechowski | 0.33h | Tried peeling back the plastic casing on the wires on my light strip and failed miserably and I made the wire tips even shorter than they were before. I'm going to try using some actual wire equipment next | 25 | msoe-sisbot |
| 2020-10-27 | Andrew Wojciechowski | 0.33h | Implemented the rest of the weather pattern, need to find some time to test with the table. | 17 | msoe-sisbot |
| 2020-10-28 | Andrew Wojciechowski | 3.58h | Started testing my light pattern on the table. I found that I need to make a few changes to have a transition to solid colors. My clear sky pattern looks OK but I'm currently struggling to find a RGBW color that looks like a storm cloud. | 17 | msoe-sisbot |
| 2020-10-29 | Andrew Wojciechowski | 1.75h | Made some adjustments to some of the colors in the weather pattern in order for storm conditions to be more grey. Also, I added transitioning to colors in the pattern and I also filled in a sample location for the pattern being Milwaukee | 17 | msoe-sisbot |
| 2020-10-29 | Andrew Wojciechowski | 1h | Standup and met with team to write status report | 7 | msoe-sisbot |

# Discussion

## Key Meetings

## Findings

## Successes

## Risk Updates

# Questions

Insert Questions here

# Conclusion

Insert Conclusion here