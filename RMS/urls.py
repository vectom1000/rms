from django.conf.urls import url
from django.contrib import admin
import rms_app.views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', rms_app.views.uebersicht, name='index'),
    url(r'^gericht/(?P<gericht_id>[0-9]{1,10})/$', rms_app.views.zeige_gericht, name='zeige_gericht'),
    url(r'^login_user/', rms_app.views.login_user, name='login'),
    url(r'^logout/', 'django.contrib.auth.views.logout'),
]
