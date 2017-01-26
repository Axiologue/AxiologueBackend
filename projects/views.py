from rest_framework import generics

from .models import Project
from .serializers import ProjectSerializer


class AxiologueProjectListView(generics.ListAPIView):
    queryset = Project.objects.filter(axiologue_project=True)
    serializer_class = ProjectSerializer


class FriendsProjectListView(generics.ListAPIView):
    queryset = Project.objects.filter(axiologue_project=False)
    serializer_class = ProjectSerializer
