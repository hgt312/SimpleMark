from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


# 用户信息模型
class UserProfile(AbstractUser):
    mobile = models.CharField(verbose_name="手机号码", max_length=20)
    count = models.IntegerField(verbose_name="工作统计", default=0)

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
