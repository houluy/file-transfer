import logging
log_config = {
    "version": 1,
    "handlers": {
        "main": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
        },
    },
    "loggers": {
        "main": {
            "level": "DEBUG",
            "handlers": ["main"],
        },
    },
}
