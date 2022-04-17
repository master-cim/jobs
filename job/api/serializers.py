from rest_framework import serializers
from mill_decision.models import Posting, Client, Message
from rest_framework.validators import UniqueTogetherValidator


class MessageSerializer(serializers.ModelSerializer):
    id_client = serializers.SlugRelatedField(
        read_only=True,
        slug_field='id'
    )
    id_posting = serializers.SlugRelatedField(
        read_only=True,
        slug_field='id')

    class Meta:
        model = Message
        fields = '__all__'


class PostingSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Posting


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ('id', 'phone', 'mobile_code', 'tag', 'timezone')
