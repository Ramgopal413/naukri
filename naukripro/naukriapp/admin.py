from django.contrib import admin
from .models import Job
from import_export.admin import ImportExportModelAdmin


# Register your models here.
class JobAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...

# admin.site.register(Job)
@admin.register(Job)
class JobAdmin(ImportExportModelAdmin):
    list_display = ("city", "title", "job_description", "max_salary", "min_salary", "employment_type",
                    "max_experience", "min_experience", "company", "location", "industry_type", "skills",
                    "posted_by")
    pass
