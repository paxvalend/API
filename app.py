from flask import Flask, jsonify, request
from db.query_raw import connection

app = Flask(__name__)

@app.route("/users", methods=["GET", "POST"])
def users():
    if request.method == 'GET':
        query = """
        SELECT * FROM valend.users
        """
        conn, cursor = connection()
        cursor.execute(query)
        result = cursor.fetchall() # fetchcall (ppycopg) digunakan untuk mengambil semua data yang sudah di execute
        return jsonify(result)

    elif request.method == 'POST':
        name = request.args.get('name')
        address = request.args.get('address')
        query = f"""
        INSERT INTO valend.users (name, address)
        VALUES ('{name}', '{address}')
        """
        conn, cursor = connection()
        cursor.execute(query)
        conn.commit()
        return jsonify({"message": f"User {name} has been created successfully"})

if __name__ == '__main__':
    app.run()
