
'''
Created on Apr 3, 2014

@author: syerram
'''
from course.models import Course, University
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError
from search.tasks import update_student_info
from student.models import Student, StudentCourse
import xml.etree.cElementTree as etree

class Command(BaseCommand):
    help = 'Upload Searchable data'

    def handle(self, *args, **options):

        university, created = University.objects.get_or_create(name = 'NYU')

        (python, created,) = Course.objects.get_or_create(code = 'py', university = university, name = 'Python')
        (java, created,) = Course.objects.get_or_create(code = 'java', university = university, name = 'Java')
        (go, created,) = Course.objects.get_or_create(code = 'go', university = university, name = 'Go')

        idx = 1
        with open(args[0], 'r') as f:
            context = etree.iterparse(f)
            for (event, element,) in context:
                if element.tag == 'row':
                    name = element.attrib['DisplayName']
                    _id = int(element.attrib['Id'])
                    course = python
                    if _id > 5000:
                        course = java
                    elif _id > 15000:
                        course = go
                    elif _id > 15000:
                        break
                    if ' ' in name:
                        idx += 1
                        names = name.strip().split(' ')
                        first_name = names[0]
                        last_name = names[(len(names) - 1)]
                        username = name.lower().replace(' ', '')[:30]
                        try:
                            user = User.objects.create(username = username, first_name = first_name, last_name = last_name)
                            student = Student.objects.create(user = user, university = university)
                            student_course = StudentCourse.objects.create(student = student, course = course)
                            update_student_info(student_course)
                        except IntegrityError:
                            continue

        print '*****',
        print 'total users %d' % idx
