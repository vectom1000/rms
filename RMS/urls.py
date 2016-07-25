from django.conf.urls import url
from django.contrib import admin
import rms_app.views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', rms_app.views.uebersicht, name='index'),
    url(r'^gericht/(?P<gericht_id>[0-9]{1,10})/$', rms_app.views.zeige_gericht, name='zeige_gericht'),
    url(r'^login_user/', rms_app.views.login_user, name='login'),
    url(r'^logout/', 'django.contrib.auth.views.logout'),
    url(r'^controll_center/', 'rms_app.views.controll_center', name='controll_center'),
    url(r'^erstelle_gericht/', 'rms_app.views.erstelle_gericht', name='erstelle_gerichter'),
    url(r'^loesche_gericht/(?P<gericht_id>[0-9]{1,10})/$', rms_app.views.loesche_gericht, name='loesche_gericht'),
    url(r'^bearbeite_gericht/(?P<gericht_id>[0-9]{1,10})/$', rms_app.views.bearbeite_gericht, name='bearbeite_gericht'),
    url(r'^erstelle_kategorie/', 'rms_app.views.erstelle_kategorie', name='erstelle_kategorie'),
    url(r'^zeige_kategorie/(?P<kategorie_id>[0-9]{1,10})/$', rms_app.views.zeige_kategorie, name='zeige_kategorie'),
]
