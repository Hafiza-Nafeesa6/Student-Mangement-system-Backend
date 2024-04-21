from django.contrib import admin


from django.contrib import admin
from app.models import Student, Class, Subject, Teacher, FeeVoucher, Result, ClassRoom

# Register your models with the admin site
admin.site.register(Student)
admin.site.register(Class)
admin.site.register(Subject)
admin.site.register(Teacher)
admin.site.register(FeeVoucher)
admin.site.register(Result)
admin.site.register(ClassRoom)
