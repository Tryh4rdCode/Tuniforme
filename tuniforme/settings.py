import os
from pathlib import Path
import dj_database_url 
from dotenv import load_dotenv 

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Clave secreta para la seguridad de Django
SECRET_KEY = 'django-insecure-6ahwh6vk__&n1+x8nkdiilc5fod#9ur56w1!v-0u*k-is4$+07'

# Modo de depuración
DEBUG = True

# Hosts permitidos
ALLOWED_HOSTS = ['*']


# Aplicaciones instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',  # Asegúrate de que esto esté incluido
    'raiz.apps.RaizConfig',
    'tienda.apps.TiendaConfig',
    'usuario.apps.UsuarioConfig',
    'carro.apps.CarroConfig',
    'pedidos.apps.PedidosConfig',
    'coreapi.apps.CoreapiConfig',
    'rest_framework',  # Añadir Django REST framework
]

SITE_ID = 1

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  # Seguridad
    'django.contrib.sessions.middleware.SessionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Añadir whitenoise aquí
    'django.middleware.common.CommonMiddleware',  # Común
    'django.middleware.csrf.CsrfViewMiddleware',  # CSRF
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Autenticación
    'django.contrib.messages.middleware.MessageMiddleware',  # Mensajes
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Clickjacking
]

# Configuración de URLs
ROOT_URLCONF = 'tuniforme.urls'

# Configuración de templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Directorio de templates
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',  # Procesador de contexto de depuración
                'django.template.context_processors.request',  # Procesador de contexto de solicitud
                'django.contrib.auth.context_processors.auth',  # Procesador de contexto de autenticación
                'django.contrib.messages.context_processors.messages',  # Procesador de contexto de mensajes
                'carro.context_processor.valor_total_carro',  # Procesador de contexto del carro
            ],
        },
    },
]

# Aplicación WSGI
WSGI_APPLICATION = 'tuniforme.wsgi.application'

# Configuración de la base de datos
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Modelo de usuario personalizado
AUTH_USER_MODEL = 'usuario.Persona'

# Validadores de contraseña
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # Validador de similitud de atributos de usuario
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # Validador de longitud mínima
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # Validador de contraseñas comunes
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # Validador de contraseñas numéricas
    },
]

# Configuración de idioma y zona horaria
LANGUAGE_CODE = 'es-cl'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Configuración de archivos estáticos
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Configuración de WhiteNoise para servir archivos estáticos
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Configuración del campo de auto incremento por defecto
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configuración del motor de sesiones
SESSION_ENGINE = "django.contrib.sessions.backends.db"
SESSION_COOKIE_SECURE = True  # Para desarrollo; asegúrate de usar True en producción con HTTPS
SESSION_COOKIE_HTTPONLY = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
SESSION_COOKIE_AGE = 1209600  # 2 semanas

# URLs de inicio y cierre de sesión
LOGIN_URL = 'nsusuario:login'
LOGOUT_REDIRECT_URL = 'nsraiz:login'

# Configuración del backend de correo electrónico
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'jonatthan.medalla@gmail.com'
EMAIL_HOST_PASSWORD = 'nanx cvrs crwn gspu'
DEFAULT_FROM_EMAIL = 'jonatthan.medalla@gmail.com'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

# Configuración de archivos multimedia
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # Directorio de archivos multimedia

# Configuración de autenticación
AUTHENTICATION_BACKENDS = [
    'usuario.backends.RUTAuthBackend',
    'django.contrib.auth.backends.ModelBackend',  # Opcional para compatibilidad con autenticación por username
]

# Configuración de Transbank
TRANSBANK_API_KEY = "597055555532"  # Código de comercio para Webpay Plus en integración
TRANSBANK_API_SECRET = "579B532A7440BB0C9079DED94D31EA1615BACEB56610332264630D42D0A36B1C"
TRANSBANK_ENVIRONMENT = "integration"  # Cambiar a "production" para producción
TRANSBANK_RETURN_URL = 'https://tuniforme.onrender.com/pedidos/transaction/commit'
TRANSBANK_FINAL_URL = 'https://tuniforme.onrender.com/pedidos/transaction/final'