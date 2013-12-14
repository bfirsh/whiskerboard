from datetime import datetime, date, timedelta
from django.db import models
from urlparse import urlparse


class Service(models.Model):
    """
    A service to track.
    """
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    description = models.CharField(max_length=255)
    connection_string = models.CharField(max_length=200, null=True)

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('service', [self.slug])

    @property
    def connection(self):
        return urlparse(self.connection_string)

    def last_five_days(self):
        """
        Used on home page.
        """
        lowest = Status.objects.default()
        severity = lowest.severity

        yesterday = date.today() - timedelta(days=1)
        ago = yesterday - timedelta(days=5)

        events = self.events.filter(start__gt=ago, start__lt=yesterday)

        stats = {}

        for i in range(5):
            stats[yesterday.day] = {
                "image": lowest.image,
                "day": yesterday,
            }
            yesterday = yesterday - timedelta(days=1)

        for event in events:
            if event.status.severity > severity:
                if event.start.day in stats:
                    stats[event.start.day]["image"] = "information"
                    stats[event.start.day]["information"] = True

        results = []

        keys = stats.keys()
        keys.sort()
        keys.reverse()

        for k in keys:
            results.append(stats[k])

        return results

    def update_status(self, status_name, reason=None):
        reason = reason or "Unknown"
        status = Status.objects.get(name=status_name)
        Event(service=self, status=status, message=reason).save()


class StatusManager(models.Manager):
    def default(self):
        return self.get_query_set().filter(severity=10)[0]


class Status(models.Model):
    """
    A possible system status.
    """
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    description = models.CharField(max_length=255)
    SEVERITY_CHOICES = (
        (10, 'NORMAL'),
        (30, 'WARNING'),
        (40, 'ERROR'),
        (50, 'CRITICAL'),
    )
    severity = models.IntegerField(choices=SEVERITY_CHOICES)
    image = models.CharField(max_length=100)

    objects = StatusManager()

    class Meta:
        ordering = ('severity',)
        verbose_name_plural = 'statuses'

    def __unicode__(self):
        return self.name


class Event(models.Model):
    service = models.ForeignKey(Service, related_name='events')
    status = models.ForeignKey(Status, related_name='events')
    message = models.TextField()
    start = models.DateTimeField(default=datetime.now)
    informational = models.BooleanField(default=False)

    class Meta:
        ordering = ('-start',)
        get_latest_by = 'start'
