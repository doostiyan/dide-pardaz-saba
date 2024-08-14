from django.urls import path
from . import views

urlpatterns = [
    path('add-brand/', views.AddBrandView.as_view(), name='add_brand'),
    path('add-mobile/', views.AddMobileView.as_view(), name='add_phone'),
    path('', views.MobileListView.as_view(), name='mobile_list'),
    path('korean-brands/', views.MobilesKoreanBrandView.as_view(), name='korean_brands'),
    path('mobiles-matching/', views.MobilesWithMatchingNationalityView.as_view(), name='mobiles_matching'),
]