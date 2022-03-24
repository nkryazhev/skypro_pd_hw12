from config import UPLOAD_FOLDER, VALID_PIC_FILETYPES
from exceptions import PictureWrongFileType


def save_picture_to_uploads(picture):
    """Function saves picture to uploads folder and return link to the picture"""
    file_name = picture.filename
    file_type = file_name.split('.')[-1]

    if file_type not in VALID_PIC_FILETYPES:
        raise PictureWrongFileType("Неправильный тип файла изображения")

    picture.save(f"./{UPLOAD_FOLDER}/{file_name}")

    return f'{UPLOAD_FOLDER}/{file_name}'
