from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from thing.serializers import ThingSerializer
from thing.models import Thing, File, Category, PriceType, Type, More, Contact, Comment

class ThingViewset(viewsets.ModelViewSet):
    serializer_class = ThingSerializer
    permission_classes_by_action = {
        'post': [permissions.IsAuthenticated],
        'get': [permissions.AllowAny],
    }
    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]

    def post(self, request):
        name = request.data.get('name')
        category_id = request.data.get('category_id')
        city_id = request.data.get('city_id')
        type_id = request.data.get('type_id')
        price_type_id = request.data.get('price_type_id')
        price_from = request.data.get('price_from', 15)
        image_file = request.data.get('image_file')
        description = request.data.get('description')
        if not name or not type_id or not category_id or not price_type_id or not image_file or not city_id:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        thing = Thing(name=name, category_id=category_id, city_id=city_id, type_id=type_id, price_type_id=price_type_id, created_by=request.user, price_from=price_from, description=description)
        thing.save()
        file = File(thing=thing, key='main_image', file=image_file)
        file.save()
        additional_image_files = request.data.getlist('additional_image_files')
        if additional_image_files:
            for image_file in additional_image_files:
                if image_file == 'null':
                    continue
                file = File(thing=thing, key='additional_image', file=image_file)
                file.save()
        return Response(status=status.HTTP_200_OK)

    def get(self, request, id):
        thing = Thing.objects.get(pk=id)
        if thing is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(thing)
        data = serializer.data
        contactable = 'none'
        commentable = 'none'
        if request.user.is_authenticated:
            if thing.created_by_id == request.user.id:
                pass
            else:
                sender_id = request.user.id
                try:
                    contact = Contact.objects.get(thing_id=id, sender_id=sender_id)
                    contactable = 'already'
                except:
                    contactable = 'allow'
        if request.user.is_authenticated:
            commented_by_id = request.user.id
            if thing.created_by_id == request.user.id:
                pass
            else:
                try:
                    comment = Comment.objects.get(thing_id=id, commented_by_id=commented_by_id)
                    commentable = 'already'
                except:
                    commentable = 'allow'
        return Response({'data': data, 'contactable': contactable, 'commentable':commentable}, status=status.HTTP_200_OK)

