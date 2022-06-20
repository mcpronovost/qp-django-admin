from django.urls import reverse
from django.apps import apps

class AdminMiddleware():
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response
    
    def get_app_list(self, app_list):
        for a in app_list:
            a_config = apps.get_app_config(a["app_label"])
            if hasattr(a_config, "Qapi"):
                a["qp_admin_order"] = a_config.Qapi.admin_order
            else:
                a["qp_admin_order"] = 89
            for m in a["models"]:
                if hasattr(m["model"], "Qapi"):
                    m["qp_admin_order"] = m["model"].Qapi.admin_order
                else:
                    if m["object_name"] == "Group":
                        m["qp_admin_order"] = 2
                    else:
                        m["qp_admin_order"] = 89
            a["models"] = sorted(a["models"], key=lambda q: q["qp_admin_order"])
        app_list = sorted(app_list, key=lambda q: q["qp_admin_order"])
        return app_list

    def process_template_response(self, request, response):
        if not request.path.startswith(reverse('admin:index')):
            return response
        try:
            app_list = response.context_data['app_list']
        except KeyError:
            return response
        # ===---
        app_list = self.get_app_list(app_list)
        response.context_data['app_list'] = app_list
        response.context_data['available_apps'] = app_list
        # ===---
        return response