from django.contrib import admin
from .models import UserFollows, Ticket, Review


# Register your models here.

class TicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'user')


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('ticket', 'rating', 'user')


class UserfollowsAdmin(admin.ModelAdmin):
    list_display = ('user', 'followed_user')


admin.site.register(Ticket, TicketAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(UserFollows, UserfollowsAdmin)
