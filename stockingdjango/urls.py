"""firstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from accounts import views as accounts_views
from stocking import views
urlpatterns = [
    #url(r'^signup/', signup_views.signup),
    url(r'^$',  accounts_views.signup, name='signup'),
    url(r'^stocks/home$', views.stockHistory, name='home'),
    url(r'^signup/$', accounts_views.signup, name='signup'),
    #url(r'^login/$', auth_views.login, name='login'),
   # url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^admin/', admin.site.urls),
#    url(r'^stocks/home2$', views.stockHistory),
    url(r'^stocks/history/(?P<symbol>[\w]+)/$', views.symbolHistory),
    url(r'^stocks/home/(?P<symbol>[\w]+)/(?P<high>[\w]+)/(?P<low>[\w]+)/$', views.riskAnalysis),
   # url(r'^stocks/home2$', views.symbolInfo),
   # url(r'^stocks/home2$', views.riskAnalysis),

]
