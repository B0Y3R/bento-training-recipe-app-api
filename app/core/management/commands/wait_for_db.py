import time

from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to pause execution
    until database is available"""

    def handle(self, *args, **options):
        # outputs a message to the screen
        self.stdout.write('Waiting for database...')
        db_connection = None

        while not db_connection:
            try:
                db_connection = connections['default']
            except OperationalError:
                self.stdout.write('Database unavailable, waiting 1 second ...')
                time.sleep(1)

        # using style makes the message green
        self.stdout.write(self.style.SUCCESS('Database available!'))
