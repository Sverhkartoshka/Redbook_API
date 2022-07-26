from django.urls import path

from .views import ObjectView, ListView, ClassificationView, DocumentView

app_name = "app"

urlpatterns = [
    path('objects/<int:classification>', ListView.as_view()),
    path('object/<int:pk>', ObjectView.as_view()),
    path('classes/', ClassificationView.as_view()),
    path('documents/', DocumentView.as_view())
]