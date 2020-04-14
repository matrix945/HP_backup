from django.conf.urls import url
from . import views
from . import models

urlpatterns = [
    url(r'^movie_all/(?P<page>\d*)', views.whole_list, {'model': models.Movie}, name='whole_list'),
    # url(r'^actor_all/(?P<page>\d*)', views.whole_list, {'model': models.Actor}, name='whole_list'),
    url(r'^movie_detail/(?P<id>.*)', views.detail, {'model': models.Movie}, name='movie_detail'),
    # url(r'^actor_detail/(?P<id>.*)', views.detail, {'model': models.Actor}, name='actor_detail'),
    # url(r'^search/(?P<item>.*)/(?P<query_string>.*)/(?P<page>\d*).*', views.search, name='search'),
    url(r'^seen/(?P<movie_id>.*)', views.seen, name='seen'),

    url(r'^add_seen/(?P<movie_id>.*)', views.add_seen, name='seen'),

    url(r'^add_one/(?P<movie_id>.*)', views.add_two, name='seen'),
    url(r'^add_two/(?P<movie_id>.*)', views.add_two, name='seen'),
    url(r'^add_three/(?P<movie_id>.*)', views.add_three, name='seen'),
    url(r'^add_four/(?P<movie_id>.*)', views.add_four, name='seen'),
    url(r'^add_five/(?P<movie_id>.*)', views.add_five, name='seen'),

    url(r'^recommend/(?P<movie_id>.*)', views.a_recommend, name='seen'),


    url(r'^expect/(?P<movie_id>.*)', views.expect, name='expect'),
    url(r'^add_expect/(?P<movie_id>.*)', views.add_expect, name='expect'),
    url(r'^search_suggest/(?P<query_string>.*)', views.search_suggest, name='search_suggest'),
]
