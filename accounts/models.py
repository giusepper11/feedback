from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
# Create your models here.

CHOICES_GENRE = ('M', _('Masculino')), ('F', _('Feminino'))


class Profile(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name=_('Usuário'))
    photo = models.ImageField(_('Foto'), upload_to='photos')
    bio = models.TextField(_("Mini-bio"), blank=True)
    birthday = models.DateField(_("Nascimento"), blank=True)
    genre = models.CharField(_("Sexo"), max_length=1,
                             choices=CHOICES_GENRE, blank=True)
    phone = models.CharField(_("Celular"), max_length=14, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = _('Perfil')
        verbose_name_plural = _('Perfis')

    def __str__(self):
        return 'Perfil - {}'.format(self.pk)
