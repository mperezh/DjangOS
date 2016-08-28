from django.contrib import admin
from home.models import App, ProcessList, MemoryTable, MemorySpace

admin.site.register(App)
admin.site.register(ProcessList)
admin.site.register(MemoryTable)
admin.site.register(MemorySpace)
