from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from kangram.notifications import views as notification_views


from . import models, serializers
# Create your views here.


class ListAllImages(APIView):

    def get(self, request, format=None):
        all_images = models.Image.objects.all()
        serializer = serializers.ImageSerializer(all_images, many=True)

        return Response(data=serializer.data)


class ListAllComments(APIView):

    def get(self, request, format=None):
        all_comments = models.Comment.objects.all()
        serializer = serializers.CommentSerializer(all_comments, many=True)

        return Response(data=serializer.data)


class ListAllLikes(APIView):

    def get(self, request, format=None):
        all_likes = models.Like.objects.all()
        serializer = serializers.LikeSerializer(all_likes, many=True)

        return Response(data=serializer.data)


class Feed(APIView):

    def get(self, request, format=None):
        user = request.user
        following_users = user.following.all()
        image_list = []

        for following_user in following_users:
            user_images = following_user.images.all()[:1]
            print(user_images.query)
            for image in user_images:
                image_list.append(image)
            # print("{}: {}".format(following_user, following_user.images.all()[:1]))

        my_images = user.images.all()[:2]

        for image in my_images:
            image_list.append(image)

        sorted_list = sorted(image_list, key=lambda image: image.created_at, reverse=True)

        print(sorted_list)
        # print(user)
        # print(following_users)
        # print(request.query_params)
        serializer = serializers.ImageSerializer(sorted_list, many=True)

        return Response(serializer.data)


class LikeImage(APIView):

    @classmethod
    def post(cls, request, image_id, format=None):
        user = request.user
        try:
            image_founded = models.Image.objects.get(id=image_id)
        except models.Image.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        try:
            existing_like = models.Like.objects.get(creator=user, image=image_founded)
        except models.Like.DoesNotExist:
            new_like = models.Like.objects.create(creator=user, image=image_founded)
            new_like.save()
            notification_views.create_notification(
                user, image_founded.creator,
                'like', image_founded)
            return Response(status=status.HTTP_201_CREATED)
        else:
            # existing_like.delete()
            return Response(status=status.HTTP_304_NOT_MODIFIED)


class UnLikeImage(APIView):
    @classmethod
    def delete(cls, request, image_id, format=None):
        user = request.user
        try:
            image_founded = models.Image.objects.get(id=image_id)
        except models.Image.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        try:
            existing_like = models.Like.objects.get(creator=user, image=image_founded)
        except models.Like.DoesNotExist:
            # models.Like.objects.create(creator=user, image=image_founded)
            return Response(status=status.HTTP_304_NOT_MODIFIED)
        else:
            existing_like.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class CommentOnImage(APIView):

    @classmethod
    def post(cls, request, image_id, format=None):

        user = request.user
        try:
            image_founded = models.Image.objects.get(id=image_id)
        except models.Image.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.CommentSerializer(data=request.data)

        if serializer.is_valid():
            print ("valid")
            serializer.save(creator=user, image=image_founded)
            notification_views.create_notification(
                user, image_founded.creator, 'comment',
                image_founded, serializer.data['message'])

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Comment(APIView):

    @classmethod
    def delete(cls, request, comment_id, format=None):
        user = request.user
        try:
            comment = models.Comment.objects.get(id=comment_id, creator=user)
        except models.Comment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class Search(APIView):

    def get(self, request, format=None):

        hashtags = request.query_params.get('hashtags', None)

        if hashtags is not None:

            hashtags = hashtags.split(",")

            images = models.Image.objects.filter(tags__name__in=hashtags)

            serializer = serializers.UserProfileImageSerializer(images, many=True)

            return Response(data=serializer.data, status=status.HTTP_200_OK)

        else:

            return Response(status=status.HTTP_204_NO_CONTENT)


class ModerateComments(APIView):
    @classmethod
    def delete(cls, request, image_id, comment_id, format=None):

        user = request.user

        try:
            comment_to_delete = models.Comment.objects.get(
                id=comment_id, image__id=image_id, image__creator=user)
            comment_to_delete.delete()
        except models.Comment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(status=status.HTTP_204_NO_CONTENT)


class ParamTest(APIView):

    def get(self, request, format=None):
        test = request.GET['test']
        test2 = request.GET['test2']
        print(test)
        print(test2)

        return Response(status=200)
#
# def get_key(image):
#     return image.created_at


