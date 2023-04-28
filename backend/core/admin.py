from django.contrib import admin

from .models import *


@admin.register(Teacher)
class TimeTableAdmin(admin.ModelAdmin):
    list_display = ['id', 'last_name', 'first_name', 'middle_name']
    list_editable = ['last_name', 'first_name', 'middle_name']
    ordering = ['last_name']
    search_fields = ['last_name', 'first_name', 'middle_name']
    save_as = True


@admin.register(Cabinet)
class TimeTableAdmin(admin.ModelAdmin):
    list_display = ['id', 'cabinet_name']
    list_editable = ['cabinet_name']
    ordering = ['cabinet_name']
    search_fields = ['cabinet_name']
    save_as = True


@admin.register(CourseNumber)
class TimeTableAdmin(admin.ModelAdmin):
    list_display = ['id', 'course_number']
    list_editable = ['course_number']
    ordering = ['course_number']
    search_fields = ['course_number']
    save_as = True


@admin.register(Group)
class TimeTableAdmin(admin.ModelAdmin):
    list_display = ['id', 'group_name', 'course_number']
    list_editable = ['group_name', 'course_number']
    ordering = ['group_name', 'course_number']
    search_fields = ['group_name', 'course_number']
    save_as = True


@admin.register(Theme)
class TimeTableAdmin(admin.ModelAdmin):
    list_display = ['id', 'theme_name']
    list_editable = ['theme_name']
    ordering = ['theme_name']
    search_fields = ['theme_name']
    save_as = True


@admin.register(Subgroups)
class TimeTableAdmin(admin.ModelAdmin):
    list_display = ['id', 'subgroups_name']
    list_editable = ['subgroups_name']
    ordering = ['subgroups_name']
    search_fields = ['subgroups_name']
    save_as = True


@admin.register(NumberLesson)
class TimeTableAdmin(admin.ModelAdmin):
    list_display = ['id', 'numberlesson_name', 'starttimelesson', 'endtimelesson', 'short']
    list_editable = ['numberlesson_name', 'starttimelesson', 'endtimelesson', 'short']
    ordering = ['numberlesson_name', 'starttimelesson', 'endtimelesson']
    search_fields = ['numberlesson_name', 'starttimelesson', 'endtimelesson']
    save_as = True


@admin.register(Lesson)
class TimeTableAdmin(admin.ModelAdmin):
    list_display = ['id', 'number', 'theme', 'teacher', 'group', 'subgroup', 'cabinet', 'date']
    list_editable = ['number', 'theme', 'teacher', 'group', 'subgroup', 'cabinet', 'date']
    ordering = ['-date', 'number', 'group']
    search_fields = ['date', 'number', 'group', 'cabinet', 'teacher']
    save_as = True


@admin.register(Week)
class TimeTableAdmin(admin.ModelAdmin):
    list_display = ['id', 'day', 'date_start', 'date_end', 'practice']
    list_editable = ['day', 'date_start', 'date_end', 'practice']
    ordering = ['day', 'date_start', 'date_end']
    search_fields = ['day', 'date_start', 'date_end']
    save_as = True


admin.site.site_header = 'ЕЭТК'
admin.site.index_title = 'Админка сайта'