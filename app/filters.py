import django_filters
from django_filters import DateFilter
from .models import *

class TrademarkFilter(django_filters.FilterSet):
    class Meta:
        model = Trademark
        fields = ['trademarkName', 'trademarkClass', 'dateCreated', 'uploadedBy']

class ContainerFilter(django_filters.FilterSet):
    class Meta:
        model = Container
        fields = ['productName', 'containerNo', 'agentName', 'dateCreated', 'uploadedBy']