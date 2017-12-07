from django.conf.urls import include, url
from django.contrib import admin
from main import views as main_views

urlpatterns = [
    # Examples:
    # url(r'^$', 'assignment.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^cleaners/', include('cleaners.urls', namespace='cleaners')),
    url(r'^cities/', include('cities.urls', namespace='cities')),
    url(r'^customers/', include('customers.urls', namespace='customers')),
    url(r'^$', main_views.SignUp.as_view(), name='signup')
]
