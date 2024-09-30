from django.contrib import admin
from .models import Restaurant, Dinner, Review, Reviewer

admin.site.register(Restaurant)
admin.site.register(Dinner)
admin.site.register(Review)
admin.site.register(Reviewer)
