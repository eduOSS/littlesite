#from django.shortcuts import render,get_object_or_404,render 
#from django.http import HttpResponseRedirect
#from django.core.urlresolvers import reverse 
#from django.views import generic 
#from punch.models import Punch, Clock 
#
## Create iyour views here.
# 
#from django.http import HttpResponse
#class IndexView(generic.ListView):
#    template_name = 'punch/index.html'
#    context_object_name = 'latest_punch_list'
#    def get_queryset(self):
#         return Punch.objects.order_by('-pub_date')[:5]
#
#class DetailView(generic.DetailView):
#    model = Punch
#    template_name = 'punch/detail.html'
from django.http import HttpResponse
from django.template import RequestContext, loader
from user.models import User,Clock
from django.shortcuts import render,get_object_or_404
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
import datetime

def index(request):
    latest_user_list = User.objects.order_by('-regi_date')[:5]
    context = {'latest_user_list':latest_user_list}
    return render(request,'user/index.html',context)

def detail(request,user_id):
    user = get_object_or_404(User,pk=user_id)
    return render(request,'user/detail.html',{'user':user})

def clock(request,users_id):
    p = get_object_or_404(User,pk=users_id)
    if p.log_num > 1:
        c_pre = get_object_or_404(Clock,id=p.log_num-1,user_id=users_id)
        #how about c_pre = p.clock_set.get(id=p.log_num-1,user_id=users_id)?
    else:
        c_pre = p.clock_set.create(clock_date=p.regi_date,clock_text="init",id=1,user_id=users_id)
        c_pre.save()

    if timezone.now() - c_pre.clock_date >= datetime.timedelta(seconds = 10):
        #c = p.clock_set.create(user_id=users_id,id=p.log_num,clock_date=timezone.now())
        c = Clock(user_id=users_id,id=p.log_num,clock_date=timezone.now())
        p.log_num += 1
        p.coins += 1
        c.save()
        p.save()
        return HttpResponseRedirect(reverse('user:results', args=(p.id,)))
    else:
        return render(request,'user/detail.html',{'user':p})

def results(request,user_id):
    user = get_object_or_404(User,pk=user_id)
    return render(request,'user/results.html',{'user':user})
