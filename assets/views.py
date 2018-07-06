#_*_ coding:utf-8 _*_

from django.shortcuts import render
from assets import models
from django.template import RequestContext
from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect

def index(request):
    template = get_template('assets/index.html')
    request_context = RequestContext(request)
    request_context.push(locals())
    html = template.render(request_context)
    return HttpResponse(html)
   

