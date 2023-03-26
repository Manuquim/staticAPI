
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [
            {#"id": self._generateId(),
            'id': 1,
             'firstName':"John",
             'lastName':self.last_name,
             'age':33,
             'lucky numbers':[7,13,22]},
             {#"id": self._generateId(),
             'id':2,
             'firstName':"Jane",
             'lastName':self.last_name,
             'age':39,
             "lucky numbers":[10,14,3]},
             {"id": 3,
             "firstName":"Jimmy",
             'lastName':self.last_name,
             'age':5,
             'lucky numbers':[1]}]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        #member["id"]=self._generateId()
        member["lastName"]=self.last_name
        self._members.append(member)
        return self._members  

    def update_member(self, id, member):
        ## you have to implement this method
        ## loop the list and replace the member with the given id
        delete_member(self, id)
        member["id"]=id
        add_member(member)

    def delete_member(self, member_id):
        for member in self._members:
            if member['id'] == member_id:
                self._members.remove(member)
                return True
                
        return False

    def get_member(self, member_id):
        # fill this method and update the return
        #x=list(filter(lambda member : member["id"]==member_id,self._members))
        #if(x==None):
            #return x
        #return x
        for member in self._members:
            if(member["id"]==member_id):
                return member
        
    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
