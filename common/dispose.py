#-*-coding:utf-8 -*-
import web
import os
import json
from mode import mode
from inic import setting
import datetime
import time
import sys
reload(sys)
sys.setdefaultencoding('utf8')
prefix = 'ii_'

class Base:
    def __init__(self):
        self._conf=setting.config
        #self.vali_login()

    def get_list(self,list):
        if list is None:return render.err(msg= u'\u7528\u6237\u4e0d\u5b58\u5728')
        return [i for i in list]

    def datestr(self,date):
        return web.datestr(date)

    def datefmt(self,times):
        times = time.localtime(times)
        return time.strftime("%Y-%m-%d %H:%M:%S",times)
    
    def datenow(self, fmt="%Y-%m-%d %H:%M:%S"):
        return datetime.datetime.strftime(datetime.datetime.now(), fmt)
		
    def date_now_other(self, fmt="%Y-%m-%d %H:%M:%S"):
        return datetime.datetime.strftime(datetime.datetime.now(), fmt)

    def client(self,type='REQUEST_URI',url='htt://kii.com'):
        return web.ctx.env.get(type,url)

    def pages(self,total,num,per,path="/admin/menu/menulist/20/"):
        self.total = total
        self.per = per
        self.url = path
        self.next=num + 1
        self.pro =num - 1
        print self.pro
        limit=""
        nums =0
        if self.total%self.per ==0:
            pages = self.total/self.per
        else:
            pages = self.total/self.per + 1

        if num < 3:   
            for n in range(1,num+3):
                if n is not num:
                    limit +="<a href="+self.url+"%d" % (n)+">"+"%d" % (n)+"</a>"
                else:
                    limit +="<span class='current'>"+"%d" % (n)+"</span>"
        elif num < pages:
            for n in range(num-2,num+2):
                if n is not num:
                    limit +="<a href="+self.url+"%d" % (n)+">"+"%d" % (n)+"</a>"
                else:
                    limit +="<span class='current'>"+"%d" % (n)+"</span>"
        else:
            for n in range(num-3,num+1):
                if n is not num:
                    limit +="<a href="+self.url+"%d" % (n)+">"+"%d" % (n)+"</a>"
                else:
                    limit +="<span class='current'>"+"%d" % (n)+"</span>"
        if self.next >pages:
            self.next =num
        if self.pro ==0:
            self.pro =num
        return  "%d" % (total)+"条记录"+"%d/%d" % (num,pages) + "页&nbsp;&nbsp;" +"<a href="+self.url+"%d" % (self.next)+">下一页</a>" +limit+"<a href="+self.url+"%d" % (self.pro)+">上一页</a>"+"<a href="+self.url+"1>首页</a>"+"<a href="+self.url+"%d" % (pages)+">尾页</a>"
    def upload(self,args,home_dir):
        self.filedir = '%s/static/upload/ad/' % home_dir
                
    #获取栏目名
    ''''
	def getcategoryName(self,id,tb="ii_category"):
        arg = self.get_list(mode.get_only_data(int(id),tb))		
        return arg[0].cate_name
    '''

    def datacsv(self):
        import csv
        pass

    def datapdf(self):
        pass
	
    def dataword(self):
        pass

    def get_login(self):
        session =web.config.get("_session")
        return {'name':session.get('u'),'uid':session.get('uid'),'type':session.get('type')}

    def vali_login(self):
        login_user = self.get_login()
        if login_user.get('uid') is None:
            session =web.config.get("_session")
            return web.seeother('/admin/')
        else:
            print 'ok'
    def put_msg(self):
        return web.seeother('/admin/login')	

	

class Index:
    def GET(self):
        id = web.input(num="",type="")
        list=[]
        pyDict = mode.get_by_id(id.num, prefix+id.type)
        if not pyDict:
            web.header('Content-Type', 'application/json')
            return json.dumps({u'error':u'404'})
        for i in pyDict:
            list.append(i)
        web.header('Content-Type', 'application/json')
        return json.dumps(list)

class Static:
    def GET(self,file):
        web.seeother('/static/'+file);


