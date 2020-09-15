This is a project proposal
Generally it includes the stuff below.
Requirements
Use the API to add voice control (Alexa, Google Home, etc…)
Create an app to convert an image into a path file that instructs the table how to draw a likeness of the image on the table
Train an AI to generate new aesthetically pleasing designs
Develop a logo like language to program paths that can be sent to the table (this could potentially result in a Discovery World exhibit)
Create a simulator
Software Architecture and Modeling
Design
Testing
Tools 
Third Party Components
Documentation


Stuff to Research this Week
What is a SIsyphus table / company?    @everyone
A sisyphus table is a kinetic table with sand in the middle and you can control a ball in the middle to create art designs using the ball in the middle. The company sisyphus industries provides the tables and firmware for the tables.
About page for Sisyphus table: https://sisyphus-industries.com/about/
Capable of producing some of the dopest pictures, like ever.
What does their software look like?  
It looks like we don’t have access to the software itself but the table itself connects over WIFI and we can send requests to it or there is a smartphone app for connecting to the table.
Article for connecting to the table: https://sisyphus-industries.zendesk.com/hc/en-us/articles/360004786031-Connecting-to-your-table
Example python library for controlling the sisyphus table: https://github.com/jkeljo/sisyphus-control 
It looks like you can create your own paths or get custom paths for the table. 
Link to getting more paths: https://sisyphus-industries.zendesk.com/hc/en-us/articles/360004786271-How-do-I-get-more-tracks-paths-
Sisyphus web center for creating more paths: https://webcenter.sisyphus-industries.com/  
What does their software actually run on?
It seems like there is some OS/Firmware running on the table and you can plug an SD card into the table
Link to Firmware troubleshooting: https://sisyphus-industries.zendesk.com/hc/en-us/articles/360035854171-Firmware-upgrade-troubleshooting
Link to reimaging an SD card: https://sisyphus-industries.zendesk.com/hc/en-us/articles/360004729932-Steps-to-re-image-SD
From an interview conducted a few years ago (2016?) it looks like the sisyphus table is using a Raspberry pi 3. Two motors control the “Sisbot” (larger tables) or two stepper motors using Trinamic drivers for smaller ones.
Popular Raspberry Pi magazine did an issue on the Sisyphus project, too, listing some more of the technical details.
Firmware is in C, written by Brain Schmalz originally for the EggBot (customized for the sisyphus application)
Node runs on top of that (yay JS)
Lots of math on top of that 
Who’s in charge (ask Dr. Taylor)? @George
Will we need to get our own table? Or should we use yours?
Dr. Taylor was assuming that since he pitched the project we would use his.
One of his “lofty” ideas was a combo of Sisyphus tables to create a Mega Sisyphus table that would be an installation at Discovery world or maybe MSOE.
Dr. Taylor was going to contact Sisyphus Industries to see if they wanted to engage with MSOE in collaboration - i.e. do they have any projects they want some free labor for. We need to probably follow up with Dr. Taylor or contact Sisyphus industries ourselves.
Dr. Taylor said there are multiple avenues for this project 
Schedule a call? Maybe? Schedule permitting?
George was able to talk briefly with Dr. Taylor but a follow up with a list of questions should probably be with the whole team if possible.
Dr. Taylor said he would be the primary stakeholder or POP for this project if we partner with Sisyphus industries.
What does their open source community look like?
What does the community actually do?
The community tab on the Sisyphus website is to support others with setting up their tables and for creating new tracks mainly for the table.There’s not that much coding related stuff in this community forum.
Users can also contribute to this site which allows users to graphically design a shape and then download the code for the shape.
How big are they?
Possible addition of +5 sisyphus tables
Use admissions/maintenance $$$ to purchase sisyphus
Ideation for Project Directions
Alexa voice API for drawing patterns/switching patterns
Machine learning stylization
Swarm of multiple sisyphus tables (LED & pattern synchronization?)
Discovery World?
Use Docker + Kubernetes for orchestration :) 🤮 
Be able to take a picture of a design and generate the right type of file for the table to be able to draw the picture (image recognition/pathfinding?)
Sisyphus Table Emulator for testing or standalone (Online/Desktop Application)
Music for formation of a soundscape
Deep Dream ML Path creator
Phone/Web app to draw picture and upload to table
If we were to do this we should look at the existing mobile app and track editor for the table
Sisyphus Industries generated project
Discovery World generated project
Recreate Sisyphus table knockoff
Open source?
Exploration into reverse engineering software and hardware
Make sure to add ample security :) 
MEGA
Sisyphus Table Games
Twitch plays sisyphus
Maze
Sisyphus Animation - via time lapse
Sisyphus Soccer



