from django.db import models


class App(models.Model):
    app_id = models.CharField(max_length=60, default="")
    app_name = models.CharField(max_length=60)
    cpu_use = models.IntegerField(default=0)
    memory_use = models.IntegerField(default=0)
    disk_use = models.IntegerField(default=0)

    def __str__(self):
        return self.app_name


class ProcessList(models.Model):
    app = models.OneToOneField(App)

    def __str__(self):
        return self.app.app_name


class MemoryTable(models.Model):
    list = models.CharField(max_length=5000)
    list_length = models.IntegerField(default=0)

    def __str__(self):
        return str(self.list_length)


class MemorySpace(models.Model):
    app = models.ForeignKey(App)
    start = models.IntegerField(default=0)
    length = models.IntegerField(default=0)

    def __str__(self):
        return "{}, {}, {}".format(self.app.app_id, self.start, self.length)
