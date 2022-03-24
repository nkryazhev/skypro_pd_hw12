# main / views.py
from flask import Blueprint, request, render_template
from main.utils import PostsManager
from config import POST_PATH
from exceptions import DataLayerError
import logging

# Init new blueprint
main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


# view /
@main_blueprint.route('/')
def page_index():
    logging.info("Главная страница запрошена")
    return render_template("index.html")


# view /search
@main_blueprint.route('/search')
def page_search():

    req = request.args['s']
    logging.info(f"Запрошен поиск постов по слову: {req}")

    post_manager = PostsManager(POST_PATH)

    try:
        posts_by_word = post_manager.get_post_by_word(req)
        if posts_by_word:
            logging.info(f"Найдено {len(posts_by_word)} постов")
            return render_template("post_list.html", query=req, posts=posts_by_word)
        else:
            logging.info(f"Постов не найдено")
            return f"По запросу {req} ничего ненайдено"
    except DataLayerError:
        logging.info(f"Возникла ошибка с чтением из файла")
        return "Ошибка чтения файла с данными"
