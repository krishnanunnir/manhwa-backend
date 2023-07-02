from django.views.generic import TemplateView

from .models import Blog, Manhwa, ManhwaList, Tags


class ManhwaTemplateView(TemplateView):
    template_name = "web/index.html"
