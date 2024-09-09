from rest_framework import serializers
from core.models import Player, News, FormerPlayer, Gallery,Staff,Shop,Sponser

class PlayerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Player
    fields = '__all__'

class SponserSerializer(serializers.ModelSerializer):
  class Meta:
    model = Sponser
    fields = '__all__'
    


class FormerPlayerSerializer(serializers.ModelSerializer):
  class Meta:
    model = FormerPlayer
    fields = '__all__'

class GallerySerializer(serializers.ModelSerializer):
  class Meta:
    model = Gallery
    fields = '__all__'

class StaffSerializer(serializers.ModelSerializer):
    qualification = serializers.SerializerMethodField()
    career = serializers.SerializerMethodField()
    class Meta:
        model = Staff
        fields = '__all__'

    def get_qualification(self, obj):
        qualifications = obj.qualification.split('\\n')
        return '\n'.join(qualifications)
    
    def get_career(self, obj):  # Fix the typo here
        career_lines = obj.career.split('\\n')
        return '\n'.join(career_lines)
    
class ShopSerializer(serializers.ModelSerializer):
  class Meta:
    model = Shop
    fields = '__all__'

class NewsSerializer(serializers.ModelSerializer):
  class Meta:
    model = News
    fields = '__all__'