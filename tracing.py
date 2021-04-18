import logging
from jaeger_client import Config
from config import Config as AppConfig


def init_tracer(service):
    logging.getLogger('').handlers = []
    logging.basicConfig(format='%(message)s', level=logging.DEBUG)

    config = Config(
        config={
            'sampler': {
                'type': 'const',
                'param': 1,
            },
            'logging': True,
            'local_agent': {
                'reporting_host': AppConfig.JAEGER_HOST,
            },
        },
        service_name=service
    )

    return config.initialize_tracer()
