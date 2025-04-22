from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from lms.models import Course, Lesson


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(ModelSerializer):
    lessons_count = SerializerMethodField()
    lessons = LessonSerializer(read_only=True)

    def get_lessons_count(self, lesson):
        return Lesson.objects.count()

    class Meta:
        model = Course
        fields = ["id", "title", "preview", "description", "lessons_count", "lessons"]