Project Idea
Stuart
Grace
Joe
Andy
George
Sum
Alexa
7
9
6
3
9
34
ML Stylize
2
3
9
2
8
24
Swarm
8
5
5
8
7
33
Picture to Path
5
1
1
1
5
13
Emulator
10
4
7
4
3
28
Soundscape
11
8
3
7
11
40
Deep Dream
4
6
10
5
4
29
Draw Picture
6
7
2
6
6
27
Knockoff
1
2
11
9
1
24
Games
3
12
8
10
10
43
Animation
9
10
4
11
2
36
Soccer
12
11
12
12
12
59

Prioritized List
Picture to Path
Knockoff & ML Stylize
Draw Picture
Emulator
Deep Dream
Swarm
Alexa
Animation
Soundscape
Games
Soccer

2020-04-23 Action Items
Contact Taylor @ George
Contact Sisyphus Industries for potential partnership
Show Taylor Prioritized List
Schedule Group Meeting with Taylor
If point of contact - add to Slack workspace
Start 3rd Party Components in Project Proposal @ Grace
Brainstorming
Picture to Path @ Joe
Knockoff @ Grace
ML Stylize @ Stuart
Draw Picture @ Andy
Emulator @ George
Schedule Next Meeting @ Grace
When: 2020-04-30 5:00 
Tentative Agenda
Discuss Brainstorming Results
Update from discussions with Taylor

Brainstorming

Note: There is a PDF file in the drive which details some more math about the table as well as the custom .thr file that the table uses for its tracks. That PDF file was created by a sisyphus community member

Draw Picture
General Workflow: Take the picture and convert it to a .thr file or a .svg. Then the .thr or .svg can be uploaded to the table or to https://webcenter.sisyphus-industries.com/  
An open source web app like this already exists for .thr files: https://sandify.org/
Written in React
GitHub repository: https://github.com/jeffeb3/sandify
Another open source project which takes any image and converts it to a sisyphus track
Written in Java 7
GithubRepository: https://github.com/markyland/SisyphusForTheRestOfUs
Ideas for this
Mobile (Tablet) / Web Interface
Save tracks that people have drawn so that they can be edited later
Provide predefined kinetic shapes that people can edit
Interface with styluses on the tablet or on the web for people to create their own kinetic drawings
Provide the ability to download a preview as a PNG and to create a THR file from it
For the PNG we can add the ability to share it via Email/Google Drive/Camera Roll in the mobile app and from the web interface we can add the ability to download the PNG onto a computer.
For the THR we can add the ability to share it via Email/Google Drive from the mobile app and we can add the ability to download the file in the web interface to a computer

