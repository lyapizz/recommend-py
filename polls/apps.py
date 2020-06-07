from django.apps import AppConfig


class PollsConfig(AppConfig):
    name = 'polls'

    def ready(self):
        # noinspection PyUnresolvedReferences
        import polls.signals
