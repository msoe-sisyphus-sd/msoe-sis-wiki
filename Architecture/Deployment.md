# Hardware for Table


# Deploying msoe-sislisten


# Deploying the AI Server
## Options
The team evaluated the following service providers for deployment platforms:
* AWS (Amazon Web Services)
* Google Cloud
* Azure Cloud
* Heroku
* Python Anywhere
* ROSIE (MSOE's Supercomputer)

## Pros and Cons

### AWS
Deploying to AWS went smoothly due to the extensive documentation available for AWS. The service was deployed on Andy's personal account and it was deployed using ElasticBeantalk

Endpoint was exposed on
`http://sisyphus-mood-lighting-ai-service-env.eba-pv7u2crr.us-east-2.elasticbeanstalk.com/get_mood_color_from_audio_stream`

Pros
* Easy setup
* Good performance

Cons
* Lots of pricing options and it's confusing
* A custom domain is needed in order to enable https

### Google Cloud
Gcloud setup was not terribly difficult due to extensive documentation. Service was deployed under Grace's person account for starting out, for free in keeping with Google's "Always Free" tier:
* https://cloud.google.com/free/docs/gcp-free-tier

Endpoint was exposed on 
`https://sisbot-ai-service.uc.r.appspot.com/get_mood_color_from_audio_stream`.

Pros:
* Easy setup
* Good monitoring
* Transparent pricing
* Https by default

Cons:
* Possibility of going over free tier limits may mean that a formal production would cost money
* Not nearly as fast as AWS

### Azure Cloud
Azure cloud has widespread report of poor availability:
https://status.azure.com/en-us/status/history/

In fact, the author had issues setting up the app to even try it out due to issues with azure's availability:
![image](uploads/f18fcd892b8cf2d658e0785cd44e82c0/image.png)

For this reason, we did not explore future avenues with Azure.

### Heroku
Heroku has a completely free tier and was our first deployment attempt.

Pros: Completely, absolutely free.

Cons: Apps in the free tier are put to sleep when not in use, and this wakeup time can cause first-in-awhile-requests to exceed 20 seconds.

Pros:
* Completely free
* Https by default

Cons:
* Falls asleep 
* Slower

### Python Anywhere
We could not deploy the server on PythonAnywhere. PythonAnywhere gives you a linux shell that you can use to deploy the server but with the free tier you are only limited to 512 MB of space on the server. As a result we could not install all of the pip dependencies needed for the AI service. As a result we choose not to explore PythonAnywhere further.

### ROSIE 
The team spoke with Gagan on 4/05/2021 about using ROSIE as a deployment platform. For longterm deployment, this project must get passed off to another MSOE team, as ROSIE is not defined for longtime development. Furthermore, if deployed on ROSIE, the endpoint will not be accessible from beyond campus.

For development purposes, the host is `h-mgmt3.hpc.msoe.edu`, and the team folder is located `/data/sdp/ratsm`. The conda environment set aside for the team is `ratsm-flask` and can be activated with `conda activate ratsm-flask`.

Note that as of 04/08/2021, there is an issue with ports not being accessible from outside of the management node. 

Pros:
-- TODO

Cons:
-- TODO

## Latency Results
![image](uploads/e27ebd35f3c7a5080a1756b520f7cbb2/image.png)

From the 3 services we were able to test, it appears that AWS is the fastest although this is probably due to the lack of TLS. 

Script for latency gathering:
````
from listener import call_mood_lighting_ai_service
import wave
import datetime
import requests

ai_service_gcloud = 'https://sisbot-ai-service.uc.r.appspot.com/get_mood_color_from_audio_stream'

ai_service_heroku = 'https://sisyphus-mood-lighting-server.herokuapp.com/get_mood_color_from_audio_stream'

ai_service_aws = 'http://sisyphus-mood-lighting-ai-service-env.eba-pv7u2crr.us-east-2.elasticbeanstalk.com/get_mood_color_from_audio_stream'
def audio_sample():
    with wave.open('test/count.wav', 'r') as audio_file:
        return audio_file.readframes(audio_file.getnframes())


def latency_for_service(ai_service):
    t = 0

    for i in range(0, 10):
        t_1 = datetime.datetime.now()

        request_headers = { 'Content-Type': 'application/octet-stream' }
        data = { 'audioSample': audio_sample() }
        response = requests.post(ai_service, headers=request_headers, data=data)
        t_2 = datetime.datetime.now()
        if response.status_code != requests.codes.ok:
            print(f'Error in sending AI request - code: {response.status_code}')
            print(response.text)
            return -1

        elapsed = t_2 - t_1
        t = t + elapsed.total_seconds()

    print(f'Average of ten calls: {t / 10.0}s')

print('Heroku time: ')
latency_for_service(ai_service_heroku)
print('Gcloud time: ')
latency_for_service(ai_service_gcloud)
print('AWS time:')
latency_for_service(ai_service_aws)
````

## Final Decision
#### TODO