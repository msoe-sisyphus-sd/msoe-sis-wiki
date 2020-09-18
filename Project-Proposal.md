## SISYPHUS TABLE 2020-2021
### SE400, Senior Design
### Milwaukee School of Engineering
### Rage Against the State Machine Team
#### Grace Fleming, Joe Casper, Stuart Enters,  Andy Wojciechowski, George Burkhardt

## PROJECT DESCRIPTION
Sisyphus Industries is a corporation founded and chaired by CEO Dr. Bruce Shapiro. The company’s primary (and only) product, the Sisyphus table, is a kinesthetic device featuring a marble rolling through a thin layer of sand, making symmetric, circular and spiraling patterns that provide a calming experience for viewers. Our student development team will be assisting Sisyphus industries in the implementation of pre-conceptualized features related to the table, as well as providing innovative spikes towards introducing and implementing new features.
## STAKEHOLDERS
Primary: Sisyphus (CEO Dr. Bruce Shapiro & team)
Dr. Bruce Shapiro, CEO and founder of Sisyphus industries, is our primary stakeholder, since he oversees the development, sales and distribution of the Sisyphus table. Level of support from Dr. Shapiro will be determined throughout the project, but initially we expect that most communication will come through our product owner, Dr. Taylor.
Secondary: Matt Klundt
As the lead developer at Sisyphus industries besides Bruce, Matt will have ownership of the code after our senior design team’s partnership with Sisyphus comes to a conclusion. In the interest of leaving Matt a maintainable, robust and reliable codebase, we list him as our secondary stakeholder.
Product Owner: Dr. Taylor
Dr. Taylor is the expected advisor for this team, having introduced the idea of working on a Sisyphus table to the team. Since thus far, he has also been a point of contact for Dr. Shapiro and has affirmed his interest in advising the project’s progress throughout the year, he will serve as a suitable interface with which the team can interact with Sisyphus industries.
## STANDARDS
As a project built in partnership with Sisyphus Industries, the final product will be asked to meet certain engineering standards of quality.
The agile framework Scrum will be used as the primary process for development.
The team will remain in consistent and continual conversations with the client about product requirements.
New code submitted will be compatible with the existing mathematical drawing algorithms.
Third party tools used for documentation,  continuous integration, source control, etc., will be appropriately documented.
Any changes to tools in usage or tool choice will be likewise documented and changes communicated to appropriate stakeholders.
New code added by developers will contain appropriate unit tests that achieve at least 50% coverage. Unit tests shall pass, and shall follow the arrange-act-assert format.
Setup, testing and deployment (if applicable) shall be documented in a wiki by developers.
Documentation will include any and all design patterns introduced into the codebase by developers.
CONSTRAINTS
Development of any features must be concluded by May of 2021.
The cost of any additional sensors shall not exceed the negotiated cost agreed up by MSOE and Sisyphus Industries.
The hardware environment for the software shall be restricted to the Raspberry Pi 3.
No code shall be committed to the codebase that does not pass review with Sisyphus Industries.
CONTENT DEMONSTRATION FOR SOFTWARE ENGINEERING
Prerequisite knowledge required for this project consists of the following:
Scrum framework
Javascript
Python
Client-Server architecture
Embedded systems
Source control
Good testing practices
Trawling for requirements

## PROJECT TECHNOLOGIES & SUPPORT FACILITIES
### Docker
The issue of setting up development environments has grown exponentially in complexity of the past decade. Moreover, the Sisyphus codebase relies heavily upon laborious shell scripts to configure a developer’s environment. To mitigate this and enable a platform-agnostic, portable, quick environment setup for developers, a docker container based on Raspbian will be created and configured to use shared volumes. The docker image can be published to DockerHub permitting that no proprietary Sisyphus code is included, then pulled by developers directly. Alternatively, if the issue of hypervisor conflict on Windows becomes an issue, programmatically defining a Vagrant virtual machine will serve as a backup option.
Gitlab & Gitlab CI
Per MSOE’s requirements for senior design projects, this project will plan to use gitlab for source control of software, and will likely make use of the included continuous integration (CI) functionality available through gitlab. Gitlab is seen as the primary choice for these rules due to its easy integration of source code management, CI, and project planning. Given that the current project uses github, however, the team will also be open to the prospect of changing source control systems if necessary.
### Text editors/IDE per developer preference
On the choice of IDE or text editor, no official team statement shall be made. Due to the web nature of this project and the subsequent large range of tools available, developers should choose an environment they feel comfortable developing. Suggestions include VScode and Webstorm. 
### Testing
Since we are integrating with an existing repo, we need to understand what the testing procedures are (if any). If none we would want to introduce tests for any new code we develop. For the JavaScript code we look to use the standard JavaScript testing framework Mocha and we look to bring in the additional frameworks Chai and Sinon for improved assertions and mocking. Additionally for any Python code we develop we look to use the popular framework Pytest for writing tests for that code. 
### Sisyphus Table 
One will be donated to us by Sisyphus Industries, and the team is able to use Dr. Taylor’s table for testing. The table runs on a Raspberry Pi 3 and comes with programmable RGBW lights.  Various sensors are planned to be added to the table, possibly including sound, light, and heat sensors, or other sensors that are to be determined later. 
## BUDGET
Being that Dr. Taylor has a Sisyphus table he is willing to let us work with and that Sisyphus Industries is planning on sending an additional model, the team does not plan on incurring any expenses at the time of this proposal.
As the team moves forward in the project and explores different domains of the table there remains a possibility to explore additional sensors to the system. The hope would be that Sisyphus industries would sponsor such exploration but the team might be responsible for sourcing and purchasing different sensors.
The tentative budget for the start of the project is: $0.00

