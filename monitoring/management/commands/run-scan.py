from django.core.management.base import BaseCommand, CommandError
from monitoring.w3af import myw3af
from django.utils import timezone
from datetime import timedelta
from django.conf import settings

from monitoring.models import Website

class Command(BaseCommand):
    help = 'Run scans'

    def add_arguments(self, parser):
        #parser.add_argument('poll_id', nargs='+', type=int)
        pass

    def handle(self, *args, **options):

        w3af_instanz = myw3af()
        w3af_instanz.set_scan_profile()
        w3af_instanz.set_free_server()

        time_limit = timezone.now() - timedelta(days=14)

        Websites = Website.objects.filter(cron=1, last_scan__lte=(time_limit)).order_by('-last_scan')

        for site in Websites:
            w3af_instanz.start_scan(site)
