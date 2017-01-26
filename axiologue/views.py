from drf_multiple_model.views import MultipleModelAPIView


from projects.models import Project
from projects.serializers import ProjectSerializer
from blog.models import Post
from blog.serializers import PostListSerializer
from events.models import Event
from events.serializers import EventListSerializer


class LandingView(MultipleModelAPIView):
    objectify = True

    queryList = [
        (
            Project.objects.filter(axiologue_project=True)[:5],
            ProjectSerializer, 'axiologue_projects'
        ),
        (
            Project.objects.filter(axiologue_project=False)[:5],
            ProjectSerializer, 'friends_projects'
        ),
        (
            Post.objects.all()[:5], PostListSerializer, 'blog'
        ),
        (
            Event.objects.order_by('-start')[:5],
            EventListSerializer, 'events'
        )
    ]
