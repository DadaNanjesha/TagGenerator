from django.urls import path
from .views import GenerateQRCodeView, QRCodeHomeView

app_name = "qrcode"

urlpatterns = [
    path("generate/", GenerateQRCodeView.as_view(), name="generate"),
    path("", QRCodeHomeView.as_view(), name="home"),
]