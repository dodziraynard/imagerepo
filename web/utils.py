import requests
from django.conf import settings
from imagerepo import local_settings
# from requests.auth import HTTPBasicAuth


def get_image_tags(image_url):
    print("URL: "+image_url)
    if settings.DEBUG:
        # since immaga cannot download the image from the localhost (your pc).
        image_url = 'https://docs.imagga.com/static/images/docs/sample/japan-605234_1280.jpg'  # dummy image
    return requests.get(
        'https://api.imagga.com/v2/tags?image_url=%s' % image_url,
        auth=(local_settings.API_KEY, local_settings.API_SECRET))
