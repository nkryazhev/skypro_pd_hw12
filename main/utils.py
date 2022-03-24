import json
from config import PREVIEW_LIM
from exceptions import DataLayerError


class PostsManager:
    """Class to handle common operations with posts"""

    def __init__(self, post_path):
        self.path_to_json = post_path

    def load_json(self):
        """Load posts from JSON"""
        post_list = []
        try:
            with open(self.path_to_json, 'r', encoding='utf-8') as file:
                for parsed_json in json.load(file):
                    post_list.append(Post(parsed_json['pic'], parsed_json['content']))
            return post_list
        except (FileNotFoundError, json.JSONDecodeError):
            raise DataLayerError("JSON файл ненайден или произошла ошибка при открытии файла")

    def save_json(self, post):
        """Save new post to JSON file"""
        data = {"pic": post.picture, "content": post.content}
        try:
            with open(self.path_to_json, 'r+', encoding='utf-8') as file:
                parsed_json = json.load(file)

                parsed_json.append(data)

                file.seek(0)  # Rewind to beginning of the file
                json.dump(parsed_json, file, ensure_ascii=False, sort_keys=True, indent=4)
                file.truncate() # Delete the rest if dump is smaller than original content
        except (FileNotFoundError, json.JSONDecodeError):
            raise DataLayerError("JSON файл ненайден или произошла ошибка при открытии файла")

    def get_post_by_word(self, word) -> list:
        """Function find posts that has requested words in content"""
        found_posts = []
        post_list = self.load_json()

        for post in post_list:
            if post.has_substring(word):
                found_posts.append(post)

        if found_posts:
            return found_posts


class Post:
    """Generic post class"""

    def __init__(self, picture, content):
        self.picture = picture
        self.content = content

    def has_substring(self, substring) -> bool:
        """Check if post content has requested substring"""
        if substring.lower() in self.content.lower():
            return True
        else:
            return False

    def get_preview(self) -> str:
        """Function returns post content preview string"""
        if len(self.content) > PREVIEW_LIM:
            return self.content[0:PREVIEW_LIM] + '...'
        else:
            return self.content
