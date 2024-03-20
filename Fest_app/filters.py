import django_filters

from Fest_app.models import participant 


class ContestFilter(django_filters.FilterSet):
    class Meta:
        model=participant
        fields=['Contest_Name']




