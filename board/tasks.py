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
    except requests.exceptions.RequestException:
        # for an unknown reason, curl may work here, and requests fail
        # so let's try it out
        skip_ssl_flag = '-k ' if not verify_ssl else ''
        p = subprocess.Popen(
            ('curl %s %s-m 3 -I' %
            (service.connection_string, skip_ssl_flag)).split(),
            stdout=subprocess.PIPE)

        res = p.communicate()[0]
        if any([status in res for status in
               ('500', '501', '502', '503', '504')]):
            service.update_status('Down', res)
        else:
            service.update_status('Up', res)


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
