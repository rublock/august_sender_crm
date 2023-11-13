command = '/var/www/august_sender_crm/venv/bin/gunicorn'
python_path = '/var/www/august_sender_crm/config'
bind = '0.0.0.0:8001'
workers = 5
user = 'www'
raw_env = 'DJANGO_SETTINGS_MODULE=config.settings'
