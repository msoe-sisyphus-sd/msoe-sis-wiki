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
