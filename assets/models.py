#_*_ coding: utf-8 _*_
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import sys
 
reload(sys)
sys.setdefaultencoding('utf8')

#SERVICE_BOOL_CHOICES = ((True, u"启动"), (False, u"停止"))

#@python_2_unicode_compatible
#class Server_Brand(models.Model):
#    name = models.CharField(max_length=50)
#
#    def __str__(self):
#        return self.name

server_brand = (
    (0, u"亚马逊云"),
    (1, u"阿里云"),
    (2, u"腾讯云"),
    (3, u"华为云"),
    (4, u"七牛云"),
)

@python_2_unicode_compatible
class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    pm = models.CharField(max_length=30)
    desc = models.TextField()
    
    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Project(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, blank=True, null=True)
    product_name = models.ForeignKey(Product)
    pm = models.CharField(max_length=30)
    telephone = models.CharField(max_length=11)
    git_url = models.URLField()
    desc = models.TextField()

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Server(models.Model):
    name = models.CharField(max_length=100)
    ipaddress = models.CharField(max_length=30, null=False)
    mac = models.CharField(max_length=30, blank=True, null=True)
    project_name = models.ManyToManyField(Project, null=False)
    brand = models.IntegerField(choices=server_brand)
    CPU = models.CharField(max_length=30)
    memcache = models.CharField(max_length=10, blank=False, null=False)
    space = models.CharField(max_length=10, blank=False, null=False)
    
    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Service(models.Model):
    name = models.CharField(max_length=50)
    server_name = models.ForeignKey(Server)
    project_name = models.ManyToManyField(Project, null=False)
    status = models.BooleanField()  
    desc = models.TextField()

    def __str__(self):
        return self.name















