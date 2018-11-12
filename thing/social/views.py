from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from thing.models import Contact, Comment, Stat

class ContactViewset(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        thing_id = request.data.get('thing_id')
        sender_id = request.user.id
        title = request.data.get('title')
        description = request.data.get('description')
        if not thing_id or not sender_id or not title:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        try:
            contact = Contact.objects.get(thing_id=thing_id, sender_id=sender_id)
            contact.title = title
        except:
            contact = Contact(thing_id=thing_id, sender_id=sender_id, title=title)
        if description:
            contact.description = description
        contact.save()

        return Response(status=status.HTTP_200_OK)

class CommentViewset(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        thing_id = request.data.get('thing_id')
        commented_by_id = request.user.id
        description = request.data.get('description')
        score = request.data.get('score')
        if not thing_id or not description or not score:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        try:
            comment = Comment.objects.get(thing_id=thing_id, commented_by_id=commented_by_id)
            comment.description = description
            comment.score = score
        except:
            comment = Comment(thing_id=thing_id, commented_by_id=commented_by_id, description=description, score=score)
        comment.save()

        return Response(status=status.HTTP_200_OK)

class StatViewset(viewsets.ModelViewSet):
    queryset = Stat.objects.all()
    permission_classes = [permissions.AllowAny]

    def incVisit(self, request, thing_id):
        try:
            stat = Stat.objects.get(thing_id=thing_id, key='visit_count')
            visit_count = int(stat.value) + 1
            stat.value = visit_count
        except:
            stat = Stat(thing_id=thing_id, key='visit_count', value='1')
        stat.save()
        return Response(status=status.HTTP_200_OK)

    def getVisit(self, request, thing_id):
        visit_count = 0
        try:
            stat = Stat.objects.get(thing_id=thing_id, key='visit_count')
            visit_count = int(stat.value)
        except:
            visit_count = 0
        return Response({'visit_count':visit_count}, status=status.HTTP_200_OK)