from Database import sessionlocal
from model.user import User
from auth import hash_password
 
def create_user_service(user_data):
   db=sessionlocal()
   hashed_password=hash_password(user_data.password)
   new_user=User(
      username=user_data.username,
      password=hashed_password
   )
   db.add(new_user)
   db.commit()
   db.refresh(new_user)
   db.close()
   return new_user