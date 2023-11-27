command = '/var/www/august_sender_crm/venv/bin/gunicorn'
python_path = '/var/www/august_sender_crm/config'
bind = '127.0.0.1:8001'
workers = 5
user = 'www'
raw_env = 'DJANGO_SETTINGS_MODULE=config.settings'
