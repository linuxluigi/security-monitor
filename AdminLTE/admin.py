from copy import deepcopy

from django.contrib import admin

from mezzanine.forms.admin import FormAdmin
from mezzanine.forms.models import Form
from mezzanine.galleries.admin import GalleryAdmin
from mezzanine.galleries.models import Gallery
from mezzanine.pages.admin import PageAdmin
from mezzanine.pages.models import RichTextPage, Link


# add the icon to page subclasses in the admin
page_fieldsets = deepcopy(PageAdmin.fieldsets)
page_fieldsets[0][1]["fields"].insert(-4, "icon")
#page_fieldsets[0][1]["fields"] += ("icon",)
PageAdmin.fieldsets = page_fieldsets
GalleryAdmin.fieldsets = page_fieldsets

form_fieldsets = deepcopy(FormAdmin.fieldsets)
form_fieldsets[0][1]["fields"].insert(-7, "icon")
#form_fieldsets[0][1]["fields"] += ("icon",)
FormAdmin.fieldsets = form_fieldsets

admin.site.unregister(Form)
admin.site.register(Form, FormAdmin)
admin.site.unregister(Gallery)
admin.site.register(Gallery, GalleryAdmin)
admin.site.unregister(RichTextPage)
admin.site.register(RichTextPage, PageAdmin)
admin.site.unregister(Link)
admin.site.register(Link, PageAdmin)
