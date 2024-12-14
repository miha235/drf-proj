from django.contrib.auth.management.commands import createsuperuser
from django.core.management import CommandError

class Command(createsuperuser.Command):
    def handle(self, *args, **options):
        # Принудительно указываем, что 'username' - это 'email'
        options['username'] = options.get('email')
        # Вызываем стандартную команду для создания суперпользователя
        super().handle(*args, **options)
