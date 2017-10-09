#config.py
class Config(object):
	"""
	Common configuration file
	"""
class DevelopmentConfig(Config):
	"""
	Development COnfigurations
	"""

	DEBUG = True
	SQLALCHEMY_ECHO = True

class ProductionConfig(Config):
	"""
	Production Configurations
	"""
	DEBUG = False

app_config = {
	'development' : DevelopmentConfig,
	'production'  : ProductionConfig
}
