from rest_framework.viewsets import ModelViewSet
from .models import Course
from .serializers import CourseSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Lesson
from .serializers import LessonSerializer


class LessonListCreateView(ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


