import requests
from requests import ConnectionError
from urllib3.exceptions import ResponseError
import os


def get_image_directory(dir_name=None):
    directory = dir_name
    if not os.path.exists(directory):
        try:
            os.makedirs(directory)
        except PermissionError:
            return None
    return os.path.abspath(directory)


def download_image(img_url=None, img_path=None):
    try:
        response = requests.get(img_url)
        with open(img_path, "wb") as file:
            file.write(response.content)
            return img_path
    except (ConnectionError, ResponseError):
        return None


def get_file_url_extension(file_url):
    separated_file_url = file_url.split("/")
    file_extension = separated_file_url[-1].split(".")[1]
    return file_extension


if __name__ == '__main__':
    pass
