#-*-coding:utf-8 -*-
import web
import os
from web.contrib.template import render_mako

db = web.database(host="127.0.0.1",dbn="mysql",db='kiidb',user="root",pw="123456")

prefix = 'ii_'

render_app= render_mako(
        directories=["templates/app"],
        input_encoding='utf-8',
        output_encoding='utf-8'
)

render_cms= render_mako(
        directories=["templates/cms"],
        input_encoding='utf-8',
        output_encoding='utf-8'
)

render_ber= render_mako(
        directories=["templates/menmber"],
        #input_encoding='utf-8',
        output_encoding='utf-8'
)

render_status = render_mako(
        directories=["templates/sus"],
        #input_encoding='utf-8',
        output_encoding='utf-8'
)

render_init= render_mako(
        directories=["/"],
        input_encoding='utf-8',
        output_encoding='utf-8'
)

config = web.storage(
    email='T-KIRIN@QQ.COM',
    site_name = u'm72s.com',
    site_desc = 'cms',
    static = '/static',
	##cookie键值
    cookie_secure = "61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o"
)
#web.template.Template.globals['config'] = config
#web.template.Template.globals['render'] = render
#render = web.template.render('templates/', cache=False)
#web.header("Content-Type","text/csv;charset=utf-8")
#session设置
web.config.debug = True
web.config.session_parameters['cookie_name']='webpy_session_id'
web.config.session_parameters['cookie_domain'] = 'http://m72s.com'
web.config.session_parameters['timeout'] =7200
web.config.session_parameters['ignore_expiry'] = False
web.config.session_parameters['ignore_change_ip'] = False
#web.config.session_parameters['secret_key'] = 'fLjUfxqXtfNoIldA0A0J'
web.config.session_parameters['expired_message'] = 'Session expired'
