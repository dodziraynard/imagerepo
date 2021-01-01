# Image Repo

An online repository of images where you can upload and download images.

## Environment requirements

- Python 3
- Pip

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
- Enter the code below into the `local_settings.py`

```python
SECRET_KEY = "your  app screts key"
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = 'google auth02 key'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'google auth02 secret key'
DEBUG = True
ALLOWED_HOSTS = ["localhost"]
```

## It works

- Visit the homepage
- Search for images based on their titles and tags
- Download images that users have uploaded and made available publicly

- Register using using gmail or username and password at `/accounts/register`
- Upload images at `/accounts/upload`
- Make the image public or private
- The system tags the uploaded images using AI to improve searching

- Log in and visit `/accounts`
- Delete or make your images public or private
