from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import generics


from mill_decision.models import Posting, Client, Message
from .serializers import PostingSerializer, ClientSerializer
from .serializers import MessageSerializer


class ClientViewSet(viewsets.ModelViewSet):
    """Клиентов могут создавать и редактировать
    только авторизованные пользователи"""
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    permission_classes = (IsAuthenticated,)


class PostingViewSet(viewsets.ModelViewSet):
    """
    Публикации могут создавать и редактировать
    только авторизованные пользователи
    """
    queryset = Posting.objects.all()
    serializer_class = PostingSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = LimitOffsetPagination
    ordering_fields = '__all__'
    ordering = ('pub_date',)


# class PostingList(generics.ListCreateAPIView):
#     queryset = Posting.objects.all()
#     serializer_class = PostingSerializer
#     permission_classes = (IsAuthenticated,)


# class PostingDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Posting.objects.all()
#     serializer_class = PostingSerializer
#     permission_classes = (IsAuthenticated,)


class MessageViewSet(viewsets.ModelViewSet):
    """ Рассылки могут создавать и редактировать
    только авторизованные пользователи"""
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        message = get_object_or_404(Message)
        return message.all()

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            post=get_object_or_404(Message, id=self.kwargs.get('post_id'))
        )
