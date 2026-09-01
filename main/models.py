from django.db import models

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    priority = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Todo"
        verbose_name_plural = "Todos"
