from rest_framework import serializers

from .models import Teacher, Cabinet, CourseNumber, Group, Theme, Subgroups, NumberLesson, Lesson, Week


# class LessonSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Week
#         fields = ('day', 'date_start', 'date_end', 'practice')
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('id', 'last_name', 'first_name', 'middle_name')


class CabinetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cabinet
        fields = ('id', 'cabinet_name')


class CourseNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseNumber
        fields = ('id', 'course_number')


class GroupSerializer(serializers.ModelSerializer):
    course_number = CourseNumberSerializer()

    class Meta:
        model = Group
        fields = ('id', 'group_name', 'course_number')


class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = ('id', 'theme_name')


class SubgroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subgroups
        fields = ('id', 'subgroups_name')


class NumberLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = NumberLesson
        fields = ('id', 'numberlesson_name', 'starttimelesson', 'endtimelesson', 'short')


class LessonSerializer(serializers.ModelSerializer):
    number = NumberLessonSerializer()
    teacher = TeacherSerializer()
    cabinet = CabinetSerializer()
    theme = ThemeSerializer()
    group = GroupSerializer()
    subgroup = SubgroupsSerializer()

    class Meta:
        model = Lesson
        fields = ['id', 'number', 'teacher', 'cabinet', 'theme', 'group', 'subgroup', 'date']


class WeekSerializer(serializers.ModelSerializer):
    day = LessonSerializer()

    class Meta:
        model = Week
        fields = ['id', 'day', 'date_start', 'date_end', 'practice']



# class StudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Student
#         fields = ['id', 'name', 'course', 'email', 'gender']

