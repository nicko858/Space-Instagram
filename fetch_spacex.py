import requests
from requests import ConnectionError
from urllib3.exceptions import ResponseError
from common_tools import get_file_url_extension
from common_tools import download_image
from common_tools import get_image_directory
import os


def get_spacex_img_urls(spacex_latest_launch_data):
    img_urls = spacex_latest_launch_data["links"]["flickr_images"]
    return img_urls


def get_spacex_latest_launch_data():
    url = 'https://api.spacexdata.com/v3/launches/latest'
    payload = {}
    headers = {}
    try:
        response = requests.get(url,
                                headers=headers,
                                data=payload,
                                allow_redirects=False)
        if response.ok:
            return response.json()
    except (ConnectionError, ResponseError):
        return None


def fetch_spacex_last_launch(image_dir):
    spacex_latest_launch_data = get_spacex_latest_launch_data()
    if not spacex_latest_launch_data:
        return "SpaceX api is unavailable!"
    spacex_img_urls = get_spacex_img_urls(spacex_latest_launch_data)
    downloaded_images = {}
    for number, img_url in enumerate(spacex_img_urls, start=1):
        file_extension = get_file_url_extension(img_url)
        img_filename = "spacex{}.{}".format(number, file_extension)
        file_path = os.path.join(image_dir, img_filename)
        downloaded_image = download_image(img_url, file_path)
        if not downloaded_image:
            downloaded_images[img_url] = False
        else:
            downloaded_images[img_url] = True
    return downloaded_images


if __name__ == '__main__':
    image_dir = get_image_directory(dir_name="images")
    if not image_dir:
        exit("Permission problems!")
    spacex_downloaded_images = fetch_spacex_last_launch(image_dir)
    if not isinstance(spacex_downloaded_images, dict):
        exit(spacex_downloaded_images)
    for image_url, status in spacex_downloaded_images.items():
        if not status:
            print("Couldn't download image {}".format(image_url))
