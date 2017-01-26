from django.db import models

from shared.models import OrderedModel


class Project(OrderedModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    url = models.URLField()

    axiologue_project = models.BooleanField()

    list_order = models.PositiveSmallIntegerField(blank=True, null=True)

    def __str__(self):
        return self.title

    ordering_field = 'list_order'
    def get_ordering_queryset(self):
        return self.objects.all()
