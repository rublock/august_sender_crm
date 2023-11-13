#!/bin/bash
source /var/www/august_sender_crm/venv/bin/activate
exec gunicorn -c "/var/www/august_sender_crm/config/gunicorn_config.py" config.wsgi
