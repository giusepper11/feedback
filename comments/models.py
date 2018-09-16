from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User


# Create your models here.


class Circle(models.Model):
    name = models.CharField(_("Nome"), max_length=50)

    class Meta:
        ordering = ['id']
        verbose_name = _('Circulo')
        verbose_name_plural = _('Circulos')

    def __str__(self):
        return self.name


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('Usuário'))
    comment = models.TextField(_('Comentário'))
    circle = models.ForeignKey(Circle, on_delete=models.CASCADE, verbose_name=_('Circulo'))
    create_at = models.DateField(auto_now_add=True)

    class Meta:
        ordering= ['id']
        verbose_name = _('Comentario')
        verbose_name_plural = _('Comentários')

    def __str__(self):
        return self.comment
