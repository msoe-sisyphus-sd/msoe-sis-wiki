# Sprint Goal
A user will be able to enable mood lighting and see its effects on the lab Sisyphus table.

# Burndown Chart

![image](uploads/640a95dca695ff249a19bd8fc20cb796/image.png)

# Team Commitment

## Burkhardt, Robert
* Hours: 4.5h
* Rating (0-10): 6 
* Summary:

|       Date | Hours Spend | Description                                                                                                                                                                                                                                                                                                                                                                  | Issue | Repository  |
|------------|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|-------------|
| 2021-02-25 | 1h          | Met with Bruce for sprint review                                                                                                                                                                                                                                                                                                                                             | #59   | msoe-sisbot |
| 2021-03-09 | 0.25h       | Weekly team stand up                                                                                                                                                                                                                                                                                                                                                         | #59   | msoe-sisbot |
| 2021-03-09 | 0.75h       | Met with team to further discuss architecture and refined our understanding of the architecture.  See wiki article https://gitlab.com/groups/msoe.edu/sdl/sd21/sisyphus/-/wikis/Architecture/First-Pass-Architecture-Draft for updated diagram.                                                                                                                              | #55   | msoe-sisbot |
| 2021-03-11 | 1h          | Met with team to write up status report and review Andy's MR                                                                                                                                                                                                                                                                                                                 | #59   | msoe-sisbot |
| 2021-03-11 | 1.5h        | Began map colors against songs playing to get a better idea of spread across songs and to verify that different colors are being produced for different audio emotions and valences. Additionally, located the part of sisbot that requires change for smoothing between two colors: https://gitlab.com/msoe.edu/sdl/sd21/sisyphus/msoe-sisbot/-/blob/master/sisbot.js#L1276 | #58   | msoe-sisbot |



## Casper, Joseph
* Hours: 4
* Rating (0-10): 2
* Summary: 

| Date | User |	Hours Spent | Description | Issue | Repository |
| ------ | ------ | ------ | ------ | ------ | ------ |
| 2021-02-25 | casperjm | 1h | Met with Bruce for sprint review | #59 | msoe-sisbot |
| 2021-03-08 | casperjm | 1h | Weekly team stand up | #59 | msoe-sisbot |
| 2021-03-11 | casperjm | 1h | Met with team for status report | #59 | msoe-sisbot |
| 2021-03-11 | casperjm | 1h | More UI debugging, researched Backbone to see if there was anything that we were missing, but couldn't tell if that was the issue or not | #59 | msoe-sisbot |


I didn't get much work done this week. I was spending a lot of time getting set up for my new classes for the quarter. Also, I had a second round of interviews with a company, and my current job interviewed me to hire me full time, so I've had to spend time preparing for those. I don't have any more job related things to do on my radar, so I should be able to get more senior design work done next week. 

In senior design this week, I spent a little time trying to get to the bottom of the checkbox ticket. I've figured more out about why it isn't being called, but have yet to figure out how it isn't being called. Starting next week, I'll start working on sisbot code instead of the UI code to get me more acquainted with the system. 


## Enters, Stuart
* Hours: 7
* Rating (0-10): 4
* Summary:
| Date | User | Hours Spent | Description | Issue/MR | Repository |
|--|--|--|--|--|--|
| 2021-02-12 | Stuart Enters | 2h | Team meeting & end of sprint work (Review, Plan, Status Report) | Group Meetings Time Log | msoe-sisbot |
| 2021-03-09 | Stuart Enters | 1h | Team sync meeting | Q3 Ceremonies | msoe-sisbot |
| 2021-03-11 | Stuart Enters | 1h | Status report with team | Q3 Ceremonies | msoe-sisbot |
| 2021-03-11 | Stuart Enters | 1h | Reviewed Andy's MR | Q3 Ceremonies | msoe-sisbot |
| 2021-03-11 | Stuart Enters | 2h | Worked on resolving UI bug where it doesn't call endpoint | Spike: Mood Lighting & Integration | msoe-sisbot |

As with most everyone else, I wasn't super productive this week. I did try to put some good time in today, and am hoping to get an effective headstart over the weekend to get back in the swing of things

## Fleming, Grace
* Hours: 9.75
* Rating (0-10): 8
* Summary: I didn't do as much actual implementation as I could have.

