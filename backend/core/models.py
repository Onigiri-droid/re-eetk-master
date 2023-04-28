from django.db import models


class Teacher(models.Model):
    last_name = models.CharField('Фамилия', max_length=20)
    first_name = models.CharField('Имя', max_length=20)
    middle_name = models.CharField('Отчество', max_length=20)

    def __str__(self):
        return f'{self.last_name}'

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'


class Cabinet(models.Model):
    cabinet_name = models.CharField('Кабинет', max_length=20)

    def __str__(self):
        return f'{self.cabinet_name}'

    class Meta:
        verbose_name = 'Кабинет'
        verbose_name_plural = 'Кабинеты'


class CourseNumber(models.Model):
    course_number = models.PositiveSmallIntegerField('Номер курса', default='1')

    def __str__(self):
        return f'{self.course_number}'

    class Meta:
        verbose_name = 'Номер курса'
        verbose_name_plural = 'Номера курсов'


class Group(models.Model):
    group_name = models.CharField('Группа', max_length=20)
    course_number = models.ForeignKey(CourseNumber, verbose_name='Номер курса', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.group_name}'

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class Theme(models.Model):
    theme_name = models.CharField('Предмет', max_length=20)

    def __str__(self):
        return f'{self.theme_name}'

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'


class Subgroups(models.Model):
    subgroups_name = models.CharField('Номер подгруппы', max_length=5)

    def __str__(self):
        return f"{self.subgroups_name}"

    class Meta:
        verbose_name = 'Подгруппа'
        verbose_name_plural = 'Подгруппы'


class NumberLesson(models.Model):
    numberlesson_name = models.CharField('Номер пары', max_length=5)
    starttimelesson = models.TimeField('Начало пары')
    endtimelesson = models.TimeField('Конец пары')
    choiseble = (
        ('', ''),
        ('Сокращенное', 'Сокращенные')
    )
    short = models.CharField('Сокращенная пара?', choices=choiseble, max_length=255, blank=True)

    def __str__(self):
        return f"{self.numberlesson_name} {self.short}"

    class Meta:
        verbose_name = 'Номер пары'
        verbose_name_plural = 'Номера пар'


class Lesson(models.Model):
    number = models.ForeignKey(NumberLesson, verbose_name='Номер пары', on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, verbose_name='Преподаватель', on_delete=models.CASCADE)
    cabinet = models.ForeignKey(Cabinet, verbose_name='Кабинет', on_delete=models.CASCADE)
    theme = models.ForeignKey(Theme, verbose_name='Предмет', on_delete=models.CASCADE)
    group = models.ForeignKey(Group, verbose_name='Группа', on_delete=models.CASCADE)
    subgroup = models.ForeignKey(Subgroups, verbose_name='Номер подгруппы', blank=True, null=True, on_delete=models.CASCADE)
    date = models.DateField('Дата пары')

    def __str__(self):
        return f"{self.number} - {self.teacher} - {self.group} - {self.theme} - {self.cabinet} - {self.date}"

    class Meta:
        verbose_name = 'Пара'
        verbose_name_plural = 'Пары'


# class Practice(models.Model):
#     name = models.CharField('Какая практика/либо отсутствие', max_length=200, blank=True, null=True)
#     practice_start = models.DateField('Дата начала практики', blank=True, null=True)
#     practice_end = models.DateField('Дата конца практики', blank=True, null=True)
#
#     def __str__(self):
#         return f"{self.name} - {self.practice_start} - {self.practice_end}"
#
#     class Meta:
#         verbose_name = 'Практика'
#         verbose_name_plural = 'Практика'


class Week(models.Model):
    day = models.ForeignKey(Lesson, verbose_name='Пары на день', blank=True, null=True, on_delete=models.CASCADE)
    date_start = models.DateField('Дата начала недели')
    date_end = models.DateField('Дата конца недели')
    practice = models.BooleanField('Практика')

    def __str__(self):
        return f'{self.day} - {self.date_start} - {self.date_end}'

    class Meta:
        verbose_name = 'Неделя'
        verbose_name_plural = 'Недели'


# Пока хз
# class CourseWeek(models.Model):
#     week = models.ForeignKey(Week, verbose_name='Неделя пар группы', on_delete=models.CASCADE)
#     course_numbers = models.ForeignKey(CourseNumber, verbose_name='Номер курса', on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f'{self.course_numbers} - {self.week}'
#
#     class Meta:
#         verbose_name = 'Курсовая неделя'
#         verbose_name_plural = 'Курсовые недели'
