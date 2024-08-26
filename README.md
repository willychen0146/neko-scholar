<h1 align="center">Neko Scholar</h1>

<div align="center">

![neko-scholar](https://github.com/user-attachments/assets/cc73292f-b2b8-49ae-8d41-05b3edd90fa2)

[![en](https://img.shields.io/badge/lang-en-red)](https://github.com/willychen0146/neko-scholar/blob/main/README.md)
[![中文](https://img.shields.io/badge/lang-中文-green.svg)](https://github.com/willychen0146/neko-scholar/blob/main/README.zh-TW.md)

Neko Scholar is a web forum designed to be a user-friendly academic discussion platform for high school and junior college students.

</div>

## Features

### Community and User Management
- **Account System**: Secure account creation and management using Django forms.
- **Messaging**: Internal messaging system facilitates seamless communication.
- **Email Integration**: Integrated with Gmail for efficient email notifications and updates.

### Post Management
- **Post Creation and Browsing**: Create, browse, and discover posts on diverse topics.
- **Markdown Support**: Utilize markdown syntax and toolbar for rich text formatting.
- **Comments and Reactions**: Engage with posts and comments through reactions and threaded discussions.
- **Post Tracking**: Bookmark and manage followed posts for quick access.

### Administration Tools
- **Content Moderation**: Efficient tools for moderators to manage and moderate content.
- **User Management**: Admin dashboard for user account management and permissions.

### Additional Features
- **Light/Dark Mode**: Enhance readability with a light/dark theme option.
- **Tagging**: Categorize posts with tags for efficient organization and search.
- **Search Functionality**: Powerful search capabilities by tags, titles, and date ranges.

## Technologies Used
### Frontend
- **Bootstrap**: Responsive UI components for modern web design.
- **jQuery**: Enhances frontend interactivity and user experience.

### Backend
- **Django**: Robust Python framework for backend development.
- **PostgreSQL**: Reliable relational database management system.

### Infrastructure
- **Amazon S3**: Secure static file storage and delivery.

## Getting Started:

### Prerequisites and dependencies
- Python 3.11
- Django 5.0.4
- PostgreSQL

### Setup and usage
1. Clone the repository.
```sh
# Clone the repository.
git clone https://github.com/willychen0146/neko-scholar.git
```

2. Run `setup_env.sh` to setup the env.

```sh
# This will create a virtual environment and install the required packages.
sh ./setup_env.sh
```

3. **(Optional)** Create a file name `.env` under `./neko-scholar/blog`, then configure Django settings for Django secret key, database, aws bucket, email integration (You can also use other database like SQLite which is the default setting of Django, or static files save location like saving locally which is also the default setting of Django, you can adjust the setting inside the `./neko-scholar/blog/settings.py` file to achieve this).

    - `.env` file configuration
        ```
        # Example of ".env" file
        SECRET_KEY= your/Django/secret/key
        DEBUG=True
        DATABASE_URL= your/database/config
        DATABASE_USER= your/database/config
        DATABASE_PASS= your/database/config
        EMAIL_HOST=smtp.gmail.com
        EMAIL_PORT=587
        EMAIL_HOST_USER= your/email/host/config
        EMAIL_HOST_PASSWORD= your/email/host/config
        AWS_ACCESS_KEY_ID= your/aws/config
        AWS_SECRET_ACCESS_KEY= your/aws/config
        AWS_STORAGE_BUCKET_NAME= your/aws/config
        ```
    - `settings.py` configuration
        ```python
        # You can adjust the setting inside the './neko-scholar/blog/settings.py'

        # Database setting
        DATABASES = {
            # Default using the sqlite3 as database locally.
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": BASE_DIR / "db.sqlite3",
            }
            # "default": dj_database_url.config(default=env('DATABASE_URL')) # Use this line instead to use Postgres or other database for production.
        }

        # SMTP Configuration (This is for the email backend settings, you can use your own email configuration)
        EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
        # EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
        # EMAIL_HOST = env('EMAIL_HOST')
        # EMAIL_PORT = env('EMAIL_PORT')
        # EMAIL_USE_TLS = True
        # EMAIL_HOST_USER = env('EMAIL_HOST_USER')
        # EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')

        # AWS S3 Bucket Configuration (This is for the S3 bucket settings, you can use your own static files save location configuration)
        # AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')
        # AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
        # AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
        # AWS_S3_FILE_OVERWRITE = False
        # AWS_DEFAULT_ACL = None
        # DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage' # Uncomment this line to use S3 bucket for media files storage
        ```

4. Make migrations (generate tables) with `python manage.py makemigrations accounts`.
5. Apply migrations with `python manage.py migrate`.
6. Start the development server using `python manage.py runserver`.

### Docker setup
You can also using Docker to launch the server directly, first download the [Docker image file](https://drive.google.com/file/d/1Ss0jQvlAzZZhTm0VW7jJZh-On0iVqoYm/view?usp=drive_link) and then build it.

```sh
# Load the Docker image file
docker load -i neko-scholar.tar

# Launch neko-scholar using Docker
docker run -p 8000:8000 neko-scholar:latest
```

### **Custom Database or Static Files (Optional)**
If you want to set up an external `database` and `static files` storage location instead of the default SQLite3 and static folder: 

- **For database:** Configure the database settings in both `settings.py` and the `.env` file. You can use PostgreSQL or another database system (We use [Render](https://render.com/) server to deploy our project and also using their PostgreSQL as our online database).
- **For static files:** Configure the static file settings in both `settings.py` and the `.env` file. You can use AWS S3 or another storage service (We use [Amazon AWS S3 Bucket](https://aws.amazon.com/tw/s3/) as our online static file storage location).

## Authors

- [@NoMercySusie](https://github.com/willychen0146)
- [@Jason-2021](https://github.com/Jason-2021)
- [@a55678891](https://github.com/a55678891)

## License

This project is licensed under the [MIT License](LICENSE).
