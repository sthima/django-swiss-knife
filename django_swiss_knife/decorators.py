from django.conf import settings
from auditlog.registry import auditlog


def audit(cls):
    if getattr(settings, 'AUDITLOG_ENABLED', False):
        auditlog.register(cls)
    return cls
