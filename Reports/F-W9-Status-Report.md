# Sprint Goal

Continue exploring different light patterns and being investigating additional inputs to affect lighting schemes.

# Burndown Chart

![image](uploads/9ae33e1b3faf1b74b8fae7da4b7e5182/image.png)

# Team Commitment

## Burkhardt, Robert
###### Hours: X
###### Rating (0-10): X
###### Summary:

Insert Summary Here

## Casper, Joseph
###### Hours: 11.75
###### Rating (0-10): 7
###### Summary:

| Date | User | Hours Spent | Description | Issue/MR | Repository |
|------|------|-------------|-------------|----------|------------|
| 2020-11-02 | casperjm21 | 45m | Met with team for stand up, presentation planning and planning for the week | #7 | msoe-sisbot |
| 2020-11-04 | casperjm21 | 5h | Finished setting up lights locally | #25 | msoe-sisbot | 
| 2020-11-04 | casperjm21 | 1h 30m | Backlog grooming with team | #7 | msoe-sisbot | 
| 2020-11-05 | casperjm21 | 1h 30m | Tried out different holiday APIs to see if any are usuable | #13| msoe-sisbot | 
| 2020-11-05 | casperjm21 | 3h | Status report meeting with team | #7 | msoe-sisbot | 

Finally got my lights set up on my home pi, and worked on the holiday lights pattern. Setting up the lights took much, much longer than I was expecting so I wasn't able to complete the holiday lights. I've made good progress on it so far, though. I have the implementations of light patterns on holidays but I need to find an API that will give me the dates of holidays that occur on different dates every year, like Easter and Thanksgiving.

## Enters, Stuart
###### Hours: 9.5
###### Rating (0-10): 3
###### Summary:

So... where to begin. I technically did some work for this week - I got CI working again and got one task done for the light pattern I'm developing - but I had a unprecedented series of setbacks that inhibited any more work. I have had a number of anxiety attacks this week, a massive workload for other classes, a medical emergency to deal with, unfortunate events in my personal life, and spent the majority of today getting tested for Covid and then going into quarantine. Needless to say, this isn't a reflection of my best work. Doubly unfortunately: with the projected workload for next week, I don't really see this improving. Obviously I will try to improve, but I do not know if I will have the ability to represent myself well for this project.

## Fleming, Grace
###### Hours: 13
###### Rating (0-10): 8
###### Summary:
| Date         |      User    | Hours Spent | Description | Issue/MR | Repository |
|--------------|--------------|-------------|-------------|----------|------------|
| 2020-10-30   | Grace Fleming| 2h          | Worked on determining why the android app isn't able to listen for notifications. Realized a few things I messed up with the service declaration. Also realized I needed to ask permissions for notification detection before I could use it. After implementing the permissions work, making sure that the notificaiton service is enabled before starting the app and then adding code t serve as the actual notificaiton listener, I was able to finally get the app to respond to a notification by printing a string. After that I researched how to make an easy web request. I started out trying to make a vanilla java request, but this didn't compile correctly. After that I turned to google and found the loopj library which is evidently quite standard. HOPEFULLY using it is simple, but Android studio wouldn't import the com.loopj.android.http package until I added the package as a dependency in my build.gradle file.| #20 | msoe-sisbot |
| 2020-10-31   | Grace Fleming| 2.5h        | After dealing with Gradle build issues for about half an hour (finally fixed by restarting Android Studio) I got my app to intercept a notification and make a POST to the table to get the current status, and it was able to extract the existing LED pattern, although I was blocked for awhile by not having android permissions to use the internet, and then blocked again when I tried to use a SyncHttpClient (apparently for handling the response, you need an AsyncHttpClient). This will be important since the steps for showing a notification are going to look something like: 1) get current status 2) pulse different pattern 3) set pattern back to status found in (1). Next time I plan to add functionality to change the pattern. | #20 | msoe-sisbot |
| 2020-11-04   | Grace Fleming| 4.h         | Added API calls to the app to take the saved pattern from the table, change the primary color to a set value, change the pattern, and then change the pattern back to original. Ran into issues with the NotificationWatcher from Android (reports 2 notify calls for a single push notification). Issue is known on many platforms. Created a (temporary) workaround. Realistically, workaround will need more attention if this is to go into production. Finally, dealt with some synchronicity issues. Fixed by chaining asynchronous callbacks. | #20 | msoe-sisbot |
| 2020-11-04   | Grace Fleming| 1.5h        | Groomed PBI's with the team :) | #7 | msoe-sisbot |
| 2020-11-05 | Grace Fleming |3h | Merge party, review, presentation drafting, new sprint plan, and status report | Sprint 2 Ceremonies | msoe-sisbot |

