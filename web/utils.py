import requests
from django.conf import settings
from imagerepo import local_settings

# from requests.auth import HTTPBasicAuth


def get_image_tags(image_url):
    print("URL: "+image_url)
    if settings.DEBUG:
        image_url = 'https://imagerepo.pythonanywhere.com/assets/uploads/images/101_m3qcQH3.jpg'
    return requests.get(
        'https://api.imagga.com/v2/tags?image_url=%s' % image_url,
        auth=(local_settings.api_key, local_settings.api_secret))


if __name__ == "__main__":
    image_url = 'https://docs.imagga.com/static/images/docs/sample/japan-605234_1280.jpg'
    response = get_image_tags(image_url)

    if response.status_code == 200:
        if response.json().get("status").get("type") == "success":
            tags = response.json().get("result").get("tags")
            string_tags = ""
            for tag in tags:
                if float(tag.get("confidence")) > 40:
                    string_tags += f'{tag.get("tag").get("en")} '
            print(string_tags.strip())
