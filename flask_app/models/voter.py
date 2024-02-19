from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import database
from flask import flash
from flask_app import app

import re
email_regex=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class Voter:
    def __init__(self ,data):
        self.id=data['id']
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.email=data['email']
        self.cin=data['cin']#for id number
        self.region=data['region']
        self.vote=data['vote']
        self.age=data['age']
        self.password=data['password']
        self.is_banned=data['is_banned']
        self.first_time=data['first_time']
        # self.new_password=data['new_password']
        # self.confirm_password=data['confirm_password']
    @classmethod
    def create(cls,data):
        query="""INSERT INTO voters
        (first_name,last_name,email,password,birthdate,region,cin,vote,is_banned,first_time) VALUES
                (%(first_name)s,%(last_name)s,%(email)s,%(password)s
                ,%(birthdate)s,%(region)s,%(cin)s,0,0,1);"""
        return connectToMySQL(database).query_db(query,data)
# =======
        
    @classmethod
    def create(cls,data):
        query="""INSERT INTO voters
        (first_name,last_name,email,password,age,region,cin,vote,is_banned) VALUES
                (%(first_name)s,%(last_name)s,%(email)s,%(password)s,%(age)s
                ,%(region)s,%(cin)s,0,0);"""
# >>>>>>> 3c3bf16395b435605074b89d4d06bb470246df0d
        return connectToMySQL(database).query_db(query,data)
    
    @classmethod
    def new_vote(cls,data):
        query="""INSERT INTO votes
        (vote_id,condidate_id,region) VALUES
                (%(vote_id)s,%(condidate_id)s,%(region)s);"""
        return connectToMySQL(database).query_db(query,data)
    
    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM voters WHERE id = %(id)s;"
        result = connectToMySQL(database).query_db(query, data)
        if result:
            return cls(result[0])  
        else:
            return None 
    @classmethod
    def get_all(cls):
        query="""SELECT * FROM voters;"""
        db_result=connectToMySQL(database).query_db(query)
        all_voters=[]
        for row in db_result:
            all_voters.append(row)
        return all_voters
    
    @classmethod
    def get_voter_by_email(cls,data):
        query="""SELECT * FROM voters WHERE email =%(email)s;"""
        db_result=connectToMySQL(database).query_db(query,data)
        if db_result:
            return cls(db_result[0])
        return None
    
    @classmethod
    def get_voter_by_id(cls,data):
        query="""SELECT * FROM voters WHERE id=%(id)s;"""
        db_result=connectToMySQL(database).query_db(query,data)
        if db_result:
            return cls(db_result[0])
        return None
    
    @staticmethod
    def update(data):
        query="""
            UPDATE voters SET is_banned=%(x)s WHERE id=%(id)s;
            """ 
        return connectToMySQL(database).query_db(query,data)
    @classmethod
    def update_first_time(cls,data):
        query="""UPDATE voters SET first_time=%(first_time)s WHERE id=%(id)s;"""
        return connectToMySQL(database).query_db(query,data)
    @staticmethod
    def update_first(data):
        query="""UPDATE voters SET first_time=0,password=%(password)s WHERE id=%(id)s;"""
        return connectToMySQL(database).query_db(query,data)
    @classmethod
    def update_vote(cls,data):
        query="""UPDATE voters SET vote=1 WHERE id=%(id)s;"""
        return connectToMySQL(database).query_db(query,data)
    @staticmethod
    def validate(data):
        is_valid=True
        countM=0
        countm=0
        countnumber=0
        if len(data['first_name'])<3 or len(data['last_name'])<3:
            is_valid=False
            flash('please enter a valid first_name and last_name mean too short')
        if not email_regex.match(data['email']):
            is_valid=False
            flash('your email is invalid')
        if data['region']=="Select your region":
            is_valid=False
            flash('please select your region')
        if data['age']=="" or int(data['age'])<18:
            is_valid=False
            flash('please insert your birthday and 18 years old at least')
        if len(data['password'])<8:
            for i in range(len(data['password'])):
                if "A"<data['password'][i]<"Z":
                    countM+=1
                elif "a"<data['password'][i]<"z":
                    countm+=1
                else:
                    countnumber+=1
            if countM==0 or countm==0:
                is_valid=False
                flash('Must contain at least one Upper Case and one Camel Case and one number')
        if len(data['cin'])<8:
            flash('Please Insert Correctly Your Cin Number')
            is_valid=False
        else:
            for i in range(len(Voter.get_all())):
                print(Voter.get_all()[i])
                print(Voter.get_all()[i]['cin'])
                if  data['cin'] == Voter.get_all()[i]['cin']:
                    is_valid=False
                    flash('this Id already Exit')
                    break
        return is_valid
    @staticmethod
    def validate_new(data):
        is_valid=True
        if data['new_password']=="":
            is_valid=False
            flash('the password mustnt be empty please input the password')
        if data['confirm_password']!=data['new_password']:
            is_valid=False
            flash('the confirmation is wrong pls fix that')
        return is_valid    

class Vote:
    def __init__(self,data):
        self.vote_id=data['vote_id']
        self.condidate_id=data['condidate_id']
        self.region=data['region']

    @classmethod
    def voter_get_all(cls):
        query="""SELECT * FROM votes ;"""
        all_votes=[]
        db_result=connectToMySQL(database).query_db(query)
        for row in db_result:
            all_votes.append(cls(row))
        return all_votes
    @classmethod
    def count_voter(cls,data):
        query="""SELECT count(*) AS all_count,region 
        from votes WHERE condidate_id=%(condidate_id)s AND
        vote_id=%(vote_id)s
        GROUP BY region HAVING region=%(region)s;"""
        db_result=connectToMySQL(database).query_db(query,data)
        count=[]
        print(count)
        for row in db_result:
            count.append(row)
        return count
