
from mongoengine import *
import datetime



class Teachers(Document):

    teacher_id=StringField()
    name = StringField()
    department= StringField()
    ctime=DateTimeField(default=datetime.datetime.now)


class Courses(Document):
    # obj_id = ObjectIdField()
    course_id=StringField()
    credit=IntField()
    name = StringField()
    department = StringField()
    teacher = StringField()
    ctime=DateTimeField(default=datetime.datetime.now)

class Comments(Document):
    content_id=StringField()
    student_id=StringField()
    course_id=StringField()
    teacher_id=StringField()
    content = StringField()
    ctime=DateTimeField(default=datetime.datetime.now)
