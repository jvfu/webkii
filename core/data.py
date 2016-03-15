#-*-coding:utf-8 -*-
from inic import setting
from mode import mode
import json
import re
render = setting.render_cms
#def put_dict(name,id,num):    
def decide(name):
    lst =['menu','nav','menulist','category','setting','advert','weixin','recharge']
    if name in lst: 
        return True
    return False


#def get_menu():
def get_difference_data(name):
    return mode.get_all('ii_'+name)

def check_admin_data(user,pwd):
    return None
	
def put_dict(name,id,num):
    GetDictData = {'menu':get_difference_data,'nav':get_difference_data,'menulist':get_difference_data,'category':get_difference_data,'setting':get_difference_data,'advert':get_difference_data,'weixin':get_difference_data,'recharge':get_difference_data}
    return GetDictData[name](name)