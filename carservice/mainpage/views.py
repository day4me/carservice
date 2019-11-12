from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, View
from bootstrap_datepicker_plus import DatePickerInput
from .models import Request, Services
from django.contrib.auth import get_user_model
from .forms import ServiceForm
from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse
from django.template.loader import render_to_string
import weasyprint

from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum, Count, Avg
from datetime import datetime


def home(request):
    return render(request,'mainpage/index.html')

class RequestListView(LoginRequiredMixin, ListView):
    model=Request
    template_name='users/profile.html'
    context_object_name = 'requests'
    ordering = ['date_begin']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class RequestCreateView(LoginRequiredMixin, CreateView):
    template_name='mainpage/request_form.html'
    form_class = ServiceForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        messages.success(self.request, f'Замовлення додано')
        return '/profile' # or whatever url you want to redirect to


class RequestUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Request
    form_class = ServiceForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        req = self.get_object()
        if self.request.user == req.author:
            return True
        return False

    def get_success_url(self):
        messages.success(self.request, f'Замовлення оновлено')
        return '/profile' # or whatever url you want to redirect to


class RequestDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Request

    def test_func(self):
        req = self.get_object()
        if self.request.user == req.author:
            return True
        return False

    def get_success_url(self):
        messages.success(self.request, f'Замовлення видалено')
        return '/profile' # or whatever url you want to redirect to


@staff_member_required
def AdminRequestPDF(request, pk):
    req = get_object_or_404(Request, id=pk)
    html = render_to_string('mainpage/pdf.html', {'request': req})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename=request_{}.pdf'.format(req.id)
    weasyprint.HTML(string=html).write_pdf(response,
               stylesheets=[weasyprint.CSS('https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css')])
    return response


class Chart(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'mainpage/chart.html',{})


class ChartData(APIView):
    
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        this_year = datetime.now().year
        req = Request.objects.all()
        itemss=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for request in Request.objects.filter(date_end__year=this_year, status="Оплачено").values_list('date_end__month').annotate(sm=Sum('service__price')).order_by('date_end__month'):
            if request[0] == 1:
                itemss[0] = request[1]
            elif request[0] == 2:
                itemss[1] = request[1]
            elif request[0] == 3:
                itemss[2] = request[1]
            elif request[0] == 4:
                itemss[3] = request[1]
            elif request[0] == 5:
                itemss[4] = request[1]
            elif request[0] == 6:
                itemss[5] = request[1]
            elif request[0] == 7:
                itemss[6] = request[1]
            elif request[0] == 8:
                itemss[7] = request[1]
            elif request[0] == 9:
                itemss[8] = request[1]
            elif request[0] == 10:
                itemss[9] = request[1]
            elif request[0] == 11:
                itemss[10] = request[1]
            else:
                itemss[11] = request[1]

        labels = ['Січень', 'Лютий', 'Березень', 'Квітень', 'Травень', 'Червень', 'Липень', 'Серпень', 'Вересень', 'Жовтень', 'Листопад', 'Грудень']
        #default_items = items
        data = {
            "labels": labels,
            "default": itemss
        }

        return Response(data)