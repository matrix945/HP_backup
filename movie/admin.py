from django.contrib import admin
from movie.models import *


class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'movieid', 'rate')


class ActorAdmin(admin.ModelAdmin):
    list_display = ('name', 'actorid')


class RatingAdmin(admin.ModelAdmin):
    list_display = ('username', 'movieid',"rate","timestamp")


admin.site.register(Movie, MovieAdmin)
# admin.site.register(Actor, ActorAdmin)
admin.site.register(Rating, RatingAdmin)
