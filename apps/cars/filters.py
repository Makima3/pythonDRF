from django.http import QueryDict
from django.db.models import QuerySet
from rest_framework.exceptions import ValidationError
from .models import CarModel


def filter_cars(query: QueryDict) -> QuerySet:

    qs = CarModel.objects.all()
    for k, v in query.items():
        match k:
            case 'year__gt':
                qs = qs.filter(year__gt=v).order_by('-year').reverse()
            case 'year__lt':
                qs = qs.filter(year__lt=v)
            case 'year__lte':
                qs = qs.filter(year__lte=v)
            case 'year__gte':
                qs = qs.filter(year__gte=v)
            case 'volume_engine__gte':
                qs = qs.filter(volume_engine__gte=v)
            case 'volume_engine__lte':
                qs = qs.filter(volume_engine__lte=v)
            case 'volume_engine__gt':
                qs = qs.filter(volume_engine__gt=v)
            case 'volume_engine__lt':
                qs = qs.filter(volume_engine__lt=v)
            case 'color__end':
                qs = qs.filter(color__iendswith=v)
            case 'color__start':
                qs = qs.filter(color__istartswith=v)
            case 'color__contains':
                qs = qs.filter(color__contains=v)
            case 'brand__end':
                qs = qs.filter(brand__iendswith=v)
            case 'brand__start':
                qs = qs.filter(brand__istartswith=v)
            case 'brand__contains':
                qs = qs.filter(brand__contains=v)
            case _:
                raise ValidationError({'Details': f'Invalid value for query: {k}'})
    return qs
