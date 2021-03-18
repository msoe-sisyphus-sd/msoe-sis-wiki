# Sprint Goal

A user will be able to enable mood lighting and see its effects on the lab Sisyphus table.

# Burndown Chart

Link Chart Here

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
* Hours: X
* Rating (0-10): X
* Summary:

Insert Summary Here

## Fleming, Grace
* Hours: 9.5
* Rating (0-10): 8
* Summary: I got some stuff done this week finally, but I wasn't super focused and wasted some time on configuring my environment.

| Date       | User          | Hours Spent | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Issue/MR                                       | Repository  |
|------------|---------------|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------|-------------|
| 2021-03-12 | Grace Fleming | 2h          | Specked out code, but was unable to test because I couldn't connect to VPN using George's instructions. Since I have a different distro, I tried using the Ubuntu 20.04 recommended VPN instructions, but those haven't worked for me either yet :(                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Handle Sisyphus Table Audio Streaming Response | msoe-sisbot |
| 2021-03-12 | Grace Fleming | 1h          | Status report & reviewed Andy's PR for #56                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Q3 Ceremonies                                  | msoe-sisbot |
| 2021-03-15 | Grace Fleming | 1h          | Filled in the translator() and communicator() methods (see architecture diagram). Still need manual/unit testing.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Handle Sisyphus Table Audio Streaming Response | msoe-sisbot |
| 2021-03-16 | Grace Fleming | 1h          | Argue with myself about whether or not global variables are OK here because of the multi-threading approach. Looked into Celery (multithreading library for Python). Come to the conclusion that Python is not the language for doing real-time audio processing. Discuss feasibility of switching languages with Andy. Agree to bring concerns up to team during weekly Tuesday meeting.                                                                                                                                                                                                                                                                                                                                                                                                 | Handle Sisyphus Table Audio Streaming Response | msoe-sisbot |
| 2021-03-17 | Grace Fleming | 3.50h       | Spent a looooong time trying to get Pyaudio for windows working. Tried installing the VSBuild tools (since that is what the error said to do). That didn't work, so I eventually ended up crying to Andy about it who gave me a link to a whl file for installing it. The reaadme.md has been updated with info on how to install pyadudio. Then my windows machine had some issues with pytest :cry: , basically my machine would hang indefinitely while trying to run tests. I eventually solved this by clapping 6 times, turning in a circle while singing "Ring around the Rosie", and running pytest from inside the test directory. It worked this time! I was then able to find errors in my test/code, and get those pushed into a branch. There is currently a PR out for #57. | Handle Sisyphus Table Audio Streaming Response | msoe-sisbot |
| 2021-03-17 | Grace Fleming | 1h          | Standup with team & grooming. Also did some team bonding, which was surprisingly not that bad.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Q3 Ceremonies                                  | msoe-sisbot |

## Wojciechowski, Andrew
* Hours: X
* Rating (0-10): X
* Summary:

Insert Summary Here

# Discussion

## Key Meetings

## Findings

## Successes

## Risk Updates

# Questions

Insert Questions here

# Conclusion

Insert Conclusion here

# Don't forget the special sauce