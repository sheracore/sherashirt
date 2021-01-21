from django.urls import path, include

from rest_framework.routers import DefaultRouter

from billing import views


router = DefaultRouter()

router.register('shippers', views.ShipperViewSet)

app_name = 'billing'

urlpatterns = [
	path('', include(router.urls))
]