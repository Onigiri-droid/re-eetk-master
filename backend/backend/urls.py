from django.contrib import admin
from django.urls import path, include

from core.views import WeekList, NumberLessonDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/v1/lessonlist', LessonAPIView.as_view()),
    path('api/v1/lessonlist/', WeekList.as_view({'get': 'list'})),
    path('api/v1/lessonlist/num', NumberLessonDetail.as_view({'get': 'list'})),
    path('', include('core.urls')),
]
