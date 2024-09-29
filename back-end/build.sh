#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt

# Convert static asset files
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
python manage.py migrate

# Create your super user (check your env vars)
if [ $(echo "from django.contrib.auth.models import User; print(User.objects.filter(username='nome_do_superuser').exists())" | python manage.py shell) == "False" ]; then
    python manage.py createsuperuser --no-input
fi