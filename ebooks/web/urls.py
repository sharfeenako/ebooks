from . import views
from django.urls import path


app_name='web'

urlpatterns = [
    path('',views.index,name='index'),
    path('shop',views.shop,name='shop'),
    path("login",views.login_1,name="login"),
    path("signup",views.register_1,name="signup"),
    path('comments/submit/', views.comment_submit, name='comment_submit'),
    path('shop_detail/<int:id>/',views.shop_detail,name='shop_detail'),
    path("book",views.book,name="book"),
    path('logout/',views.logout_1,name='logout'),



    

]