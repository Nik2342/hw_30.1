from django.urls import path

from users.apps import UsersConfig
from users.views import (
    PaymentListAPIView,
    PaymentCreateAPIView,
    PaymentRetrieveAPIView,
    PaymentUpdateAPIView,
    PaymentDestroyAPIView,
)

app_name = UsersConfig.name

urlpatterns = [
    path("payment/", PaymentListAPIView.as_view(), name="payment-list"),
    path("payment/create/", PaymentCreateAPIView.as_view(), name="payment-create"),
    path(
        "payment/<int:pk>/", PaymentRetrieveAPIView.as_view(), name="payment-retrieve"
    ),
    path(
        "payment/<int:pk>/update/",
        PaymentUpdateAPIView.as_view(),
        name="payment-update",
    ),
    path(
        "payment/<int:pk>/delete",
        PaymentDestroyAPIView.as_view(),
        name="payment-delete",
    ),
]
