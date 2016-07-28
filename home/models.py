from django.db import models


class App(models.Model):
    app_id = models.CharField(max_length=60, default="")
    app_name = models.CharField(max_length=60)
    cpu_use = models.DecimalField(max_digits=5, decimal_places=2)
    memory_use = models.DecimalField(max_digits=5, decimal_places=2)
    disk_use = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.app_name

