import time
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from movie.models import *
from django.http import HttpResponse
import json
import math
import codecs

# from movie.initializer import search_cache, search_index

self_threshold = 0
common_threshold = 2
debug = True


def add_seen(request, movie_id):
    if request.is_ajax():
        history = Seen.objects.filter(movieid_id=movie_id, username=request.user.get_username())
        if len(history) == 0:
            movie = Popularity.objects.get(movieid_id=movie_id)
            weight = movie.weight
            movie.delete()
            new_record = Popularity(movieid_id=movie_id, weight=weight + 3)
            new_record.save()
            new_record = Seen(movieid_id=movie_id, username=request.user.get_username())
            new_record.save()
            return HttpResponse('1')
        else:
            history.delete()
            return HttpResponse('0')


def add_one(request, movie_id):
    print("Add one mark to this movie : " + str(movie_id))
    rates = Rating.objects.filter(movieid_id=movie_id, username=request.user.get_username())
    print(rates)
    timestp = int(time.time())
    if len(rates) == 0:
        print("this movie and user have not linked yet")
        new_record = Rating(username=request.user.get_username(), rate=2, movieid_id=movie_id, timestamp=timestp)
        new_record.save()
        print("succeed")
    else:
        print("u marked before")
    return HttpResponse('1')


def add_two(request, movie_id):
    print("Add two mark to this movie : " + str(movie_id))
    rates = Rating.objects.filter(movieid_id=movie_id, username=request.user.get_username())
    timestp = int(time.time())
    if len(rates) == 0:
        print("this movie and user have not linked yet")
        new_record = Rating(username=request.user.get_username(), rate=2, movieid_id=movie_id, timestamp=timestp)
        new_record.save()
        print("succeed")
    else:
        print("u marked before")
    return HttpResponse('1')


def add_three(request, movie_id):
    print("Add three mark to this movie : " + str(movie_id))
    rates = Rating.objects.filter(movieid_id=movie_id, username=request.user.get_username())
    timestp = int(time.time())
    if len(rates) == 0:
        print("this movie and user have not linked yet")
        new_record = Rating(username=request.user.get_username(), rate=3, movieid_id=movie_id, timestamp=timestp)
        new_record.save()
        print("succeed")
    else:
        print("u marked before")
    return HttpResponse('1')


def add_four(request, movie_id):
    print("Add four mark to this movie : " + str(movie_id))
    rates = Rating.objects.filter(movieid_id=movie_id, username=request.user.get_username())
    timestp = int(time.time())
    if len(rates) == 0:
        print("this movie and user have not linked yet")
        new_record = Rating(username=request.user.get_username(), rate=4, movieid_id=movie_id, timestamp=timestp)
        new_record.save()
        print("save successfully")
    else:
        print("u marked before")
    return HttpResponse('1')


def add_five(request, movie_id):
    print("Add five mark to this movie : " + str(movie_id))
    rates = Rating.objects.filter(movieid_id=movie_id, username=request.user.get_username())
    timestp = int(time.time())
    if len(rates) == 0:
        print("this movie and user have not linked yet")
        new_record = Rating(username=request.user.get_username(), rate=5, movieid_id=movie_id, timestamp=timestp)
        new_record.save()
        print("save successfully")
    else:
        print("u marked before")
    return HttpResponse('1')


def add_expect(request, movie_id):
    if request.is_ajax():
        history = Expect.objects.filter(movieid_id=movie_id, username=request.user.get_username())
        if len(history) == 0:
            movie = Popularity.objects.get(movieid_id=movie_id)
            weight = movie.weight
            movie.delete()
            new_record = Popularity(movieid_id=movie_id, weight=weight + 3)
            new_record.save()
            new_record = Expect(movieid_id=movie_id, username=request.user.get_username())
            new_record.save()
            return HttpResponse('2')
        else:
            history.delete()
            return HttpResponse('0')


@csrf_protect
def detail(request, model, id):
    items = []
    try:
        if model.get_name() == 'movie' and id != 'None':
            try:
                d = Popularity.objects.get(movieid_id=id)
                weight = d.weight
                d.delete()
                new_record = Popularity(movieid_id=id, weight=weight + 1)
                new_record.save()
            except:
                new_record = Popularity(movieid_id=id, weight=1)
                new_record.save()
            label = 'actor'
            object = model.objects.get(movieid=id)
            records = Act.objects.filter(movieid_id=id)
            if request.user.get_username() != '':
                seen_list = [str(x).split('|')[1] for x in
                             Seen.objects.filter(username=request.user.get_username())]
                expect_list = [str(y).split('|')[1] for y in
                               Expect.objects.filter(username=request.user.get_username())]
                if id in seen_list:
                    object.flag = 1
                if id in expect_list:
                    object.flag = 2
            for query in records:
                for actor in Actor.objects.filter(actorid=query.actorid_id):
                    items.append(actor)
        if model.get_name() == 'actor':
            label = 'movie'
            object = model.objects.get(actorid=id)
            records = Act.objects.filter(actorid_id=id)
            for query in records:
                for movie in Movie.objects.filter(movieid=query.movieid_id):
                    items.append(movie)
    except:
        return render(request, '404.html')
    return render(request, '{}_list.html'.format(label), {'items': items, 'number': len(items), 'object': object})


