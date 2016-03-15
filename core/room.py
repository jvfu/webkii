#-*-coding:utf-8 -*-

import web
import json
from inic import setting
from mode import mode
from common import dispose
import datetime
import time
import data
import os
#db = setting.db
pre= setting.prefix
render = setting.render_cms
Base = dispose.Base

'''
this is a cms main controller
'''

'''
information data cache
'''
class AdminBase(Base):
    def __init__(self):
        Base.__init__(self)
        

'''
cms login
'''
class Login(AdminBase):
    def __init__(self):
        AdminBase.__init__(self)      
      
    def GET(self):
        
        return render.login(msg=self)

    def POST(self):
        args = web.input()
        username = web.net.websafe(args.username)
        password = web.net.websafe(args.password)
        if username=='': return render.err(msg= '用户名不能为空')
        if password=='': return render.err(msg= u'\u5bc6\u7801\u9519\u8bef')
        getAdmin= mode.get_admin_info(username)
        if getAdmin is None: return render.err(msg= u'\u7528\u6237\u4e0d\u5b58\u5728')
        adminInfo=getAdmin[0]
        if password==adminInfo.password: 
            web.setcookie(setting.config.cookie_secure,username, 7200)
            web.config._session= {'u':username,'uid':adminInfo.uid,'type':adminInfo.type}
            return render.success(msg= u'\u767b\u9646\u6210\u529f',url="/admin/login")
        else:
            render.err(msg= u'\u5bc6\u7801\u9519\u8bef')
'''
cms center index(homepage)
'''			
class Index(AdminBase):
    def __init__(self):
        AdminBase.__init__(self)
        self.vali_login()

    def GET(self):
        self.li=self.get_list(mode.get_by_id(0,pre+'menu'))
        return render.index(page=self)

'''
menu control center 信息（栏目）调度
'''
class Menu(AdminBase):
    def __init__(self):
        AdminBase.__init__(self)
        self.vali_login()

    def GET(self,type,id,num):
        if num=='' or int(num) == 0 :num=1
        if id=='': render.err(msg= '数据错误')
		
        GetStatus=data.decide(type)

        if GetStatus is False: return render.err(msg= '数据错误')

        if type=="menulist":
            count = mode.get_count(pre+'info')[0]
            self.pagebar = self.pages(count.id,int(num),10)
            num =(int(num) - 1) * 10
            n= self.get_list(mode.get_pagelist(pre+'info',10,num))
            self.lt = self.get_list(mode.get_all(pre+'category'))
        else:
            n = self.get_list(data.put_dict(type,id,num))

        print n
        self.id=id
        self.li=n
        self.type =type
        self.list =self.get_list(mode.get_by_id(int(id),pre+'menu'))
        return render.menu(page=self)

'''
advertisement 广告
'''

class Advert(AdminBase):
    def __init__(self):
        AdminBase.__init__(self)
        self.vali_login()
		
    def GET(self):
        return render.menulist()

    def POST(self):
        x = web.input(file={})

        homedir = os.getcwd()
        filedir = '%s/static/upload/img' % homedir
        if 'file' in x:
            filepath=x.file.filename.replace('\\','/')
            filename=filepath.split('/')[-1]
            path = str(self.date_now_other("%Y%m%d%H%M%S"))+'.jpg'
            fout = file(filedir +'/'+ path,'wb')
            fout.write(x.file.file.read())
            fout.close()
        web.header('Content-Type', 'application/json')		
        return  json.dumps({'url':path,"error":1})
		

class Addlist:
    def __init__(self):
        AdminBase.__init__(self)
        self.vali_login()

    def GET(self):
        return render.addlist()

class Artlist:
    def __init__(self):
        AdminBase.__init__(self)
        self.vali_login()
    def GET(self):
        return render.artlist()

class Addart:
    def __init__(self):
        AdminBase.__init__(self)
        self.vali_login()
    def GET(self):
        return render.addart()
		
class Menber:
    def __init__(self):
        AdminBase.__init__(self)
        self.vali_login()
    def GET(self):
        return render.admin_menber()
		
class Tain:
    def __init__(self):
        AdminBase.__init__(self)
        self.vali_login()
    def GET(self):
        return render.tain()
    def POST(self):
        return render.tain()
		
class System(AdminBase):
    def __init__(self):
        AdminBase.__init__(self)
        self.vali_login()

    def GET(self):
        return self.client('REMOTE_ADDR')+self.client('REQUEST_URI')
        return render.system()

