from rest_framework import serializers
from app.models import Builder

class BuilderSerializer(serializers.Serializer):
    name = serializers.CharField()
    fixt_brand = serializers.CharField()
    markup = serializers.FloatField()
    base_trap_price = serializers.IntegerField()
    base_house_color = serializers.CharField()
    kitchen_faucet = serializers.CharField()
    garbage_disposal = serializers.CharField()
    closet = serializers.CharField()
    closet_seat = serializers.CharField()
    pedestal_lav = serializers.CharField()
    base_pri_lav_faucet = serializers.CharField()
    base_sec_lav_faucet = serializers.CharField()
    base_shower_trim = serializers.CharField()
    base_ts_trim = serializers.CharField()
    water_heater = serializers.CharField()
    sewer_line = serializers.IntegerField()
    water_line = serializers.IntegerField()