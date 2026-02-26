from django.contrib import admin
from managecash.models import *

admin.site.register(AuthUserModel)
admin.site.register(CashModel)
admin.site.register(ExpenceModel)