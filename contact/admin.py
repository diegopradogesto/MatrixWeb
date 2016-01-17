from django.contrib import admin
from models import Feedback

class FeedbackAdmin(admin.ModelAdmin):
    date_hierarchy = "sent_time"
    list_display = ('name', 'twitter_account', 'email', 'sent_time')
    fields = ('name', 'twitter_account', 'email', 'subject', 'body')
    search_fields = ('name', 'twitter_account', 'email', 'subject', 'body')
    
    class Meta:
        verbose_name = "Feedback"
        verbose_name_plural = "Feedback"

admin.site.register(Feedback, FeedbackAdmin)