'''
infomation editor 信息编辑
'''
class Editor(AdminBase):
    def __init__(self):
        AdminBase.__init__(self)
        self.vali_login()

    def GET(self,type):
        return render.err(msg= u'\u7528\u6237\u4e0d\u5b58\u5728')

    def POST(self):
        self.vali_login()
        args = web.input()
        if args.typec=="nav":
            put= mode.put_nav('ii_'+args.typec,args)
            if put is not None:
                 dict={}
                 dict['msg']=u'\u5df2\u5b8c\u6210'
                 return json.dumps(dict)

        if args.typec=="menu":
            put= mode.put_menu('ii_'+args.typec,args)
            if put is not None:
                 dict={}
                 dict['msg']=u'\u5df2\u5b8c\u6210'
                 return json.dumps(dict)

        if args.typec=="menulist":
            args['writer']=self.get_login().get('name')
            args['add_time']=int(time.time())
            put= mode.put_art("ii_info",args)
            if put is not None:
                 dict={}
                 dict['msg']=u'\u5df2\u5b8c\u6210'
                 return json.dumps(dict)
				 
        if args.typec=="category":
            args['add_time']=int(time.time())
            put= mode.put_cagte("ii_"+args.typec,args)
            if put is not None:
                 dict={}
                 dict['msg']=u'\u5df2\u5b8c\u6210'
                 return json.dumps(dict)
        if args.typec=="advert":
            args['add_time']=int(time.time())
            put= mode.put_advert("ii_"+args.typec,args)
            if put is not None:
                 dict={}
                 dict['msg']=u'\u5df2\u5b8c\u6210'
                 return json.dumps(dict)
				 
'''
infomation update 信息更新
'''
class Record(AdminBase):
    def __init__(self):
        AdminBase.__init__(self)
        self.vali_login()

    def GET(self,type,id):
        if type == "menulist":
            data=self.get_list(mode.get_only_data(int(id),"ii_info"))[0]
        if type == "nav":
            data=self.get_list(mode.get_only_data(int(id),"ii_"+type))[0]
        if type == "menu":
            data=self.get_list(mode.get_only_data(int(id),"ii_"+type))[0]
        if type == "category":
            data=self.get_list(mode.get_only_data(int(id),"ii_"+type))[0]
        self.id=int(id)
        self.type=type
        self.data=data
        return render.record(page=self)

    def POST(self,type,id):
        args= web.input()
        print args
        if type == "menulist":
            PutInDb= mode.updata_info(int(id),args,"ii_info")
        if type == "nav":
            PutInDb= mode.updata_nav(int(id),args,"nav")
        if type == "menu":
            PutInDb= mode.updata_menu(int(id),args,"ii_menu")
        if type == "category":
            PutInDb= mode.updata_category(int(id),args,"ii_category")
        if PutInDb is None:return render.err(err= u'\u7528\u6237\u4e0d\u5b58\u5728')

        dict={}
        dict['msg']=u'\u5df2\u5b8c\u6210'
        return json.dumps(dict)


'''
infomation deleter 信息删除
'''
class Deleter(AdminBase):
    def __init__(self):
        AdminBase.__init__(self)
        self.vali_login()
    def GET(self):
        return 0
    def POST(self):
        id= web.input().get('id')
        name= web.input().get('name')
        if id ==0: return  json.dumps(status=2)
        if name == '': return json.dumps(status=2)
        grs= mode.del_all(id,pre+name)
        if grs is not None:
            dict={}
            dict['msg']=u'\u5df2\u5220\u9664'
            return json.dumps(dict)
 

class Tag(AdminBase):
    def __init__(self):
        AdminBase.__init__(self)
        self.vali_login()
    def GET(self):
        import sys, urllib, urllib2, json
        url = 'http://apis.baidu.com/baidu_communication/sms_verification_code/smsverifycode?phone=15308628980&content=1234'
        req = urllib2.Request(url)
        req.add_header('apikey','48afdcf75954f7f6f52cdb4685be03ef')
        res = urllib2.urlopen(req)
        con =res.read()
        return json.dumps(con)

'''
total data　统计数据
'''
class Total(AdminBase):
    def __init__(self):
        AdminBase.__init__(self)
        self.vali_login()
    def GET(self):
        se = web.config.get("_session")
        if se.get('type') > 0:
            Cokie = web.cookies().get(setting.config.cookie_secure)
            if not Cokie is None:
                return  render.total()
        raise web.seeother("/admin/")


'''
logout 退出
'''	
class Loges(AdminBase):
    def __init__(self):
        AdminBase.__init__(self)
        self.vali_login()
    def GET(self):
        web.config._session= {'u': '','type':False}
        web.config._session.clear()
        raise web.seeother("/admin/")
		
		
'''
>>> import tqdm
>>> form tqdm import *
  File "<stdin>", line 1
    form tqdm import *
            ^
SyntaxError: invalid syntax
>>> from tqdm import *
>>> import time
>>> for  i in tqdm(range(1000)):
...     time.sleep(.01)
...

import time 
import requests
from tomorrow import threads
@threads(5)
def download(url):
	return requests.get(url)

if __name__ ==="__main__":
	start =time.time()
	responses =[download(url) for url in urls]
	html = [response.text for response in responses]
	end  = tiem.time()
	print "Time %f secconds" % (end - start)

'''