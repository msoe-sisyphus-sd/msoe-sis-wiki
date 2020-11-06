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
###### Hours: X
###### Rating (0-10): X
###### Summary:

Insert Summary Here

## Enters, Stuart
###### Hours: X
###### Rating (0-10): X
###### Summary:

Insert Summary Here

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
###### Hours: X
###### Rating (0-10): X
###### Summary:

Insert Summary Here

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
