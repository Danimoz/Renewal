from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from .models import Trademark, Container
from django.core.paginator import Paginator
from .filters import ContainerFilter, TrademarkFilter
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.utils import timezone
import datetime

# Create your views here.
def home(request):
    return render(request, 'app/home.html')

@login_required
def dashboard(request):
    return render(request, 'app/dashboard.html')

@login_required
def trademark(request):
    trads = Trademark.objects.all()
    tradtot = Trademark.objects.count()
    prodren = Trademark.objects.filter(renewalDoc__exact='').count()
    expi = [x.id for x in trads if x.shelfLife - timezone.now() <= datetime.timedelta(days=185)]
    exp = Trademark.objects.filter(id__in=expi).count()
    trexpired = Trademark.objects.filter(id__in=expi).order_by('-dateRenewed')
    paginator = Paginator(trads, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    myFilter = TrademarkFilter(request.GET, queryset=trads)
    trads = myFilter.qs
    context = {'trads':trads, 'page_obj':page_obj, 'trexpired':trexpired, 'tradtot':tradtot, 'exp':exp, 'prodren':prodren, 'myFilter':myFilter}
    return render(request, 'app/trademark.html', context)

@login_required
def container(request):
    cont = Container.objects.all()
    conttot = Container.objects.count()
    prodren = Container.objects.filter(receiptDoc__exact='').count()
    expi = [x.id for x in cont if x.expiryDate - timezone.now() <= datetime.timedelta(days=185)]
    exp = Container.objects.filter(id__in=expi).count()
    trexpired = Container.objects.filter(id__in=expi).order_by('-dateRenewed')
    paginator = Paginator(cont, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    maiFilter = ContainerFilter(request.GET, queryset=cont)
    cont = maiFilter.qs
    context = {'cont':cont, 'page_obj':page_obj, 'conttot':conttot, 'exp':exp, 'trexpired':trexpired, 'prodren':prodren, 'maiFilter':maiFilter}
    return render(request, 'app/container.html', context)

class TrademarkCreateView(LoginRequiredMixin, CreateView):
    model = Trademark
    fields = ['trademarkName', 'trademarkClass']
    success_url = '/dashboard'

    def form_valid(self, form):
        form.instance.uploadedBy = self.request.user
        return super().form_valid(form)

class ContainerCreateView(LoginRequiredMixin, CreateView):
    model = Container
    fields = ['productName', 'containerNo', 'agentName']
    success_url = '/dashboard'

    def form_valid(self, form):
        form.instance.uploadedBy = self.request.user
        return super().form_valid(form)

class TrademarkUpdateView(LoginRequiredMixin, UpdateView):
    model = Trademark
    fields = ['trademarkName', 'trademarkClass', 'acknowledgeDoc', 'acceptanceDoc', 'cert', 'renewalDoc', 'dateRenewed']
    success_url = '/trademark'

    def form_valid(self, form):
        form.instance.uploadedBy = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        trademark = self.get_object()
        if self.request.user == trademark.uploadedBy:
            return True
        return False

class ContainerUpdateView(LoginRequiredMixin, UpdateView):
    model = Container
    fields = ['productName', 'containerNo', 'agentName', 'receiptDoc', 'endorsementDoc', 'dateRenewed', 'expiryDate']
    success_url = '/container'

    def form_valid(self, form):
        form.instance.uploadedBy = self.request.user
        return super().form_valid(form)

    def test_func(self):
        cobtainer = self.get_object()
        if self.request.user == container.uploadedBy:
            return True
        return False

class TrademarkDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Trademark
    success_url = '/dashboard'

    def test_func(self):
        trademark = self.get_object()
        if self.request.user == trademark.uploadedBy:
            return True
        return False

class ContainerDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Container
    success_url = '/dashboard'

    def test_func(self):
        container = self.get_object()
        if self.request.user == container.uploadedBy:
            return True
        return False

class TrademarkDetailView(DetailView, LoginRequiredMixin, UserPassesTestMixin):
    model = Trademark
    template_name = 'app/tradview.html'
    context_object_name = 'trads'

class ContainerDetailView(DetailView, LoginRequiredMixin, UserPassesTestMixin):
    model = Container
    template_name = 'app/contview.html'
    context_object_name = 'cont'


def render_pdf_view(request, *args, **kwargs):
    pk = kwargs.get('pk')
    trads = get_object_or_404(Trademark, pk=pk)
    
    template_path = 'app/pdf1.html'
    context = {'trads': trads}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
