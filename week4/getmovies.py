"""
利用The Movie DB（https://www.themoviedb.org）提供的API接口获取周星驰及其相关演员的基本信息和参演电影的基本信息。
"""
import requests
import json
import re
import time
from tradition2simple import traditional2simple


api_key = '05e2d11033dddf7ebf8a9bb3fba94dc0'
person_detail_url = 'https://api.themoviedb.org/3/person/{person_id}?api_key={api_key}&language=zh-cn'
movie_cast_url = 'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={api_key}'
person_movie_detail_url = 'https://api.themoviedb.org/3/person/{person_id}/movie_credits?api_key={api_key}&language=zh-cn'
all_movie_genres_url = 'https://api.themoviedb.org/3/genre/movie/list?api_key={api_key}&language=zh-cn'
chinese_pattern = re.compile(u"[\u4e00-\u9fa5]+")   # 用于查找汉字，选取演员的中文名

movies_nt=open('./movies.nt','a',encoding='utf-8')

def get_all_genres():
    """
    获取所有的电影类型
    :return:
    """
    r = requests.get(all_movie_genres_url.format(api_key=api_key))
    json_result = json.loads(r.content)
    genres = json_result['genres']
    genre_list = list()

    for g in genres:
        genre_list.append((g['id'], g['name']))

    return genre_list


def get_movie_cast(movie_id):
    # type: (int) -> list
    """
    获取此电影所有参演演员的ID
    :param movie_id:
    :return:
    """
    cast_list = list()
    r = requests.get(movie_cast_url.format(movie_id=movie_id, api_key=api_key))
    json_result = json.loads(r.content)
    movie_cast = json_result['cast']

    for cast in movie_cast:
        cast_list.append(cast['id'])

    return cast_list


def get_person_detail(person_id):
    """
    获取该演员的基本信息
    :param person_id:
    :return:
    """
    detail_list = list()
    r = requests.get(person_detail_url.format(person_id=person_id, api_key=api_key))
    json_result = json.loads(r.content)
    #英文姓名
    movies_nt.write('<person:%s> <name:en> "%s".\n' %(json_result['id'],json_result['name']))
    #中文姓名
    chinese_name=""
    for tmp in json_result['also_known_as']:
        if chinese_pattern.search(tmp):
            chinese_name=tmp.strip()
    if chinese_name:
        movies_nt.write('<person:%s> <name:cn> "%s".\n' %(json_result['id'],chinese_name))
    #简介
    #movies_nt.write("<person:%s> <type:biography> <%s>.\n" %(json_result['id'],json_result['biography'].replace("\n","\\n")))
    #性别
    movies_nt.write('<person:%s> <type:gender> "%s".\n' %(json_result['id'],json_result['gender']))
    #地区
    movies_nt.write('<person:%s> <type:place_of_birth> "%s".\n' %(json_result['id'],json_result['place_of_birth']))

def get_person_movie_credits(person_id):
    """
    获取该演员参演的所有电影的基本信息
    :return:
    """
    movie_id_list = list()
    movie_detail_list = list()
    movie_genre_list = list()

    r = requests.get(person_movie_detail_url.format(person_id=person_id, api_key=api_key))
    json_result = json.loads(r.content)
    person_movies = json_result['cast']

    for movie in person_movies:
        detail_list = list()
        title=traditional2simple.tradition2simple(movie['original_title'].strip())
        detail_list.append(title)
        #参与的影片
        movies_nt.write('<person:%s> <type:credits> "%s".\n' %(person_id,title))
        movies_nt.write('<movies:%s> <name:cn> "%s".\n' %(movie['id'],title))
        movies_nt.write('<movies:%s> <type:vote_count> %s.\n' %(movie['id'],movie['vote_count']))
        movies_nt.write('<movies:%s> <type:release_date> "%s".\n' %(movie['id'],movie['release_date']))

        try:
            detail_list.append(traditional2simple.tradition2simple(movie['overview'].strip().replace('\n', '')))
        except KeyError:
            detail_list.append(None)

        try:
            detail_list.append(movie['vote_average'])
        except KeyError:
            detail_list.append(None)

        detail_list.append(movie['id'])

        try:
            detail_list.append(movie['release_date'])
        except KeyError:
            detail_list.append(None)

        movie_id_list.append(movie['id'])
        movie_detail_list.append(tuple(detail_list))

        single_movie_pair_list = list()
        for genre_id in movie['genre_ids']:
            single_movie_pair_list.append((movie['id'], genre_id))
        movie_genre_list.append(single_movie_pair_list)

    return movie_id_list, movie_detail_list, movie_genre_list


if __name__ == '__main__':
    crawled_person_id_set = set()  # 记录获取过的人物
    crawled_movie_id_set = set()  # 记录获取过的电影

    #mysql_cursor.execute("SET FOREIGN_KEY_CHECKS = 0")

    start_time = time.time()
    # TODO 获取所有的电影类型，存入genre表中
    all_movie_genres = get_all_genres()
    #mysql_cursor.executemany(insert_genre_command, all_movie_genres)

    # TODO 初始人物设置为周星驰
    start_person_id = 57607

    person_detail = get_person_detail(start_person_id)

    print('插入周星驰个人信息......')
    print(person_detail)

    movies_id, movies_detail, movies_genres = get_person_movie_credits(start_person_id)

    person_movie_id_pair = [(start_person_id, m) for m in movies_id]

    print('插入周星驰出演的所有电影信息......')
    mg_pair = list()
    for mg in movies_genres:
        mg_pair.extend(mg)

    person_id_queue = set()

    print('获取周星驰参演电影的所有其他演员ID........')
    for m_id in movies_id:
        crawled_movie_id_set.add(m_id)  # 记录已存储周星驰所参演电影的信息

        for cast_id in get_movie_cast(m_id):
            person_id_queue.add(cast_id)
    print('获取成功......\n')

    print('获取其他演员的基本信息及参演的所有电影的信息........')
    person_detail_list = list()
    person_movies_list = list()
    person_movie_pair_list = list()
    print('共有{0}个演员的信息需要获取。'.format(len(person_id_queue)-1))

    for index, p_id in enumerate(person_id_queue):
        print('获取第{0}个演员的基本信息和其参演的所有电影的信息。'.format(index+1))
        if p_id not in crawled_person_id_set:
            person_detail_list.append(get_person_detail(p_id))
            movies_id, movies_detail, movies_genres = get_person_movie_credits(p_id)
            person_movies_list.append((movies_id, movies_detail, movies_genres))    # 添加当前演员出演的所有电影的信息
            person_movie_pair_list.extend([(p_id, m) for m in movies_id])   # 添加当前演员与其出演电影的id对
            crawled_person_id_set.add(p_id)

    print('获取成功......\n')

    #mysql_cursor.executemany(insert_person_command, person_detail_list)
    #mysql_cursor.executemany(insert_person_movie_command, set(person_movie_pair_list))

    movie_list = list()
    genre_pair_list = list()
    # TODO 保存这些演员出演的电影基本信息到movie表与movie_genre表中
    for person_movie in person_movies_list:
        movies_id, movies_detail, movies_genres = person_movie

        for index, m_id in enumerate(movies_id):
            if m_id not in crawled_movie_id_set:
                movie_list.append(movies_detail[index])
                genre_pair_list.extend(movies_genres[index])
                crawled_movie_id_set.add(m_id)
    print('共花费时间{0}s'.format(time.time() - start_time))
