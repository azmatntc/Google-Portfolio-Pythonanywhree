#!/bin/bash
echo "Installing Python requirements..."
pip install -r requirements.txt

echo "Running migrations..."
python manage.py migrate

echo "Creating superuser..."
python manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'azmatntc@gmail.com', 'admin123')
    print("Superuser 'admin' created with password 'admin123'")
else:
    print("Superuser 'admin' already exists")
EOF

echo "Setup complete."
