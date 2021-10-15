from django import template
from django.db.models import Count, F
from django.core.cache import cache

from news.models import Category
register = template.Library()


@register.simple_tag(name='get_list_categories')
def get_categories():
    return Category.objects.annotate(cnt=Count('news')).filter(cnt__gt=0)

@register.inclusion_tag('news/list_categories.html')
def show_categories(arg1='Hello', arg2='Wrodls'):
    
    # categories = Category.objects.annotate(cnt=Count('news')).filter(cnt__gt=0)
    categories = Category.objects.annotate(cnt=Count('news')).filter(cnt__gt=0)
    return {'categories': categories, "arg1": arg1, "arg2": arg2}