def whole_list(request, model, page):
    if page is None:
        return render(request, '404.html')
    page = int(page)
    objects = model.objects.all()
    total_page = int(math.ceil(len(objects) / 10))
    if page > total_page:
        return render(request, '404.html')
    last_item_index = 10 * page if page != total_page else len(objects)
    pages = []
    end_distance = total_page - page
    start_page_num = page - 5 if end_distance >= 5 else page - 10 + end_distance
    end_page_num = page + 5 if page > 5 else 10
    for i in range(start_page_num, end_page_num + 1):
        if 1 <= i <= total_page:
            pages.append(i)
    data = {'items': objects[10 * (page - 1):last_item_index], 'current_page': page, 'page_number': total_page,
            'pages': pages}
    return render(request, '{}_list.html'.format(model.get_name()), data)


# def search(request, item, query_string, page):
#     if item is None or query_string is None or page is None:
#         return render(request, '404.html')
#     query_string = query_string.replace("%20", " ")
#     if item == 'movie':
#         result = [search_index.data_in_memory['movie_dict'][movie_id] for movie_id in
#                   search_index.search_movie(query_string)]
#     elif item == 'actor':
#         result = [search_index.data_in_memory['actor_dict'][actor_id] for actor_id in
#                   search_index.search_actor(query_string)]
#     else:
#         return render(request, '404.html')
#     page = int(page)
#     total_page = int(math.ceil(len(result) / 10))
#     if page > total_page and total_page != 0:
#         return render(request, '404.html')
#     last_item_index = 10 * page if page != total_page else len(result)
#     pages = []
#     end_distance = total_page - page
#     start_page_num = page - 5 if end_distance >= 5 else page - 10 + end_distance
#     end_page_num = page + 5 if page > 5 else 10
#     for i in range(start_page_num, end_page_num + 1):
#         if 1 <= i <= total_page:
#             pages.append(i)
#     return render(request, item + '_search.html',
#                   {'items': result[10 * (page - 1):last_item_index], 'length': len(result),
#                    'query_string': query_string, 'current_page': page, 'page_number': total_page, 'pages': pages})


def search_suggest(request, query_string):
    result = search_cache.get(query_string)
    if result is not None:
        return HttpResponse(json.dumps(result, ensure_ascii=False))
    movie_list, actor_list = [], []
    search_result = search_index.search_suggest(query_string)
    for i, movie_id in enumerate(search_result[0]):
        movie = search_index.data_in_memory['movie_dict'].get(movie_id)
        movie_list.append({'movieid': movie.movieid, 'poster': movie.poster, 'title': movie.title})
        if i == 2:
            break
    for i, actor_id in enumerate(search_result[1]):
        actor = search_index.data_in_memory['actor_dict'].get(actor_id)
        actor_list.append({'actorid': actor.actorid, 'photo': actor.photo, 'name': actor.name})
        if i == 2:
            break
    result = {'movie': movie_list, 'actor': actor_list, 'text': query_string}
    search_cache.set(query_string, result)
    return HttpResponse(json.dumps(result, ensure_ascii=False))


@csrf_protect
def seen(request, movie_id):
    print(movie_id)  # empty
    print(request.user.get_username())
    if request.POST:
        try:
            d = Rating.objects.get(username=request.user.get_username(), movieid_id=movie_id)
            d.delete()
        except:
            return render(request, '404.html')
    records = Rating.objects.filter(username=request.user.get_username())
    movies = []
    for record in records:
        print(record)
        print(record.movieid_id)
        movies.append(Movie.objects.get(movieid=record.movieid_id))
    # TODO     made change hereeeeeeeeeeeeeeeeeeeeeeeeeeeeeee except seen
    return render(request, 'Seen.html', {'items': movies, 'number': len(movies)})


def expect(request, movie_id):
    if request.POST:
        try:
            d = Expect.objects.get(username=request.user.get_username(), movieid_id=movie_id)
            d.delete()
        except:
            return render(request, '404.html')
    records = Expect.objects.filter(username=request.user.get_username())
    movies = []
    for record in records:
        movie_id = str(record).split('|')[1]
        movies.append(Movie.objects.get(movieid=movie_id))
    return render(request, 'Seen.html', {'items': movies, 'number': len(movies)})


def a_recommend(request, movie_id):
    print("recommend function init")
    username = request.user.get_username()
    print("run recommend for this user: " + username)
    recomm = core_running(username)

    if not recomm:
        print("recommend" + " is ")

        print("user didn't pass pre alg test")
        return render(request, 'recommend.html', {'recommend_flag': False})

    movies = []
    a = Movie.objects.get(movieid=recomm[0])
    print("recommend movie id is ")
    print(a)
    movies.append(a)
    return render(request, 'recommend.html', {'items': movies, 'number': len(movies), 'recommend_flag': True})


