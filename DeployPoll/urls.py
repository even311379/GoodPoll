"""DeployPoll URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static

from mysite import views

app_name = 'mysite'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('add_poll/',views.add_poll,name='add_poll'),
    path('add_poll_item/<int:id>',views.add_poll_item,name='add_poll_item'),
    path('show_poll/<int:id>',views.show_poll,name='show_poll'),
    path('accounts/',include('allauth.urls'))
    # path('list/',views.listing),
    # path('post/',views.posting),
    # path('delete/<int:pk>',views.post_remove,name='PostRemove'),
    # path('login/',views.login),
    # path('logout/',views.logout),
    
] 

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
