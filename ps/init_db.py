from model import *
from read import *
from mongoengine import *

connect('gdp')
for t in teacher_list:
    Teachers(teacher_id=t["id"],dep=t["dept"],name=t["name"]).save()

course=set()
for co in course_list:
    if not co["c_id"] in course:
        course.add(co["c_id"])
        Courses(name=co["name"],credit=2,course_id=co["c_id"],teacher=co["teacher"],department =co["dep"]).save()

for com in comment_list:
    Comments(content_id=com["course"],content=com["content"],teacher_id=com["teacher_id"],
            student_id="1",course_id=com["c_id"]).save()
