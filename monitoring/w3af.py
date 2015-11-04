from .models import W3af_server, W3af_scan, W3af_findings
from django.utils.translation import ugettext as _
from w3af_api_client import Connection, Scan
from django.utils import timezone
from datetime import timedelta
from annoying.functions import get_object_or_None
from django.conf import settings

class myw3af:
    error = ""
    succes = ""
    scan_profile = ""

    def set_scan_profile(self):
        '''
        from check_my_site.w3af import get_scan_profile
        get_scan_profile()
        '''
        profile = ('w3af_profiles/OWASP_TOP10.pw3af')
        self.scan_profile = file(profile).read()

    def set_free_server(self):
        time_limit = timezone.now() - timedelta(minutes=120)
        server_list = W3af_server.objects.filter(running=1)
        for server in server_list:
            print server.server_name
            server_status = self.get_server_status(server)
            if server_status == None:
                print "no scan"
                self.set_server_cleanup(server, server_status)
            elif server.last_scan < time_limit or server_status.running == "Stopped":
                print "get findings"
                self.get_findings(server, server_status)
                self.set_server_cleanup(server, server_status)

    def get_findings(self, server, server_status):
        for found in server_status.get_findings():
            href = found.resource_href
            old_found = get_object_or_None(W3af_findings, href=href, scan_object=server.Scan)
            if not old_found:
                scan_findings = W3af_findings(href=href)
                scan_findings.scan_object = server.Scan
                scan_findings.url = server_status.conn.send_request(href, method='GET')[1]['url']
                scan_findings.desc = server_status.conn.send_request(href, method='GET')[1]['desc']
                long_description = server_status.conn.send_request(href, method='GET')[1]['long_description']
                if long_description:
                    scan_findings.long_description = long_description
                scan_findings.plugin_name = server_status.conn.send_request(href, method='GET')[1]['plugin_name']
                scan_findings.save()

    def set_server_cleanup(self, server, server_status):
        server.Scan.stop_scan = timezone.now()
        server.Scan.save()

        if server_status:
            server_status.cleanup()

        server.running = False
        server.save()

    def get_server_status(self, server):
        try:
            conn = Connection(server.host)
            #add auth
            scan = Scan(conn)
            scan.scan_id = conn.get_scans()[0].scan_id
            scan.running = conn.get_scans()[0].status
        except:
            scan = None
        return scan


    def start_scan(self, UserWebsite):
        #add set_free server

        try:
            server = W3af_server.objects.filter(running=0).order_by('-last_scan')[:1]
            server = server[0]
        except:
            server = None

        if not server:
            self.error = _('No server slot free, please try again later!')
        else:
            conn = Connection(server.host)
            #add auth
            scan = Scan(conn)

            try:
                scan.start(self.scan_profile, [UserWebsite.url])
                self.succes = _('Server scan started, please wait a litte time for feedback!')
            except:
                self.error = _('Sorry, we got a server error, please try again later!')

            if self.succes:
                scan_object = W3af_scan(Website=UserWebsite)
                scan_object.save()

                server.last_scan = timezone.now()
                server.running = True
                server.Scan = scan_object
                server.save()

                UserWebsite.last_scan = timezone.now()
                UserWebsite.save()

            #add remove try from server start
