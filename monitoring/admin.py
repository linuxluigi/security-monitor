from django.contrib import admin
from django.utils.translation import ugettext as _

from .models import W3af_server, Website, W3af_scan, W3af_findings

class ScanInline(admin.TabularInline):
    model = W3af_scan
    extra = 0

class FindingsInline(admin.TabularInline):
    model = W3af_findings
    extra = 0

class WebsiteAdmin(admin.ModelAdmin):
    fieldsets = [
        (_('Basic'),             {'fields': ['User', 'url', 'registred', 'last_scan', 'cron'],}),
    ]
    inlines = [ScanInline]
    list_display = ('User', 'url', 'registred', 'last_scan', 'cron')
    search_fields = ['User', 'url', 'registred', 'last_scan']

class w3af_serverAdmin(admin.ModelAdmin):
    fieldsets = [
        (_('Basic'),             {'fields': ['server_name', 'notice', 'host', 'username', 'password'],}),
        (_('Active'),             {'fields': ['running', 'last_scan', 'registred'],}),
    ]
    list_display = ('server_name', 'host', 'running', 'last_scan', 'registred')
    search_fields = ['server_name', 'notice', 'host', 'username', 'password', 'running', 'last_scan', 'registred']

class ScanAdmin(admin.ModelAdmin):
    fieldsets = [
        (_('Basic'),             {'fields': ['Website', 'start_scan', 'stop_scan'],}),
    ]
    inlines = [FindingsInline]
    list_display = ('get_Website', 'start_scan', 'stop_scan')
    search_fields = ['Website', 'start_scan', 'stop_scan']
    def get_Website(self, obj):
        return obj.Website.url

    get_Website.short_description = _('URL')
    get_Website.admin_order_field = 'Website__Website'
    '''
    def get_server(self, obj):
        get_server = obj.server
        if get_server == None:
            return get_server
        else:
            return get_server.server_name
    get_url.short_description = _('Server Name')
    get_url.admin_order_field = 'server__server_name'
    '''

admin.site.register(Website, WebsiteAdmin)
admin.site.register(W3af_server, w3af_serverAdmin)
admin.site.register(W3af_scan, ScanAdmin)
