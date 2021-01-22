r# Sprint Goal
Investigate mapping audio to colors and how to integrate a Python ML model with the existing code base.

# Burndown Chart
![image](uploads/a0f70325bc186effbe13cfb963b8f099/image.png)

*Note: this is incorrect, we did not complete 1 issue worth 5 points. Gitlab just wants us to look good* :shrug: 

# Team Commitment

## Burkhardt, Robert
* Hours: 9h
* Rating (0-10): 7.28
* Summary:

| Date | Hours Spent | Description | Issue / MR | Repository | 
| --- | --- | --- | --- | --- |
| 2021-01-18 | 1h | Stand up and grooming with team | #7 | msoe-sisbot |
| 2021-01-19 | 3h | Evaluated pyAudio, sounddevice, and pyalsaaudio on DX and abilities. I also discovered that pyAudio is only tied to pyAudioAnalysis in name only - there is no formal dependency which means any sound library could be used. | #44 | msoe-sisbot | 
| 2021-01-20 | 1h | Spent a bit of time understanding what PulseAudio and it's associated Python wrappers are. In short, it's a sound server with a wide breadth of capabilities but it seem a bit overkill for what we're trying to achieve and considering the ML model will probably be taking up a majority of CPU resources - best to keep the foot print of the audio stream as small as possible. | #44 | msoe-sisbot | 
| 2021-01-21 | 1h | Recorded results and evaluation in the wiki article https://gitlab.com/msoe.edu/sdl/sd21/sisyphus/msoe-sisbot/-/wikis/Spikes:-Audio-Interfaces in choosing the best hardware and software solutions - this should help justifying our decision in our tech report | msoe-sisbot |
| 2021-01-21 | ~3h | Sprint Planning, Retro, Sprint 4 Update, Status Report etc. | #7 | msoe-sisbot |

## Casper, Joseph
* Hours: 11.25
* Rating (0-10): 3
* Summary:


| Date | User |	Hours Spent | Description | Issue | Repository |
| ------ | ------ | ------ | ------ | ------ | ------ |
| 2021-01-15 | casperjm | .25h | Met with Dr. Taylor to show off some of the code in the repo  | #7 | msoe-sisbot |
| 2021-01-18 | casperjm | 1h | Monday stand up and backlog grooming  | #7 | msoe-sisbot |
| 2021-01-18 | casperjm | 2h | Spent time trying to connect to my Pi (only to find out that the SD card was dead later) | #41 | msoe-sisbot |
| 2021-01-19 | casperjm | 1h | Met with Grace, she figured out that the SD card was dead. I started setting up my new card.  | #41 | msoe-sisbot |
| 2021-01-20 | casperjm | 4h | Set up my Pi and the sisyphus repos. Spent a lot of time trying to get the siscloud server to run, only to be blocked by many errors. | #41 | msoe-sisbot |
| 2021-01-21 | casperjm | 3h | Sprint wrap up meeting  | #7 | msoe-sisbot |

This week I spent all of my time debugging issues with my Pi. I played around with it for a while by myself to try to figure out why it wasn't running, and Grace helped me out and told me that the SD card was dead (which is odd, since I haven't touched the Pi in about a month and it was working fine). I got my new card set up with Raspbian and all of the sisyphus code. Before I could finish the ticket that I had, I ran into more issues trying to run the app on the Pi. I reached out to the team during stand up Thursday, and George gave me a potential fix. 




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
* Hours: 11.58
* Rating (0-10): 9
* Summary:
Lots of effort this week in prep for sprint review. I thought that was ok, but feel like I should have more concrete deliverables :thinking:

