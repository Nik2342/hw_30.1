from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from lms.models import Course, Lesson
from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self) -> None:
        super().setUp()
        self.user = User.objects.create(email="test@test.com")
        self.course = Course.objects.create(title="Курс", description="Курс")
        self.lesson = Lesson.objects.create(
            title="Урок 1",
            video_link="https://youtube.com/",
            description="Первый урок",
            course=self.course,
            owner=self.user,
        )
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        """Тестирование получения урока."""
        url = reverse("lms:lesson_detail", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), self.lesson.title)

    def test_lesson_create(self):
        """Тестирование создания урока."""
        url = reverse("lms:lesson_create")
        data = {
            "title": "Урок 2",
            "video_link": "https://youtube.com/",
            "description": "Второй урок",
            "course": self.course.pk,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 2)

    def test_lesson_update(self):
        """Тестирование изменения урока."""
        url = reverse("lms:lesson_update", args=(self.lesson.pk,))
        data = {
            "title": "Урок 3",
        }
        response = self.client.patch(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), "Урок 3")

    def test_lesson_delete(self):
        """Тестирование удаления урока."""
        url = reverse("lms:lesson_delete", args=(self.lesson.pk,))

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)


class CourseTestCase(APITestCase):

    def setUp(self) -> None:
        super().setUp()
        self.user = User.objects.create(email="test@test.com")
        self.course = Course.objects.create(
            title="Курс 2", description="Курс 2", owner=self.user
        )
        self.client.force_authenticate(user=self.user)

    def test_course_retrieve(self):
        """Тестирование получения курса."""
        url = reverse("lms:course-detail", args=(self.course.pk,))
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), self.course.title)

    def test_course_create(self):
        """Тестирование создания курса."""
        url = reverse("lms:course-list")
        data = {
            "title": "Курс",
            "description": "",
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Course.objects.all().count(), 2)

    def test_course_update(self):
        """Тестирование изменения курса."""
        url = reverse("lms:course-detail", args=(self.course.pk,))
        data = {
            "title": "Курс 3",
        }
        response = self.client.patch(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), "Курс 3")

    def test_course_delete(self):
        """Тестирование удаления курса."""
        url = reverse("lms:course-detail", args=(self.course.pk,))

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Course.objects.all().count(), 0)
