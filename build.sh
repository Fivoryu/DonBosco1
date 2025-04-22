set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input

python manage.py migrate

if [ "$CREATE_SUPERUSER" = "true" ]; then
  python manage.py shell << END
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username="${DJANGO_SUPERUSER_USERNAME}").exists():
    User.objects.create_superuser("${DJANGO_SUPERUSER_USERNAME}", "${DJANGO_SUPERUSER_EMAIL}", "${DJANGO_SUPERUSER_PASSWORD}")
END
fi