import os
import sys


def manage():
    # Prepare the TS environment.
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'i18n.settings')
    # Execute
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
