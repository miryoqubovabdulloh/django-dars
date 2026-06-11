from django.contrib import admin
from django.urls import path
from mahsulotlar.views import index_page
from mahsulotlar.views import dasturlar_page
from mahsulotlar.views import mevalar_page
from mahsulotlar.views import kitoblar_page

urlpatterns = [
    path('index/', index_page),
    path('dasturlash/', dasturlar_page),
    path('mevalar/', mevalar_page),
    path('kitoblar/', kitoblar_page),
    path('admin/', admin.site.urls),
]