| Date | User | Hours Spent | Description | Issue/MR | Repository |
|------|------|-------------|-------------|----------|------------|
|2021-01-15| Grace Fleming | 1h	| Met with team to do status report | Group Meetings Time Log| msoe-sisbot |
|2021-01-15 | Grace Fleming |0.33h | Met with Dr. Taylor for weekly meeting | Group Meetings Time Log | msoe-sisbot |
| 2021-01-17 | Grace Fleming | 0.25h| Cleaned & pushed demo code to a repository so it's ready for our sprint review.|	Spike: Mood Lighting & Alternative Algorithms| msoe-sisbot |
|2021-01-18 | Grace Fleming |	1h	|  Stand up and grooming with the team. Discussed the goals and outcomes from this sprint, and tried to plan for the next one, despite that being sort of difficult without a firm architecture.| Group Meetings Time Log | msoe-sisbot |
|2021-01-18| Grace Fleming |0.75h | Started writing a home-baked solution based on some guy's dataset that he was kind enough to post on github. I got this from a post some guy wrote about using tensorflow and a bunch of fancy machine learning techniques to predict labels. Reading through the guy's approach is quite complicated, so I'm going to try and simplify it a bit (also I have doubts about my pathetic MSOE laptop cannot train a neural network without choking).| 	Spike: Mood Lighting & Alternative Algorithms | msoe-sisbot |
|2021-01-18 | Grace Fleming | 1.25h | Worked on slides for sprint review, and worked on a decision matrix for ML vs non-ML approaches. Will eventually need Stuart's input as expected. | Spike: Mood Lighting & Alternative Algorithms | msoe-sisbot |
|2021-01-19 | Grace Fleming|0.50h| Helped Joe with some raspberry pi troubleshooting |	Spike: Mood Lighting & Integration | msoe-sisbot |
|2021-01-19 | Grace Fleming | 2.50h | Worked some more on my home-grown solution to predict valence based off of ML characteristics. I used feature vectors of energy and tempo, and attempted to use these with a SGDRegressor and a SVR (Support Vector Regression, trying with rbf, sigmoid and poly kernels). So far I haven't been able to produce anything accurate...in fact, most of my accuracy has been below 50% :cry: | Spike: Mood Lighting & Alternative Algorithms | msoe-sisbot |
|2021-01-19 | Grace Fleming |1h	 | Talked through goals in sprint with Stuart, as there was confusion. | Spike: Mood Lighting & Alternative Algorithms | msoe-sisbot |
| 2021-01-20 | Grace Fleming |1.50h | Worked some more on crafting a home-grown machine learning algorithm. It was pretty rough. The dataset I identified turned out to not be very helpful. Being from the Spotify data warehouses, most of the features included in the music samples won't be things we can easily pull from listening to raw audio. Doing a PCA analysis to find correlation between tempo, energy and mood lead to some very disappointing graphs, which I'll post here for longevity in another comment. Furthermore, multiple papers provide evidence that somewhere in the vein of 20-30 features are needed to accurate predict valence or emotion. So I don't think I'm going to be able to find a sufficient dataset to use to train my algorithm, at least not one publicly available. Certainly not me and my two sad features pulled from the Spotify dataset. | Spike: Mood Lighting & Alternative Algorithms | msoe-sisbot |
| 2021-01-21 | Grace Fleming | 1.50h | Trying to get web server working on port 3001, being passed thru the NAT proxy. Having issues with the cordova.js script loading. | Group Meetings Time Log | msoe-sisbot |
## Wojciechowski, Andrew
* Hours: 10.5h
* Rating (0-10): 8
* Summary:

| Date | User | Hours Spent | Description | Issue/MR | Repository |
|------|------|-------------|-------------|----------|------------|
| 2021-01-18 | @wojciechowskia | 1h | Stand up with the team. Discussed end of sprint items with the team and started planning out PBIs for next sprint. | #7 | msoe-sisbot |
| 2021-01-19 | @wojciechowskia | 3.5h | Explored the performance implications of listening to audio input. Put together a demo to continuously stream data from a Raspberry PI to a server with sockets. PyAudio did not run into any performance issues on the Raspberry PI when listening to input and I was able to eventually add the ML with the server. I also stripped OpenCV out of the current ML algorithm which seemed to help performance especially when running on the PI. | #40 | msoe-sisbot |
| 2021-01-19 | @wojciechowskia | 0.25h | Wrote up remaining performance investigation results on the wiki. | #40 | msoe-sisbot |
| 2021-01-21 | @wojciechowskia | 2h | Investigated issues with the siscloud web server not working on port 3001 on seniordesigntable.msoe.edu. Found an issue where the request to /sisbout/connect was timing out. Found that the request was missing the port. Once that was fixed that revealed another issue where requests were using local IPs instead of the seniordesigntable.msoe.edu address. We plan to write up a PBI to investigate this issue. | #7 | msoe-sisbot |
| 2021-01-21 | @wojciechowskia | 3.75h | Meeting with the team to do sprint planning, retrospective, status report, and discussed sprint review tomorrow.  | #7 | msoe-sisbot |


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