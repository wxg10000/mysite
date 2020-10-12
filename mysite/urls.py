"""mysite URL Configuration
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
from django.conf.urls import include
from django.contrib import admin
from app01 import views,forms

urlpatterns = [
    # 管理员账户登陆
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.index),
    # url(r'^index/',views.index),
    url(r'^login/',views.login),
    url(r'^register/',views.register),
    url(r'^logout/',views.logout),
    url(r'^captcha', include('captcha.urls')),
   ]


admin.site.site_header = ' 田野的管理平台'
admin.site.site_title = ' 田野的管理平台'
admin.site.index_title = '模型管理'
admin.site.index_template = 'admin/index.html'