def load_data():
    filename_user_movie = 'ratings.dat'
    filename_movie_info = 'movies.dat'

    user_movie = {}
    for line in open(filename_user_movie):
        (userId, itemId, rating, timestamp) = line.strip().split('::')
        user_movie.setdefault(userId, {})
        user_movie[userId][itemId] = float(rating)

    movies = {}
    # for line in open(filename_movieInfo):
    #     (movieId, movieTitle) = line.split('::')[0:2]
    #     movies[movieId] = movieTitle
    with codecs.open(filename_movie_info, 'r', encoding='utf8') as f:
        text = f.readlines()
    # for line in open(filename_movieInfo):

    for line in text:
        (movieId, movieTitle) = line.split('::')[0:2]
        movies[movieId] = movieTitle
    return user_movie, movies


'''
pre common test

1) Tester doesn't have enough movies -> fail // less than `self_threshold`
2) Loop through all users if nobody has enough common movies with tester fail // less than pre set `common_threshold`

return the common movies amount of all users
[1, 0, 0, 0, 0, 1, 0, 2, 1 ........]
 
'''


def pre_common_test(movieSet, tester):
    common = []
    if len(tester) < self_threshold:
        return False
    else:
        movies_value_set = movieSet.values()
        counter = 0
        for i in movies_value_set:
            for k in tester:
                if k in i:
                    counter = counter + 1
            common.append(counter)
            counter = 0

        print("common is")
        print(common)

        if max(common) < common_threshold:
            return False
        else:
            return common


'''

calculate the rank matrix. No common movies -> -1 

return [172.0, -1, -1, -1, -1, 148.0, -1, 317.0, 212.0, 1019.0, -1 ........]

'''


def cal_matrix(common, movies, tester):
    moviesCopy = dict(movies)
    iCounter = 0
    matrix = []
    rank = 0

    for i in moviesCopy:
        if common[iCounter] == 0:
            matrix.append(-1)
        else:
            rank = cal_rank(moviesCopy[i], tester)
            matrix.append(rank)
        iCounter = iCounter + 1

    print("matrix is ")
    print(matrix)
    return matrix


'''
core algorithm
 
movie: (userid , dict_rate{}) single node
tester: {'573': 3.0, '589': 4.0}

'''


def cal_rank(movies, tester):
    rank = 0
    for k in tester:
        if k in movies:
            tempCounter = (tester[k] - movies[k]) * (tester[k] - movies[k])
            rank = rank + tempCounter
    return rank


def core_running(username):
    user_movie, movies = load_data()
    # ('6040', {'573': 4.0, '589': 4.0, '1': 3.0, '2068': 4.0, '592': 2.0, '593': 5.0, '3016': 2.0, '3017': 1.0,
    # '2070': 4.0, '1419': 3.0, '2076': 5.0, '3039': 2.0, '903': 4.0, '904': 4.0, '908': 4.0, '910': 4.0, '912': 5.0,
    # '1090': 3.0, '1091': 1.0, '1094': 5.0, '562': 5.0, '1096': 4.0, '1097': 4.0})
    # user_movie is the rate pair (userid , dict_rate{})

    records = Rating.objects.filter(username=username)

    tester = {}
    # tester = {'573': 3.0, '589': 4.0, '34': 3.0, '344': 3.0, '24': 3.0, '178': 3.0}
    for record in records:
        tester.update({record.movieid_id: record.rate})

    print("tester user data is ")
    print(tester)

    com = pre_common_test(user_movie, tester)  # [1, 0, 0, 0, 0, 1, 0, 2, 1 ........]

    if not com:
        return False

    result = cal_matrix(com, user_movie, tester)  # [172.0, -1, -1, -1, -1, 148.0, -1, 317.0, 212.0, 1019.0, -1 ....]
    s = set(result)
    sorted(s)
    s.remove(-1)
    mini = min(s)  # mini is the most likely guy in userCF
    print("mini is " + str(mini))
    print(len(result) == len(com))  # com and result should be matched with each other

    # findMaxCommon = []
    tempMax = -1
    tempIndexMax = -1

    # re-organize if we have several same rank user profile we pick the most common

    for i in range(len(result)):
        if result[i] == mini:
            temp = com[i]
            if temp > tempMax:
                tempMax = temp
                tempIndexMax = i
            # findMaxCommon.append(com[i])

    print("the best index is at the postition : " + str(tempIndexMax) + " with common number of :" + str(tempMax))

    # remove_depu_list = dict(user_movie[str(tempIndexMax+1)])

    remove_depu_list = {k: v for k, v in user_movie[str(tempIndexMax + 1)].items() if k not in tester}

    aaa = {k: v for k, v in sorted(remove_depu_list.items(), key=lambda item: item[1])}

    print("recommend list contains ")
    print(aaa)
    print("\n")

    recommend_movie = aaa.popitem()

    return recommend_movie
