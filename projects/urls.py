from django.contrib import admin
# from django.conf.urls import url, include
# from django.conf.urls import url
from django.urls import re_path as url, include
from django.contrib.auth import views as auth_views
from django.contrib.auth import views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    url('admin/', admin.site.urls),
    url('',include('awwards.urls')),
    url('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    # url(r'^logout/$', views.logout, {"next_page": '/'}),
    url('api-auth/', include('rest_framework.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)