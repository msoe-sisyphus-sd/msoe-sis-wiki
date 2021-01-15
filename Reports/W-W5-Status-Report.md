# Sprint Goal
Investigate mapping audio to colors and how to integrate a Python ML model with the existing code base.

# Burndown Chart
![image](uploads/1553f6cf15ca89b057cfeea42d462af1/image.png)

# Team Commitment

## Burkhardt, Robert
* Hours: X
* Rating (0-10): X
* Summary:

Insert Summary Here

## Casper, Joseph
* Hours: X
* Rating (0-10): X
* Summary:

Insert Summary Here

## Enters, Stuart
* Hours: 8
* Rating (0-10): 6
* Summary:

| Date | Hours Spent | Description | Issue | Repository |
| --- | --- | --- | --- | --- |
| 2020-1-8 | 20m | Met with Taylor for weekly meetup | #7 | msoe-sisbot |
| 2020-1-13 | 2h | Discussed direction of issue w/ Grace and decided to split out issue into sub-issues | #43 | msoe-sisbot |
| 2020-1-14 | 4h | Figured out how to connect to table and tested light pattern | #19 | msoe-sisbot |
| 2020-1-14 | 40m | Wrote documentation for testing patterns on the table via Postman & ssh | #7 | msoe-sisbot |
| 2020-1-14 | 1h | Met w/ team for standup & status report | #7 | msoe-sisbot |


## Fleming, Grace
* Hours: X
* Rating (0-10): X
* Summary:

Insert Summary Here

## Wojciechowski, Andrew
* Hours: 5.39
* Rating (0-10): 6
* Summary:

| Date | User | Hours Spent | Description | Issue/MR | Repository |
|------|------|-------------|-------------|----------|------------|
| 2021-01-08 | @wojciechowskia | 0.25h | Standup with the team. Also, discussed checking with Dr. Taylor when the tech report is due as well as the sprint review. | #7 | msoe-sisbot |
| 2021-01-11 | @wojciechowskia | 1h | Investigated CPU utilization and temperature of the sound output to color spike. Determined that CPU utilization was about at 100% with the lights and the temperature was about 46 degrees celsius after running the algorithm. | #40 | msoe-sisbot |
| 2021-01-12 | @wojciechowskia | 0.17h | Purchased a USB microphone to use for testing performance. | #40 | msoe-sisbot |
| 2021-01-12 | @wojciechowskia | 1.5h | Wrote code to test the performance of recording 5 seconds of audio from a microphone continuously and sending it to a server to do the machine learning. Awaiting a microphone for testing.| #40 | msoe-sisbot |
| 2021-01-13 | @wojciechowskia | 0.5h | Read up on SPI vs. PWM vs PCM a bit. Nothing was mentioned about performance concerns between the methods but I am going to compare the performance with the LED library next and eventually audio when I get my USB microphone| #40 | msoe-sisbot |
| 2021-01-14 | @wojciechowskia | 1h | Spent some time looking into the performance implications of PWM vs. SPI for the lights. Found that SPI took less CPU utilization so then I ran the ML spike on the PI without the lights and the CPU utilization was still at 100%| #40 | msoe-sisbot |
| 2021-01-14 | @wojciechowskia | 1h | Standup and wrote status report with the team | #7 | msoe-sisbot |

# Discussion

## Key Meetings
* Friday 1/8: Met with Dr. Taylor to discuss project and risks associated with with the new direction. We also developed a new format for weekly sync meetings between the team and Dr. Taylor.
* Monday 1/11: sync meeting (missed by 2/5 of the team for various life issues). 
* Thursday 1/14: Status report meeting

## Findings
* Sisyphus app code is difficult to run.
* Documentation for team development process is poor.
* Physical audio features extracted from audio can be used to describe the mood of an audio/musical segment.

## Successes
* ML algorithm developed from demo works on Ubuntu 20.04 to effectively colorize music mood.
* Stuart got his light pattern working.

## Risk Updates
* Dr. Schilling performed a firmware upgrade to the lab topology. No abnormalities have been identified in network access, but it's something to be aware of.
* The ML algorithm being used is CPU-intensive and eats up 100% of a raspberry pi  4B+'s cpu.

# Questions
* Specific timeline for tech report?
* Is the due date for the self-guided learning in canvas actually accurate? (the 28th)

# Conclusion
The team remains excited about the project direction, and is currently considering multiple methods of implementation (pi vs. phone vs. external hardware under the table). The team plans to have a fully functioning demo as well as decision matrices for design decisions surrounding software/hardware considerations prepared for next week's sprint review.