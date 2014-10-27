# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from devmanage.models import Ip
from devmanage.models import Device
from django.db.models import Q
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger

each_page=2

@login_required
def ip_view(request):
    '''show ip list'''
    #del ip
    if request.method =='POST':
        ip=request.POST.getlist('post_ip')
        for i in ip:
            p=Ip.objects.get(ipaddr=i)
            p.delete()

    ip_list=Ip.objects.all().order_by('ipaddr')
    paginator=Paginator(ip_list,each_page)
    page=request.GET.get('page',1)

    try:
        show_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        show_list = paginator.page(1)
    except (EmptyPage,InvalidPage):
        # If page is out of range (e.g. 9999), deliver last page of results.
        show_list = paginator.page(paginator.num_pages)
    return render_to_response('ip_manage.html',{'username':request.user.username,'show_list':show_list,'paginator':paginator})

@login_required
def dev_view(request):
    '''show dev list'''
    if request.method =='POST':
        ip=request.POST.getlist('post_ip')
        for i in ip:
            p=Device.objects.get(ipaddr=i)
            p.delete()

    #show  Paginator
    dev_list=Device.objects.all()
    paginator=Paginator(dev_list,each_page)
    page=request.GET.get('page',1)

    try:
        show_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        show_list = paginator.page(1)
    except (EmptyPage,InvalidPage):
        # If page is out of range (e.g. 9999), deliver last page of results.
        show_list = paginator.page(paginator.num_pages)
    dev_list=Device.objects.all()
    return render_to_response('dev_manage.html',{'username':request.user.username,'show_list':show_list,'paginator':paginator})

@login_required
def add_ip(request):
    '''add ip'''
    if request.method == 'POST':
        ip=request.POST.get('ipaddr')
        if len(Ip.objects.filter(ipaddr=ip)) != 0:
            return render_to_response('add_ip.html',{'username':request.user.username,'add_error':'IP已经存在!'})
        else:
            p=Ip(
                ipaddr=request.POST.get('ipaddr'),
                hostname=request.POST.get('hostname'),
                ostype=request.POST.get('ostype'),
                ports=request.POST.get('ports'),
                application=request.POST.get('application'),
                )
            p.save()

    return render_to_response('add_ip.html',{'username':request.user.username})

@login_required
def add_dev(request):
    '''add dev'''
    if request.method =='POST':
        ip=request.POST.get('ipaddr')
        if len(Device.objects.filter(ipaddr=ip)) != 0:
            return render_to_response('add_dev.html',{'username':request.user.username,'add_error':'IP已经存在!'})
        else:
            p=Device(
                ipaddr=request.POST.get('ipaddr'),
                cpu=request.POST.get('cpu'),
                memory=request.POST.get('memory'),
                location=request.POST.get('location'),
                product=request.POST.get('product'),
                platform=request.POST.get('platform'),
                sn=request.POST.get('sn'),
                )
            p.save()

    return render_to_response('add_dev.html',{'username':request.user.username})


@login_required
def search_ip(request):
    '''search ip list'''
    if 'search' in request.GET and request.GET.get('search'):
        s_text=request.GET.get('search')
        if len(s_text) != 0:
            qset=(
                Q(ipaddr__icontains = s_text)|
                Q(hostname__icontains = s_text)|
                Q(ostype__icontains = s_text)|
                Q(ports__icontains = s_text)|
                Q(application__icontains = s_text)
                )
            ip_list=Ip.objects.filter(qset).order_by('ipaddr')
            if len(ip_list) == 0:
                return render_to_response('ip_manage.html',{'username':request.user.username,'search_error':'查找内容不存在！'})

        paginator=Paginator(ip_list,each_page)
        page=request.GET.get('page',1)
        try:
            show_list = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            show_list = paginator.page(1)
        except (EmptyPage,InvalidPage):
            # If page is out of range, deliver last page of results.
            show_list = paginator.page(paginator.num_pages)
        return render_to_response('ip_manage.html',{'username':request.user.username,'show_list':show_list,'paginator':paginator,'s_text':s_text})

@login_required
def search_dev(request):
    '''search dev list'''
    if 'search' in request.GET and request.GET.get('search'):
        s_text=request.GET.get('search')
        if len(s_text) != 0:
            qset=(
                Q(ipaddr__icontains = s_text)|
                Q(cpu__icontains = s_text)|
                Q(memory__icontains = s_text)|
                Q(location__icontains = s_text)|
                Q(product__icontains = s_text)|
                Q(platform__icontains = s_text)|
                Q(sn__icontains = s_text)
                )
            ip_list=Device.objects.filter(qset).order_by('ipaddr')
            if len(ip_list) == 0:
                return render_to_response('dev_manage.html',{'username':request.user.username,'search_error':'查找内容不存在！'})

        paginator=Paginator(ip_list,each_page)
        page=request.GET.get('page',1)
        try:
            show_list = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            show_list = paginator.page(1)
        except (EmptyPage,InvalidPage):
            # If page is out of range, deliver last page of results.
            show_list = paginator.page(paginator.num_pages)
        return render_to_response('dev_manage.html',{'username':request.user.username,'show_list':show_list,'paginator':paginator,'s_text':s_text})

@login_required
def mod_ip(request):
    if 'ip' in request.GET:
        ip=request.GET.get('ip')
        ip_info=Ip.objects.get(ipaddr=ip)

    if request.method =='POST':
        ip=request.GET.get('ip')
        Ip.objects.filter(ipaddr=ip).update(
            hostname=request.POST.get('hostname'),
            ostype=request.POST.get('ostype'),
            ports=request.POST.get('ports'),
            application=request.POST.get('application'),
            )

    return render_to_response('add_ip.html',{'username':request.user.username,'ip_info':ip_info})



@login_required
def mod_dev(request):
    if 'ip' in request.GET:
        ip=request.GET.get('ip')
        ip_info=Device.objects.get(ipaddr=ip)

    if request.method =='POST':
        ip=request.GET.get('ip')
        Device.objects.filter(ipaddr=ip).update(
            cpu=request.POST.get('cpu'),
            memory=request.POST.get('memory'),
            location=request.POST.get('location'),
            product=request.POST.get('product'),
            platform=request.POST.get('platform'),
            sn=request.POST.get('sn'),
            )

    return render_to_response('add_dev.html',{'username':request.user.username,'ip_info':ip_info})




