from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import View
from django.utils import timezone
from .models import Usuario, Edicao, Noticia


class IndexView(View):
    def get(self, request, *args, **kwargs):
        ultimas_noticias = Noticia.objects.filter(data__lte=timezone.now()).order_by('-data')[:5]
        return render(request, "index.html", {'ultimas_noticias': ultimas_noticias})