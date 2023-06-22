from django.db import models

# Create your models here.
status_choices = [('new', 'Новая'), ('in_progress', 'В процессе'), ('done', 'Сделано')]


class Todo(models.Model):
    content = models.CharField(max_length=200, null=False, blank=False, verbose_name="Описание")
    status = models.CharField(max_length=50, null=False, blank=False, verbose_name="Статус", choices=status_choices,
                              default=status_choices[0][0])
    details = models.TextField(max_length=2000, null=True, blank=True, verbose_name="Детальное описание")
    created_at = models.CharField(max_length=50, null=True, blank=True, verbose_name="Дата выполнения")

    def __str__(self):
        return f"{self.pk} {self.content}: {self.status}"

    class Meta:
        db_table = "To-Do list"
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
