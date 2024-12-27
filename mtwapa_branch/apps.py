from django.apps import AppConfig


class MtwapaBranchConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mtwapa_branch'

    def ready(self):
        import mtwapa_branch.signals  # Import the signals here
