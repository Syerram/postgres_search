from course.models import University, Course
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

class Student(models.Model):
    university = models.ForeignKey(University)
    user = models.OneToOneField(User)
    active = models.BooleanField(_('Active'), default = True)

    class Meta:
        verbose_name_plural = 'Students'

    def __unicode__(self):
        return self.user.first_name

class StudentCourse(models.Model):
    student = models.ForeignKey(Student)
    course = models.ForeignKey(Course)

    class Meta:
        unique_together = (('student', 'course'),)
        verbose_name_plural = 'Student Courses'

    def __unicode__(self):
        return '%s.%s' % (self.student.user.first_name, self.course.name)

    def save(self, force_insert = False, force_update = False, using = None, update_fields = None):
        """
        Intecepts save and creates a task for updating student info
        """
        from search.tasks import update_student_info
        super(StudentCourse, self).save(force_insert = force_insert,
                                        force_update = force_update, using = using,
                                        update_fields = update_fields)
        update_student_info.delay(self)
