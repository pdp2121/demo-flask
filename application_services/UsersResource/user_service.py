from application_services.BaseApplicationResource import BaseRDBApplicationResource
from database_services.RDBService import RDBService


class UserResource(BaseRDBApplicationResource):

    def __init__(self):
        super().__init__()

    @classmethod
    def get_links(cls, resource_data):
        pass

    @classmethod
    def get_data_resource_info(cls):
        return 'aaaaaF21E6156', 'users'

    @classmethod
    def get_all_user_data(cls, dbName):
        res = RDBService.get_full_table(dbName, "user")
        return res
    
    @classmethod
    def get_user_data_by_id(cls, dbName, userID):
        res = RDBService.get_by_id(dbName, "user", userID)
        return res
    
    @classmethod
    def get_user_address_by_id(cls, dbName, userID):
        res = RDBService.get_by_foreign_id(dbName, "user", "address", "addressID", "ID", userID)
        return res
