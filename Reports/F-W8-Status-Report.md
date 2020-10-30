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
###### Hours: 3h 20m + today
###### Rating (0-10): 6
###### Summary:

| Date | User | Hours Spent | Description | Issue/MR | Repository |
|------|------|-------------|-------------|----------|------------|
| 2020-10-23 | casperjm21 | 30m | Met with Dr. Taylor | #7 | msoe-sisbot |
| 2020-10-26 | casperjm21 | 20m | Met with team to do stand up and discuss Thursday deliverables | #7 | msoe-sisbot | 
| 2020-10-28 | casperjm21 | 2h 30m | Learned about how to use a breadboard, set up initial circuit for lights | #25| msoe-sisbot | 
| 2020-10-29 | casperjm21 | xh | Fixed neopixel not found bug, worked more on making lights work | #25| msoe-sisbot | 
| 2020-10-29 | casperjm21 | xh | Status report meeting with team | #7 | msoe-sisbot | 

I finally got my hardware, so I'm working on setting up the lights on my Pi. I wasn't familiar with breadboards or circuits, so I spent some time learning about how to do that without frying any of my electronics. After getting an initial set up, I tried running some light testing code, but ran into installation errors. I got some help from my team and resolved the installation errors, but the lights still aren't lighting up, so I'm assuming there's still some wiring issues. 

## Enters, Stuart
###### Hours: X
###### Rating (0-10): X
###### Summary:

Insert Summary Here

## Fleming, Grace
###### Hours: 9.17
###### Rating (0-10): 9
###### Summary:

| Date | User | Hours Spent | Description | Issue/MR | Repository |
|------|------|-------------|-------------|----------|------------|
| 2020-10-26 | Grace Fleming | 0.33h | Reviewed Stuart's PR. | Spike: Setting up automated testing and CI | msoe-sisbot |
| 2020-10-26 | Grace Fleming | 0.33h | Stand-up. Talked about merging in Stuart's PR. Made sure there weren't any special submissions for this week besides the team member communication evaluations. | Group Meetings Time Log | msoe-sisbot |
| 2020-10-27 | Grace Fleming | 4.50h | Spent about 30 minutes researching which framework to use for a simple demo after determining Matt couldn't give us Cordova access. Picked React Native since it seem cross-platform and simple to set up. Wasted about an hour trying to get it set up in a docker container which didn't fully work since the command the dockerfile was using didn't apply to our project, and I didn't want to mess with trying to fix some open source coder's hippee dockerfile on Dockerhub. Switched to using React Native on Windows, where I successfully installed a ran a React-Native app (~30 minutes). Then looked into using a notification listener inteface (installable through npm of course). This ballooned into a 40 minute let's-go-down-the-bunnyhole approach because I couldn't get the npm package working, since it claimed it was missing some internal Android libraries. I finally got frustrated enough to throw my hands in the air and decide 'let's just use Android native, sorry iOS users for thisdemo.' FROM there I installed Android Studio, but the initial installation wasn't quite right--the gradle VM wouldn't start. I tried a few things with adjusting the memory size for gradle since wise folks on Stack overflow had various silver bullet fixes. In the end after ~40 minutes of looking, I simply restarted, re-installed Android Studio and this time it worked (~20 minutes). I had to add my personal android device to my machine in developer mode so that I could run the app. After doing that I created a simple app that RUNS on my google pixel 2 (and the android studio emulator) which took ~30 minutes. I am in the process of implementing the notification listener service, which seems like it's going to work (another ~20 minutes). | Spike: Sync table with phone notifications | msoe-sisbot |
| 2020-10-29 | Grace Fleming | 3h | Looked into controlling lights remotely (again). Found endpoint (with assistance) to control table lighting pattern (1h). Also messed around with trying to get Android to listen for notifications. The app will build, but the service will not start. I am fairly sure it is not an Android API level issue,; basically the service gets loaded but not enabled. Hopefully it is just something dumb I'm doing that I'll figure out soon (2h) | Spike: Sync table with phone notifications | msoe-sisbot |
| 2020-10-29 | Grace Fleming | 1h | Worked on status report/standup with the team | Group Meetings Time Log | msoe-sisbot |

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
* Met Friday 2020-10-23 to meet with Dr. Taylor to review status report and Team Components draft
* Met Monday 2020-10-26 to perform stand up for work completed over the weekend
* Met Thursday 2020-10-29 to work on status report

## Findings
N/A

## Successes
* The team continues to make progress

## Risk Updates
* Some of the team members are dealing with wiring issues but those will be resolved short-circutly

# Questions
* Does our presentation draft require a recording?

# Conclusion
The team feels good-ish. We're making progress but there is a bit of worry surrounding how much of the work will be completed by next week. We don't foresee any issues right now. The team hopes you're doing well Dr. Taylor and hopes to see you up and about soon :heart:.
