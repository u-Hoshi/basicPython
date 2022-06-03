# Serializerとは、クエリセットやモデルインスタンスのような複雑なデータをJSON形式のフォーマットに変換する

from rest_framework import serializers
from jobs.models import JobOffer


class JobOffersSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobOffer
        fields = "__all__"
