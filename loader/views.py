from flask import Blueprint, request, render_template
from loader.utils import save_picture_to_uploads
from main.utils import PostsManager, Post
from config import POST_PATH
from exceptions import DataLayerError, PictureWrongFileType
import logging

# Затем создаем новый блюпринт, выбираем для него имя
loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')


@loader_blueprint.route('/post')
def add_post_form():
    logging.info("Страница добавления поста запрошена")
    return render_template("post_form.html")


@loader_blueprint.route('/add_post', methods=["POST"])
def add_post():
    logging.info("Отправлен запрос на добавления поста")
    post_manager = PostsManager(POST_PATH)

    content = request.form.get("content")
    picture = request.files.get("picture")

    if not picture or not content:
        logging.info("Отсутствует картинка или текст")
        raise DataLayerError("Отсутствует картинка или текст поста")

    try:
        picture_link = save_picture_to_uploads(picture)
        post = Post(picture_link, content)
        post_manager.save_json(post)
        logging.info(f"Пост создан")
        return render_template("post_uploaded.html", post=post)
    except PictureWrongFileType:

        logging.info(f"Неправильный тип данных изображения")
        return "Неправильный тип данных изображения"
