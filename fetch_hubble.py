import requests
from requests import ConnectionError
from urllib3.exceptions import ResponseError
from common_tools import get_file_url_extension
from common_tools import download_image
from common_tools import get_image_directory
import os


class HubbleAPIUnavailable(Exception):
    pass


def get_hubble_img_url(hubble_response_data):
    image_files = hubble_response_data["image_files"]
    image_url = image_files[0]["file_url"]
    return image_url


def get_image_data_from_hubble(image_id):
    try:
        url = "http://hubblesite.org/api/v3/image/{}".format(image_id)
        response = requests.get(url)
        if response.ok:
            return response.json()
    except (ConnectionError, ResponseError):
        return None


def get_images_data_from_hubble_collection(collection_name):
    try:
        url = "http://hubblesite.org/api/v3/images/{}".format(collection_name)
        response = requests.get(url)
        if response.ok:
            return response.json()
    except (ConnectionError, ResponseError):
        raise HubbleAPIUnavailable("Hubble api is unavailable!")


def get_huble_images_id(hubble_data):
    images_id = [img["id"] for img in hubble_data]
    return images_id


def fetch_hubble_images(image_dir, images_id):
    download_status = {}
    for image_id in images_id:
        hubble_data = get_image_data_from_hubble(image_id)
        if not hubble_data:
            print("Cannot get data for image_id={}!".format(image_id))
            continue
        hubble_img_url = get_hubble_img_url(hubble_data)
        file_extension = get_file_url_extension(hubble_img_url)
        img_filename = "{}.{}".format(image_id, file_extension)
        file_path = os.path.join(image_dir, img_filename)
        downloaded_image = download_image(hubble_img_url, file_path)
        download_status[image_id] = True if downloaded_image else False
    return download_status


if __name__ == '__main__':
    image_dir = get_image_directory(dir_name="images")
    hubble_collection = "wallpaper"
    if not image_dir:
        exit("Permission problems!")
    try:
        huble_data = get_images_data_from_hubble_collection(hubble_collection)
    except HubbleAPIUnavailable as error:
        exit(error)
    huble_images_id = get_huble_images_id(huble_data)
    hubble_downloaded_images = fetch_hubble_images(image_dir, huble_images_id)
    for image_id, status in hubble_downloaded_images.items():
        if not status:
            print("Couldn't download image_id={}".format(image_id))
    print("Images from collection - '{}' - downloaded!".format(hubble_collection))
