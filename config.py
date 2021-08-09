import os


class Config:

    DEBUG = False

    DEVELOPMENT = False

    SECRET_FLAVOR = os.getenv("SECRET_FLAVOR", "this-is-the-default-flavor")


class ProductionConfig(Config):

    pass


class StagingConfig(Config):

    DEBUG = True


class DevelopmentConfig(Config):

    DEBUG = True

    DEVELOPMENT = True