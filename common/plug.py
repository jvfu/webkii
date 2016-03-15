#-*-coding:utf-8 -*-
import web
import json
import os

class fun:
   def __init__(self):
       self.list =['menu','nav','menulist','setting','category','addlist','alter']
       self.dict ={}
   def fun_iterates(self,type):
       if self.iterates(type):

       else:
           self.dict['msg']=u'\u5df2\u5b8c\u6210'
           return json.dumps(dict)

   def iterates(self,type):
       for i in self.list:
           if type == i:
               return True
       return False
