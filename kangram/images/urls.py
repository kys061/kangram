from django.conf.urls import url

from . import views

# /images/3/like/ POST
# 0. create the url and the view
# 1. take the id from the url
# 2. we want to find an image with this id
# 3. we want to create a like for that image

urlpatterns = [
    # url(
    #     regex=r'^all/$',
    #     view=views.ListAllImages.as_view(),
    #     name='all_images'
    # ),
    # url(
    #     regex=r'^comments/$',
    #     view=views.ListAllComments.as_view(),
    #     name='all_Comments'
    # ),
    # url(
    #     regex=r'^likes/$',
    #     view=views.ListAllLikes.as_view(),
    #     name='all_likes'
    # ),
    # GET
    url(
        regex=r'^$',
        view=views.Feed.as_view(),
        name='feed'
    ),
    # POST
    url(
        regex=r'(?P<image_id>\d+)/likes/$',
        view=views.LikeImage.as_view(),
        name='like_image'
    ),
    # POST
    url(
        regex=r'(?P<image_id>\d+)/unlikes/$',
        view=views.UnLikeImage.as_view(),
        name='unlike_image'
    ),
    # POST
    url(
        regex=r'(?P<image_id>\d+)/comments/$',
        view=views.CommentOnImage.as_view(),
        name='comment_image'
    ),
    # delete
    url(
        regex=r'comments/(?P<comment_id>\d+)/$',
        view=views.Comment.as_view(),
        name='comment'
    ),
    # for testing query parameters...
    url(
        regex=r'p',
        view=views.ParamTest.as_view(),
        name='test_param'
    ),

]






