from django.urls import path, include
from rest_framework.routers import SimpleRouter

from lms.apps import LmsConfig
from lms.views import (
    CourseViewSet,
    LessonListAPIView,
    LessonCreateAPIView,
    LessonRetrieveAPIView,
    LessonUpdateAPIView,
    LessonDestroyAPIView,
)

app_name = LmsConfig.name
router = SimpleRouter()
router.register("", CourseViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("lessons/", LessonListAPIView.as_view(), name="lesson_list"),
    path("lessons/create/", LessonCreateAPIView.as_view(), name="lesson_create"),
    path("lessons/<int:pk>/", LessonRetrieveAPIView.as_view(), name="lesson_detail"),
    path(
        "lessons/<int:pk>/update/", LessonUpdateAPIView.as_view(), name="lesson_update"
    ),
    path(
        "lessons/<int:pk>/delete/", LessonDestroyAPIView.as_view(), name="lesson_delete"
    ),
]
