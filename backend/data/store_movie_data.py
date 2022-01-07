# -*- coding: utf-8 -*-
import csv
import os
import sys
from app import db
from models import *
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import json

def store_movie_json():
    with open('./data/real/naver_movie_story.json', 'r', encoding="utf-8") as f:
        movies = json.load(f)
        # print(json.dumps(movies, ensure_ascii=False, indent=4))
        
        movie_id = 1
        character_id = 1
        for movie in movies['data']:
            rtime = movie['rtime'].strip()
            try:
                rtime = int(rtime[:-1])
                # print(rtime)
            except:
                # print("continue")
                continue
            # print(json.dumps(movie, ensure_ascii=False, indent=4))
            kor_title = movie['title']
            eng_title = movie['subtitle']
            image_link = movie['image']
            pub_year = movie['pubDate']
            director = movie['director']
            rating = movie['rating']
            story = movie['story']

            if kor_title and eng_title and image_link and pub_year and director and rating and story:
                db.session.add(Movie(movie['title'], movie['subtitle'], movie['image'], movie['pubDate'], movie['director'], movie['rating'], movie['story'], rtime))

            genres = movie['genre'].split()
            # print(genres)
            for genre in genres:
                db.session.add(MovieGenre(genre, movie_id))

            actors = movie['actors'][1:-1].split(', ')
            for actor in actors:
                db.session.add(ActorInMovie(actor[1:-1], movie_id))

            char_n_mbti = movie['mbti'].split()
            for cNm in char_n_mbti:
                character_name = cNm[-6]
                character_mbti = cNm[-5:-1]
                db.session.add(Character(character_mbti, character_name))
                db.session.add(CharacterInMovie(character_id, movie_id))
                character_id += 1
            movie_id += 1
    db.session.commit()


def store_chracter_image():

    with open('./data/real/naver_movie_story.json', 'r', encoding="utf-8") as f:
        characters = json.load(f)
        # print(json.dumps(movies, ensure_ascii=False, indent=4))

        for character in characters[0]:
            c = db.session.query(Character).filter(Character.name == character['role'], Character.mbti == character['mbti']).first()
            c.image_link = character['img_url']
    
    db.session.commit()
