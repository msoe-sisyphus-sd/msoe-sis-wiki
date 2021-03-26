# Sislisten Repository

## Options for the location of new code ("sislisten") are as follows:
1. Place module in existing `sisbot` server. New endpoints will be added to `sisbot`.
2. Place new project (server) on pi.

## Pros and Cons of Approaches:
### 1. Place module in existing `sisbot` server. New endpoints will be added to `sisbot`.
#### Pros
* Easy to copy server-side code
* Server is already running - no major changes will have to be made to the startup process
* Placing code in `sisbot` server aligns with the existing theme of having the `sisbot` server be the sole interface to the table.

#### Cons
* Placing code in the `sisbot` server carries high risk. The `sis*` repos traditionally have been extremely difficult to run and set up.
* Placing code in the `sisbot` server communication from JS -> sockets -> python. This could get messy.
* If this approach is taken, the `sislisten` module will be coupled tightly to the `sisbot` repository, which will as a result couple it tightly to a raspberry pi.


### 2. Place new project (server) on pi.
#### Pros
* Can write server in any language, since client will not care. Easiest to use is python.
* This does not couple the server to a specific architecture.

#### Cons
* This will not comply with the existing methodology that all table manipulation be done through the `sisbot`.

## Evaluation:
2. Place new project (server) on pi.
   * Assume that eventually, `sisproxy` will start `sislisten`.
   * `sisproxy` will be built to run on any machine that can run python. It will not be architecture-bound to a raspberry pi.

https://msoe365-my.sharepoint.com/personal/wojciechowskia_msoe_edu/Documents/Microsoft%20Teams%20Chat%20Files/Architecture.PNG

# Updated Architecture 2021-03-09
![architecture](uploads/58da94527e83a97382e8d7db667018c4/architecture.png)


# Notes On Updated Architecture:
* Audio is collected in `sislisten` via a periodic task. This periodic task is kicked off by the `Scheduler` class, which is a wrapper on the native python `threading.timer()` task. 
* After `sislisten` collects audio (an `audio_stream`) then the audio is passed to a separate thread to be sent to the AI server and communicated back to the table. Eventually, translation capabilities involving user settings will be added to this. The tasks of calling the AI service with the audio sample, translating (in future) and communicating the color to the table are collectively known as the "pipeline." Pipelines are run by threads from a thread pool. The thread pool object is part of the native python implementation (`ThreadPoolExecutor`).
