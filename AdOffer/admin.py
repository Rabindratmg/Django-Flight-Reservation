from django.contrib import admin
from .models import Flight,BookSeat, Payment

# Register your models here.
admin.site.register(Flight)
admin.site.register(BookSeat)
admin.site.register(Payment)

