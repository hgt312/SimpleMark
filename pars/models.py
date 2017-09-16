from django.db import models

from users.models import UserProfile

# Create your models here.


# 段落信息模型
class Paragraph(models.Model):
    id = models.CharField(verbose_name="id", max_length=30, primary_key=True)
    paragraph = models.TextField(verbose_name="段落内容", default="")
    count = models.IntegerField(verbose_name="计数", default=0)

    class Meta:
        verbose_name = "段落信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.id)


# 提交结果模型
class Result(models.Model):
    question = models.TextField(verbose_name="问题内容")
    answer = models.TextField(verbose_name="答案内容")
    paragraph_id = models.CharField(verbose_name="id", max_length=30, null=True, blank=True)
    paragraph = models.TextField(verbose_name="段落")
    user = models.ForeignKey(UserProfile, verbose_name="用户")

    class Meta:
        verbose_name = "提交结果"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.username + '-' + self.paragraph_id

    def save(self, *args, **kwargs):
        try:
            paragraph = Paragraph.objects.get(id=self.paragraph_id)
            paragraph.count += 1
            paragraph.save()
            user = UserProfile.objects.get(id=self.user.id)
            user.count += 1
            user.save()
        except Exception as e:
            pass
        super(Result, self).save(*args, **kwargs)

