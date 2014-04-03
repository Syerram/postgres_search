from django.db import models
from django.utils.translation import ugettext_lazy as _
from search import STUDENT_SEARCH_TABLE_NAME
from student.models import Student

class StudentFullTextSearch(models.Model):
    """
        Model (document) created syncronously. searchable document updated asyncronously.

        The manual migration adds a new field called "student_doc", which is of type "tsvector".
        This field type isn't supported by Django. We could create a custom field type but
            we will never going to use contents of "tsvector" directly.


        Options for async update:
        1. We can perform on "post_save" signal of User and StudentCourse [not really async]
        2. Create a management job that will update this model invoked by a cron.
            2.1 a better way would be adding an extra field like 'dirty' to the models, so the CRON will only update those
        3. Same as above but via django celery
        4. Use 3rd party message broker like AWS SQS, RabbitMQ etc. Highly scalable!

        We will do #3.

        """

    student = models.OneToOneField(Student, verbose_name = _('Student'))
    title = models.CharField(_('Entity'), max_length = 255, db_index = True)

    class Meta:
        db_table = STUDENT_SEARCH_TABLE_NAME

    def __unicode__(self):
        return self.title
