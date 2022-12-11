from django.urls import re_path,path
from GiveAway import views

from django.conf.urls.static import static
from GiveAwayApi.settings import MEDIA_ROOT, MEDIA_URL


urlpatterns = [
    re_path(r'^item$', views.ItemsApi),
    re_path(r'^item/([0-9]+)$', views.ItemsApi),
    re_path(r'^item/SaveFile$', views.SaveFile),
    path('',views.Home),
    path('home',views.Home),
    path('browsefreebie',views.BrowseFreebie),
    path('postfreebie',views.PostFreebie)
]+static(MEDIA_URL,document_root=MEDIA_ROOT)