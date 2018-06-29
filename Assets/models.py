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
    name = models.CharField(max_length=100, verbose_name="项目名")
    slug = models.CharField(max_length=100, blank=True, null=True, verbose_name="别名")
    product_name = models.ForeignKey(Product, verbose_name="所属产品线")
    pm = models.CharField(max_length=30, verbose_name="项目负责人")
    telephone = models.CharField(max_length=11, verbose_name="联系方式")
    desc = models.TextField(verbose_name="项目描述")

    def __unicode__(self):
        return self.name

    def meta:
        verbose_name="项目名称"
    

class Server(models.Model):

class Service(models.Model):
