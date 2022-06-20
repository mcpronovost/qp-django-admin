from tabnanny import verbose
from django.db import models
from django.utils.translation import gettext_lazy as _

class qpAdminSettings(models.Model):

    class Meta:
        verbose_name = _("Admin Settings")
        verbose_name_plural = _("Admin Settings")
    
    class Qapi:
        admin_order = 1
