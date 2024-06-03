# from fastapi import FastAPI
# from signup import router as signup_router
# from fastapi import APIRouter, HTTPException, Form
# import mysql.connector




# router = APIRouter()

# def get_db_connection():
#     # Connect to your MySQL database
#     return mysql.connector.connect(user='root', password='', host='127.0.0.1', database='test2')

# @router.post("/signup")
# async def signup(username: str = Form(...), password: str = Form(...), email: str = Form(...)):
#     try:
#         mydb = get_db_connection()
#         mycursor = mydb.cursor()

#         # Insert the new user into the 'user' table
#         sql = "INSERT INTO user (username, password, email) VALUES (%s, %s, %s)"
#         val = (username, password, email)
#         mycursor.execute(sql, val)
#         mydb.commit()

#         return {"message": f"User {username} successfully registered."}
#     except mysql.connector.Error as err:
#         return {"message": f"Error inserting record: {err}"}
#     finally:
#         mycursor.close()
#         mydb.close()

# # Existing code and routers...
