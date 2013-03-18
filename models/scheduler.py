from gluon.scheduler import Scheduler
scheduler = Scheduler(db)

import urllib2

def test_rest():
	base = 'http://ipchannels.integreen-life.bz.it/parkingFrontEnd'
	function = '/rest/parking-ids'

	url = base + function
	request = urllib2.Request(url)
	data = urllib2.urlopen(request).read()
	
	return data


def test_rest2():
	semantic_error = a + b	
	return data
