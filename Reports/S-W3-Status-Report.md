# Sprint Goal

A user will be able to enable mood lighting and see its effects on the lab Sisyphus table.

# Burndown Chart

![MicrosoftTeams-image](uploads/497b736d7fb8b99af9322aff537d7a7b/MicrosoftTeams-image.png)

# Team Commitment

## Burkhardt, Robert
* Hours: 11
* Rating (0-10): 8
* Summary:

|       Date | Hours Spent | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Issue |
| --- | --- | --- |---|
| 2021-03-19 | 0.5h        | Met with Dr. Taylor and was serenaded                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | #59   |
| 2021-03-22 | 1.0h        | Weekly stanup meeting with team and learning a bit about how to work in siscloud (Backbone models)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | #59   |
| 2021-03-25 | 2.5h        | Standup, merge party, sprint plan updates, sprint planning, review, and final status report (woot woot)!                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | #59   |
| 2021-03-22 | 3.0h        | Finished recording audio and added smoothing transition to the ML output. Essentially there are two variables that are being used to force smoother colors. The first is making the color map less gradient. This is achieved through changing a hyper-parameter step which is currently used to generate the gradient size on the color map. The second variable is to make the output coordinates (valence and energy) "sticky". A sticky variable is one that does not change unless it meets a certain threshold of difference against its previous value (in the case of testing I used 10%, but this should be adjustable by the user and thus be a another setting. | #58   |
| 2021-03-24 | 3.0h        | Spent some time drafting a better visualization of the previous and post colors. Honestly it doesn't look amazing as different songs keep mapping to the same general color (of blueish gray) but this might be an issue of bias in the sample data. However, it is possible to see that there is more "blocking"/grouping of colors due to the smoothing functions. Maybe in future sprints we can tune these parameters but I think they would be better served as user settings (which is a tentative goal of next sprint).                                                                                                                                             | #58   |
| 2021-03-25 | 1.0h        | Spent time with @casperjm21 testing the smoothing functionality on the table.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | #58   |



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
* Hours: 8
* Rating (0-10): 6 
* Summary:

| Date | User |	Hours Spent | Description | Issue | Repository |
| ------ | ------ | ------ | ------ | ------ | ------ |
| 2021-03-19 | enterss | 1h | Weekly meeting with Dr. Taylor | #59 | msoe-sisbot |
| 2021-03-25 | enterss | 4h | Worked on getting the spawning endpoint set up for siscloud to call | #61 | msoe-sisbot |
| 2021-03-25 | enterss | 3h | End of sprint meeting with team| #59 | msoe-sisbot |

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
* Hours: 7.58
* Rating (0-10): 8
* Summary:

| Date | User | Hours Spent | Description | Issue/MR | Repository |
|------|------|-------------|-------------|----------|------------|
| 2021-03-22 | @wojciechowskia | 1h | Made changes that Matt suggested in an email and they did not work. Verified that some event handlers could be hit with breakpoints and the toggle_mood_lighting function could not be hit with a breakpoint and I responded to Matt. | #59 | msoe-sisbot |
| 2021-03-23 | @wojciechowskia | 1.25h | Hopped on a call with Matt to fix the mood lighting checkbox issue. Ended up merging with upstream and fixing the location of where the checkbox should be where the current model matches the sisbot model | #41 | msoe-sisbot |
| 2021-03-23 | @wojciechowskia | 0.5h | Standup, I explained siscloud to the team and discussed planning for next sprint | #59 | msoe-sisbot |
| 2021-03-24 | @wojciechowskia | 0.33h | Hooked up calling sislisten from siscloud | #61 | msoe-sisbot |
| 2021-03-24 | @wojciechowskia | 1h | Looked at issues we were seeing with the thread pools. It seemed to be working better if we didn't raise an error and I changed it to just print out an error to the console. It also seems like there's a potential issue either in sislisten or the AI Service that prevents struct.unpack from working. | #61 | msoe-sisbot |
| 2021-03-25 | @wojciechowskia | 0.25h | Shelled out the sprint 7 plan | #59 | msoe-sisbot |
| 2021-03-25 | @wojciechowskia | 3.25h | Standup, reviewing MRs, sprint planning, retro, writing status report and planning out demo with the team | #59 | msoe-sisbot |

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