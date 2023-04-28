from urllib import request
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.forms import model_to_dict, inlineformset_factory
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, CreateView, UpdateView
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import LoginUserForm, LessonFormSet
from .mixins import SuperuserRequiredMixin
from .models import Lesson, Teacher, Cabinet, CourseNumber, Group, Theme, Subgroups, NumberLesson, Week
from .serializers import LessonSerializer, CourseNumberSerializer, GroupSerializer, ThemeSerializer, \
    SubgroupsSerializer, NumberLessonSerializer, WeekSerializer, TeacherSerializer, CabinetSerializer


# class LessonAPIView(APIView):
#     def get(self, request):
#         week = Week.objects.all().values()
#         teacher = Teacher.objects.all().values()
#         cabinet = Cabinet.objects.all().values()
#         group = Group.objects.all().values()
#         theme = Theme.objects.all().values()
#         lesson = Lesson.objects.all().values()
#         number_lesson = NumberLesson.objects.all().values()
#         # return Response({
#         #     'week': list(week),
#         #     'teacher': list(teacher),
#         #     'cabinet': list(cabinet),
#         #     'group': list(group),
#         #     'theme': list(theme),
#         #     'lesson': list(lesson),
#         #     'number_lesson': list(number_lesson)
#         # })
#         return Response({
#             'lesson': LessonSerializer(lesson, many=True).data
#         })
#
#
#     def post(self, request):
#         post_new = Week.objects.create(
#             title=request.data['title'],
#             content=request.data['content'],
#             cat_id=request.data['cat_id']
#         )
#         return Response({'post': model_to_dict(post_new)})
class LessonDetail(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class TeacherDetail(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class CabinetDetail(viewsets.ModelViewSet):
    queryset = Cabinet.objects.all()
    serializer_class = CabinetSerializer


class CourseNumberDetail(viewsets.ModelViewSet):
    queryset = CourseNumber.objects.all()
    serializer_class = CourseNumberSerializer


class GroupDetail(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ThemeDetail(viewsets.ModelViewSet):
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer


class SubgroupsDetail(viewsets.ModelViewSet):
    queryset = Subgroups.objects.all()
    serializer_class = SubgroupsSerializer


class NumberLessonDetail(viewsets.ModelViewSet):
    queryset = NumberLesson.objects.order_by('numberlesson_name')
    serializer_class = NumberLessonSerializer


class WeekList(viewsets.ModelViewSet):
    queryset = Week.objects.all()
    serializer_class = WeekSerializer


# Авторизация
class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('main')


def LogoutUser(request):
    logout(request)
    return redirect('login')


# Bird from
class CreateTableView(SuperuserRequiredMixin, TemplateView):
    template_name = "index.html"

    def get(self, *args, **kwargs):
        formset = LessonFormSet(queryset=Lesson.objects.none())
        return self.render_to_response({'lesson_formset': formset})
    # Define method to handle POST request

    def post(self, *args, **kwargs):
        formset = LessonFormSet(data=self.request.POST)
        # Check if submitted forms are valid
        if formset.is_valid():
            formset.save()
            messages.success(self.request, 'Расписание было создано!')
            return redirect(reverse_lazy('main'))
        return self.render_to_response({'lesson_formset': formset})