from django.contrib import admin
from mysite import models

# Register your models here.
class PollAdmin(admin.ModelAdmin):
    list_display = ('name','explination','poll_logo','created_at', 'enabled')
    ordering = ('-created_at',)

class PollItemAdmin(admin.ModelAdmin):
    list_display = ('poll', 'name', 'vote')
    ordering = ('poll',)

class VoteHistoryAdmin(admin.ModelAdmin):
    list_display = ('poll','pollitem', 'voter', 'vote_time')
    ordering = ('vote_time',)

admin.site.register(models.Poll, PollAdmin)
admin.site.register(models.PollItem, PollItemAdmin)
admin.site.register(models.VoteHistory, VoteHistoryAdmin)