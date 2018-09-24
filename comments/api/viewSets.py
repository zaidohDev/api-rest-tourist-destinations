from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from comments.models import Comment
from comments.api.serializers import CommentSerializer


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated, )
    # authentication_classes = (TokenAuthentication,)
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('user', 'approved')
