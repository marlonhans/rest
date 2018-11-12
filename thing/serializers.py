from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Category, City, Thing, PriceType, Type, File, More, Comment, Contact
from system.models import Profile
from django.db.models import Avg

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ThingSerializer(serializers.ModelSerializer):
    main_image__path = serializers.SerializerMethodField()
    type__name = serializers.SerializerMethodField()
    created_by__name = serializers.SerializerMethodField()
    created_by__phone = serializers.SerializerMethodField()
    city__name = serializers.SerializerMethodField()
    category__name = serializers.SerializerMethodField()
    price_type__name = serializers.SerializerMethodField()
    more = serializers.SerializerMethodField()
    additional_image_paths = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField()
    contact_count = serializers.SerializerMethodField()
    score_average = serializers.SerializerMethodField()

    class Meta:
        model = Thing
        fields = '__all__'

    def get_comment_count(self, obj):
        return len(Comment.objects.filter(thing=obj))
    def get_contact_count(self, obj):
        return len(Contact.objects.filter(thing=obj))
    def get_score_average(self, obj):
        avg = Comment.objects.filter(thing=obj).aggregate(Avg('score'))
        return avg['score__avg']
    def get_comments(self, obj):
        comments_ = []
        comments = Comment.objects.filter(thing=obj).order_by('-commented_on','-id')
        for comment in comments:
            commentor_name = comment.commented_by.first_name+' '+comment.commented_by.last_name
            profile = Profile.objects.get(user=comment.commented_by)
            commentor_photo = 'profile/__no_name__.jpg'
            if profile.photo:
                commentor_photo = profile.photo.name
            comments_.append({
                'description': comment.description,
                'score': comment.score,
                'commented_on': comment.commented_on,
                'commentor.name': commentor_name,
                'commentor.photo': commentor_photo,
            })
        return comments_
    def get_additional_image_paths(self, obj):
        additional_image_paths = []
        files = File.objects.filter(thing=obj, key='additional_image')
        if files is not None:
            for file in files:
                additional_image_paths.append(file.file.name)
        return additional_image_paths
    def get_main_image__path(self, obj):
        try:
            file = File.objects.get(thing=obj, key='main_image')
            return file.file.name
        except File.DoesNotExist:
            return 'project_img/__no_image__.jpg'
    def get_created_by__name(self, obj):
        user = User.objects.get(pk=obj.created_by_id)
        return user.username
    def get_created_by__phone(self, obj):
        profile = Profile.objects.get(user_id=obj.created_by_id)
        return profile.phone
    def get_category__name(self, obj):
        category = Category.objects.get(pk=obj.category_id)
        return category.name
    def get_city__name(self, obj):
        city = City.objects.get(pk=obj.city_id)
        return city.name
    def get_type__name(self, obj):
        type = Type.objects.get(pk=obj.type_id)
        return type.name
    def get_price_type__name(self, obj):
        priceType = PriceType.objects.get(pk=obj.price_type_id)
        return priceType.name
    def get_more(self, obj):
        mores = More.objects.filter(thing=obj)
        data = {}
        for more in mores:
            data[more.key] = more.value
        return data

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'
        
class PriceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceType
        fields = '__all__'

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'
