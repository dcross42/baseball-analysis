from pybaseball import batting, pitching
from database import Database
import pandas as pd

#Class to handle importing fangraphs data from via Pybaseball
class FangraphsImport:

    def __init__(self, config_file ):
        self.db_connection = Database(config_file)

    def import_fangraphs_batting(self, table, start, end, cache=False):
        if cache:
            from pybaseball import cache
            cache.enable()
        
        data = batting(start, end)
        
        data.to_sql(table, self.db_connection.get_connection(), if_exists='append')
    
    def import_fangraphs_pitching(self, table, start, end, cache=False):
        if cache:
            from pybaseball import cache
            cache.enable()
       
        data = pitching(start, end)
        
        data.to_sql(table, self.db_connection.get_connection(), if_exists='append')

