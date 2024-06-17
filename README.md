# Blog WebApp using Django
This is a WebApp for creating and reading blogs powered by django. The file storage and static files are hosted on a Azure container.

### Home Screen
![Home Page](https://github.com/quirrelHK/Django-WebApp/blob/main/mywebapp/media/about/home.png)

### Profile Screen
![Home Page](https://github.com/quirrelHK/Django-WebApp/blob/main/mywebapp/media/about/profile.png)

## How to run the App
### Clone this repo
```console
git clone https://github.com/quirrelHK/Django-WebApp.git

cd Django-WebApp
```

### Install the requirements
```console
pip install -r requirements.txt
```
### Creating local database
```console
cd mywebapp

python manage.py makemigrations

python manage.py migrate
```

### Run the app
```
python manage.py runserver
```

### Some additional setup
#### File Storage
You would need to setup blob storage on Azure or AWS s3 for storing files. Make sure the environment variables in the `settings.py` matches the ones on the could storage. Or you can simply save the files locally by changing the default file storage and static files storage locations in the `settings.py` file.

#### Email service
You also need to provide a email host user and host password of sending password reset confirmation to a user. This can be done by going to your gmail account and look of the app password. The host password would be this password.

