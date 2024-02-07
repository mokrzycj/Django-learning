from django.contrib import admin
from .models import Appointment, Review

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'specialist', 'date', 'status')
    search_fields = ('patient__user__username', 'specialist__user__username', 'status')
    list_filter = ('status', 'date')

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('appointment', 'rating', 'comment')
    search_fields = ('appointment__specialist__user__username', 'appointment__patient__user__username', 'rating')

admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(Review, ReviewAdmin)
