from django.contrib import admin
from django.urls import path,include

from . import views
from django.conf.urls.static import static
from django.conf import settings

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'', views.UserViewSet)


urlpatterns = [
    path('', views.home,name='home'),
    path('contact', views.contact,name='contact'),
    path('signup', views.sign_up,name='signup'),
    path('login', views.login,name='login'),
    path('logout', views.logout,name='logout'),
    path('course/<str:slug>/', views.course,name='course'),
    path('checkout/<str:slug>/', views.checkout,name='checkout'),
    path('verify_payment', views.verify_payment,name='verify_payment'),
    path('mycourse', views.mycourse,name='mycourse'),
    path('rest_api/', include(router.urls)),
  

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

