from pybaseball import statcast
from database import Database
import pandas as pd

#Class to handle importing statcast data from MLB Savant via Pybaseball
class StatcastImport:

    def __init__(self, config_file ):
        self.db_connection = Database(config_file)

    def import_statcast(self, table, start, end, team=None, verbose=True, cache=False):
        if cache:
            from pybaseball import cache
            cache.enable()
        if team is not None:
            data = statcast(start, end, team, verbose)
        else:
            data = statcast(start, end, verbose)
        
        data.to_sql(table, self.db_connection.get_connection(), if_exists='append')

