from django.contrib import admin
from .models import *

admin.site.register(Test)
admin.site.register(Section)
admin.site.register(Question)
admin.site.register(Passage)
admin.site.register(Choice)
admin.site.register(Explanation)
admin.site.register(Answer)
admin.site.register(TotalScore)