from gluon.scheduler import Scheduler
scheduler = Scheduler(db)

import urllib2

def rest_getParkingIds():
	base = 'http://ipchannels.integreen-life.bz.it/parkingFrontEnd'
	function = '/rest/getParkingIds'

	url = base + function
	request = urllib2.Request(url)
	data = urllib2.urlopen(request).read()
	
	return data

