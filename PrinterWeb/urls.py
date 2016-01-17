from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns("",
	url(r"^$", direct_to_template, {"template": "homepage.html"}, name="home"),
	url(r"^about/", direct_to_template, {"template": "about.html"}, name="about"),
	url(r"^workshop/", direct_to_template, {"template": "workshop.html"}, name="workshop"),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^account/", include("account.urls")),
    url(r"^blog/", include("zinnia.urls")),
    url(r"^contact/", include("contact_form.urls")),
    url(r"^comments/", include("django.contrib.comments.urls")),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
