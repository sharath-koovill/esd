import datetime
from django.utils import timezone
from django.db import models
from django.db.models import Q
from sevalinks.models import User, Notification
import models as contactsModel

class ContactsManager(object):

    def friends(self, user_id):
        selectColumns = "SELECT user.user_id as u_user_id, user.first_name as u_first_name, user.last_name as u_last_name, user.username as u_username, user.user_identifier as u_user_identifier, image.user_image as u_user_image, "
        selectColumns = selectColumns + "pr.user_profession as u_user_profession, ed.user_college_active as u_user_college_active, loc.user_area as u_user_area "
        fromTables = "FROM sevalinks_user AS user "
        join = "LEFT JOIN contacts_contacts AS contacts on "
        join = join + "((contacts.user_one_id=user.user_id OR contacts.user_two_id=user.user_id) AND user.user_id!='" + str(user_id) + "') "
        join = join + "LEFT JOIN sevalinks_userimage AS image on image.user_id_id=user.user_id "
        join = join + "LEFT JOIN sevalinks_userlocation AS loc on user.user_id=loc.user_id_id "
        join = join + "LEFT JOIN sevalinks_usereducation AS ed on user.user_id=ed.user_id_id "
        join = join + "LEFT JOIN sevalinks_userprofession AS pr on user.user_id=pr.user_id_id "
        condition = "WHERE ((contacts.user_one_id = '" + str(user_id) + "') OR (contacts.user_two_id = '" + str(user_id) + "')) "
        condition = condition + "AND contacts.status = '1' "

        query = selectColumns + fromTables + join + condition
        print query
        return self.get_user(query)

    def invitations(self, user_id):
        selectColumns = "SELECT user.user_id as u_user_id, user.first_name as u_first_name, user.last_name as u_last_name, user.username as u_username, user.user_identifier as u_user_identifier, image.user_image as u_user_image, "
        selectColumns = selectColumns + "pr.user_profession as u_user_profession, ed.user_college_active as u_user_college_active, loc.user_area as u_user_area "
        fromTables = "FROM sevalinks_user AS user "
        join = "LEFT JOIN contacts_contacts AS contacts on "
        join = join + "(contacts.user_one_id=user.user_id OR contacts.user_two_id=user.user_id) AND user.user_id!='" + str(user_id) + "' "
        join = join + "LEFT JOIN sevalinks_userimage AS image on image.user_id_id=user.user_id "
        join = join + "LEFT JOIN sevalinks_userlocation AS loc on user.user_id=loc.user_id_id "
        join = join + "LEFT JOIN sevalinks_usereducation AS ed on user.user_id=ed.user_id_id "
        join = join + "LEFT JOIN sevalinks_userprofession AS pr on user.user_id=pr.user_id_id "
        condition = "WHERE ((contacts.user_one_id = '" + str(user_id) + "') OR (contacts.user_two_id = '" + str(user_id) + "')) "
        condition = condition + "AND contacts.status = '0' "

        query = selectColumns + fromTables + join + condition
        print query
        return self.get_user(query)

    def blocked_users(self, user_id):
        selectColumns = "SELECT user.user_id as u_user_id, user.first_name as u_first_name, user.last_name as u_last_name, user.username as u_username, user.user_identifier as u_user_identifier, image.user_image as u_user_image, "
        selectColumns = selectColumns + "pr.user_profession as u_user_profession, ed.user_college_active as u_user_college_active, loc.user_area as u_user_area "
        fromTables = "FROM sevalinks_user AS user "
        join = "LEFT JOIN contacts_contacts AS contacts on "
        join = join + "(contacts.user_one_id=user.user_id OR contacts.user_two_id=user.user_id) AND user.user_id!='" + str(user_id) + "' "
        join = join + "LEFT JOIN sevalinks_userimage AS image on image.user_id_id=user.user_id "
        join = join + "LEFT JOIN sevalinks_userlocation AS loc on user.user_id=loc.user_id_id "
        join = join + "LEFT JOIN sevalinks_usereducation AS ed on user.user_id=ed.user_id_id "
        join = join + "LEFT JOIN sevalinks_userprofession AS pr on user.user_id=pr.user_id_id "
        condition = "WHERE ((contacts.user_one_id = '" + str(user_id) + "') OR (contacts.user_two_id = '" + str(user_id) + "')) "
        condition = condition + "AND contacts.status = '3' "

        query = selectColumns + fromTables + join + condition
        print query
        return self.get_user(query)

    def get_user(self, query):
        from django.db import connection
        with connection.cursor() as cursor:
            cursor.execute(query)
            rows = self.dictfetchall(cursor)
        return rows

    def dictfetchall(self, cursor):
        "Return all rows from a cursor as a dict"
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]

    def invite(self, user_one_id, user_two_id, user_action_id):
        targetUser = user_two_id
        if user_one_id > user_two_id:
            user_two_id, user_one_id = user_one_id, user_two_id
        cont = contactsModel.Contacts(user_one_id=user_one_id, user_two_id=user_two_id, status=0, user_action_id=user_action_id)
        cont.save()
        notice = Notification(source_id=user_action_id, target_id=targetUser, description_id="0", category_id="0")
        notice.save()

    def accept_invitation(self, user_one_id, user_two_id, user_action_id):
        sourceUser = user_one_id
        if user_one_id > user_two_id:
            user_two_id, user_one_id = user_one_id, user_two_id
        contactsModel.Contacts.objects.filter((Q(user_one_id=user_one_id) | Q(user_two_id=user_two_id)) & Q(user_action_id=user_action_id) & Q(status=0)).update(status=1)
        notice = Notification(source_id=sourceUser, target_id=user_action_id, description_id="1", category_id="0")
        notice.save()

    def block(self, user_one_id, user_two_id, user_action_id):
        if user_one_id > user_two_id:
            user_two_id, user_one_id = user_one_id, user_two_id
        cont = contactsModel.Contacts.objects.filter((Q(user_one_id=user_one_id) | Q(user_two_id=user_two_id)) & Q(user_action_id=user_action_id))
        if len(cont.values()) > 0:
            cont.update(status=3)
        else:
            cont = contactsModel.Contacts(user_one_id=user_one_id, user_two_id=user_two_id, status=3, user_action_id=user_action_id)
            cont.save()

    def unblock(self, user_one_id, user_two_id, user_action_id):
        if user_one_id > user_two_id:
            user_two_id, user_one_id = user_one_id, user_two_id
        cont = contactsModel.Contacts.objects.filter((Q(user_one_id=user_one_id) | Q(user_two_id=user_two_id)) & Q(user_action_id=user_action_id) & Q(status=3))
        cont.delete()

    def decline(self, user_one_id, user_two_id, user_action_id):
        if user_one_id > user_two_id:
            user_two_id, user_one_id = user_one_id, user_two_id
        cont = contactsModel.Contacts.objects.filter((Q(user_one_id=user_one_id) | Q(user_two_id=user_two_id)) & Q(user_action_id=user_action_id) & Q(status=0))
        cont.update(status=2)

    def remove(self, user_one_id, user_two_id):
        if user_one_id > user_two_id:
            user_two_id, user_one_id = user_one_id, user_two_id
        cont = contactsModel.Contacts.objects.filter((Q(user_one_id=user_one_id) | Q(user_two_id=user_two_id)) & Q(status=1))
        cont.delete()

    def connection_count(self, user_id):
        cont = contactsModel.Contacts.objects.filter((Q(user_one_id=user_id) | Q(user_two_id=user_id)) & Q(status=1))
        #cont = self.filter((Q(user_one_id=user_id) | Q(user_two_id=user_id)) & Q(status=1))
        print cont
        if cont:
            return cont.count()
        else:
            return 0

    def check_connection(self, user_one_id, user_two_id):
        otherUser = user_two_id
        if user_one_id > user_two_id:
            user_two_id, user_one_id = user_one_id, user_two_id
        cont = contactsModel.Contacts.objects.filter((Q(user_one_id=user_one_id) | Q(user_two_id=user_two_id))).values()
        if cont and cont[0]["status"] == 0 and cont[0]["user_action_id"] == otherUser:
            return 4
        elif cont:
            return cont[0]["status"]
        else:
            return -1

    def check_notification(self, user_id):
        notice = Notification.objects.filter(Q(target_id=user_id) & Q(is_active=True)).values()
        return notice

    def ack_notification(self, user_id, category):
        Notification.objects.filter(Q(target_id=user_id) & Q(is_active=True) & Q(category_id=category)).update(is_active=False, ack_date=timezone.now())
