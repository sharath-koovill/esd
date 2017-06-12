import classifieds.settings as settings
from django.db import connection


class Search(object):    
    
    def __init__(self, user_id, start, end, count):
        self.start = start
        self.end = end
        self.count = count
        self.user_id = user_id        
    
    def construct_query(self, searchName, searchProfession="", searchLocation="", searchBlocked=True):
        self.searchName = searchName
        self.searchProfession = searchProfession
        self.searchLocation = searchLocation
        self.searchBlocked = searchBlocked
        
        selectColumns = "SELECT user.user_id, user.first_name, user.last_name, user.username, user.user_identifier, image.user_image, "
        selectColumns = selectColumns + "pr.user_profession, ed.user_college_active, loc.user_area "
        fromTables = "FROM sevalinks_user AS user "
        join = "LEFT JOIN sevalinks_userimage AS image on image.user_id_id=user.user_id "
        join = join + "LEFT JOIN sevalinks_userlocation AS loc on user.user_id=loc.user_id_id "
        join = join + "LEFT JOIN sevalinks_usereducation AS ed on user.user_id=ed.user_id_id "
        join = join + "LEFT JOIN sevalinks_userprofession AS pr on user.user_id=pr.user_id_id "
        condition = "WHERE ((user.first_name LIKE '" + searchName + "%') OR (user.last_name LIKE '" + searchName + "%')) "
        condition = condition + "AND user.user_id !='" + self.user_id + "' AND user.user_active ='1' "
        if searchProfession:
            condition = condition + "AND pr.user_profession LIKE '" + searchProfession + "%' "
        if searchLocation:
            condition = condition + "AND loc.user_area LIKE '" + searchLocation + "%' "
        self.query = selectColumns + fromTables + join + condition
        print self.query
        
    def search_user(self):
        with connection.cursor() as cursor:
            cursor.execute(self.query)
            rows = self.dictfetchall(cursor)        
        return rows
    
    def dictfetchall(self, cursor):
        "Return all rows from a cursor as a dict"
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]
