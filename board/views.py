from board.models import Service, Status
import datetime
from django.views.generic import ListView, DetailView

class BoardMixin(object):
    def get_context_data(self, **kwargs):
        context = super(BoardMixin, self).get_context_data(**kwargs)
        context['statuses'] = Status.objects.all()
        return context


def get_past_days(num):
    date = datetime.date.today()
    dates = []
    
    for i in range(1, num+1):
        dates.append(date - datetime.timedelta(days=i))
    
    return dates


class IndexView(BoardMixin, ListView):
    context_object_name = 'services'
    queryset = Service.objects.all()
    template_name = 'board/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['default'] = Status.objects.default()
        context['past'] = get_past_days(5)
        return context


class ServiceView(BoardMixin, DetailView):
    model = Service

