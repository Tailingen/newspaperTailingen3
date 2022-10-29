from django_filters.widgets import RangeWidget
from django_filters import FilterSet, RangeFilter
from .models import Post
from django.db import models

class PostFilter(FilterSet):
   class Meta:
       model = Post
       fields = {
           'title': ['icontains'],
           'author': ['exact'],
           'time_in': ['range'],
       }
       filter_overrides = {
           models.DateField: {
               'filter_class': RangeFilter,
               'extra': lambda f: {'widget': RangeWidget(attrs={'placeholder': 'YYYY/MM/DD'}),},
           }
       }