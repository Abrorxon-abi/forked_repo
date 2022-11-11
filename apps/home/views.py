from .models import *
from django import template
from django.urls import reverse
from django.template import loader
from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .function.dates import (dates, date_for_filter, year, mounth)
from django.http import HttpResponse, HttpResponseRedirect
from .function.graphs import (graph_1_paymant, graph_2_paymant, graph_1_transfer, graph_2_transfer)



@login_required(login_url="/login/")
def index(request):
    week = dates(7)
    p_res = Payment.objects.filter(created_at__range = [week[1], week[0]])
    status_res = Status.objects.all()
    data = { "graph_1":{}, 'nav':{}, 'graph_2':{}, "for_list":[] } 
    for i in status_res:
        data['nav'][i.name] = 0
    graf = graph_1_paymant(x = p_res, dan=week[1], gacha=week[0])
    data['graph_1'] = graf['data']
    data['graph_2'] = graph_2_paymant(x = p_res, dan=week[1], gacha=week[0], z = data['nav'].keys())
    data['nav']["Оборот"] = graf['circulation']
    data['nav']['Приболь'] = graf['profit']    
    for_list = p_res[:20]


    for i in for_list:
        data['for_list'].append(
            {
                "id":i.id,
                "sum":i.sum,
                "date":i.created_at.strftime("%d-%m-%y %H:%M:%S")
                }
            )
    return render(request, 'home/index.html', context=data)




@login_required(login_url="/login/")
def pages(request):
    context = {}
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))



@login_required(login_url="/login/")
def transfers(request):
    sort_by = request.GET
    if sort_by:
        mounth = date_for_filter(x = sort_by)
        p_res = Transfer.objects.filter(created_at__range = [mounth[1], mounth[0]])
    else:
        mounth = dates(30)
        p_res = Transfer.objects.filter(created_at__range = [mounth[1], mounth[0]])
    data = {}
    status_res = Status.objects.all()
    data = { "graph_1":{}, 'nav':{}, 'graph_2':{}} 

    for i in status_res:
        data['nav'][i.name] = 0
    graf = graph_1_transfer(p_res, mounth[1], mounth[0])
    data['graph_1'] = graf['data']
    data['graph_2'] = graph_2_transfer(x = p_res, dan=mounth[1], gacha=mounth[0], z = data['nav'].keys())
    data['nav']["Оборот"] = graf['circulation']
    data['nav']['Приболь'] = graf['profit']

    years = year( x = Transfer.objects.first() )
    
    data['year'] = years
    return render(request, 'home/transfers.html', context=data)




@login_required(login_url="/login/")
def pay_history(request):
    sort_by = request.GET
    if sort_by:
        if sort_by['id_transfer_s'] == '0' and sort_by['id_transfer'] != '':
            p_res = Payment.objects.filter(id = int(sort_by['id_transfer']))
            p = Paginator(p_res, 1)
            page = p.page(1)
        elif sort_by['status'] != '':
            p_res = Payment.objects.filter(status__id = int(sort_by['status']))
            p = Paginator(p_res, int(sort_by['pagination']))
            page = p.page(1)

    else:
        p_res = Payment.objects.all().order_by('-created_at')
        p = Paginator(p_res, 10)
        page = p.page(1)

    id_t = [x.id for x in list(p_res.reverse())]

    status_res = Status.objects.all()
    years = year( x = Payment.objects.first() )

    data = {'status':status_res, 'years':years, 'mounth':mounth(), 'id_t':id_t}
    return render(request, 'home/payment_history.html', context=data)
    



