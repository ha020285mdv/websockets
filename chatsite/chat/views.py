from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = 'index.html'

class Room(TemplateView):
    template_name = 'room.html'
