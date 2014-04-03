'''
Created on Apr 3, 2014

@author: syerram
'''
from __future__ import absolute_import
from celery import shared_task
from django.db import connection, transaction
from postgres_search.views import get_object_or_None
from search import STUDENT_SEARCH_TABLE_NAME, STUDENT_SEARCH_TSV_COL_NAME
from search.models import StudentFullTextSearch

@shared_task(ignore_result = True)
@transaction.commit_on_success
def update_student_info(student_course):
    """
        This is a contrived example that insert/updates the search table for all rows in StudentCourse.
        We will use raw SQL execution since tsvector, AFAIK, has no bindings in python/django yet.

        Note: You can use the same task to submit the document to ElasticSearch, AWS CloudSearch,
            Lucence Index etc.
            Also, it can be called from User.save(.. . The method will need to take into account differnet models

        Ranking:
            You can boost results by weighting searchable columns and rank those results by multiplying with a factor.
            Example. Assume, we store 'reputation' along with 'title' in StudentFullTextSearch. Reputation is simply a numeric
                number and higher value indicates a better student.
                The goal is to boost students with high reputation on the top.
                1. You can use set_weight(to_tsvector('english', student_course.user.first_name), 'A') || ..
                2. When searching you can 'order by ts_rank(title, to_tsquery(search_term)) * reputation DESC' which will return all
                    students with mactching names but ordered by their reputation

        """
    cursor = connection.cursor()
    stud_document = [student_course.student.user.first_name, student_course.student.user.last_name, student_course.course.name]
    stud_doc_db = get_object_or_None(StudentFullTextSearch, student_id = student_course.student_id)
    if stud_doc_db:
        title = '%s, %s' % (stud_doc_db.title, student_course.course.name)
        sql = """UPDATE {table_name}
                    SET {column_name} = to_tsvector('english', COALESCE(%s,'')),
                    title = %s
                WHERE student_id=%s""".format(table_name = STUDENT_SEARCH_TABLE_NAME, column_name = STUDENT_SEARCH_TSV_COL_NAME)

        cursor.execute(sql, [' '.join(stud_document), title, student_course.student.id])
    else:
        title = '%s %s enrolled %s' % tuple(stud_document)
        sql = """INSERT INTO {table_name} ("student_id", "{column_name}", "title")
                 VALUES (%s, to_tsvector(\'english\', COALESCE(%s,\'\')), %s)""".format(
                                    table_name = STUDENT_SEARCH_TABLE_NAME,
                                    column_name = STUDENT_SEARCH_TSV_COL_NAME)

        cursor.execute(sql, [student_course.student.id, ' '.join(stud_document), title])

    transaction.set_dirty()
