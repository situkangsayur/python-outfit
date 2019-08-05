logging = {
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format':
            '%(asctime)s, %(levelname)s:%(filename)s(%(lineno)d)> %(message)s'
        }
    },
    'handlers': {
        'critical_file_handler': {
            'backupCount': 20,
            'class': 'logging.handlers.RotatingFileHandler',
            'encoding': 'utf8',
            'filename': 'tests/test_logs/critical.log',
            'formatter': 'simple',
            'level': 'CRITICAL',
            'maxBytes': 10485760
        },
        'debug_console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
            'level': 'DEBUG',
            'stream': 'ext://sys.stdout'
        },
        'debug_file_handler': {
            'backupCount': 20,
            'class': 'logging.handlers.RotatingFileHandler',
            'encoding': 'utf8',
            'filename': 'tests/test_logs/debug.log',
            'formatter': 'simple',
            'level': 'DEBUG',
            'maxBytes': 10485760
        },
        'error_file_handler': {
            'backupCount': 20,
            'class': 'logging.handlers.RotatingFileHandler',
            'encoding': 'utf8',
            'filename': 'tests/test_logs/errors.log',
            'formatter': 'simple',
            'level': 'ERROR',
            'maxBytes': 10485760
        },
        'info_file_handler': {
            'backupCount': 20,
            'class': 'logging.handlers.RotatingFileHandler',
            'encoding': 'utf8',
            'filename': 'tests/test_logs/info.log',
            'formatter': 'simple',
            'level': 'INFO',
            'maxBytes': 10485760
        },
        'production_console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
            'level': 'INFO',
            'stream': 'ext://sys.stdout'
        }
    },
    'loggers': {
        'development': {
            'handlers': [
                'debug_console',
                'debug_file_handler',
                'info_file_handler',
                'error_file_handler',
                'critical_file_handler'
            ],
            'level': 'DEBUG',
            'propagate': True
        },
        'production': {
            'handlers': [
                'production_console',
                'info_file_handler',
                'error_file_handler',
                'critical_file_handler'
            ],
            'level': 'INFO',
            'propagate': True
        }
    },
    'version': 1
}

