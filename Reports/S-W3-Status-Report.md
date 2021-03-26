# Sprint Goal

A user will be able to enable mood lighting and see its effects on the lab Sisyphus table.

# Burndown Chart

![MicrosoftTeams-image](uploads/497b736d7fb8b99af9322aff537d7a7b/MicrosoftTeams-image.png)

# Team Commitment

## Burkhardt, Robert
* Hours: 
* Rating (0-10): 
* Summary:


## Casper, Joseph

* Hours: 9
* Rating (0-10): 8.5
* Summary:

| Date | User |	Hours Spent | Description | Issue | Repository |
| ------ | ------ | ------ | ------ | ------ | ------ |
| 2021-03-19 | casperjm | 1h | Weekly meeting with Dr. Taylor | #59 | msoe-sisbot |
| 2021-03-24 | casperjm | 4h | Made good progress on smoothing light colors, met with George the following day to finalize it | #58 | msoe-sisbot |
| 2021-03-25 | casperjm | 2h | Met with George to finish up the smoothing light PBI | #58 | msoe-sisbot |
| 2021-03-25 | casperjm | 2.5h | Met with team to write sprint documents and have a merge party | #59 | msoe-sisbot |

This week I finished up the smoothing PBI, with some help with George. Nothing else besides that

## Enters, Stuart
* Hours: 
* Rating (0-10): 
* Summary:


## Fleming, Grace
* Hours: 8.0
* Rating (0-10): 7
* Summary: 

| Date       | User          | Hours Spent | Description                                                                                                                                                                                                                                                                                                                                                                                                                                               | Issue/MR                                    | Repository  |
|------------|---------------|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------|-------------|
| 2021-03-19 | Grace Fleming | 0.5h        | Taylor meeting                                                                                                                                                                                                                                                                                                                                                                                                                                            | Q3 Ceremonies                               | msoe-sisbot |
| 2021-03-23 | Grace Fleming | 2h          | Read up on thread pool patttern, how to create periodic tasks in python, etc. Begin implementation. Required to learn about args* and kwargs** in order to do the previous. Still in syntax error land, but making progress (probably). Will phone for help soon if cannot get past them.                                                                                                                                                                 | Add Audio Light Settings Controls to Sisbot | msoe-sisbot |
| 2021-03-24 | Grace Fleming | 1.50h       | Attempted to implement Thread Pool Executor pattern. I don't think this worked yet, but I was able to at least kick off a periodic task using a singleton (this should prevent us getting DOS-ed). This task can successfully call the AI service and start translating it, although it can't parse the response yet (since the AI service is still sending back colors). It also isn't kicking the task off on a separate thread, which is concerning :\ | Add Audio Light Settings Controls to Sisbot | msoe-sisbot |
| 2021-03-24 | Grace Fleming | 0.50h       | Standup, Andy explained siscloud, & sprint planning discussion                                                                                                                                                                                                                                                                                                                                                                                            | Q3 Ceremonies                               | msoe-sisbot |
| 2021-03-25 | Grace Fleming | 2.5h        | Standup, merge party, sprint plan update, sprint plan planning, some story pointing, crying because tired, retro review, status report.                                                                                                                                                                                                                                                                                                                   | Q3 Ceremonies                               | msoe-sisbot |
| 2021-03-25 | Grace Fleming | 1h          | Sislisten final touches (cut out translator for now)                                                                                                                                                                                                                                                                                                                                                                                                      | Add Audio Light Settings Controls to Sisbot | msoe-sisbot |

## Wojciechowski, Andrew
* Hours: 
* Rating (0-10): 
* Summary:

# Discussion

## Key Meetings
* 3/19 Meeting with Dr. Taylor
* 3/22 Standup and initial sprint planning discussions
* 3/23 Andy's meeting with Matt to discuss Siscloud
* 3/25 Standup, reviewing MR's, retro, and writing status report

## Findings
* Siscloud is built using a hierarchy of model objects

## Successes
* We finally got the mood lighting checkbox working in siscloud
* We finished every one of our planned PBIs this sprint
* We also have a new LED strip on order
* We've been able to deploy code to Dr. Taylor's table

## Risk Updates
* We've noticed that the AI service has been returning a lot of 500 errors along with some responses that successfully return a color
* Our next sprint will be our first 2 week sprint

# Questions

* For the OWASP analysis do you want an explanation or just a category for each item?

# Conclusion
The team feels that this sprint was very successful and is excited to continue making good progress on the project.