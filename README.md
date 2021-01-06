# Image Repo

An online repository of images where you can upload and download images.

## Language and Libraries

- Python 3
- Django 3

## API Keys

- [Google OAuth2](https://developers.google.com/identity/protocols/oauth2) - For gmail login.
- [Imagga](https://imagga.com/) - For tagging.

## Installation

Clone this repository and open it in your prefered editor e.g. VS code.

```bash
git clone https://github.com/dodziraynard/imagerepo.git

cd imagerepo

pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate
```

## Running

- Create `local_settings.py` file in `/imagerepo/imagerepo`
- Enter the code below into the `local_settings.py` and update the keys.

```python
SECRET_KEY = "your_app_screts_key"
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = 'google_oauth2_key'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'google_auth02_secret_key'
API_KEY = 'imagga_api_key'
API_SECRET = 'imagga_secret_key'
DEBUG = True
ALLOWED_HOSTS = ["localhost"]
```

## Testing

- There are 22 tests

```bash
    python manage.py test
```

## How it works

- Visit the homepage.
- Search for images based on their titles and tags.
- Download images that users have uploaded and made available publicly.

- Register using using gmail or username and password at `/accounts/register`
- Upload images at `/accounts/upload`.
- Make the image public or private.
- The system tags the uploaded images using AI to improve searching.

- Log in and visit `/accounts` to delete or make your images public or private.

## Live demo

[https://imagerepo.pythonanywhere.com/](https://imagerepo.pythonanywhere.com/)

## Demo limitation

- Rate limiting by `pythonanywere.com` (free account) thus tagging is not working in the live demo.
- [Running locally](https://github.com/dodziraynard/imagerepo/blob/main/web/utils.py)

## Possible improvements

- Using a task queue library e.g. [django-celery](https://docs.celeryproject.org/en/stable/django/first-steps-with-django.html) and redis to tag images asynchronously.
- Generating smaller versions of the uploaded image for use as thumbnails.
