from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'TGBot start'

    def handle(self, *args, **options):
        print('ok')