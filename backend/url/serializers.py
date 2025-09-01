from rest_framework import serializers
from .models import URL
from datetime import timedelta

class URLSerializer(serializers.ModelSerializer):
    url = serializers.URLField(source='original_url') 
    shortLink = serializers.SerializerMethodField()
    expiry = serializers.SerializerMethodField()

    class Meta:
        model = URL
        fields = ['url', 'shortcode', 'validity', 'created_at', 'shortLink', 'expiry']
        extra_kwargs = {
            'shortcode': {'required': False},
            'validity': {'required': False},
        }

    def get_shortLink(self, obj):
        request = self.context.get('request')
        host = request.get_host() if request else 'localhost'
        return f"https://{host}/{obj.shortcode}"

    def get_expiry(self, obj):
        expiry_time = obj.created_at + timedelta(minutes=obj.validity)
        return expiry_time.isoformat() + 'Z'
    
