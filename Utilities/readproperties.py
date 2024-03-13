"""
configParser is a Python standard library module that allows parsing
configuration files in .ini format. INI stands for initialization,
a simple and common file format used to store configuration data,
such as application settings, database credentials, or API keys.
"""
import configparser

config = configparser.RawConfigParser()
config.read(".//Configuration//config.ini")

class ReadConfig():
    @staticmethod
    def getapplicationURL():
        url = config.get("common info", 'baseURL')
        return url

    @staticmethod
    def getusername():
        username = config.get("common info", 'username')
        return username

    @staticmethod
    def getpassword():
        password = config.get("common info", 'password')
        return password



