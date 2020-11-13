---
Requirements - Definition and analysis including selecting at least one stakeholder. You will need to become familiar with the domain.
Requirements definition:
* Title: Requirement number along with the requirement
Description: Gives more information about what the requirement is trying to achieve
* Rationale: Why this requirement is being included
* Originator: Who this requirement came from
* Fit criterion: The action that needs to be satisfied in order to call the requirement complete
* Customer satisfaction: An estimate on how happy this would make a customer
* Customer dissatisfaction: An estimate on how unhappy this would make a customer should it not be implemented
* Priority: Scale 1-10 on how important this requirement is in relation to other requirements
* Dependencies: The numbers of other requirements that must be completed to work on this one 
* History: The date of the last time this requirement was modified
## Software Architecture and Modeling
### It should involve some interesting elements of software system design, including thoughtful exploration of the architecture to support iterations.
The Sisyphus table consists of 3 distinct parts - the motor control, the lights control, and the server that orchestrates all operations and communicates with the client app which provides user controls. These parts map to real world elements of the table and serve as a consistent separation of concerns. For the beginning of our project we were tasked with exploring the lighting system and generating new and interesting interactions. This requires knowledge of how the system and it’s APIs work but also requires understanding of how commands are sent from the server and processed by the lighting module. While the team is not drafting an architecture from scratch any changes made must be rectified against the current architecture or must investigate and address shortcomings.
For example, to control the lights a command is sent from the client app to the table’s server which will then gather data from the appropriate locations (data stores for color preference, current ball position queried from motor control), package it, and send it over a local file server connection to the lighting module. Planned work for incorporating APIs to determine lighting behavior must understand, and extend this client-server architecture in order to produce new functionality.
Additionally, the team is investigating producing a “releasable” upgrade which will introduce new functionality to the system. For example, the team may choose to incorporate motion controls that move the ball and adjust the lights based on user actions. New additions like this would require their own architecture of sub-modules (how is data passed around, how are interfaces exposed, etc.) and integration into the larger table’s architecture.

## Design - Strategies employed, such as the use of patterns and allowances for evolution of the product.
### The system currently does not use any patterns and this has resulted in monolithic files and copy-pasted files with duplicated behavior and code. This means the codebase is ripe for patterns and refactors to introduce modern software strategies that would make the code more maintainable, and understandable.
One such example is the lighting module. Each lighting pattern has its own file with two functions (an init and update). The init behavior is nearly identical across files while the update contains the business logic for executing the different lighting patterns. This module can be refactored to use a strategy pattern (context uses common interface, multiple implementations).
In keeping with agile principles, the team does not plan on working on refactors outright but will rather incorporate re-writes and patterning as code is modified with other work. With new functionality, patterns and other design strategies will be considered in how to best implement the work.

## Testing
### How good is the automation of the testing and was it considered from the beginning?

For testing the table in our PBIs we go through testing our changes on the table manually as well as writing automated tests for our PBIs. We considered this from the beginning and we setup a separate Git repository for writing our unit tests and we setup automating testing infrastructure for the Python lights module using PyTest and for the JavaScript module using the mocha and chai frameworks.

## Security and Privacy
### How are you addressing security and privacy? Are you using best practices?
We haven’t had to worry about security and privacy yet since it’s early in the project and we’re working on getting other things set up first. But in the future we’ll have to make sure that the Raspberry Pi  is secure making it difficult for bad actors to access the Pi.Also, on the Pi we’ll have to worry about making sure that any secret data on the Raspberry PI is stored securely on the PI using methods like encryption. Also, for the web components of our application we’ll want to make sure that the web endpoints on the table aren’t accessible by unwanted actors.

## Tools
### Good use of development, testing, and management tools (including GitLab). 
* Gitlab 
  * Issue Tracking - we utilized the Gitlab native issue tracker to assign tasks to specific people, track the time we were spending on each issue, and commenting on knowledge acquisitions to create a detailed log for anyone else who viewed the issue
  * Milestones - as a scrum team we leveraged the Gitlab milestones to act as sprints, assigning issues to be completed, tracking our burndown, and grooming the backlog to ensure the maximum priority tasks are always getting completed
  * Wiki - we utilized the builtin wiki in Gitlab to keep track of our external documentation: from ceremonies to brainstorming to meeting logs
  * CI - we created a project to run our test set against all the existing projects on a push
* Hardware - our hardware for this project is somewhat set. However, we have had to overcome a number of problems in order to develop locally. For developing code controlling the lights, we each had to purchase the relevant hardware, and then adapt the code so it will work locally. We also needed to interface with the existing hardware, so we set up a live-stream on twitch.tv and got ssh capabilities exposed on a VPN.
* Pytest and Mocha - we integrated PyTest and Mocha in order to test the codebase.
* Pylint & ESLint - in order to improve the quality of the code, the team introduced linters to the projects. These will hopefully ensure that the code we are adding to the project is clear, readable, and maintainable
Experimentation and Prototyping - Applied to unknown technology to improve knowledge and reduce risks. As the architecture is developed and key mechanisms are determined, what risks arise and how will you address them in the development process?
While this project is fairly limited where new technology is concerned, we are interested in improving some out of date software packages included in the existing application. To do this, we are creating prototypes of the existing code with the newer packages to gauge the difficulty of upgrading the codebase

