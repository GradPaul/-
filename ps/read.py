# -*- coding: utf-8 -*-
import json
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
from bson import ObjectId


object_list=[]
course_dict={}

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
        new_teacher={}
        new_teacher["_id"]=ObjectId()
        new_teacher["department"]=obj["dept"]
        new_teacher["name"]= obj["name"]
        teacher_list.append(new_teacher)
        for comment in obj["comments"]:
            course=course_dict.get(comment["course"])
            if not course:
                new_course={}
                new_course["_id"]=ObjectId()
                new_course["teacher_id"]=new_teacher["_id"]
                new_course["name"]=comment["course"]
                new_course["department"]=obj["dept"]
                course_dict[comment["course"]]=new_course
                course=new_course
            new_comment={}
            new_comment["course_id"]=course["_id"]
            new_comment["content"]= comment["content"]
            new_comment["teacher_id"]= new_teacher["_id"]
            comment_list.append(new_comment)

course_list = [ course_dict[k] for k in course_dict ]
