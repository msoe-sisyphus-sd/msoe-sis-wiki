# Sprint Goal

Original Goal: Investigate two new user-table domains to test feasibility and level of interactivity.

New Goal: Investigate mapping audio to colors and how to integrate a Python ML model with the existing code base.

# Burndown Chart

![image](uploads/d49d9bad9fef2ec3e917db958913b1ac/image.png)

# Team Commitment

## Burkhardt, Robert
* Hours: X (including time over breaks)
* Rating (0-10): 6.87
* Summary:

| header | header |
| ------ | ------ |
| cell | cell |
| cell | cell |

## Casper, Joseph
* Hours: X
* Rating (0-10): X
* Summary:

Insert Summary Here

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
* Hours: X
* Rating (0-10): X
* Summary:

Insert Summary Here

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

# Conclusion

The team has chosen a project direction and is ready to get to work!