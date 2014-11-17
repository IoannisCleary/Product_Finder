from django.contrib import admin
from product_finder.models import Request,Response,User,Category

admin.site.register(Request)
admin.site.register(Response)
admin.site.register(User)
admin.site.register(Category)