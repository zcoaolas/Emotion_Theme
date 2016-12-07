from Emotion import *
from ChangeTheme import *
from Camera import *

import requests
from os.path import join, abspath

#import leancloud

requests.utils.DEFAULT_CA_BUNDLE_PATH = join(abspath('.'), 'cacert.pem')

if __name__ == "__main__":

    #leancloud.init("9k55DgHBy3vlUcADfgsuOFGb-gzGzoHsz", "AkNIdMmXRftH2jmCkouYlaiW")

    capture()
    e = identify()

    print("Your emotion is " + e + "\n")
    if e != '':
        change_theme(e)
    else:
        print('Sorry, cannot identify you.')
