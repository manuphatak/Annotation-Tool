"""
Serialize Pubmed objects.
"""

# Third Party Packages
from rest_framework.serializers import HyperlinkedModelSerializer

# Annotation Tool Project
from annotation_tool.users.serlializers import UserSerializer

# Local Application
from .models import EntryMeta


class EntryUserSerializer(UserSerializer):
    """
    Remove `pubmed_entries` from User serializer.
    """

    # noinspection PyDocstring
    class Meta(UserSerializer.Meta):
        fields = tuple(field for field in UserSerializer.Meta.fields if field != 'pubmed_entries')


class EntryListSerializer(HyperlinkedModelSerializer):
    """
    Serialize pubmed entries.
    """

    class Meta:
        model = EntryMeta.model
        fields = ('url', 'pubmed_id') + EntryMeta.all_fields


class EntryDetailSerializer(HyperlinkedModelSerializer):
    """
    Serialize pubmed entry.
    """

    user = EntryUserSerializer()

    # noinspection PyDocstring
    class Meta:
        model = EntryMeta.model
        fields = ('pubmed_id',) + EntryMeta.all_fields

        depth = 1