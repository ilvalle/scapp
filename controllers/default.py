# -*- coding: utf-8 -*-
### required - do no delete

#def download(): return response.download(request,db)
#def call(): return service()
#def error(): return dict()
### end requires

def index():
	return redirect(URL(c='plugin_cs_monitor', f='index'))

def user(): 
	if not request.args(0) or request.args(0) in ['login']:
		response.view = 'default/%s.html' % request.args(0) or 'login'
	return dict(form=auth())