| Date       | User          | Hours Spent | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Issue/MR                                 | Repository  |
|------------|---------------|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------|-------------|
| 2021-02-15 | Grace Fleming | 1h          | Met with team to distribute work and figure out a timeline for finishing our large pile of paperwork.                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Q3 Ceremonies                            | msoe-sisbot |
| 2021-02-16 | Grace Fleming | 0.25h       | Followed up with Bruce on last missed sprint review                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Q3 Ceremonies                            | msoe-sisbot |
| 2021-02-16 | Grace Fleming | 1h          | Met and talked with Andy about where to put the sislisten repo in respect to the rest of the repositories. Determined it would be best to build a separate repository that would act as a server. Pros of this approach are separation of concerns & reduced risk since less development on Sisyphus' internal code needs to be done. Cons are that we will break the pattern of having sisbot be a single interface to the table. After discussion, created repository with minimal flask server. Finally, added minimal setup instructions. Repo exists here | Document Final Architecture              | msoe-sisbot |
| 2021-02-16 | Grace Fleming | 0.50h       | Documented (in wiki article) design decisions made by Andy and myself this morning. It is likely the rest of the team will contribute additionally. Wiki article is here                                                                                                                                                                                                                                                                                                                                                                                       | Document Final Architecture              | msoe-sisbot |
| 2021-02-17 | Grace Fleming | 2h          | Finished summarizing technical decisions in the technology report, wrote what felt like an exhaustive summary of the use of 3rd-party components in our codebase for the Team Components report, and threw a cherry on top by beginning the Threat Analysis under the "Security and Privacy" section of the report. Will need to finish Repudiation, Information Disclosure, Denial of Service and Elevation of Privilege later.                                                                                                                               | Document Final Architecture              | msoe-sisbot |
| 2021-03-09 | Grace Fleming | 1h          | Stand-up and making design decisions and participated in diagramming final results.                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Q3 Ceremonies                            | msoe-sisbot |
| 2021-03-10 | Grace Fleming | 1h          | Talked with Andy about how we want to implement this functionality and how it's going to fit into other parts of our design                                                                                                                                                                                                                                                                                                                                                                                                                                    | Handle Sisyphus Table Streaming Response | msoe-sisbot |
| 2021-03-11 | Grace Fleming | 2h          | Specked out code, but was unable to test because I couldn't connect to VPN using George's instructions. Since I have a different distro, I tried using the Ubuntu 20.04 recommended VPN instructions, but those haven't worked for me either yet :(                                                                                                                                                                                                                                                                                                            | Handle Sisyphus Table Streaming Response | msoe-sisbot |
| 2021-03-11 | Grace Fleming | 1h          | Status report and reviewed Andy's PR (#56)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Handle Sisyphus Table Streaming Response | msoe-sisbot |

## Wojciechowski, Andrew
* Hours: 7h
* Rating (0-10): 8
* Summary:

| Date | User | Hours Spent | Description | Issue/MR | Repository |
|------|------|-------------|-------------|----------|------------|
| 2021-02-16 | @wojciechowskia | 0.5h | Discussion with Grace about design decisions needed for our PBIs. We need to discuss these with the team. | #55 | msoe-sisbot |
| 2021-02-25 | @wojciechowskia | 1h | Sprint review meeting with Bruce | #59 | msoe-sisbot |
| 2021-03-08 | @wojciechowskia | 1h | Moved some code over to msoe-sislisten and shelled out that repository more. Implemented calling the ai service as a application/x-www-form-urlencoded request which I think will allow us to send both the stream along with custom options in the future. Need to talk with Grace about coordinating future work on the sislisten repo. | #56 | msoe-sisbot |
| 2021-03-09 | @wojciechowskia | 0.5h | Discussed potential designs for sislisten with Grace. Came up with a list of points to talk about with the team. | #55 | msoe-sisbot |
| 2021-03-09 | @wojciechowskia | 1h | Discussed designs for sislisten with the team and came up with an architecture diagram with the team. | #55 | msoe-sisbot |
| 2021-03-11 | @wojciechowskia | 2h | Finalized the code need to make a request to the AI Service by changing the type to be an octet-stream and added raising an error when a HTTP error is returned. I also moved the periodic tasks into their own module and tweaked a few command line arguments for the sislisten server. I also wrote an integration test verifying that we can make a request to the ai service via sislisten and verify that we get a valid response. Finally I setup GitLab CI for sislisten to run any automated tests on very commit. | #56 | msoe-sisbot |
| 2021-03-11 | @wojciechowskia | 1h | Reviewed and made changes to the MR made for the audio streaming request MR that I created and wrote the status report with the team. | #59 | msoe-sisbot |

# Discussion

## Key Meetings
* 2021/02/25 - Met with Bruce to show him our findings (no demo)
* 2021/03/09 - weekly sync meeting & some architecting (see new diagram at bottom of First Pass Arch. wiki page)
* 2021/03/11 - weekly status report meeting, reviewed a PR for issue #56

## Findings
* Gitlab still hasn't fixed the reverse burndown issue
* vpn setup in linux is hard :(

## Successes
* Did a lot of architecting for our Tuesday sync meeting relative to sislisten's role and composition
* Andy set up automated testing in the sislisten repository 
* We were able to close PBI #56 thanks to Andy's work

## Risk Updates
* Lights flicker on the production table, suggesting burned-out LED's
* Possible issues with Heroku's wake-up latency (think about moving to ROSIE? What about long-term solution?)

# Questions
* Senior design show - how's that going to work? In-person?
* Do we make a physical poster or a virtual one?
* We are planning to finish this current sprint at the end of week 3, making this sprint a 3-week sprint. Are we approved for two-week sprints after that with the caveat of cutting down on the paperwork in some fashion (up for discussion)?

# Conclusion
The team is relieved that this is going to be their last quarter of MSOE (dear 18-year-old-me picking a school: MSOE is good for the future bank account in like 30 years after loans are paid off, bad for the soul/mental health/sleep schedule/etc). Architecture planning has been fun and the team feels like it's given them a clear picture of what to implement; the team is excited to produce an MVP by the end of week 3.
