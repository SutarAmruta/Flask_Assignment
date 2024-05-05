import mysql.connector as sql

class usermodel():
    def __init__(self): 
        try:
            self.con = sql.connect(
            host="localhost",
            user="root",
            password="root123",
            database="api_1db"
            )
            self.cur=self.con.cursor(dictionary=True)
            self.con.autocommit = True
            print("connection Sucessful...!")
        except:
            print("connection Error...!")

    def user_getall_model(self):
          self.cur.execute("select * from api_table1")
          result=self.cur.fetchall()
          return result
    
    def user_add_model(self,data):
            self.cur.execute(f"INSERT INTO api_table1(firstName,LastName,Contact,Email,Password1)VALUES('{data['firstName']}','{data['LastName']}','{data['Contact']}','{data['Email']}','{data['Password1']}')")
            x = data["Password1"]
            if len(x)>8:
                 print("Please enter 8 digit password")
            elif len(x)<8:
                 print("Please enter 8 digit password")
            elif len(x)==8:
                 print("Your password is correct")

            return "User data added successfully" 
                
    '''
    def user_update_model(self,data):
        try:
             self.cur.execute(f"Update api_table1 SET firstName = ('{data['firstName']}')LastName=('{data['LastName']}')),Contact=('{data['Contact']}'),Email=('{data['Email']}'),Password1=('{data['Password1']}'WHERE firstName={data['firstName']})")
             self.cur.execute("select Password1 * from api_table1")
             result=self.cur.fetchall()
 
             for i in result:
                x=i[0]
                if len(x) == 8:
                    self.new_pass = (x[0:8])

                    self.cur.execute(f"UPDATE api_table1 SET Password1 = '{self.new_pass}' WHERE Password1 ='{x}' ") 
                    return result
                else:
                      print("Please Enter 8 Digit valid Password")
        except:
             return "User data updated successfully"
     '''
    
    def user_delete_model(self,data):
         self.cur.execute(f"DELETE FROM api_table1 WHERE Password1 like '%123' ")
         print(f"{data}['firstName']")
         result=self.cur.fetchall()
         return result 
     