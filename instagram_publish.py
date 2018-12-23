from common_tools import get_image_directory
from instabot import Bot
from os import getenv
from os import listdir
from os.path import isfile
from os.path import join
from dotenv import load_dotenv

load_dotenv()


def instagram_login():
    inst_login = getenv("INST_LOGIN")
    inst_passwd = getenv("INST_PASSWD")
    bot.login(username=inst_login, password=inst_passwd)


def upload_photo(image_files):
    for image in image_files:
        bot.upload_photo(image)


def get_image_files_list(path_to_images):
    only_files = [join(image_dir, file)
                  for file in listdir(path_to_images)
                  if isfile(join(image_dir, file))]
    only_jpg_files = [file for file
                      in only_files
                      if file.endswith('.jpg')]
    return only_jpg_files


if __name__ == '__main__':
    image_dir = get_image_directory(dir_name="images")
    if not image_dir:
        exit("Permission problems!")
    image_files = get_image_files_list(image_dir)
    bot = Bot()
    instagram_login()
    upload_photo(image_files)
    bot.logout()

