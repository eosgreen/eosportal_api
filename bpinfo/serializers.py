from django.contrib.auth.models import User
from rest_framework import serializers

from bpinfo.models import Snippet,BlockProducer


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(
        view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ('url', 'id', 'highlight', 'owner', 'title', 'code',
                  'linenos', 'language', 'style')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    bpinfo = serializers.HyperlinkedRelatedField(
        many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'bpinfo')


class BlockProducerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = BlockProducer
        fields = ('url', 'id', 'bp_name', 'organisation', 'location', 'node_addr',
                  'port_http', 'port_ssl', 'port_p2p','block_signing_key')
