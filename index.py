#-*-coding:utf-8 -*-
from inic.url import urls
from inic import setting
import web


#404错误
def notfound(): 
   render = setting.render_app
   return web.notfound(render.err(err=u'\u9875\u9762\u4e0d\u5b58\u5728'))

#500错误
def internalerror():
    render = setting.render_app
    return web.internalerror("Bad, bad server. No donut for you.") 

#session存储与设置
db=setting.db
#硬盘存储session = web.session.Session(app,web.session.DiskStore('sessions'))
#数据库存储

app = web.application(urls, globals())
    #app.internalerror = internalerror  
app.notfound = notfound
    #session = web.session.Session(app,web.session.DBStore(db, 'ii_sessions'),initializer={'user': 0})
    #session = web.session.Session(app,web.session.DiskStore('sessions'),initializer={'user': -1})
    #web.config._session = session
if web.config.get('_session') is None:
    global session
    session = web.session.Session(app, web.session.DiskStore('sessions'),initializer={'user': -1})
    web.config._session = session
else:
    session = web.config._session


if __name__ == "__main__":

    app.run()