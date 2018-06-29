from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="产品线")
    desc = models.TextField()
    slug = models.CharField(max_length=100, blank=True, null=True, verbose_name="别名")

    def __unicode__(self):
        return self.name

    def meta:
        verbose_name="产品线"

class Project(models.Model):
    project_name = models.CharField(amx_length=100, varbose_name="项目名")
    

class Server(models.Model):

class Service(models.Model):
