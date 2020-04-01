from tgext.celery.celery import celery_app
from tgext.mailer import get_mailer
from tg import config
import logging

celery_app.config_from_object(config.get('celery_configuration_object'))

log = logging.getLogger(__name__)


@celery_app.task(name='mailtemplates_async_send_email')
def mailtemplates_async_send_email(message):
    """Sends email asynchronously throuh tgext.celery"""
    log.info('mailtemplates_async_send_email started')
    mailer = get_mailer(None)
    mailer.send_immediately(message)
    log.info('mailtemplates_async_send_email ended')
