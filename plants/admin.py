from django.contrib import admin
from .models import Plant

@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    # 讓後台清單顯示這三個欄位
    list_display = ('scientific_name', 'common_name_zh')
    # 增加搜尋功能
    search_fields = ('scientific_name', 'common_name_zh')