import configparser
import sqlalchemy as sql

#Helper class to encapsulate a database connection
#TODO: use my datbase helper class to expand database options
class Database:
    
    def __init__(self, config_file):
        config = configparser.ConfigParser()

        config.read('database_creds.cfg')

        user = config['USER']['user']
        password = config['USER']['password']
        host = config['USER']['host']
        port = config['USER']['port']
        database = config['USER']['database']

        conn_string = f'postgres://{user}:{password}@{host}:{port}/{database}'
        self.connection = sql.create_engine(conn_string)
    
    def get_connection(self):
        return self.connection



