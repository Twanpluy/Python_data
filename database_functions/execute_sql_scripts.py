from connect_db import connect_db

conn = connect_db()
cursor = conn.cursor()

with open('database_functions\create_linkedin_job_table.sql', 'r') as f:
    sql_script = f.read()
    cursor.execute(sql_script)

conn.commit()
cursor.close()
conn.close()