from django.db import connection
from django.db.models import Q
from django.http import HttpResponse
from django.views.generic.base import View
from postgres_search.views import JSONEnabledMixin
from search import STUDENT_SEARCH_TSV_COL_NAME
from search.models import StudentFullTextSearch
from student.models import StudentCourse
import operator
import simplejson

class StudentSearchListView(JSONEnabledMixin, View):

    def get(self, request):
        results = []
        if request.GET.get('v', '1') == '2':
            q_results = StudentFullTextSearch.objects.extra(where = [
                                "{column_name} @@ plainto_tsquery('english', %s )".format(column_name = STUDENT_SEARCH_TSV_COL_NAME)],
                                params = [request.GET.get('term')
                        ])
            for q in q_results:
                results.append({'title': q.title})

        else:
            # yikes
            filter_terms = [Q(student__user__last_name__icontains = request.GET.get('term')),
                            Q(student__user__first_name__icontains = request.GET.get('term')),
                            Q(course__name__icontains = request.GET.get('term'))]
            q_results = StudentCourse.objects.select_related('student__user', 'course').filter(reduce(operator.or_, filter_terms))
            for q in q_results:
                results.append({'title': '%s %s enrolled %s' % (q.student.user.first_name, q.student.user.last_name, q.course.name)})

        print connection.queries
        return HttpResponse(simplejson.dumps({'results': results}), status = 200, content_type = 'application/json')
