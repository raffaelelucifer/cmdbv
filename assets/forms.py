#_*_encoding: utf-8 *_*

from django import forms
from django.forms import ModelForm
from assets import models

class ProductForm(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = ['name', 'slug', 'pm', 'desc']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = '产品线名称'
        self.fields['slug'].label = '别名'
        self.fields['pm'].label = '产品经理'
        self.fields['desc'].label = '简介'

class ProjectForm(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = ['name', 'slug', 'product_name', 'pm', 'telephone', 'git_url', 'desc']

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = '项目名称'
        self.fields['slug'].label = '别名'
        self.fields['product_name'].label = '所属产品线'
        self.fields['pm'].label = '负责人'
        self.fields['teltphone'].label = '联系电话'
        self.fields['git_url'].label = '代码仓库地址'
        self.fields['desc'].label = '简介'

class ServerForm(forms.ModelForm):
    class Meta:
        model = models.Server
        fields = ['name', 'ipaddress', 'mac', 'project_name', 'brand', 'CPU', 'memcache'. 'space']

    def __init__(self, *args, **kwargs):
        super(SuperForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = '主机名称'
        self.fields['ipaddress'].label = 'IP地址'
        self.fields['mac'].label = 'MAC地址'
        self.fields['project_name'].label = '所属项目'
        self.fields['brand'].label = '服务器品牌'
        self.fields['CPU'].label = 'CPU型号'
        self.fields['memcache'].label = '内存'
        self.fields['space'].label = '物理内存'
        
class ServiceForm(forms.ModelForm):
    class Meta:
        model = models.Service
        fields = ['name', 'servername', 'project_name', 'status', 'desc']
        
    def __init__(self, *args, **kwargs):
        super(ServiceForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = '服务名称'
        self.fields['servername'].label = '所属服务器'
        self.fields['project_name'].label = '所属项目'
        self.fields['status'].label = '服务状态'
        self.fields['desc'].label = '简介'
