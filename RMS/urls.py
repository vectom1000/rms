from django.conf.urls import url
from django.contrib import admin
import rms_app.views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', rms_app.views.hello, name='index')
]