## Wojciechowski, Andrew
###### Hours: 16.75
###### Rating (0-10): 9
###### Summary:
| Date | User | Hours Spent | Description | Issue | Repository |
|--------------|--------------|-------------|-------------|----------|------------|
| 2020-11-01 | Andrew Wojciechowski | 2.50h | Continued testing each of the weather patterns without the API. Got each of them working except for the thunder storming pattern. I will continue working to get the thunder storming pattern working and then I will move on testing the pattern with the Weather API after that. | #17 | msoe-sisbot |
| 2020-11-02 | Andrew Wojciechowski | 0.75h | Standup with team. Shelled out slides for presentation and planned out things to do for the week | #7 | msoe-sisbot |
| 2020-11-04 | Andrew Wojciechowski | 2.50h | Got of all of the patterns working for clear conditions, snowing, overcast, raining, and thunderstorming. Now I just need to work on getting everything hooked up to the API. | #17 | msoe-sisbot |
| 2020-11-04 | Andrew Wojciechowski | 1.50h | Groomed PBIs on the backlog with the team. | #7 | msoe-sisbot |
| 2020-11-05 | Andrew Wojciechowski | 0.50h | Fixed the remaining issues with the weather pattern involving how we call the weather API. Opened up a merge request for the new pattern. | #17 | msoe-sisbot |
| 2020-11-05 | Andrew Wojciechowski | 0.50h | Resolving and replying to MR feedback | #17 | msoe-sisbot |
| 2020-11-05 | Andrew Wojciechowski | 0.50h | Looked into writing automated testing. Ran into issues with installing the pip dependencies with the requirements.txt file on my local PI. I plan on reporting the issues to the team later. | #17 | msoe-sisbot |
| 2020-11-05 | Andrew Wojciechowski | 5h | Tried for a long time to get the wires on my light strip working by pealing off the plastic casing on the wires. My red wire is fine but I think I messed up and I cut the black wire to the point where it's really difficult to plug in now. Ordered a RGBW strip as a backup if this issue could not be resolved and I got in contact with my team about bringing the strip down to campus and using some tools that my other team members have that could potentially salvage the wire. | #25 | msoe-sisbot |
| 2020-11-05 | Andrew Wojciechowski | 3.50h | Met with the team for standup, end of sprint merge party, sprint 2 retro, sprint 3 planning, going over the presentation, and to write the status report | #7 | msoe-sisbot |

# Discussion

## Key Meetings
* No regular meeting with Dr. Taylor this week.
* Monday night standup and presentation (draft) coordination
* Wednesday night grooming and Sprint 3 planning
* Thursday night merge party, sprint review, finalization of Sprint 3 plan, presentation draft review and status report.

## Findings
* `npm` does not behave the way that it claims it does. Handling many dependencies on different architectures is challenging; there is no good way to isolate dependency loading.
* Web app UI (typically containerized in Cordova) is run browser and can therefore be accessed without a mobile device.
* Wiring presents many issues.

## Successes
* Weather pattern implemented!
* Presentation draft completed!
* Huge progress made with linting
* Fun exploratory spike created


## Risk Updates
* Lots of carryover into the next sprint could make next sprint really easy, or really difficult.
* We're all very busy with the end of the quarter; this has and will likely continue to negatively impact our ability to complete PBI's going into Sprint 3.

# Questions
* How are you feeling, Dr. Taylor?
* PBI Sizing
  * Are they too large? How about adding a PBI for each subtask? The team feels that part of the reason our velocity was so low this sprint is due to the 'discrete' nature of PBI's. Would making them smaller allow for a more granular burndown and accurate representation of effort vs output? Or would this create situations where 'work' is completed without customer-impacting value?

# Conclusion
The team didn't finish out the sprint how they'd pictured. Despite this, the team is excited to demo the results of their work to Bruce, gauge his interest in upcoming PBI's. Going into the next sprint, the team is wiser, more cynical, but ready to face any challenges that come head-on.
