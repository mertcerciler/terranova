

SECRET_KEY = 'd1f9hifjr9du%zrc0dsjmvdwu^qyg=(@k)fyewqchq8yndfsy6buv5&#a!9=k42&+y$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False 

ALLOWED_HOSTS = ['165.22.199.218', 'terranovahayat.com', 'www.terranovahayat.com' ]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'terranova_prod',
        'USER': 'dbadmin',
        'PASSWORD': 'abc123!',
        'HOST': 'localhost'
    }
}




