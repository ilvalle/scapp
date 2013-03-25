# -*- coding: utf-8 -*-

#########################################################################
## This scaffolding model makes your app work on Google App Engine too
## File is released under public domain and you can use without limitations
#########################################################################

## if SSL/HTTPS is properly configured and you want all HTTP requests to
## be redirected to HTTPS, uncomment the line below:
# request.requires_https()

db = DAL('sqlite://storage.sqlite',pool_size=1,check_reserved=['all'])

# response.optimize_css = 'concat,minify,inline'
# response.optimize_js = 'concat,minify,inline'

from gluon.tools import Auth, Service, PluginManager, prettydate
auth = Auth(db)
service, plugins = Service(), PluginManager()

## create all tables needed by auth if not custom tables
auth.define_tables(username=False, signature=False)

## configure email
mail = auth.settings.mailer
mail.settings.server = 'smtp.digital.tis.bz.it:25'
#mail.settings.sender = 'you@gmail.com'
#mail.settings.login = 'username:password'

## configure auth policy
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True
auth.settings.actions_disabled.append('register')

db.auth_user.email.widget = lambda f,v: SQLFORM.widgets.string.widget(f, v,_placeholder=T('Email'), _class="input-block-level")
db.auth_user.password.widget = lambda f,v: SQLFORM.widgets.string.widget(f, v, _placeholder=T('Password'), _class="input-block-level", _type="password")
