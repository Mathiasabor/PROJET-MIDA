from django.contrib import admin

# Register your models here.

from .models import Livre
from .models import Theses
from .models import Consultes
from .models import Categories
from .models import Telecharge

admin.site.register(Livre)
admin.site.register(Categories)
admin.site.register(Theses)
admin.site.register(Consultes)
admin.site.register(Telecharge)

