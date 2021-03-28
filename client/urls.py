from django.urls import path
from . import views
from .views import ClientCreateView, DeviceRegistartionView

urlpatterns = [
    path('client/new/', ClientCreateView.as_view(), name='client-create'),
    path('device/entry/', DeviceRegistartionView, name='device-entry'),

]
