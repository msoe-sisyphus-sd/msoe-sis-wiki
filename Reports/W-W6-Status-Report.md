r# Sprint Goal
Investigate mapping audio to colors and how to integrate a Python ML model with the existing code base.

# Burndown Chart
<TODO>

# Team Commitment

## Burkhardt, Robert
* Hours: 
* Rating (0-10): 
* Summary:

| Date | Hours Spent | Description | Issue / MR | Repository | 
| --- | --- | --- | --- | --- |


## Casper, Joseph
* Hours: 
* Rating (0-10): 
* Summary:

| Date | User |	Hours Spent | Description | Issue | Repository |
| ------ | ------ | ------ | ------ | ------ | ------ |


## Enters, Stuart
* Hours: 19
* Rating (0-10): 10
* Summary:

| Date | User |	Hours Spent | Description | Issue | Repository |
| ------ | ------ | ------ | ------ | ------ | ------ |
2021-01-14 | Stuart Enters | 4h	| Figured out how to connect to table and tested light pattern | LED Axis Tracking of the Ball | msoe-sisbot
2021-01-14 | Stuart Enters | 0.67h | Wrote documentation for testing patterns on the table via Postman & ssh | Group Meetings Time Log | msoe-sisbot
2021-01-18 | Stuart Enters | 1h	| Standup w/ team. Talked about end of sprint plans and created a few PBIs for next sprint | Group Meetings Time Log | msoe-sisbot
2021-01-18 | Stuart Enters | 4h	| Discussed finer details of goal with Grace due to a misunderstanding I had with. Worked on finding a new avenue of work that will still be useful | Spike: Mood Lighting & Alternative Algorithms | msoe-sisbot
2021-01-19 | Stuart Enters | 2h	| Worked on implementing new solution for spike | Spike: Mood Lighting & Alternative Algorithms | msoe-sisbot
2021-01-21 | Stuart Enters | 5h	| Implemented non ML classifier for music | Spike: Mood Lighting & Alternative Algorithms | msoe-sisbot
2021-01-21 | Stuart Enters | 3h	| Did sprint 5 planning with team, as well as Retro and status report |  Group Meetings Time Log | msoe-sisbot


## Fleming, Grace
* Hours: 
* Rating (0-10): 
* Summary:

| Date | User | Hours Spent | Description | Issue/MR | Repository |
|------|------|-------------|-------------|----------|------------|

## Wojciechowski, Andrew
* Hours: 
* Rating (0-10): 
* Summary:

| Date | User | Hours Spent | Description | Issue/MR | Repository |
|------|------|-------------|-------------|----------|------------|


# Discussion

## Key Meetings
* 1/15 - Grace & Joe met (separately) with Dr. Taylor to show him development process/techniques being used by the team. 
* 1/18 - Team stand up, and grooming of essential PBI's for the next sprint
* 1/21 - Sprint 4 termination activities, Sprint 5 opener activities, Sprint 4 Retro and weekly status meeting. Some Sprint Review preparation activities for tomorrow.

## Findings
* Siscloud is very broken when trying to access remotely
* SD cards are not robust :( (RIP Joe's SD card for his Pi)
* PyAudioAnalysis doesn't actually rely on PyAudio. The formal recommendation is using PyAudio library with PortAudio under the hood, and USB microphones if they can be acquired.
* Creating our owm ML algorithm from scratch seems difficult given the lack of available datasets and the time investment required to train and troubleshoot an algorithm. 

## Successes
* The removal of OpenCV from the current ML lights demo cut down CPU utilization by 40-50%
* Local audio streaming seems possible on a raspberry pi without serious performance degredations
* The team has learned a lot about this new feature, and had a change to explore multifarious different potential architecture directions.

## Risk Updates
* Developing involving the siscloud repo locally is more difficult to work with than we would have hoped.
* The plan for next quarter involves 3 very large PBI's, particularly an architecture PBI that will require cross-collaboration from the whole team.
* It's week 6 at MSOE during winter quarter, availability to work on PBI's (and as a result, team morale) is struggling

# Questions
* n/a

# Conclusion
The team is ready to jump into the next sprint. There is some general fatigue with the current setting (winter, MSOE week 6), but the team is optimistic that this challenge can be surmounted by interest in the project and the promise of a break 5 weeks away. The team is interested to see the reactions of our stakeholders when presented with our sprint 4 work tomorrow.
.