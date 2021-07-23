from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class Tarefa(models.Model):
    """Model definition for Tarefa.

    Atributos:
    nome
    descricao
    entrega
    status
    usuario

    """

    nome = models.CharField(("Nome"), max_length=50)
    descricao = models.TextField(_("Descrição"))
    entrega = models.DateField(
        _("Data de entrega"), auto_now=False, auto_now_add=False)
    status = models.IntegerField(
        _("Status"), choices=[(0, "Concluído"), (1, "Não concluído")], default=1)
    usuario = models.ForeignKey(User, verbose_name=_(
        "Usuário"), on_delete=models.CASCADE)

    criacao = models.DateTimeField(
        _("Data de criação"), auto_now=False, auto_now_add=True)

    class Meta:
        """Meta definition for Tarefa."""

        verbose_name = 'Tarefa'
        verbose_name_plural = 'Tarefas'

    def __str__(self):
        """Unicode representation of Tarefa."""
        return f'{self.nome} para {self.entrega}'
