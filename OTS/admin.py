from django.contrib import admin
from OTS.models import Candidate,Question,Result
# Register your models here.
mymodels=[Candidate,Question,Result]
admin.site.register(mymodels)
