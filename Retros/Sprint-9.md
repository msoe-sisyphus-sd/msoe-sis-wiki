# Retrospective Sprint 9 :eyeglasses: 


## What We Wanted to Get Better At - Did it Happen?
> Daily Asynchronous Standup (for real this time)

Improvements were made as we did this more during the sprint than in previous sprints, however during the second week we reverted to our previous communication style.

> Test changes in a table environment sooner

Yes, despite coming out of last sprint needing to essentially rebuild the Pi image on a newer Raspbian version, the team did deploy and test changes on the table sooner in the sprint. In fact, a couple of defects/bugs were caught and corrected due to this change in process.

> Senior Sprinting :checkered_flag: :runner:  We are _totally_ going to be so _fully engaged_ with this final sprint - just you see. Like we're gonna rewrite the whole project from scratch in Rust and Clojure. You may have you'rre doubts, but we're v speedy bois. :fish:

_Someone_ downloaded Kyrgyzstanian botnet software which corrupted our complete rewrite so we've lost all progress made on this front :cry:

The responsible party knows who they are...

## What We Wanted to Stop - Did it stop?
> Attempting to mark sub-tasks done. It doesn't fit with our flow and it is honestly a hinderance on our process. Daily Asynchronous Standup should solve the issue of tracking and understanding low-level work completion

Sub-tasks who? We don't know her...

> Merge Parties - They crept back in during last sprint and we wanted to send them to kingdom come in this final sprint

No big merge parties this sprint - we did have 2 MRs open at once but that was due to last sprint carry over (which had already been reviewed).

> Last-minute Sprint Work. We hope that during our final retrospective and team meeting that we only need to meet to fill out paper work and all sprint work is completed well before the deadline.

Nope, work was completed without procrastination.

## What we should continue doing - How We Did
>  Communication

The members of the team don't hate each other so we're all still on talking terms (for now).

> Vaccinations :syringe:

People (including Andy, Andy's Parents, Dolly Parton - but not Grace), (and those who got Moderna :nauseated_face:) have gotten vaccines and full immunity.

![image](uploads/df56be974a5a518d14f978f5d4212a01/image.png)

## What to Start Doing
* Relaxing
* Facing our existential dread

## What to Stop Doing
* Doing Grooming
* Doing Sprint Work
* Deferring our existential dread

## What We Should Continue Doing - New/Current
* Being Amazing
* Bullying those who received the Moderna or Johnson-and-Johnson vaccine


## George Burkhardt
* Issues: #47, #50, Audio Script

This sprint I spent some time looking into the underlying implementation of beat detection to gain a better understanding of it. Additionally, I very briefly assisted Grace in trying to upgrade the image to one more suitable for running Python 3.7. Additionally, I spent a bit of time developing a script that allows team members to play music via the bluetooth speaker in lab (although that's not super helpful at this point). Finally, once the new table image was up and going (all due in part to Grace's hard work), I briefly manually tested the changes to the web app to ensure everything was in working order. Essentially, I kinda performed a grab bag of activities this sprint.


## Joe Casper

This sprint, I tried to implement beat detection for the table with Stuart. PyAudioAnalysis has a built in beat detection function, and we tried to make it work. However, there were error reading in the file, and it didn't work. We tried looking up how to fix it, but there is no documentation or examples of anyone using this, and the one question on stack overflow did not have an answer.


## Stuart Enters



## Grace Fleming
* Issues: #66

I started off the sprint by trying again to upgrade python on the table. This failed miserably, ruining another SD card image. I got in contact with Matt, who unhelpfully sent me directions for what I'd just tried; fortunately I was pursuing a second approach: getting the sisyphus codebase up and running on a newer image of Raspbian. This met more success; by Friday of the first week of the sprint I had node up and running on the card after instaling PhantomJS. There were some issues with getting the lights working. This was solved when Andy pointed out that although I had cloned the library for the lights, I had failed to compile it :face_palm: . After I did this, the lights started working! From there, I played cat-and-mouse with a few other issues, none of which took long to solve. By Monday evening, the entire combined codebase was running completely on the table.

All that was left to do was write a service file for the table. I met with Matt in a videocall to discuss this idea where it became evident that Matt only sort of knew what I was getting at but he told me to "go for it" so I did; the service files and environment file have been created and added to yet another repository along with a `README.md` that specifies how they should be placed in the image.

## Andy Wojciechowski
* Issues: #66

In this sprint I spent a lot of time on mood lighting color tuning. I changed the color map to be based on the shortest distance from a mood color center. This made the color more consistent as there was no more color interpolation and points for songs were now just mainly around 2 different mood regions. I also tuned this more by making the neutral region smaller as I noticed there were a lot of neutral results in my initial tests of the color map. I also did a lot of mood lighting testing on the table hooked up with siscloud and I fixed some issues that I found when testing on the table. Those involved I fixed a crash where we weren't cleaning up the audio stream properly on the table and I fixed an issue where we weren't starting the sislisten server properly with help from Grace. I determined that there were still some limitations where occasionally we get audio results that have a 0 valence and energy even when playing a song. Also, the algorithm gets more inconsistent results in rooms with bad acoustics. Finally, I recorded a video showing the results of the new color map.