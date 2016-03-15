#-*-coding:utf-8 -*-
import web
import json
import os
from inic import setting
from web import form
from datetime import datetime


render = setting.render_cms

class Upload:
    def GET(self):
        return '1321'

    def POST(self):
        x = web.input(imgFile={})
        homedir = os.getcwd()
        filedir = '%s/static/upload/img' %homedir
        if 'imgFile' in x:
            filepath=x.imgFile.filename.replace('\\','/')
            filename=filepath.split('/')[-1]
            fout = file(filedir +'/'+ filename,'wb')
            fout.write(x.imgFile.file.read())
            fout.close()
        web.header('Content-Type', 'application/json')		
        return  json.dumps({'url':'/static/upload/img/'+filename,"error":0})