## Third Party Components
### Demonstrate your skill in discovering and employing third party components.
 
This project involves the integration of many third-party components. The tech stack relies exclusively on a raspberry pi 3 model A architecture, integrates Adafruit Neopixel lights with a third-party custom python library, uses Apache Cordova for running the mobile app, and runs a web server through node.
To this tech stack, our team has added linters for python (pylint) and Javascript (ESlint) to prevent compilation mistakes and other stylistic errors since we are unable to run the actual code in a pipeline due to not having a docker container with a raspberry pi’s architecture. Linters, however, can be run in an architecture agnostic fashion and can prevent major issues from entering into the codebase. We also added unit testing frameworks (see “Tools” section).
We are also considering updating some of the third-party components of the system (such as the python library) to bring the codebase up to date.
The team is also making use of a variety of third-party components to perform development and debugging, such as the VSCode SFTP plugin (to develop on a different device’s file system), MobaXTerm/Putty (SSH clients), CURL (making web requests in an SSH session) and Win32Imager (to create and write backup copies of SD cards). For more information on third-party components integrated by the team into the project, see the “Tools” section.


## Documentation
This takes many forms including continuous documentation such as notes associated with tasks that are updated regularly, weekly reviews, sprint reviews, and other artifacts such as a technology report, discussions of where you achieved specific course outcomes, project presentations, poster, and final report. 


The team currently manages a wiki that exists alongside the fork of the codebase. This structured wiki include weekly status reports submitted to our advisor, sprint plans that document promised work, and sprint reports and retrospectives that analyze completed work and the team’s process in order to reduce development risk and ensure incremental and sustainable progress is made during the course of the project.
All ABET-type requirements (such as technology reports, and outcomes) are documented in the wiki as well in order to maintain a single source of truth for artifacts relating to the project.

## Managing Risks
### Strategies employed to manage risk.
 
There are many risks associated with our project, both in terms of development continuation and completion. Risks whose threat to the project is highest and most likely are listed below:
* The Product Owner will lose interest in the project or be otherwise indisposed to provide useful feedback.
  * Managing Risk: Even without proper feedback from the Product Owner, our team can continue to innovate new ways to interact with the table. In addition to our primary Product Owner, the team and team’s advisor can together serve as a proxy product owner team to decide what areas of investigation and development are worth pursuing.
Development on the product will become difficult or impossible due to the deprecated nature of Python 2.7, the outdated rpi_ws281x lighting library, the use of Node 8, and the fading support of the Cordova cross-platform web and mobile framework.
 * **Managing Risk:** Look into upgrading libraries that can be upgraded. In particular, perform incremental upgrades as code areas are worked on and investigated.
* Development Environments
  * Local development environments do not mirror the production environment precisely, since developers don’t have their own tables. Developers are developing locally with different raspberry pi versions and their own versions of Neopixel strips that are not identical to the strips used on a production table.
  * **Managing Risk:** Developers can interface consistently about issues with their setups to ensure that when a developer faces an issue with their setup the issue is not replicated across setups. Once a person has their development environment completed, they can distribute an image from their SD card for a certain platform (e.g., the Raspberry pi 4). This should help with consistency across setups. For those using Raspberry Pi 3’s, a production image from a production raspberry pi can be used. 

  * There is only one production environment. This production environment is located in a common lab that all developers have access to at MSOE (DH329); however, this lab has the potential of not remaining open if the institution must revert to complete-online instruction due to the pandemic.
  * **Managing Risk:** A webcam has been placed on the production environment to enable remote development. Since the team is able to exert some level of control over the production environment locally, in-person access does not need to be frequent. In the case of a total closure of the labs (no personnel permitted inside the building), the table can be migrated to a team member’s house, or accommodations with MSOE to allow 1 team member into the building at an agreed upon interval of time can be arranged.
  * Both local and production environments have proved to be quite brittle. Local setups behave strangely on occasion (interacting oddly due to apartment wiring issues) and the production environment has had issues with the LED lights shorting out.
  * **Managing Risk:** The production table as well as the miniature table owned by Dr. Taylor had their lights replaced by Sisyphus Industries after the lights burned out. Our team has resolved to be more careful about plugging/unplugging the table to prevent future burnouts.

## Standards Used
### Identify industry standards used in the project. 
* PEP 8 - code standard for python code. Implemented with pylint.
* Standard JS - code standard for JavaScript code. Implemented with eslint.
* ISO 8601 - Date and time standard. Used whenever dates are present.
* GitLab CI - Pipeline manager. Runs with each commit. 
