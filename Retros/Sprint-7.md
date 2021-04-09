# Retrospective Sprint 7 :eyeglasses: 


## What We Wanted to Get Better At - Did it Happen?

> Have more async checkins with the team and sidebar longer issues during standup.

Last Thursday, our wrap up meeting was async. Discussions about things like hosting the server on Rosie also happened offline. 

> Prepare retro points before retro to discuss with the team

We did not, we will plan on doing this next time

## What We Wanted to Stop Doing - Did we stop?

> Merge parties on the day the sprint ends

We had one MR on the day the sprint ended, which is better than last week, in which there were 5

## What we should continue doing - How We Did

> Team Bonding activities

We played games after some meetings

> Avoiding Senior Slide for Senior Design

Some of the team feels like they are sliding, others do not 

> Doing asynchronous backlog grooming
 We did our grooming asynchronously

## What to Start Doing

* Daily asynchronous stand ups 
* Marking subtasks as "done" as soon as the subtask is finished

## What to Stop Doing

* Procrastinating 

## What We Should Continue Doing - New/Current

* Team bonding after meetings
* Async grooming
* Not contributing to the police state

# Personal Contributions

## George:


## Joe:

In this sprint, I worked on adding sislisten to the sisproxy startup script. Now, when the table boots up, sislisten will automatically start as well. I tried to do this by adding it to the configs.js file in sisproxy, but it got really messy really fast due to how incohesive the current code is, so Stuart wrote a shell script to start sislisten, and I added this script to run on startup. After getting this running locally, George and I added sislisten to the table. We ran into a lot of issues downloading dependencies, but we got it running and ready for demo tomorrow.  


## Stuart:


## Grace:

Issues: #62

This sprint I worked on deployment of the table service. First, I researched available cloud providers. Then, I researched the pros and cons of each platform. Next, I selected Gcloud and Azure as potential candidates (touching base with my counterpart on the issue, Andy). I then did a deploy of our application to Gcloud, and explored the costs of running it in the cloud (or really, how to keep it free!). From there I attempted Azure, but was stymied by outages. After further research I found complaints about the platform’s availability and nixed it from further investigation. I also attempted a development deployment on ROSIE, our supercomputer, but was blocked by firewall issues with port forwarding (HPC Admin is addressing now). Due to the sprint ending, I gathered latency statistics from the completed test deployments, reported these statistics, and selected google cloud as the best option for our prototype deployment. I did not put in as many hours as I could have this sprint, owing to academic and school burnout, but will attempt to correct this shortcoming in subsequent sprints.


## Andy:

Issues: #62

In this sprint I looked into deploying the AI service on an optimal platform. I spent the first part of the sprint researching how people deploy Flask AI services and found that people use the standard cloud providers and I found an additional service called PythonAnywhere. I was able to get the service deployed to AWS ElasticBeanstalk pretty easily using the CLI but I found that https is not enabled by default and that you need to own a custom domain in order to enable https. I also explored PythonAnywhere but eliminated it pretty quickly since the free tier is limited to 512 MB of space on the server. I also attended the meeting to potentially deploy this on Rosie with Grace, Gagan, and George. Finally, I got performance statistics for AWS and I discussed the results with Grace and we decided that Google Cloud is the winner if we can't deploy it on Rosie.