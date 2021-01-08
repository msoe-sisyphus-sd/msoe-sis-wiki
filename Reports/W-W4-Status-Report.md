# Sprint Goal

Original Goal: Investigate two new user-table domains to test feasibility and level of interactivity.

New Goal: Investigate mapping audio to colors and how to integrate a Python ML model with the existing code base.

# Burndown Chart

![image](uploads/d49d9bad9fef2ec3e917db958913b1ac/image.png)

# Team Commitment

## Burkhardt, Robert
* Hours: 9 (including time over breaks)
* Rating (0-10): 6.87
* Summary:

| Date | Hours Spent | Description | Issue / MR | Repository |
| --- | --- | --- | --- | --- |
| 2020-12-18 | 1h30m | Sprint review with Sisyphus Industries | #7 | msoe-sisbot |
| 2020-12-21 | 1h15m | Met with team to discuss sprint review and chose project direction | #7 | msoe-sisbot |
| 2020-12-28 | 1h | Spent time with team grooming backlog issues for new project direction (Audio and Lights with AI) | #7 | msoe-sisbot |
| 2021-01-04 | 1h | Weekly meeting to confirm and assign PBIs as well as plan out Technology report | #7 | msoe-sisbot |
| 2021-01-06 | 1h | Spent some time looking at different Python Audio Libraries and seeing if they could interface with a USB microphone pretty easily (specifically PyAudio and Sound Device). Future work is seeing if PortAudio is required or if there's a way to do it without an intermediate library | #44 | msoe-sisbot |
| 2021-01-07 | 2h | Spent time re-configuring local setup because I had made some changes to the ALSA and other interfaces that needed to be corrected for future use - my USB sound card was no longer recognized. I was able to get the Pi back to a state of operation so I can build out mini projects with different audio libraries to select the best one. | #44 | msoe-sisbot |
| 2021-01-07 | 1h15m | Meeting with the team. Did a standup, worked on the status report, and discussed our high level outline we put together for the tech report sections | #44 | msoe-sisbot |

## Casper, Joseph
* Hours: 8.5
* Rating (0-10): 6
* Summary:

| Date | User |	Hours Spent | Description | Issue | Repository |
| ------ | ------ | ------ | ------ | ------ | ------ |
| 2020-12-18 | casperjm | 1.5h | Product owner meeting | #7 | msoe-sisbot |
| 2020-12-21 | casperjm | 1.25h | Meeting with team to talk about product's direction | #7 | msoe-sisbot |
| 2020-12-28 | casperjm | 1h | Meeting with team to groom backlog with new direction in mind | #7 | msoe-sisbot |
| 2021-01-04 | casperjm | 1h | Meeting with team to groom backlog with new direction in mind | #7 | msoe-sisbot |
| 2021-01-07 | casperjm | 1.25h | Meeting with team to write status report and review technology report draft | #7 | msoe-sisbot |
| 2021-01-07 | casperjm | 2.5h | Fixed the rest of the eslint errors | #34 | msoe-siscloud |

We met as a team over break to decide a direction for the product, and wrote new PBIs to reflect our new goal. I worked on fixing the rest of the ~1000 eslint errors in the siscloud repo, which was pulled in from last sprint.

## Enters, Stuart
* Hours: X
* Rating (0-10): X
* Summary:

Insert Summary Here

## Fleming, Grace
* Hours: 8
* Rating (0-10): 8
* Summary:

|Date	| User|	Hours Spent|	Description|	Issue/MR|	Repository|
|--|--|--|--|--|--|
|2020-12-18 | Grace Fleming | 1.67h	| Retro, sprint finalization, status report. |	Group Meetings Time Log	| msoe-sisbot |
|2020-12-21 | Grace Fleming | 1.25h | Team discussion for a longterm project. Vote was to work on audio to color project |Group Meetings Time Log| msoe-sisbot |
|2020-12-28 | Grace Fleming | 1h | Met with the team to do backlog grooming, primarily pointing stuff we're pulling into our current sprint. | Group Meetings Time Log | msoe-sisbot |
|2021-01-04 | Grace Fleming | 1h | Tried to run the app from a regular development machine with a GUI. It did not go well (see error above). | Spike: Mood Lighting & Integration | msoe-sisbot|
|2021-01-05 | Grace Fleming | 2h | Worked on researching algorithms for converting sound to color. I think this in and of itself is going to be really hard, so I think our best bet is to get out the two key features that make audio mood easiest to classify--valence and arousal (unfortunate naming, I know) and then map those to a color grid, much like the original algorithm from the spike did. I spent most of my time investigating different algorithms to yield valence and arousal. The google doc for these research resources is here. | Spike: Mood Lighting & Alternative Algorithms | msoe-sisbot |
|2021-01-07 | Grace Fleming | 1h | Concluded there are no out-of-box algorithms for this except the one that's been created. the PyAudioAnalysis library that is popular for analysing songs is actually written by the same author as the color_your_music_mood repository I created the frankenstien demo off of. That said, I'm not sure if we should explore training our own algorithm using the pyAudioAnalysis library? | Spike: Mood Lighting & Alternative Algorithms | msoe-sisbot |

