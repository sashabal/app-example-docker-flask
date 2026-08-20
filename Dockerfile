FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py migrate && \
    python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@test.local', 'SuperPass123!') if not User.objects.filter(username='admin').exists() else None"

EXPOSE 3478

CMD ["python", "manage.py", "runserver", "0.0.0.0:3478"]
