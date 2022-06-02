# Serializerとは、クエリセットやモデルインスタンスのような複雑なデータをJSON形式のフォーマットに変換する

from dataclasses import field
from rest_framework import serializers
from jobs.models import JobOffer


class JobOffersSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobOffer
        field = "__all__"
