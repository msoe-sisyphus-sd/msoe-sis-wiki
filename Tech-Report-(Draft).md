




Senior Design: Technology Report
Dr. Taylor
Team Sisyphus
Fall 2020

Technology Report Overview
The main component that we are working with on the table is the NeoPixel rgbw light strip. One issue that has already come up is that for some unknown reason, the lights flicker and die after some use. This has been observed on both the new coffee table sent by Sisyphus and Dr. Taylor’s mini table. Another issue with the light strip is that in order to test code that we have written, we need to run code on a physical light strip. Because of this, each of us have purchased our own light strips, which will let us develop code at home, but we still need to physically be at the table in order to see if the new light pattern works on the full table. We have been thinking of setting up a livestream of the table so that we can view changes to the table remotely. 
The other component that our team will be working with is the Raspberry Pi 3 that controls the lights. This means that in order to run any code, we need to develop on the Pi. Luckily, we were all given Pis for our Real Time Systems class. There is some additional set up that needs to be done with the Pi and lights to be able to have code run locally. Another issue with the Pi is that tests can only be run on a Pi, which makes the use of CI difficult. Lastly, due to limitations with the Pi’s hardware, it will be difficult to add sensors to the table, and we are unable to play music from the Pi using the built in audio ports, we must use USB or HDMI instead. We have been thinking of workarounds for this so that we can experiment with sensors such as heat and noise, and we would like to explore playing music along with a track. 
(talk about “outdated/deprecated” technologies)

Requirements - Functional
F1: All light patterns shall be swappable on the table by a user
Description: In order to set light patterns on the table they should be available to import via a socket so that the lights module knows what the current light pattern on the table is.
Rationale: The lights module is written in Python unlike the main server for the application which is written in JavaScript. So, a way is needed in order to import light data from the JavaScript server into the Python lights module.
Originator: Andrew Wojciechowski
Fit Criterion: When a new pattern is developed, it shall not be considered “finished” until it has been tested by importing the pattern into the lights module over a socket connection from the JavaScript module to the Python module
Customer Satisfaction: 8
Customer Dissatisfaction: 10
Priority: High
Dependencies: None
History: Last modified 10/7/2020
F2: The brightness shall be adjustable on all new LED light patterns.
Description: When the LEDs are turned on for a table a user shall be able to make those lights either brighter or dimmer.
Rationale: Changing the brightness can change the effect of how the currently running track looks so a user will want to be able to change the brightness to change the effect it has on the currently running track.
Originator: Andrew Wojciechowski
Fit Criterion: When a new pattern is developed is shall not be considered “finished” until changing the brightness has been tested with the new pattern
Customer Satisfaction: 5
Customer Dissatisfaction: 5
Priority: Medium
Dependencies: None
History: Last modified 10/7/2020
F3: All light patterns shall have at least one automated test associated with them
Description: When we develop new light patterns we shall have at least one automated test associated with them written with the PyTest framework.
Rationale: If we have at least one automated test we will be easily able to rerun tests to catch if code changes will break a light pattern or not.
Originator: Andrew Wojciechowski
Fit Criterion: When a new pattern is developed, it shall not be considered “finished” until it has at least one automated test associated with the pattern
Customer Satisfaction: 1
Customer Dissatisfaction: 7
Priority: Medium
Dependencies: None
History: Last modified 10/7/2020
F4: Light patterns shall be set via the Sisyphus mobile app
Description: When we develop new light pattern a user shall be able to select a light pattern via the Sisyphus mobile app
Rationale: The Sisyphus mobile app provides an easy interface for users to control the LED lights on the table
Originator: Andrew Wojciechowski
Fit Criterion: When a new pattern is developed, it shall not be considered “finished” until it has been tested by selecting it via the Sisyphus mobile app
Customer Satisfaction: 8
Customer Dissatisfaction: 8
Priority: High
Dependencies: None
History: Last modified 10/7/2020
F5: All data needed for the light patterns shall be communicated to the lights module
Description: Data needed for the light patterns shall be communicated from the JavaScript module to the Python lights module.
Rationale: The main JavaScript server and the lights are in a different module written in Python. So, all data needed by the lights related to the ball and the current track shall be communicated to the Python lights module.
Originator: Andrew Wojciechowski
Fit Criterion: When a new light pattern is created all data needed for that pattern shall be passed to that pattern via a socket.
Customer Satisfaction: 6
Customer Dissatisfaction: 6
Priority: Medium
Dependencies: None
History: Last modified 10/7/2020
F6. All light patterns produced shall be defined and useful for tables of an arbitrary size.
Description: Light patterns should function on a user’s table regardless of the table size that they have purchased.
Rationale: Some patterns lend themselves more easily to certain tables due to the number of lights. While this might suit some patterns, a customer with an n-led table should be able to run any pattern from the sisyphus lighting pattern library.
Originator: Grace Fleming
Fit Criterion: When a new pattern is developed, it shall not be considered “finished” until it has been tested using an arbitrary number of pixels.
Customer Satisfaction: 5
Customer Dissatisfaction: 10
Priority: High
Dependencies: None
History: Last Modified 10/06/2020
Requirements - Nonfunctional
N3. Any external sensors added to the system in the course of the project shall use officially-supported drivers.
Description: If a sensor is added to the table, and a driver is required to read/write from the sensor, then the driver used shall be officially supported by the sensor manufacturer or another established institution.
Rationale: Drivers notoriously have compatibility issues. This often leads developers to choose drivers from open-source that are not officially supported. While these drivers might “get the job done” at first, they quickly fall out of support and cause headaches down the road for development. To prevent this, we recommend that all drivers used for any additional sensors in the project be driven by officially-supported drivers. 
Originator: Grace Fleming
Fit Criterion: When a sensor is added to the table, the driver (if applicable) must be published by a certified manufacterer. 
Customer Satisfaction: 0
Customer Dissatisfaction: 0
Priority: Medium
Dependencies: None
History: Last Modified 10/06/2020
N4. Any new patterns developed for lighting shall support a colorblind mode.
Description: Every pattern shall have a color palette that it can use in the event a user is colorblind.
Rationale:  Light patterns should be enjoyed by all users who purchase a table, even those whose perception of color is not the same as the majority of the human race.
Originator: Grace Fleming
Fit Criterion: When a new pattern is developed, it shall not be considered “finished” until it has a color palette that it can use for a colorblind user.
Customer Satisfaction: 3
Customer Dissatisfaction: 2
Priority: Low
Dependencies: None
History: Last Modified 10/06/2020
N5. Any new light patterns developed shall provide clear, concise and helpful diagnostic information to the logfiles.
Description: Light patterns may error out in the course of running. If this is the case, they should log to an appropriate logging location with the necessary information to make troubleshooting remotely timely and easy. This will result in a faster problem resolution for customers.
Rationale: The developers who have developed all previous lighting patterns likely know what to look for when the lights encounter issues. In the case of added light patterns that we develop, having the relevant diagnostic information on hand could be very important to diagnosing issues with the table.
Originator: Grace Fleming
Fit Criterion: When a light pattern encounters an error, it shall log to the log file and record the time of the error, the error code, a description of the code, and a stack trace if applicable.
Customer Satisfaction: 2
Customer Dissatisfaction: 5
Priority: Low
Dependencies: None
History: Last Modified 10/08/2020


