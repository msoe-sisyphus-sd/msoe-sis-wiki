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
* Hours: 7
* Rating (0-10): 5
* Summary:

| Date | User |	Hours Spent | Description | Issue | Repository |
| ------ | ------ | ------ | ------ | ------ | ------ |
| 2021-01-22 | casperjm | 1h | Met with Dr. Taylor for sprint review  | #7 | msoe-sisbot |
| 2021-01-25 | casperjm | 1.5h | Helped Andy try to get the demo working; met with Bruce  | #7 | msoe-sisbot |
| 2021-01-26 | casperjm | 3h | Had to fix my Pi again, then I worked and got the app running locally. I played around with it to try to push some changes, but now I have to figure out how to build the code. | #41 | msoe-sisbot |
| 2021-01-26 | casperjm | 1h | Tried to verify that the eslint fixes work, but the changes on the siscloud repo broke the app. I have to go through and figure out what broke. | #34 | msoe-sisbot |
| 2021-01-28 | casperjm | .5h | Weekly status report meeting  | #7 | msoe-sisbot |

Today I finally got the app running locally. My Pi broke (again) somehow, so I had to re set up raspbian and all of the sisbot code. I spent some time playing with the code and trying to make changes. I'll have to figure out how to build the app to make those changes appear. I also tried to verify that my eslint fixes worked, but it ended up breaking the app, which I'll investigate next week. 


## Enters, Stuart
* Hours: 
* Rating (0-10): 
* Summary:

| Date | User |	Hours Spent | Description | Issue | Repository |
| ------ | ------ | ------ | ------ | ------ | ------ |


## Fleming, Grace
* Hours: 9
* Rating (0-10): 5
* Summary: Didn't work as much on my PBI this week as I wanted to. I blame the extreme cold and week 7 for the lack of motivation.

|Date	|User	|Hours Spent	|Description	|Issue/MR	|Repository|
|-------|-------|--------------|--------------|---------------|--------|
|2021-01-22|Grace Fleming | 2.67h Sprint termination, sprint startup, retro, planning for sprint review tomorrow, status report |	Group Meetings Time Log | msoe-sisbot |
|2021-01-22|Grace Fleming|0.25h | moved findings to wiki | Spike: Mood Lighting & Alternative Algorithms	 |msoe-sisbot|
|2021-01-25 | Grace Fleming  | 1h | Sprint review part 2 with bruce/assigned issues with team | Group Meetings Time Log |msoe-sisbot |
|2021-01-25|Grace Fleming |0.50h | Helped out with trying to help Andy run his demo | Group Meetings Time Log |msoe-sisbot |
|2021-01-25|Grace Fleming |1h	|Checked out using bee ware to run python on a phone. Got an emulator and virtual environment put together to run through their tutorial, and successfully deployed a python app :) Unfortunately, I then tried to integrate sklearn and ran into https://github.com/beeware/briefcase/issues/471. Beeware is not going to "bee" an option. |Spike: Mood lighting & Mobile as a Artificial Intelligence Computation Platform |msoe-sisbot |
|2021-01-26 |Grace Fleming  | 0.50h | Following up with Bruce from meeting last night with articles he requested (some research required because I forgot to save the articles I read about emotion/color/audio, so had to go chase them down again).
| Group Meetings Time Log | msoe-sisbot | 
|2021-01-26 | Grace Fleming | 0.50h  | Troubleshooting pyaudio on my machine (with Stuart) |Group Meetings Time Log | msoe-sisbot |
|2021-01-26 |Grace Fleming  | 1h | Researched some more ideas about how to port ML code -> phone. So far, I have a few ideas. 1) try and use the sklearn C binaries to write an app in C for android, since android is linux we can run C on it natively. No clue about how this would work for iOS. 2) look at using a porter to port the sklearn model to java for running on android. Still not sure about iOS. 3) use an iOS machine learning framework to rewrite the algorithm for mobile. 4) Instead of trying to do machine learning with our model that's been trained to generate moods, we simply pull out audio features on the phone, and then ship those features off to a server (instead of sending whole audio). Will rendezvous with Andy about these ideas. |	Spike: Mood lighting & Mobile as a Artificial Intelligence Computation Platform | msoe-sisbot |
|2021-01-28 | Grace Fleming | 1h | Researched more into the porting of sklearn into C. Explored https://github.com/nok/sklearn-porter. Finally, emailed the professor in charge of the machine learning algorithm we are currently using requesting the dataset he used to train his algorithm and thanking him fro his work. | Spike: Mood lighting & Mobile as a Artificial Intelligence Computation Platform | msoe-sisbot |
|2021-01-28 | Grace Fleming | 1h | Worked on knowledge acquisition stuff. In my case, watched more Ben Eater videos on digital electronics and took notes. | Group Meetings Time Log | msoe-sisbot |
|2021-01-28 | Grace Fleming | 30m | Team standup & status report | Group Meetings Time Log | msoe-sisbot| 


## Wojciechowski, Andrew
* Hours: 4.75
* Rating (0-10): 5
* Summary:

| Date | User | Hours Spent | Description | Issue/MR | Repository |
|------|------|-------------|-------------|----------|------------|
| 2021-01-25 | @wojciechowskia | 2h | Spent a while trying to get the demo running on my MSOE laptop. Eventually was able to get it running by switching to my personal desktop and I tested it with the team before meeting with Bruce. | #7 | msoe-sisbot |
| 2021-01-19 | @wojciechowskia | 1h | Meeting with Bruce. Afterwards standup with the team and assigning PBIS | #7 | msoe-sisbot |
| 2021-01-19 | @wojciechowskia | 0.25h | Installed Android Studio for testing out this ML on Android | #45 | msoe-sisbot |
| 2021-01-21 | @wojciechowskia | 1h | Looked briefly into seeing what it would take to run the current ML demo on a Android app written in Java as well as how to listen to audio with Android. I think having the ML all in Java will take a lot of work. There's a porter out there to convert sk-learn code to Java but a lot of the pyAudioAnalysis library would have to be rewritten in Python in order for that to work. | #45 | msoe-sisbot |
| 2021-01-21 | @wojciechowskia | 0.5h | Standup with the team and meeting to write status report.  | #7 | msoe-sisbot |


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
