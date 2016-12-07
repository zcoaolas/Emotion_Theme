# coding: utf-8

#from __future__ import print_function
import time
import requests
import os.path
import threading
from requests.packages.urllib3.exceptions import InsecureRequestWarning
#import leancloud

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


_url = 'https://api.projectoxford.ai/emotion/v1.0/recognize'
_key = '5d46bf2e939c466e9a32a0355a2da5ae'
_maxNumRetries = 10


emotions = []


def processRequest(json, data, headers, params):

    retries = 0
    result = None

    while True:

        response = requests.request('post', _url, json=json, data=data, headers=headers, params=params, verify=False)

        if response.status_code == 429:

            print("Message: %s" % (response.json()['error']['message']))

            if retries <= _maxNumRetries:
                time.sleep(1)
                retries += 1
                continue
            else:
                print('Error: failed after retrying!')
                break

        elif response.status_code == 200 or response.status_code == 201:
            if 'content-length' in response.headers and int(response.headers['content-length']) == 0:
                result = None
            elif 'content-type' in response.headers and isinstance(response.headers['content-type'], str):
                if 'application/json' in response.headers['content-type'].lower():
                    result = response.json() if response.content else None
                elif 'image' in response.headers['content-type'].lower():
                    result = response.content

        else:
            print("Error code: %d" % (response.status_code))
            print("Message: %s" % (response.json()['error']['message']))

        break

    if len(result) >= 1:
        print(result[0])
        '''
        class toSave(leancloud.Object):
            pass

        tosave = toSave()
        tosave.set("emotionInfo", result[0])
        tosave.save()
        '''
        # Load the original image from disk
        faceScores = result[0]['scores']
        topScore = 0.0
        emotion = ''
        for (typ, sco) in faceScores.items():
            if sco > topScore:
                emotion = typ
                topScore = sco
        emotions.append(emotion)

    return


# Detect faces from an image stored on disk

# Load raw image file into memory


def identify():
    pool = []
    for i in range(3):
        pathToFileInDisk = r'face' + str(i) + '.jpg'
        with open(pathToFileInDisk, 'rb') as f:
            data = f.read()

        headers = dict()
        headers['Ocp-Apim-Subscription-Key'] = _key
        headers['Content-Type'] = 'application/octet-stream'

        json = None
        params = None

        #result =processRequest(json, data, headers, params)
        os.unlink('face' + str(i) + '.jpg')

        th = threading.Thread(target=processRequest, args=(json, data, headers, params))
        pool.append(th)

        #for th in pool:
        th.start()

    for th in pool:
        th.join()

    print("\nResults:")
    print(emotions)
    if len(emotions) == 3:
        if emotions[0] == emotions[1]:
            return emotions[0]
        else:
            return emotions[2]

    elif len(emotions) == 2:
        if emotions[0] == emotions[1]:
            return emotions[1]

    return ''
