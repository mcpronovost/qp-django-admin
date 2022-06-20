from django.contrib import admin

from qp.admin.models import qpAdminSettings


@admin.register(qpAdminSettings)
class qpAdminSettingsAdmin(admin.ModelAdmin):
    pass
