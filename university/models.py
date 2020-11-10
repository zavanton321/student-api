from random import randint

from django.contrib.auth.models import User
from django.db import models


class Student(models.Model):
    first_name = models.CharField(
        blank=False,
        max_length=100,
        verbose_name="Имя"
    )
    last_name = models.CharField(
        blank=False,
        max_length=100,
        verbose_name="Фамилия"
    )
    grade = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name="Средний балл"
    )
    registrator = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name="students"
    )
    random_data = models.CharField(
        max_length=100,
        verbose_name='Рандомное поле'
    )

    def save(self, *args, **kwargs):
        rand = str(randint(0, 100))
        self.random_data = rand
        super(Student, self).save(*args, **kwargs)

    def __str__(self):
        return self.last_name

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
