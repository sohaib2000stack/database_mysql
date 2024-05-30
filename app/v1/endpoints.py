# from fastapi import APIRouter, HTTPException, Form, Request
# from fastapi.responses import HTMLResponse
# import mysql.connector
# import logging

# router = APIRouter()

# def get_db_connection():
#     # Connect to your MySQL database
#     return mysql.connector.connect(user='root', password='',
#                                     host='127.0.0.1', database='test2')

# @router.get("/", response_class=HTMLResponse)
# async def get_form():
#     with open("index.html", "r") as form_file:
#         form = form_file.read()
#     return form

# @router.post("/save_data")
# async def save_data(id: int = Form(...), name: str = Form(...), age: int = Form(...), year: int = Form(...), address: str = Form(...)):
#     try:
#         mydb = get_db_connection()
#         mycursor = mydb.cursor()

#         sql = "INSERT INTO employee (id, name, age, year, Address) VALUES (%s, %s, %s, %s, %s)"
#         val = (id, name, age, year, address)

#         mycursor.execute(sql, val)
#         mydb.commit()
#         return {"message": f"{mycursor.rowcount} record inserted."}
#     except mysql.connector.Error as err:
#         return {"message": f"Error inserting record: {err}"}
#     finally:
#         mycursor.close()
#         mydb.close()

# @router.get("/data", response_class=HTMLResponse)
# async def get_data():
#     try:
#         mydb = get_db_connection()
#         mycursor = mydb.cursor(dictionary=True)
#         mycursor.execute("SELECT * FROM employee")
#         data = mycursor.fetchall()
#         return {"data": data}
#     except mysql.connector.Error as err:
#         print(f"Error fetching data: {err}")  # Print the error for debugging
#         return {"message": f"Error fetching data: {err}"}
#     finally:
#         mycursor.close()
#         mydb.close()




from fastapi import APIRouter, HTTPException, Form
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import mysql.connector
import json 
router = APIRouter()

class Employee(BaseModel):
    id: int
    name: str
    age: int
    year: int
    address: str

def get_db_connection():
    # Connect to your MySQL database
    return mysql.connector.connect(user='root', password='',
                                    host='127.0.0.1', database='test2')

@router.post("/save_data")
async def save_data(id: int = Form(...), name: str = Form(...), age: int = Form(...), year: int = Form(...), address: str = Form(...)):
    try:
        mydb = get_db_connection()
        mycursor = mydb.cursor()

        sql = "INSERT INTO employee (id, name, age, year, Address) VALUES (%s, %s, %s, %s, %s)"
        val = (id, name, age, year, address)

        mycursor.execute(sql, val)
        mydb.commit()
        return {"message": f"{mycursor.rowcount} record inserted."}
    except mysql.connector.Error as err:
        return {"message": f"Error inserting record: {err}"}
    finally:
        mycursor.close()
        mydb.close()

@router.get("/get_data", response_class=HTMLResponse)
async def get_form():
    try:
        mydb = get_db_connection()
        mycursor = mydb.cursor(dictionary=True)
        mycursor.execute("SELECT * FROM employee")
        data = mycursor.fetchall()
        response_data = json.dumps(data)
        return response_data 
        return data
    except mysql.connector.Error as err:
        print(f"Error fetching data: {err}")
        return {"message": f"Error fetching data: {err}"}
    finally:
        mycursor.close()
        mydb.close()
@router.put("/update_data/{user_id}")
async def update_data(user_id: int, name: str = Form(...), age: int = Form(...), year: int = Form(...), address: str = Form(...)):
    try:
        print(user_id)
        mydb = get_db_connection()
        mycursor = mydb.cursor()

        sql = "UPDATE employee SET name = %s, age = %s, year = %s, Address = %s WHERE id = %s"
        val = (name, age, year, address, user_id)

        mycursor.execute(sql, val)
        mydb.commit()
        return {"message": f"{mycursor.rowcount} record(s) updated."}
    except mysql.connector.Error as err:
        return {"message": f"Error updating record: {err}"}
    finally:
        mycursor.close()
        mydb.close()

@router.get("/get_row_data/{user_id}")
async def get_row_data(user_id: int):
    try:
        mydb = get_db_connection()
        mycursor = mydb.cursor()

        sql = "SELECT * FROM employee WHERE id = %s"
        val = (user_id,)

        mycursor.execute(sql, val)
        queried_data = mycursor.fetchone()
        if not queried_data:
            raise HTTPException(status_code=404, detail="Data not found")
        
        data = {
            'id': queried_data[0],
            'name': queried_data[1],
            'age': queried_data[2],
            'year': queried_data[3],
            'address': queried_data[4],
        }
        return data
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Database error: {err}")
    finally:
        mycursor.close()
        mydb.close()