* as of 2020-09-17, this may change. The team has identified that in the project's current state, we are unable to build the code apart from a raspberry pi. As such and in the interim, the team may be looking for additional funding to construct development environments; this is not official yet.


## DOCUMENTATION
Given that software documentation is an ABET-level standard for software engineering, our team endeavors to use the following as documentation tools:
Swagger
Swagger is an open source technology used to document web API endpoints, and provides a graphical user interface for viewers to interactively test and use endpoints for a running application, showing inputs, outputs and response codes. Our team plans to use Swagger to document new endpoints.
JSDoc or PyDoc
Since most of the existing codebase is written in javascript and python, our team expects to use JSDoc and PyDoc to document any additional methods/definitions/classes to the codebase.
Github & Gitlab Wiki
The wiki built into Github or Gitlab depending on what version control system is planned to house documentation related to our process, any research related documents, and architecture documents.
## PRELIMINARY DEVELOPMENT PLAN
### RGBW Sensor Reactions
Sisyphus Industries has tasked the team with investigating how the RGBW lights might best be used in conjunction with the table. This does not have definite requirements as it requires an exploration into how the lights can be used from an artistic perspective - less so a technical perspective.
### Areas of Investigation:
* The table’s RGBW lights change color in response to noise sensor data.
* The table’s RGBW lights change color in response to a calendar event (e.g. 4th of July, Birthday, etc.).
* The table’s RGBW lights shall change color in response to notifications when synced with different accounts and devices.
* The table’s RGBW lights can be customized by a user via a web interface.
* The table’s RGBW lights represent the time remaining for the marble to finish a currently playing track.
* The table’s RGBW lights act as a standard 3-hand clock.
* The table’s RGBW lights change as the ball’s speed changes
* The table’s RGBW lights change as the ball’s position changes
* The table’s RGBW lights update according to the percentage of the path completion
* The table’s RGBW lights follow the angle of the path that the ball is taking
The table’s RGBW lights change with respect to the current weather (temperature, humidity, cloud cover, etc.)
* The table’s RGBW lights have a strobe mode.
* The table’s RGBW lights respond to audio input (e.g., synchronization with music)
* The table’s RGBW lights change with respect to 2D color space; color space coordinates are generated correlative to the ball’s position mapped onto a color space coordinate system.
* The team plans on revisiting and refining these ideas over the summer once the team has access to the table.
TBD by Sisyphus Industries.

Sisyhpus Industries has initially tasked this team with working on the first project without revealing much in terms of their product road plan. The team expects to finish the RGBW sensor project within the first MSOE term and hopes to continue working with Sisyphus Industries on future projects.
### Team Ideas
Sans working with Sisyphus Industries beyond the RGBW project the team has developed a set of alternative projects that still exist within the domain of the Sisyphus table.
### Possible Ideas (in no specific order):
* Machine Learning Stylize: leverage different Machine Learning applications to develop a way to generate or stylize images for the Sisyphus table to draw.
* Picture to Path Application: develop a modern application that is able to convert any image of a standard format into a Theta-Rho file (.thr) which is used by the table to draw paths.
* Draw a Path Application: develop a modern application that allows the users to draw a path by hand, generate a path according to certain shape styles and parameters, and combine and build complex designs. 
* Table Emulator: develop a modern application that simulates tracing a Theta-Rho file in a digital environment.
* Sync Speed of ball to lights & music: develop an approach to lighting and ball movement that mimics the idea of a ball “dancing” to audio input

### Information Learned Over The Summer
Over the summer Dr. Taylor gave us his mini table so that we could learn how to use it for the fall. Once he did that we learned a lot about how to use the table with the Sisyphus mobile app and how to connect to the table with the mobile app. In the app we learned more about how the table uses playlists and how to play different tracks on the table. Also, in the mobile app we learned about changing different settings for the table such as ball speed and settings for the lights. That also helped us determined how those settings affected the different tracks being played where for example if the ball speed was too high the table's arm could lose track of the ball.

### Docker Investigation
Over the summer, the idea of using docker was investigated by the team. Unfortunately, Docker will not be a viable development environment solution, at least without heavy rework, at this time. This is because of significant arhictecutre differences between the raspberry pi and a windows 10 PC (ARM vs. Intel CPU's). It does seem possible, in some capacity, to run QEMU inside of a docker container inside of a virtual machine to emulate the architecture on a raspberry pi, but the memory and CPU limits of the virtual machine being used for investigation were exceeded by the heaviness of the docker container. Moreover, the virtualbox had the limitation of not having a suitable way to emulate bluetooth.

### Zero-Day Items
In the interest of getting our project up and running smoothly in the first sprint, our team has identified a number of "zero-day" items that need to be completed before the project can really be worked on:

#1 - Determining development environment & figuring out if it's possible to move away from the raspberry pi target development architecture.

#8 - Understanding the structure of the existing codebase (server-client architecture).

#3 - Forking and migrating the fork of the existing Github git repository for Gitlab for our senior design team.

#4 - The existing codebase has no tests, so we need to investigate a testing framework and integrate it (at some elementary level) with the existing codebase.

~~#5 - Determine how to work on LED's without being in-person and having a raspberry pi with NeoPixels to work on.~~ (determined impossible).

#9 - Deploy code to the actual Raspberry Pi.

#10 - Investigate & Implement FIx to Lab Networking Topology
