from django.core.management.base import BaseCommand
import getpass

class Command(BaseCommand):
    help="Says hello to users"

    def add_arguments(self, parser):
        parser.add_argument('name',type=str)
        parser.add_argument('--last_name', type=str)

    def handle(self, *args, **options):
        print(f"hello {options['name']} {options.get('last_name','')}!")