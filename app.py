from __future__ import print_function
import time
import os
import sys
import logging
import pychromecast
import pychromecast.controllers.dashcast as dashcast
from flask import Flask, url_for, request

app = Flask(__name__)
chromecasts = pychromecast.get_chromecasts()

@app.route('/')
def api_root():
    return 'Welcome'

@app.route('/hello')
def hello():
    return 'hello world'

@app.route('/show-url')
def showShares():
    if 'password' not in request.args:
        return 'Bad Request'
    
    if 'chromecast' not in request.args:
        return 'Bad Request'
    
    if 'url' not in request.args:
        return 'Bad Request'

    argPassword = request.args['password']
    argChromecast = request.args['chromecast']
    argUrl = request.args['url']

    if argPassword != "<replace before running>":
        return 'Bad Request'

    cast = next(cc for cc in chromecasts if cc.device.friendly_name == argChromecast)
    cast.wait()
    d = dashcast.DashCastController()
    cast.register_handler(d)

    if cast.is_idle == False:
        return 'Chromecast in use - aborting'

    if cast.app_id != '84912283':
        d.launch()

    d.load_url(argUrl)

    return 'Success'

if __name__ == '__main__':
    app.run()