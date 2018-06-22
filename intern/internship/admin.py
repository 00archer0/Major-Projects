from django.contrib import admin

# Register your models here.
from .models import Interintrnsip_2018,FeedBack
from import_export.admin import ImportExportModelAdmin
# Register your models here.

from import_export import resources
class internResource(resources.ModelResource):
    class Meta:
        model = Interintrnsip_2018


    
class InternAdmin(ImportExportModelAdmin):
    resource_class = internResource
    #date_hierarchy = 'publication_date'
    search_fields = ['Name']
    empty_value_display = '-empty-'
    list_filter = ('Assigned_Department','Status')
    list_display = ['Name', 'Email', 'Phone', 'CurrentCity',
                    'Institute', 'Degree',
                    'Stream', 'Choosed_Department', 'Current_Year_Of_Graduation',
                    'Performance_PG', 'Performance_UG', 'Performance_10', 'Performance_12', 
                    'Link_to_application',
                    'Assigned_Department', 'Status', 'Assigned_Username', 'Assigned_Password']
    list_editable = ( 'Assigned_Department', 'Status',  )
    
class feedback(ImportExportModelAdmin):
    
    #date_hierarchy = 'publication_date'
    search_fields = ['Name']
    empty_value_display = '-empty-'
    list_filter = ['Post']
    list_display = ['Name', 'Feedback','Email', 'Phone', 'Department',
                    'Post', 'Others',]
       
    
    
admin.site.register(Interintrnsip_2018,InternAdmin)
admin.site.register(FeedBack,feedback)    