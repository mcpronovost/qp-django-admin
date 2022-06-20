from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AdminConfig(AppConfig):
    name = "qp.admin"
    label = "qpadmin"
    verbose_name = _("QP Administration")
    
    class Qapi:
        admin_order = 1
