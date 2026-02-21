from django.db import models


class Plant(models.Model):
    scientific_name = models.CharField(max_length=255)
    common_name_zh = models.CharField(max_length=255)
    image = models.ImageField(upload_to='plants/')
    tcm_info = models.TextField(blank=True)
    feng_shui_info = models.TextField(blank=True)
    festive_info = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.common_name_zh or self.scientific_name
