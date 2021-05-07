# Retrospective Sprint 8 :eyeglasses: 


## What We Wanted to Get Better At - Did it Happen?
> Daily Asynchronous Standup (for real this time)

> Test changes in a table environment sooner

> Senior Sprinting :checkered_flag: :runner:  We are _totally_ going to be so _fully engaged_ with this final sprint - just you see. Like we're gonna rewrite the whole project from scratch in Rust and Clojure. You may have you'rre doubts, but we're v speedy bois. :fish: 

## What We Wanted to Stop - Did it stop?
> Attempting to mark sub-tasks done. It doesn't fit with our flow and it is honestly a hinderance on our process. Daily Asynchronous Standup should solve the issue of tracking and understanding low-level work completion

> Merge Parties - They crept back in during last sprint and we wanted to send them to kingdom come in this final sprint

> Last-minute Sprint Work. We hope that during our final retrospective and team meeting that we only need to meet to fill out paper work and all sprint work is completed well before the deadline.

## What we should continue doing - How We Did
>  Communication

> Vaccinations :syringe: 

## What to Start Doing


## What to Stop Doing


## What We Should Continue Doing - New/Current



## George Burkhardt

## Joe Casper


## Stuart Enters



## Grace Fleming
* Issues: #66

I started off the sprint by trying again to upgrade python on the table. This failed miserably, ruining another SD card image. I got in contact with Matt, who unhelpfully sent me directions for what I'd just tried; fortunately I was pursuing a second approach: getting the sisyphus codebase up and running on a newer image of Raspbian. This met more success; by Friday of the first week of the sprint I had node up and running on the card after instaling PhantomJS. There were some issues with getting the lights working. This was solved when Andy pointed out that although I had cloned the library for the lights, I had failed to compile it :face_palm: . After I did this, the lights started working! From there, I played cat-and-mouse with a few other issues, none of which took long to solve. By Monday evening, the entire combined codebase was running completely on the table.

All that was left to do was write a service file for the table. I met with Matt in a videocall to discuss this idea where it became evident that Matt only sort of knew what I was getting at but he told me to "go for it" so I did; the service files and environment file have been created and added to yet another repository along with a `README.md` that specifies how they should be placed in the image.

## Andy Wojciechowski