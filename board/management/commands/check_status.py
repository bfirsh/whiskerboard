from django.core.management.base import BaseCommand
from board.models import Service
from board import tasks


class Command(BaseCommand):
    help = """some help"""

    def handle(self, *args, **kw):
        for service in Service.objects.all():
            if service.connection_string:
                self.check_status(service)

    def check_status(self, service):
        checker = getattr(tasks, 'check_%s' % service.connection.scheme)
        if checker:
            checker.delay(service)
