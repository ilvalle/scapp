# -*- coding: utf-8 -*-
### required - do no delete
def user(): return dict(form=auth())
def download(): return response.download(request,db)
def call(): return service()
### end requires

def index():
	return redirect(URL(c='plugin_cs_monitor', f='index'))

def login():
	return response.render('default/login.html', form=auth.login())

def register():
	return  

def error():
    return dict()

def add_task():
	scheduler.queue_task(test_rest,repeats=0, period=10)
	return 'ciao'

import urllib2

def test_rest():
	base = 'http://ipchannels.integreen-life.bz.it/parkingFrontEnd'
	function = '/rest/parking-ids'

	url = base + function

	request = urllib2.Request(url)
	data = urllib2.urlopen(request).read()

	return data

