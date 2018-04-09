# from django.core.urlresolvers import reverse
# from django.views.generic import DetailView, ListView, RedirectView, UpdateView
#

from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models, serializers
from kangram.notifications import views as notification_views


class Explore(APIView):

    @classmethod
    def get(cls, request, format=None):

        last_five = models.User.objects.all().order_by('-date_joined')[:5]
        serializer = serializers.ListUserSerializer(last_five, many=True)
        # User.objects.get(username=user.username)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class FollowUser(APIView):

    @classmethod
    def post(cls, request, user_id, format=None):
        user = request.user

        try:
            user_to_follow = models.User.objects.get(id=user_id)
        except models.User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        print(user_to_follow)
        user.following.add(user_to_follow)
        user.save()
        notification_views.create_notification(user, user_to_follow, 'follow')

        return Response(status=status.HTTP_200_OK)


class UnFollowUser(APIView):

    @classmethod
    def post(cls, request, user_id, format=None):
        user = request.user

        try:
            user_to_follow = models.User.objects.get(id=user_id)
        except models.User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        print(user_to_follow)
        user.following.remove(user_to_follow)
        user.save()

        return Response(status=status.HTTP_200_OK)


class UserProfile(APIView):

    @classmethod
    def get_user(cls, username):
        try:
            found_user = models.User.objects.get(username=username)
            return found_user
        except models.User.DoesNotExist:
            return None

    @classmethod
    def get(cls, request, username, format=None):

        found_user = cls.get_user(username)

        if found_user is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.UserProfileSerializer(found_user)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @classmethod
    def put(cls, request, username, format=None):

        user = request.user

        found_user = cls.get_user(username)

        if found_user is None:

            return Response(status=status.HTTP_404_NOT_FOUND)

        elif found_user.username != user.username:

            return Response(status=status.HTTP_401_UNAUTHORIZED)

        else:

            serializer = serializers.UserProfileSerializer(
                found_user, data=request.data, partial=True)

            if serializer.is_valid():

                serializer.save()

                return Response(data=serializer.data, status=status.HTTP_200_OK)

            else:

                return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserFollowers(APIView):

    @classmethod
    def get(cls, request, username, format=None):
        try:
            found_user = models.User.objects.get(username=username)
        except models.User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        print(found_user)
        user_followers = found_user.follower.all()
        serializer = serializers.ListUserSerializer(user_followers, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class UserFollowing(APIView):

    @classmethod
    def get(cls, request, username, format=None):
        try:
            found_user = models.User.objects.get(username=username)
        except models.User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        print(found_user)
        user_following = found_user.following.all()
        serializer = serializers.ListUserSerializer(user_following, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class Search(APIView):

    @classmethod
    def get(cls, request, format=None):

        username = request.query_params.get('username', None)

        if username is not None:

            users = models.User.objects.filter(username__icontains=username)

            serializer = serializers.ListUserSerializer(users, many=True)

            return Response(data=serializer.data, status=status.HTTP_200_OK)

        else:

            return Response(status=status.HTTP_404_NOT_FOUND)
# class UserDetailView(LoginRequiredMixin, DetailView):
#     model = User
#     # These next two lines tell the view to index lookups by username
#     slug_field = 'username'
#     slug_url_kwarg = 'username'
#
#
# class UserRedirectView(LoginRequiredMixin, RedirectView):
#     permanent = False
#
#     def get_redirect_url(self):
#         return reverse('users:detail',
#                        kwargs={'username': self.request.user.username})
#
#
# class UserUpdateView(LoginRequiredMixin, UpdateView):
#
#     fields = ['name', ]
#
#     # we already imported User in the view code above, remember?
#     model = User
#
#     # send the user back to their own page after a successful update
#     def get_success_url(self):
#         return reverse('users:detail',
#                        kwargs={'username': self.request.user.username})
#
#     def get_object(self):
#         # Only get the User record for the user making the request
#         return User.objects.get(username=self.request.user.username)
#
#
# class UserListView(LoginRequiredMixin, ListView):
#     model = User
#     # These next two lines tell the view to index lookups by username
#     slug_field = 'username'
#     slug_url_kwarg = 'username'

