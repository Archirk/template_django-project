from django.shortcuts import render
from django.views.generic import TemplateView


def index(request):
    msg = 'I am function view'
    return render(request, 'general/index.html', {'message': msg})


class IndexView(TemplateView):
    template_name = 'general/index.html'

    def get_context_data(self, **kwargs):
        msg = 'I am class-based view'
        return {'message': msg}

