import datetime
from django.db import models
from django.utils import timezone
from PIL import Image


class Usuario(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    senha = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='media/avatar')

    um = '1'
    dois = '2'
    tres = '3'
    tipo_de_usuario = [
        (um, 'Administrador'),
        (dois, 'Colunista'),
        (tres, 'Leitor'),
    ]
    tipo = models.CharField(max_length=1, choices=tipo_de_usuario, default=3)

class Edicao(models.Model):
    usuario_id = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    data = models.DateTimeField('data de publicação', default=timezone.now())

    def publicado_recentemente(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.data <= now

    def __str__(self):
        return self.titulo


class Noticia(models.Model):
    usuario_id = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    edicao_id = models.ForeignKey(Edicao, on_delete=models.CASCADE)

    titulo = models.CharField(max_length=200)
    descricao = models.CharField(max_length=500)
    thumbnail = models.ImageField(upload_to='media/thumbnail')
    conteudo = models.TextField(default='')
    data = models.DateTimeField('data de publicação', default=timezone.now())
    categoria = models.CharField(max_length=100)

    def publicado_recentemente(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.data <= now

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    usuario_id = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    edicao_id = models.ForeignKey(Edicao, on_delete=models.CASCADE)
    noticia_id = models.ForeignKey(Noticia, on_delete=models.CASCADE)
    conteudo = models.CharField(max_length=500)
    data = models.DateTimeField('data de publicação', default=timezone.now())
    curtidas = models.IntegerField(default=0)

    def publicado_recentemente(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.data <= now

    def __str__(self):
        return self.conteudo
