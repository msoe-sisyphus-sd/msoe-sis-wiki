# Sprint Goal

Continue exploring different light patterns and being investigating additional inputs to affect lighting schemes.

# Burndown Chart

![image](uploads/f029730b01f8c248772b9e10ce856cd1/image.png)

_Please note we forgot to start a new milestone last week which means the burndown chart generated with the correct dates had a huge spike in burnup and did not produce a guide line for finishing issues so we adjusted the start date by one week in order to produce a better looking graph._

# Team Commitment

## Burkhardt, Robert
###### Hours: 5 + Thursday meeting
###### Rating (0-10): 7.5
###### Summary:

| Date | User | Hours Spent | Description | Issue/MR | Repository |
|------|------|-------------|-------------|----------|------------|
| 2020-10-16 | burkhardtr | 1h | Met with Dr. Taylor and Bruce to review sprint | #7 | msoe-sisbot |
| 2020-10-19 | burkhardtr | 1h | Met with team to do stand up and discuss Thursday deliverables | #7 | msoe-sisbot | 
| 2020-10-20 | burkhardr | 2h | Began fixing eslint errors while ensuring no regression | #28 | msoe-sisbot | 
| 2020-10-21 | burkhardtr | 1h | Looked at how the system uses theta-rho files to quickly execute on creating the lateral erase pattern | #23 | msoe-sisbot

## Casper, Joseph
###### Hours: 9
###### Rating (0-10): 7
###### Summary:

| Date | User | Hours Spent | Description | Issue/MR | Repository |
|------|------|-------------|-------------|----------|------------|
| 2020-10-16 | casperjm21 | 1h | Met with Dr. Taylor and Bruce to review sprint | #7 | msoe-sisbot |
| 2020-10-19 | casperjm21 | 1h | Met with team to do stand up and discuss Thursday deliverables | #7 | msoe-sisbot | 
| 2020-10-20 | casperjm21 | 2h | Wrote initial code and planned out holiday colors | #13| msoe-sisbot | 
| 2020-10-22 | casperjm21 | 4h | Worked on implementing the holiday light pattern | #13 | msoe-sisbot |
| 2020-10-22 | casperjm21 | 1h | Met with team to write status report and team component paper | #7 | msoe-sisbot |

## Enters, Stuart
###### Hours: 10
###### Rating (0-10): 7
###### Summary:

| Date | User | Hours Spent | Description | Issue/MR | Repository |
|------|------|-------------|-------------|----------|------------|
| 2020-10-16 | enterss | 1h | Sprint review with Bruce & Dr. Taylor | #7 | msoe-sisbot |
| 2020-10-19 | enterss | 40m | Discussed plan with team | #7 | msoe-sisbot |
| 2020-10-20 | enterss | 3m | Tested ability to ssh into the table and examined the table's setup | #9 | msoe-sisbot |
| 2020-10-19 | enterss | 4h 30m | Got hardware set up and lights running locally | #25 | msoe-sisbot |
| 2020-10-19 | enterss | 4h 30m | Worked on getting sisbot running locally | #9 | msoe-sisbot |


## Fleming, Grace
###### Hours: 8.75
###### Rating (0-10): 5
###### Summary:

| Date | User | Hours Spent | Description | Issue/MR | Repository |
|------|------|-------------|-------------|----------|------------|
| 2020-10-19|Grace Fleming|1h | Meeting with team for standup, diagnosing some weird LED issues on George's strip, and talking about the Team Components. | Group Meetings Time Log	| msoe-sisbot |
2020-10-20 | Grace Fleming| 2h	| Looked at controlling table via web requests--`curl -X POST -d 'data={"data": {"value" : 0.2}}' http://localhost:3002/sisbot/set_brightness` and that kind of thing. It works. I also looked into how to detect notifications on Android, but I think I should get access to the codebase for the app before deciding on implementation details for this. | Spike: Sync table with phone notifications| msoe-sisbot | 
| 2020-10-21 | Grace Fleming|1.50h | I tried to build/run the mobile application using Cordova. This was difficult both on my pi and table. I keep getting an error after installing cordova: `cordova SyntaxError: Unexpected token {}` when I run cordova platforms to see which platforms are supported, or even something as simple as cordova --version. I spent some time researching this and trying to figure out how Cordova is actually built. I think I am going to have to email Matt and ask about how he's building this locally if I can't figure out how this builds on my own. | Spike: Sync table with phone notifications | msoe-sisbot
|  2020-10-22  | Grace Fleming | 1.02h | Found out that Cordova works with node 10+, meaning the reason Cordova was crashing was because we are using node 8.x.x. This is problematic. When I fixed the node version then Cordova ran but failed to recognize the `siscloud` directory as a Cordova project.| Spike: Sync table with phone notifications  | msoe-sisbot |
| 2020-10-22 |Grace Fleming|1h | Meeting with team for standup, progress report writing and talking through the Team Components paperwork | Group Meetings Time Log	| msoe-sisbot |
| 2020-10-22|Grace Fleming|1h15m | Looked through the sisbot code searching for a place to put in an endpoint for a notification. The `sisbot.js` file is denser than my Aunt Sara's chocolate cake, however, and was not trivial to read through. I think after an hour of reading through server code I figured out that the proxy handles requests, and then emits the relevant information. Different event handlers respond to the emitted events (so we're not looking at 'normal' endpoints). I'll probably need to add an event handler, then for the phone notifications. Also emailed Matt asking for Cordova devenv setup directions. If he doesn't get back to me, I might be blocked on setting up the mobile app in the meantime.| Spike: Sync table with phone notifications |msoe-sisbot | 

## Wojciechowski, Andrew
###### Hours: 6.75
###### Rating (0-10): 5
###### Summary:

| Date | User | Hours Spent | Description | Issue/MR | Repository |
|------|------|-------------|-------------|----------|------------|
| 2020-10-16 | Andrew Wojciechowski| 1h | Met with Bruce and Dr. Taylor | #7 | msoe-sisbot |
| 2020-10-19 | Andrew Wojciechowski| 1h | Standup, brainstorming discussion, and started talking about the team components reflection | #7 | msoe-sisbot | 
| 2020-10-20 | casperjm21 | 1.75h | Researched weather APIs we could use I think I have a good one we could use. I also developed a mapping based on the weather to the pattern and updated the Acceptance Criteria accordingly. Afterwards then I stubbed out the new light pattern | #17 | msoe-sisbot | 
| 2020-10-21 | Andrew Wojciechowski | 1h | Implemented more of the light patterns and implemented a method to call the Weather API | #13 | msoe-sisbot |
| 2020-10-22 | Andrew Wojciechowski | 1.5h | Met with team to write status report and team component paper | #7 | msoe-sisbot |

# Discussion

## Key Meetings
* Met with product owner on 2020-10-16 to demo sprint results
    * Discussed future of project in relation to sprint planning and "concrete" project ideas to demonstrate ABET requirements
* Team met for stand up and sprint update on 2020-10-19

## Findings
* Grace found out that running the client app via Cordova isn't currently possible on a production image
    * Working on creating a "compatible" image and will reach out to Matt for any help
* Andy found a weather API
    * [https://api.openweathermap.org](https://api.openweathermap.org)

## Successes
* Grace figured out how to use the web APIs to control the table without the app
* Stuart was able to get his local development environment and lights set up

## Risk Updates
* Cordova seems difficult to work with

# Questions

N/A

# Conclusion

The team is jumping into work for Sprint 2 and is feeling good on executing this sprint. The team hopes to groom epics and features relating to lights and not relating to lights for future sprints (potentially additional external sensor inputs).