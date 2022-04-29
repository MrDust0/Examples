LOG_CONFIG = {
    'version': 1,
    'formatters': {
        'verbose': {
            'format': '%(asctime)s %(levelname)s {%(process)d %(module)s.%(funcName)s:%(lineno)d} %(message)s',
            'datefmt': '%y-%m-%d %H:%M:%S'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'simple',
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': "/tmp/some.log",
            'mode': 'a',
            'maxBytes': 512*1024*1024,
            'backupCount': 10,
            'formatter': 'verbose',
            'encoding': 'utf-8'
        },
    },
    'loggers':{
        'StreamLogger': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
        'FileLogger': {
            'handlers': ['console', 'file'],
            'level': "INFO",
        },
    }
}