Insert Summary Here

## Wojciechowski, Andrew
* Hours: 8.33
* Rating (0-10): 6
* Summary:

| Date | User | Hours Spent | Description | Issue/MR | Repository |
|------|------|-------------|-------------|----------|------------|
| 2020-12-18 | @wojciechowskia | 0.5h | Setup the Coffee table for light pattern demos and ran the magnetic light pattern before sprint review | #7 | msoe-sisbot |
| 2020-12-18 | @wojciechowskia | 1.5h | Meeting with Dr. Taylor, Bruce and Matt to demo things that we worked on and to discuss a longer term product to work on. | #7 | msoe-sisbot |
| 2020-12-21 | @wojciechowskia | 1.25h | Team discussion to discuss a larger project to work on. Team consensus was to work on the audio to color project | #7 | msoe-sisbot |
| 2020-12-28 | @wojciechowskia | 1h | Backlog grooming with the team to split up initial PBIs for the audio to color project. | #7 | msoe-sisbot |
| 2021-01-04 | @wojciechowskia | 0.83h | Met with the team to assign issues and discussed plans for writing the tech report | #7 | msoe-sisbot |
| 2021-01-05 | @wojciechowskia | 1h | Got the machine learning spike running on my Windows machine and discovered that the CPU utilization was around 25% running without the lights. I'm planning on comparing that using my PI and the lights and those next | #40 | msoe-sisbot |
| 2021-01-07 | @wojciechowskia | 0.5m | Planned out potential functional requirements for the tech report. These will be reviewed with the team later and then we'll decide on if those requirements should be refined further for the tech report or not | #7 | msoe-sisbot |
| 2021-01-07 | @wojciechowskia | 1.25h | Meeting with the team. Did a standup, worked on the status report, and discussed our high level outline we put together for the tech report sections | #7 | msoe-sisbot |

# Discussion

## Key Meetings (including those over Winter Break)
* 2020-12-18: Met with Sisyphus Industries for Sprint Review
* 2020-12-21: Team met to discuss Sprint Review and decide project direction
    * Team voted and decided to proceed with adding audio input and changing the light strip with an ML model
* 2020-12-28: Team met to draft, groom, and plan new PBIs for the new project direction
* 2020-12-29: DnD like the nerds we are :) 
* 2021-01-04: Weekly team meeting and assigning PBIs and Tech Report section drafts
* 2021-01-07: Weekly team meeting for status report and Tech Report review

## Findings
* Andy discovered that running the ML audio-light algorithm uses about 25% of the CPU (school laptop)
* Grace discovered that the ML model used in the demo relies on lyrics to detect valence
    * Believes that this was the cause of only one color being displayed during the sprint review demo

## Successes
* Team bonding
* No one got COVID over break!
* Selected a _specific_ and _actionable_ project direction!
    * We also have a laundry list of stuff to do afterwards if we type really fast!

## Risk Updates
* Project now has a reliance on ML which may be an issue if the team can't get stuff to work properly

# Questions
* Have you every played DnD?
* Are SEs just glorified typists and why is the answer 'yes'?
* Is SO2-1 actually due next week? The assignment says that it should be done during the end of the term?
* Look over our technology report pls :heart:?
    * https://docs.google.com/document/d/1kuHhPWsSv28gUTFtm2EnT9rB7Oo-t00RNutWWlnPPY8/edit?usp=sharing

# Conclusion

The team has chosen a project direction and is ready to get to work!