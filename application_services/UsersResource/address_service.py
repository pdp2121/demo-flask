from application_services.BaseApplicationResource import BaseRDBApplicationResource
from database_services.RDBService import RDBService


class AddressResource(BaseRDBApplicationResource):

    def __init__(self):
        super().__init__()

    @classmethod
    def get_links(cls, resource_data):
        pass

    @classmethod
    def get_data_resource_info(cls):
        return 'aaaaaF21E6156', 'address'

    @classmethod
    def get_all_address_data(cls, dbName):
        res = RDBService.get_full_table(dbName, "address")
        return res
    
    @classmethod
    def get_address_data_by_id(cls, dbName, addressID):
        res = RDBService.get_by_id(dbName, "address", addressID)
        return res
    
    @classmethod
    def get_address_user_by_id(cls, dbName, addressID):
        res = RDBService.get_by_foreign_id(dbName, "address", "user", "ID", "addressID", addressID)
        return res