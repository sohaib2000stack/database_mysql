from fastapi import APIRouter, HTTPException, Form, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from app.database import get_db_connection
import logging
import mysql.connector

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
    # Your existing code

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

@router.get("/", response_class=HTMLResponse)
async def get_form():
    with open("index.html", "r") as form_file:
        form = form_file.read()
    return form
