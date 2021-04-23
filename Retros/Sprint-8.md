# Retrospective Sprint 8 :eyeglasses: 


## What We Wanted to Get Better At - Did it Happen?

> Daily asynchronous stand ups

No, we did not do daily async standups. Honestly, the team just forgot that we were going to do this. However, the team was still in constant contact with other members. The team feels we're allowed a mulligan and will try again this sprint!

> Marking subtasks as "done" as soon as the subtask is finished

Nope! It's really inconvenient to go back in and update this piece of the PBI. The team doesn't really use these to track work so it just doesn't fit in our workflow at the moment (better late then never in discovering this :) ) 

## What We Wanted to Stop Doing - Did we stop?

> Procrastinating

Some of the team feels they did better in not procrastinating - completing work. However, others on the team are still wrestling with their inner procrastination daemons 😈.

## What we should continue doing - How We Did

> Team bonding after meetings

We did really well with team bonding - we made sure to do non-school, non-senior-design activities after meetings to reduce the feeling of burnout.

> Async grooming

We didn't do a ton of grooming this sprint, however the PBIs that we did have on deck were decently written out prior to meetings (from past grooming sessions).

> Not contributing to the police state

You know, our project may not be super flashy (because we fixed that in a previous PBI), but at least we aren't tracking people by their gait and assuming the worst of people. Like yes, we are recording private audio and passing it to an AI service but that's all voluntary and does not have any ethical implications about mis-identification of innocent persons :microphone: :arrow_down: 

## What to Start Doing

* Daily Asynchronous Standup (for real this time)

* Test changes in a table environment sooner

* Senior Sprinting :checkered_flag: :runner: 

We are _totally_ going to be so _fully engaged_ with this final sprint - just you see. Like we're gonna rewrite the whole project from scratch in Rust and Clojure. You may have you'rre doubts, but we're v speedy bois. :fish: 

## What to Stop Doing

* Attempting to mark sub-tasks done

It doesn't fit with our flow and it is honestly a hinderance on our process. Daily Asynchronous Standup should solve the issue of tracking and understanding low-level work completion

* Merge Parties

They crept back in during this sprint and we want to send them to kingdom come in this final sprint

* Last-minute Sprint Work

We hope that during our final retrospective and team meeting that we only need to meet to fill out paper work and all sprint work is completed well before the deadline.


## What We Should Continue Doing - New/Current

* Communication

* Vaccinations :syringe: 

# Personal Contributions

## George Burkhardt

This sprint I focused on building out the "front-of-the-front-end" where I was in charge of building the color pickers that would allow users to set preferences for each emotion to better match how they perceive the music. I was able to successfully complete the bulk of this work and worked in tandem with Stuart (who was in charge of the "back-of-the-front-end") to integrate the two parts so that it functioned smoothly. The only work I was not able to complete was testing the full solution with Grace's and Andy's changes to sislisten. I preformed manual validation and inspected the network traffic being sent but due to issues I'll shortly get into I was not able to test the integration of parts - thus the work remains incomplete but can quickly be finished starting next sprint (also pending peer review). As for why this work could not be completed, our development environment (the Lab table) decided to crash and corrupt the Pi image when trying to get a more recent version of Python installed for better testing. There were issues with the Raspbian image and it would not automagically install anything above Python 3.4 or OpenSSL 1.0.1 so I spent time with the rest of the team, in lab, on 2021-04-22 to resurrect the large Table via Taylor's Table's image and worked through different workarounds to the Python issue. Ultimately, we were unable to resolve the issue at the sprint close, so we have quite a bit of testing carry over for next sprint - however once the Python issue is resolved (we're really close) we will finish testing, review and merge, and work on our upcoming PBIs for our final sprint!

## Joe Casper

In this sprint, I converted the mood lighting server to return map coordinates instead of colors.   These coordinates are used when setting colors on the color map. After finishing this, I tested out various songs and how their color coordinates look in several runs to see if they are consistent. 

## Stuart Enters
In this sprint I was working on the back of the frontend, getting siscloud to call the proper endpoints in sislisten. I was not as productive as I wanted to be due to not being able to see what I was working on (due to a borked local setup). I was in charge of team bonding activities last week, and did some administrative behind-the-scenes activities. I also was involved in the merge party + debugging blowout that was our final night of this sprint. 

**tl;dr** spent more time debugging than developing

## Grace Fleming
* Issues: #64
I started off by implementing the translator and a new endpoint to accept user settings. This was accompanied by writing some tests (although Andy wrote the bulk of them), and adding extra validation based on both of us test's output. Later, I integrated the translator back into the pipeline for sislisten, and added logging to the thread pool so that when threads terminate due to an exception, those exceptions are logged instead of disappearing into the ether. Previously this had been a problem while debugging. 

Outside of my normal issue work, I helped out Joe a tiny bit with getting the AI service to return coordinates, and did the deploy for his work to gcloud after he was done. I also spent an hour or so on Tuesday night week 7 assisting George with getting the raspberry pi working with Bluetooth; this was mostly a google scavenger hunt but we did end up getting it working.

The night of sprint paperwork before sprint review, I spent significant time with the rest of the team trying to get python3.7 to work on the table in order to be able to run sislisten; this proved to be nearly impossible. Initially, installing python3.7 from apt broke the table so completely that it would not even come onto the network. Re-flashing the SD card on the larger table using the mini table's SD card successfully brought the table back up, but then there was reconfiguration work to do to. From there we attempted to install an updated python version by compiling python3.7 from source. This did not work, for the reason that openSSL on the pi isn't compatible with higher versions of python yet (George later made it past this issue but ran into other ones). Morning _of_ the sprint review, I spent 3+ hours configuring the table to point to sislisten on my MSOE machine instead of itself, in the process discovering that there was an integration issue with siscloud using form data to send user settings while sislisten was expecting JSON settings. Andy was able to implement a fix for this, and I was able to finish getting the lab demo ready. We rehearsed the demo a few times as well.

In general I think I worked much harder this sprint than the previous one. I didn't log very many hours, though which was a problem.

## Andy Wojciechowski
In this sprint I assisted with implementing the user settings feature in sislisten. I wrote a lot of automated test cases for that feature and I added a lot of additional validation for this feature to make sure that the data sent and used by the server is valid. I also did a lot of manual testing with this feature and I looked at the colors be translated by sislisten. I found that the colors were not what I was expecting given a song and I found that the further a point is the way from a certain center point for an emotion the more interpolated it's going to be with the other emotion colors. We ended up writing that up for an additonal PBI to be tackled next sprint. I also wrote a wiki article this sprint detailing how the code in siscloud works using the information I got from Matt at the beginning of the spring.