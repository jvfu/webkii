#-*-coding:utf-8 -*-
import web
#import json
from inic import setting
import time
from mode import mode
#from web import form
#from datetime import datetime

render = setting.render_app

class Index:
     def GET(self):
         return render.index()    
class Cash:
     def GET(self):
         data= {
             "version":1.2,
             "oid_partner":"201501291000196502",
             "sign_type":'MD5',
             "userreq_ip":'',
             "id_type":0,
             "valid_order":"10080",#10080∑÷÷”
             "user_id":1,
             "timestamp":time.strftime("%Y%m%d%H%M%S"),
             "busi_partner":'101001',
             "no_order":time.strftime("%Y%m%d%H%M%S"),
             "dt_order":time.strftime("%Y%m%d%H%M%S"),           
             "name_goods":u'\u5e73\u53f0\u8d26\u6237\u5145\u503c',
             "info_order":u'\u5e73\u53f0\u8d26\u6237\u5145\u503c',
             "money_order":0.1,
             "notify_url":"http://baidu.com",
             "url_return":"http://baidu.com",
			 "risk_item":{"frms_ware_category":"2009","user_info_mercht_userno":"123456","user_info_dt_register":"20141015165530","user_info_full_name":"zhangsan","user_info_id_no":"3306821990012121221","user_info_identify_type":"1","user_info_identify_state":"1"}
             }
         res = create("https://yintong.com.cn/payment/bankgateway.htm",data)
         return res

class Infolist():
    def GET(self):
        return render.info()

class Info():
    def GET(self,id):
        if id==0: return render.err(err=u'\u9875\u9762\u4e0d\u5b58\u5728')
        content= mode.get_info(id)
        if content is None:return render.err(err=u'\u9875\u9762\u4e0d\u5b58\u5728')
        return render.info(content=content)

def post(url, data): 
    import urllib 
    import urllib2
    req = urllib2.Request(url) 
    data = urllib.urlencode(data) 
    #enable cookie 
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor()) 
    response = opener.open(req, data) 
    return response.read()
	
def create(url, data, charset='utf-8'):
    winput=''
    for key in data:
        winput +='<input type="hidden"  id="'+str(key)+'" name="'+str(key)+'" value=\''+str(data[key])+'\'/>'
    whead='<meta http-equiv="Content-Type" content="text/html; charset=utf-8" /><title>'+u'\u8bf7\u4e0d\u8981\u5173\u95ed\u9875\u9762,\u652f\u4ed8\u8df3\u8f6c\u4e2d'+'.....</title>'
    wform='<form action="'+url+'" name="pay" id="pay" method="POST" accept-charset="'+charset+'" onsubmit="document.charset=\''+charset+'\';">'+winput+'</form>'
    wscript='<script type="text/javascript">document.getElementById("pay").submit();</script>'
    whtml=whead+wform+wscript
    return whtml
