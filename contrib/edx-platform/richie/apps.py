from django.apps import AppConfig


class MyAppConfig(AppConfig):
    name = "richie"
    verbose_name = "Richie course catalog connector"

    def ready(self):
        """
        Connect signal handlers.
        """
        from . import signals  # pylint: disable=unused-import
