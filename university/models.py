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

    def __str__(self):
        return self.last_name

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
