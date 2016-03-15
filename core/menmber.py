#-*-coding:utf-8 -*-
import web
import json
import os
from inic import setting
from web import form
from datetime import datetime
from inic import setting

render = setting.render_menmber
db = setting.db

class Index:
    def GET(self):
        config=setting.config
        return render.index(config=config)

class Login:
    def GET(self):
        return render.login()
		
    def POST(self):
        ue =setting.prefix + 'user'
        args = web.input(username="", password="")
        
        for i in db.select(ue):
            if i.username == args.username:
                if i.password == args.password:
                    web.setcookie('username', i.username, 3600)
                    web.config._session= {'u':args.username,'type':True}
                    raise web.seeother("/menmber/center")

        raise web.seeother("/menmber/login")
		
