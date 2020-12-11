from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from datetime import date

from core.models import Performance, Role


class PerformanceView(View):

    def get(self, request, pk):
        performance = get_object_or_404(Performance, pk=pk)
        plays = performance.play_set.all().filter(date__gt=date.today())
        roles = performance.role_set.all()

        context = {'performance': performance, 'plays': plays, 'roles': roles}
        return render(request, template_name='core/performance.html', context=context)
