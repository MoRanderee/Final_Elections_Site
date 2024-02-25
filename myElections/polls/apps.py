from django.apps import AppConfig


class PollsConfig(AppConfig):
    """This is the app configuration class for the Polls app
    
    :param name: The name of the application
    :type name: str
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'polls'
