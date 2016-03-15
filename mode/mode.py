#-*-coding:utf-8 -*-
import web, datetime, time
from inic import setting
db = setting.db

def get_by_id(id,tb,ext=0,order='id asc'):
    try:
        return db.select(tb, where='parentid=$id', order = order,vars=locals())
    except IndexError:
        return None

def get_only_data(id,tb):
    try:
        return db.select(tb, where='id=$id',vars=locals())
    except IndexError:
        return None

def get_all(tb,order='id asc'):
    try:
        return db.select(tb,order = order,vars=locals())
    except IndexError:
        return None
		
#login
def get_admin_info(name):
    try:
        return db.select("ii_admin",where="username=$name",vars=locals())
    except IndexError:
        return None
#nav
def put_nav(tb,arg):
    try:
        return db.insert(tb,fid=arg.fid,link=arg.link,nav_name=arg.nav_name)
    except IndexError:
        return None
#menu
def put_menu(tb,arg):
    try:
        return db.insert(tb,parentid=arg.parentid,action=arg.link,add_action=arg.link,name=arg.name)
    except IndexError:
        return None
#art
def put_art(tb,arg):
    try:
        return db.insert(tb,title=arg.title,cat_id=arg.parentid,content=arg.content,writer=arg.writer,add_time=time.mktime(datetime.datetime.now().timetuple()))
    except IndexError:
        return None
#cagtegory
def put_cagte(tb,arg):
    try:
        return db.insert(tb,parent_id=arg.parentid,url=arg.link,cate_name=arg.name,content=arg.content,cate_type=arg.parentid,is_show=arg.display,add_time=arg.add_time)
    except IndexError:
        return None

def put_advert(tb,arg):
    try:
        return db.insert(tb,title=arg.title,add_time=arg.add_time,start_time=arg.start_time,end_time=arg.end_time,ad_type=arg.display)
    except IndexError:
        return None

#page
#get count 
def get_count(tb):
    try:
        return db.select(tb, what="count(id) as id")
    except IndexError:
        return None
#page
#get pagelist
def get_pagelist(tb,size=10,num=0,order="id desc"):
    try:
        return db.select(tb,order=order,limit="$num, $size", vars=locals())
    except IndexError:
        return None
		
#info
def get_info(id):
    try:
        return db.select('ii_info',where="id=$id",vars=locals())[0]
    except IndexError:
        return None
#delet  info 
def del_info(id):
    try:
        return db.delete('ii_info', where="id=$id",vars=locals())
    except IndexError:
        return None

		
#updata info 
def updata_info(id,arg,tb='ii_info'):
    try:
        return db.update(tb, where="id=$id", title=arg.title,content=arg.content,writer=arg.writer,add_time=time.mktime(datetime.  datetime.now().timetuple()),vars=locals())
    except IndexError:
        return None

def updata_nav(id,arg,tb='ii_nav'):
    try:
        return db.update(tb, where="id=$id", fid=arg.fid,nav_name=arg.nav_name,link=arg.link,display=arg.display,bank=arg.bank,vars=locals())
    except IndexError:
        return None
#delet  all 
def del_all(id,tb):
    try:
        return db.delete(tb, where="id=$id",vars=locals())
    except IndexError:
        return None
