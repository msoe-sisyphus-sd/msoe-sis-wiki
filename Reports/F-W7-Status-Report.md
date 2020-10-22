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
###### Hours: 4 + today
###### Rating (0-10): 7
###### Summary:

| Date | User | Hours Spent | Description | Issue/MR | Repository |
|------|------|-------------|-------------|----------|------------|
| 2020-10-16 | casperjm21 | 1h | Met with Dr. Taylor and Bruce to review sprint | #7 | msoe-sisbot |
| 2020-10-19 | casperjm21 | 1h | Met with team to do stand up and discuss Thursday deliverables | #7 | msoe-sisbot | 
| 2020-10-20 | casperjm21 | 2h | Wrote initial code and planned out holiday colors | #13| msoe-sisbot | 
| 2020-10-22 | casperjm21 | xh | Worked on implementing the holiday light pattern | #13 | msoe-sisbot |
| 2020-10-22 | casperjm21 | xh | Met with team to write status report and team component paper | #7 | msoe-sisbot |

## Enters, Stuart
###### Hours: X
###### Rating (0-10): X
###### Summary:

| Date | User | Hours Spent | Description | Issue/MR | Repository |
|------|------|-------------|-------------|----------|------------|
| 2020-10-16 | enterss | 1h | Sprint review with Bruce & Dr. Taylor | #7 | msoe-sisbot |
| 2020-10-19 | enterss | 40m | Discussed plan with team | #7 | msoe-sisbot |
| 2020-10-20 | enterss | 3m | Tested ability to ssh into the table and examined the table's setup | #9 | msoe-sisbot |
| 2020-10-19 | enterss | 4h 30m | Got hardware set up and lights running locally | #25 | msoe-sisbot |
| 2020-10-19 | enterss | 4h 30m | Worked on getting sisbot running locally | #9 | msoe-sisbot |


## Fleming, Grace
###### Hours: 7.5
###### Rating (0-10): 3
###### Summary:

| Date | User | Hours Spent | Description | Issue/MR | Repository |
|------|------|-------------|-------------|----------|------------|
| 2020-10-19|Grace Fleming|1h | Meeting with team for standup, diagnosing some weird LED issues on George's strip, and talking about the Team Components. | Group Meetings Time Log	| msoe-sisbot |
2020-10-20 | Grace Fleming| 2h	| Looked at controlling table via web requests--
curl -X POST -d 'data={"data": {"value" : 0.2}}' http://localhost:3002/sisbot/set_brightness and that kind of thing. It works. I also looked into how to detect notifications on Android, but I think I should get access to the codebase for the app before deciding on implementation details for this.
| Spike: Sync table with phone notifications| msoe-sisbot | 
| 2020-10-21 | Grace Fleming|1.50h | I tried to build/run the mobile application using Cordova. This was difficult both on my pi and table. I keep getting an error after installing cordova: cordova SyntaxError: Unexpected token {} when I run cordova platforms to see which platforms are supported, or even something as simple as cordova --version. I spent some time researching this and trying to figure out how Cordova is actually built. I think I am going to have to email Matt and ask about how he's building this locally if I can't figure out how this builds on my own. | Spike: Sync table with phone notifications | msoe-sisbot
|  2020-10-22  | Grace Fleming | 1.02h | Found out that Cordova works with node 10+, meaning the reason Cordova was crashing was because we are using node 8.x.x. This is problematic. When I fixed the node version then Cordova ran but failed to recognize the `siscloud` directory as a Cordova project.| Spike: Sync table with phone notifications  | msoe-sisbot |
| 2020-10-22 |Grace Fleming|1h | Meeting with team for standup, progress report writing and talking through the Team Components paperwork | Group Meetings Time Log	| msoe-sisbot |


Hours: 7.5
Effort: 5/10

Insert Summary Here

## Wojciechowski, Andrew
###### Hours: 6.25
###### Rating (0-10): 5
###### Summary:

| Date | User | Hours Spent | Description | Issue/MR | Repository |
|------|------|-------------|-------------|----------|------------|
| 2020-10-16 | Andrew Wojciechowski| 1h | Met with Bruce and Dr. Taylor | #7 | msoe-sisbot |
| 2020-10-19 | Andrew Wojciechowski| 1h | Standup, brainstorming discussion, and started talking about the team components reflection | #7 | msoe-sisbot | 
| 2020-10-20 | casperjm21 | 1.75h | Researched weather APIs we could use I think I have a good one we could use. I also developed a mapping based on the weather to the pattern and updated the Acceptance Criteria accordingly. Afterwards then I stubbed out the new light pattern | #17 | msoe-sisbot | 
| 2020-10-21 | Andrew Wojciechowski | 1h | Implemented more of the light patterns and implemented a method to call the Weather API | #13 | msoe-sisbot |
| 2020-10-22 | Andrew Wojciechowski | 1h | Met with team to write status report and team component paper | #7 | msoe-sisbot |

# Discussion

Insert Discussion Points here

# Questions

Insert Questions here

# Conclusion

Insert Conclusion here