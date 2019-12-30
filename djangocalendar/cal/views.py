import calendar
from datetime import datetime, date, timedelta

from django.db.models import Sum
from django.db.models.functions import Coalesce
from django.http import HttpResponse
from django.views import generic
from django.utils.safestring import mark_safe

from .models import *
from .utils import Calendar


def index(request):
    return HttpResponse('hello')


class CalendarView(generic.ListView):
    model = Event
    template_name = 'calendar.html'

    @staticmethod
    def prev_month(d):
        first = d.replace(day=1)
        prev_month = first - timedelta(days=1)
        month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
        return month

    @staticmethod
    def next_month(d):
        days_in_month = calendar.monthrange(d.year, d.month)[1]
        last = d.replace(day=days_in_month)
        next_month = last + timedelta(days=1)
        month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
        return month

    def get_queryset(self):
        qs = super().get_queryset()
        d = get_date(self.request.GET.get('month', None))
        spend_sum = qs.filter(start_time__year=d.year, start_time__month=d.month).aggregate(spend_sum=Coalesce(Sum('budget'), 0))[
            'spend_sum']
        return spend_sum

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)

        context['prev_month'] = self.prev_month(d)
        context['next_month'] = self.next_month(d)

        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        spend_sum = self.get_queryset()
        context['spend_sum'] = spend_sum
        return context


def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()
