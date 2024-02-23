import mysql.connector
global cnx


cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="priyal106",
    database="hospitalapt"
)

def rstat(rid: int):
    cursor = cnx.cursor()

    query = "SELECT * FROM report where rid=%s"

    cursor.execute(query,(rid,))

    result=cursor.fetchone()

    cursor.close()

    if result is not None:
        return result[4]
    else:
        return None


# Function to call the MySQL stored procedure and insert an order item
def insert_order_item(p_name, p_gender, p_doctor, p_age, p_pid, p_date):
    try:
        cursor = cnx.cursor()
        query = "INSERT INTO apt (pid,name,age,doctor,gender,date) VALUES (%s, %s, %s, %s, %s, %s)"
        # Calling the stored procedure
        #cursor.callproc('insert_apt_item', (p_name, p_gender, p_doctor, p_age, p_pid, p_date))
        cursor.execute(query, (p_pid, p_name, p_age, p_doctor, p_gender, p_date))
        # Committing the changes
        cnx.commit()

        # Closing the cursor
        cursor.close()

        print("Order item inserted successfully!")

        return 1

    except mysql.connector.Error as err:
        print(f"Error inserting order item: {err}")

        # Rollback changes if necessary
        cnx.rollback()

        return -1

    except Exception as e:
        print(f"An error occurred: {e}")
        # Rollback changes if necessary
        cnx.rollback()

        return -1

# Function to get the next available order_id
def get_next_pid():
    cursor = cnx.cursor()

    # Executing the SQL query to get the next available order_id
    query = "SELECT MAX(pid) FROM apt"
    cursor.execute(query)

    # Fetching the result
    result = cursor.fetchone()[0]

    # Closing the cursor
    cursor.close()

    # Returning the next available order_id
    if result is None:
        return 1
    else:
        return result + 1


def delstat(pid):
    cursor = cnx.cursor()

    query = "delete FROM apt where pid=%s"

    cursor.execute(query,(pid,))

    cnx.commit()
    cursor.close()
    print("Order item deleted successfully!")
