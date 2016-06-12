# -*- coding: utf-8 -*-
import json
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
import hashlib


object_list=[]
course_list=[]

teacher_list=[]
comment_list=[]

for i in range(4):
    of=open("ps_"+str(i+1)+".txt")
    for line in of.readlines():
        try:
            obj=json.loads(line)
            object_list.append(obj)
        except BaseException:
            pass

    of.close()

for obj in object_list:
    length=len(obj["comments"])
    if length>0:
        new_obj={}
        new_obj["dept"]=obj["dept"]
        new_obj["name"]= obj["name"]
        new_obj["id"]=obj["url"][-6:]
        teacher_list.append(new_obj)
        for com in obj["comments"]:
            new_com={}
            new_com["course"]=com["course"]
            new_com["content"]= com["content"]
            new_com["teacher_id"]= new_obj["id"]
            new_com["c_id"]=hashlib.md5(com["content"]).hexdigest()
            comment_list.append(new_com)
            if com["course"]:
                new_co={}
                new_co["teacher"]=new_obj["id"]
                new_co["name"]=com["course"]
                new_co["c_id"]=hashlib.md5(com["course"]).hexdigest()
                new_co["dep"]=obj["dept"]
                course_list.append(new_co)
