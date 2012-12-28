import subprocess

from celery.decorators import task
from django.conf import settings
import requests


def http_checker(service):
    """GET on the provided URL. It should return a [2-4][0-9]{2}"""
    verify_ssl = getattr(settings, 'VERIFY_SSL', True)
    try:
        resp = requests.get(service.connection_string, verify=verify_ssl)
        if resp.status_code >= 500:
            service.update_status('Down', resp.status_code)
        else:
            service.update_status('Up', resp.status_code)
    except requests.exceptions.RequestsException as e:
        service.update_status('Down', e.message)

check_https = task(http_checker)
check_http = task(http_checker)


@task
def check_ping(service):
    """Should ping service.host"""
    res = subprocess.call(('/bin/ping -c 5 -i 0.5  -w 5 %s' %
                     service.connection.hostname).split())
    if res == 0:
        service.update_status('Up', "ping okay")
    else:
        service.update_status('Down', "ping failed")