Picture to path:
As said in “Draw Picture”, there is an open source software that allows you to upload an image and turn it into a path. 
The creator made a  Reddit post that outlines how to use it: (https://www.reddit.com/r/SisyphusIndustries/comments/83ryo8/sisyphusfortherestofus_is_ready_instructions_in/)
Issues:
Needs 3rd party software to turn your image into an svg/thr file (WinTopo)
It appears that this is Windows only (Ewwww)
The creator suggests using coloring book pages in order to get a clean image, which implies that it might not work well for regular pictures. I think it’d be more useful to turn any image into a path.
Do we fork the work that he’d done or do we rewrite ourselves?
A common way to find lines from an image is to use the Hough Transform (https://en.wikipedia.org/wiki/Hough_transform) 
Example program that finds lines in a picture using the Hough Transform using Matlab: https://www.mathworks.com/help/images/hough-transform.html
Idea: write an app that allows you to draw your own path or upload an image and upload it directly to the Sisyphus community gallery
Questions:
 how do we tell if the generated transform gives a valid path that can be created with the table
Line must be continuous
Line must start and end at either center or edge of table (if either of these aren’t satisfied, the table automatically starts/ends it at the center or edge, which may mess up the image)
Do we alter an invalid path to make it valid or do we make the user correct it themselves? Do we have a ‘pathify’ button that would do it for them?
Knockoff
The table is, at its core, just a CNC machine. The driver code is probably what would be hardest to emulate.
The magnet itself resembles a clock arm that is able to extend in/out, varying the radius of the arc the arm makes as it moves. There appear to be two primary control components on the arm. The first is a raspberry pi 3, running nodeJS. This serves as the Sisyphus table’s communication hub.
Contrary to what another source reported, this Raspberry Pi 3 talks to an SBB over serial USB, and the SBB does the low-level timed generation of step / direction signals for the motors.
Given this information, it seems unlikely that the Raspberry Pi is running a custom OS, but rather running NodeJS on top of Raspbian (fork of Debian, for reference).
The SBB runs firmware very similar to the earlier version of firmware written for a different project, but customized (although retains the EBB command syntax). Firmware author, Brian Schmalz has an active github (from Minneapolis, MN, and supports a variety of CAD/arduino/open source projects). EBB firmware is not available on github.
Given this information, we would need to consider how to emulate the firmware from the sisyphus table without needing access to the firmware itself.
This might be possible if we simply subvert the low-level firmware and use the C & python available on a native installation of Raspian.
Many nerd dweebs have addressed the idea of building their own kinetic sand table as well:
https://forum.v1engineering.com/t/does-this-count-as-a-build/6037/19 
There’s a lot of chatter on this forum and in the larger CNC community about cgode. Gcode appears is a CNC language that looks a lot like assembly, but instead of moving tiny pieces of data around, it directs a machine to do actions like starting a motor, moving a motor to a position, turning on a tool, etc.
It is likely that we would want to learn Gcode if we were going to write a knockoff machine, as that seems to be the de facto interface for CNC manipulation.
There is a nice python library available for interacting with Gcode if you don’t want to write it directly.
But it’s written for python 2.6-2.7 :(
Scratch that. We’re NOT using something written for old python, and we are NOT forward-porting the library.
At the end of my research, it seems like we would have to decide how closely to mimic the Sisyphus or what kind of kinetic table we’d want to have at all. In some ways we would be re-inventing the wheel.
Considerations:
What format would we want to give the table? Obviously not Gcode. 
Would we give the table raw SVG’s? We would need a path-finding algorithm for this.
Would we borrow the sisyphus format? If so, we’d need to re-write the backend (firmware piece).
Either way, we would need to physically machine a base piece (robotic arm, rotating pieces, etc.) which would be a challenge given our team’s skillset and our limited resource pool.

Emulator
The sisyphus table has somewhat complex math driving the motors and there seems to be a community or set of tools created around building out paths/images that looks nice which leaves us with 2 options:
Build out an emulator which performs the same calculations as the sisyphus table but emulates behavior so users can test against the emulator before uploading to the machine
This would be useful to use if we are remote next year because an emulator means we can test code without a table
Build out an emulator which acts as a digital sisyphus table for the same zen purposes
Think live Windows/MacOS background
Chrome Plugin
Website
This project option is very similar to the Knock-off project - just with less of the embedded systems and more Web development/Operating Systems development
