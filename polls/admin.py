from django.contrib import admin
from .models import Question, Option

# Register your models here.
# admin.site.register(Question)
# admin.site.register(Option)

admin.site.site_header = "Voteon Admin"
admin.site.site_title = "Voteon"
admin.site.index_title = "Welcome to Voteon Admin Section"

class OptionInline(admin.TabularInline):
    model = Option
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
    ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']})]
    inlines = [OptionInline]


admin.site.register(Question, QuestionAdmin)