import sqlite3

# Nama database
db_file = 'students.db'

# Fungsi untuk menjalankan perintah SQL
def execute_sql_command(sql_command):
    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()
    cursor.execute(sql_command)
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results

# Contoh penggunaan: Menampilkan semua data dari tabel students
sql_command = "SELECT * FROM students;"
results = execute_sql_command(sql_command)

# Menampilkan hasil
for row in results:
    print(row)