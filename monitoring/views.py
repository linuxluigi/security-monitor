from django.contrib import auth
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.db.models import Count

from .models import Website, W3af_scan, W3af_findings

def login_view(request):
    return render(request, 'dashboard/login.html')

@login_required(login_url='/dashboard/login/')
def logout_view(request):
  auth.logout(request)
  # Redirect to a success page.
  return HttpResponseRedirect("/")

@login_required(login_url='/dashboard/login/')
def index(request):
    Websites_List = Website.objects.filter(User=request.user)
    return render(request, 'dashboard/index.html', {'Websites_List': Websites_List})

@login_required(login_url='/dashboard/login/')
def url_status(request, website_id):
    UserWebsite = get_object_or_404(Website, pk=website_id, User=request.user)
    Scan_List = W3af_scan.objects.filter(Website=UserWebsite).order_by('-start_scan')
    for Scaning in Scan_List:
        Scaning.founddings = W3af_findings.objects.filter(scan_object=Scaning).count()
    return render(request, 'dashboard/url_status.html', {'Website': UserWebsite, 'Scan_List':Scan_List})

@login_required(login_url='/dashboard/login/')
def url_scan_status(request, website_id, scan_id):
    UserWebsite = get_object_or_404(Website, pk=website_id, User=request.user)
    UserScan = get_object_or_404(W3af_scan, pk=scan_id, Website=UserWebsite)
    Findings = W3af_findings.objects.filter(scan_object=UserScan)
    for found in Findings:
        if found.long_description:
            found.desc = found.long_description
    return render(request, 'dashboard/url_scan_status.html', {'Website': UserWebsite, 'Scan':UserScan, 'Findings':Findings})