Technology Changes
Potential Options
Our project is rather limited in technologies, as there is an established codebase, and deviating from it too much would cause a greater hassle on our Product Owner to reconcile our code with theirs. It is also outside of the stated scope for our project, so any changes would have to be passed through them.
That being said, some minor revisions could be made, the two greatest ones being upgrading to a modern version of Node and changing the Python code to depend on an officially released and maintained package.
Decision Criteria
For both options we plan on writing a prototype that implements the new technology. While it won't be as fully featured as the main codebase, it should be close enough that the level of effort of a full scale migration can be measured. Once this is done, an email to our Product Owner will be drafted detailing our findings. Based upon our observations and our Product Owner's feedback, we will decide whether to go ahead with the migration or not.
Rationale
For upgrading node:
  The primary benefit is for developers, as they will no longer need to manage multiple versions of node on their development machines. Also, this would allow the code to be more maintainable, as for future versions, there would be a lot less work required in an update. Potential benefits include being able to use more up to date packages, and a lower chance of security vulnerabilities. This would cost a decent amount of development time to pull off though.
For upgrading Python dependencies:
  The primary benefit is in setup, as the process of getting the light interface to work is reduced from a long, complicated shell script to one simple command. This would also allow for the exclusive use of Python 3 in the project, which would aid versioning on development machines. This solution is also a lot more maintainable, and would be easier to change in the future if a migration was required. The downside here is also in development time, as most of the code controlling the lights would have to be rewritten.

Prototype Information
Python NeoPixel LED API
The current environment for the Sisyphus Table uses a Python 2 library and C-based shim to access and control the LEDs on the table. This library is out of date (Python 2 EOL and newer official packages from Adafruit available) and makes spinning up new development hard. In addition to addressing new lighting modes (the primary task set by our primary stakeholder Sisyphus Industries) the team will engage in prototyping an update to the lighting controls by upgrading packages and refactoring the code to use standard software patterns (e.g. strategy pattern) to make the code base more maintainable and extensible
Experiments:
Replicate LED start-up script with new LED
Translate at least 2 lighting modes into a strategy-like pattern for easier modifiability and extensibility
Switch out LED Python 2 modules for Python 3 and attempt to run - correct scripts as necessary
Node 8 Runtime
The Sisyphus Table currently uses Node 8 to run it’s server and web interfaces. This version of node has been end-of-life for several years and poses security and maintainability risks to the platform. In addition to addressing new lighting modes (the primary task set by our primary stakeholder Sisyphus Industries) the team will engage in prototyping an update to the Node runtime and any associated packages so that the code base is brought into current LTS support.
Experiments:
Attempt to run with Node 12/14 - correct scripts and update packages as necessary
Audit “low-level” Node API usage for potential issues
===
The technology report should discuss your rationale for technology choices made for the project. It should be clear from your report that you considered standards and realistic constraints and used an engineering process to make technology choices for your project.
The technology report should include:
An overview of the technology related issues for you project. (Joe)
A list of requirements (functional and non-functional) for the technology to be used. (Andy: functional; Grace: nf; Joe: Help)
A list of potential technology options. (Stuart)
A set of strategies for evaluating your choices. This will likely include research as well as well chosen prototype implementations.
Prototypes should be designed to help determine whether a particular technology will be best for your project. Typically these prototypes will focus on creating functionality for the least understood aspects of your project. (George: lights, node?)
A rationale for each technology choice listing advantages and disadvantages for each option considered. Be sure to include aspects such as cost and the potential for increased risk. (Stuart)
Your target audience for this document is an ABET evaluator whose goal is to find evidence that you have
defined the requirements
identified potential technology
developed relevant experiments and/or prototypes to increase your understanding of the technology
identified and minimized risks associated with making specific selections
clearly documented and justified your choices
In particular, the technology report may be an ideal place to demonstrate proficiency with the following student outcomes for the software engineering program:
SO 1-4: A student will identify constraints in open ended problems.
SO 3-4: A student will justify tradeoffs to a member of management.
Your report will likely include summaries of experiments and/or prototypes as well as links to the raw data/code in GitLab

