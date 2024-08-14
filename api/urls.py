
from django.urls import path
from .views import MobileFilterView, MatchingMobilesList

app_name = 'api'
urlpatterns = [
    path('', MobileFilterView.as_view(), name='api-list'),
    path('mobiles/matching/', MatchingMobilesList.as_view(), name='matching-mobiles'),

]
