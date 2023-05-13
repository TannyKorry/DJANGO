from django.views.generic import ListView
from django.shortcuts import render

from .models import Student, Teachers


def students_list(request):
    template = 'school/students_list.html'
    stud = Student.objects.all()
    # stud = Student.objects.all().prefetch_related('teacher')

    context = {
        'object_list': stud
    }

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = 'group'

    return render(request, template, context)
