from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from web.views import comment_submit, shop


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('web.urls',namespace="web")),
    path('comment_submit/', comment_submit, name='comment_submit'),
    # path('comment_list/', comment_list, name='comment_list'),
    path('shop',shop,name='shop'),


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
