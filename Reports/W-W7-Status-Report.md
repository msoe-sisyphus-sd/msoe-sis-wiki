# Sprint Goal
Determine where the modified (volume-sensitive) algorithm for translating audio to color will run.

# Burndown Chart
![image](uploads/af23d354af494a860cdbea40fe1c0ed1/image.png)

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
* Hours: 
* Rating (0-10): 
* Summary:

| Date | User |	Hours Spent | Description | Issue | Repository |
| ------ | ------ | ------ | ------ | ------ | ------ |


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
* 2021-01-25 - Met with Bruce to go over sprint results, team also performed standup and assigned PBIs
* 2021-01-28 - Team met to write status report

## Findings
* `sisproxy` might be the best place to spawn the audio process, similar to how `sisbot` and `siscloud` are spawned
* Only some classifiers from `sklearn` can be ported to other libraries. SVMs (support vector machines) are one of those classifiers. However, further investigation is needed

## Successes
* @casperjm got the app running locally!

## Risk Updates
* This is no easy way to port underlying Python libraries to mobile - they all require complete rewrites

# Questions
* N/A

# Conclusion
The team is making headway into finding the best way to architect and process audio to deliver a great experience for the user.
