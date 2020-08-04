BROKER_URL='amqp://rose:rosepasswordq@mangrove.rccc.ou.edu:5672/eomf_processing'
#CELERY_RESULT_BACKEND = 'amqp://rose:rosepasswordq@mangrove.rccc.ou.edu:5672/eomf_processing'
CELERY_RESULT_BACKEND = 'mongodb'
CELERY_MONGODB_BACKEND_SETTINGS = {
    "host": "mangrove.rccc.ou.edu",
    "user": 'rose',
    "password": 'rosepasswordq',
    "port": 27017,
    "database": "eomf_processing",
    "taskmeta_collection": "celery_results" # Collection name to use for task output
}
CELERY_TASK_RESULT_EXPIRES = 300  # 5 minutes.
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT=['json']
CELERY_TIMEZONE = 'US/Central'
CELERY_ENABLE_UTC = True
CELERY_ROUTES = {
    'tasks_multi.multiple_site_modis':   {'queue': 'control_multi'},
    'tasks_multi.get_modis_year_data':   {'queue': 'processing_multi'},
}
from kombu import serialization
serialization.registry._decoders.pop("application/x-python-serialize")