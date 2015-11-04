from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone

class Website(models.Model):
    User = models.ForeignKey(User)
    url = models.URLField()
    registred = models.DateTimeField(default=timezone.now)
    last_scan = models.DateTimeField(null=True, blank=True)
    cron = models.BooleanField(default=False)

class W3af_scan(models.Model):
    Website = models.ForeignKey(Website)
    start_scan = models.DateTimeField(default=timezone.now)
    stop_scan = models.DateTimeField(null=True, blank=True)

class W3af_findings(models.Model):
    '''
    scan.conn.send_request('/scans/0/kb/0', method='GET')[1]['href']
    scan.conn.send_request('/scans/0/kb/0', method='GET')[1]['url']
    scan.conn.send_request('/scans/0/kb/0', method='GET')[1]['desc']
    scan.conn.send_request('/scans/0/kb/0', method='GET')[1]['long_description']
    scan.conn.send_request('/scans/0/kb/0', method='GET')[1]['plugin_name']
    '''
    scan_object = models.ForeignKey(W3af_scan)
    href = models.CharField(blank=True, max_length=255)
    url = models.URLField(blank=True)
    desc = models.TextField(null=True, blank=True)
    long_description = models.TextField(null=True, blank=True)
    plugin_name = models.CharField(null=True, blank=True, max_length=255)

class W3af_server(models.Model):
    server_name = models.CharField(max_length=50, default='localhost')
    Scan = models.ForeignKey(W3af_scan, blank=True, null=True,)
    notice = models.CharField(blank=True, max_length=255)
    host = models.URLField(default='http://127.0.0.1:5000/')
    username = models.CharField(blank=True, max_length=255)
    password = models.CharField(blank=True, max_length=512)
    running = models.BooleanField(default=False)
    last_scan = models.DateTimeField(null=True, blank=True)
    registred = models.DateTimeField(default=timezone.now)
    '''
    #w3af_server api config example
    host: '127.0.0.1'
    port: 5000
    verbose: False
    username: 'admin'
    # The SHA512-hashed password is 'secret'. We don't recommend using this.
    password: 'bd2b1aaf7ef4f09be9f52ce2d8d599674d81aa9d6a4421696dc4d93dd0619d682ce56b4d64a9ef097761ced99e0f67265b5f76085e5b0ee7ca4696b2ad6fe2b2'
    '''
