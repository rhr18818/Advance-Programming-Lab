from flask import Flask, render_template, request, jsonify
import sqlite3
from datetime import datetime
from part2 import recognize_face_from_base64  # Your modular function
from create_table import create_database, insert_face  # Importing from database.py

app = Flask(__name__)

# Ensure the database is created at the start of the app
create_database()

@app.route('/')
def index():
    return render_template('index.html', selected_date='', no_data=False)

<<<<<<< HEAD
@app.route('/attendance', methods=['POST'])
def attendance():
    try:
        selected_date = request.form.get('selected_date')
        selected_date_obj = datetime.strptime(selected_date, '%Y-%m-%d')
        formatted_date = selected_date_obj.strftime('%Y-%m-%d')

        conn = sqlite3.connect('attendance.db')
        cursor = conn.cursor()

        cursor.execute("SELECT name, time FROM attendance WHERE date = ?", (formatted_date,))
        attendance_data = cursor.fetchall()
        conn.close()

        if not attendance_data:
            return render_template('index.html', selected_date=selected_date, no_data=True)

        return render_template('index.html', selected_date=selected_date, attendance_data=attendance_data)

    except Exception as e:
        print(f"Error in attendance route: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/recognize', methods=['POST'])
def recognize():
    try:
        data = request.json
        if not data or 'image' not in data:
            return jsonify({"error": "No image data provided"}), 400

        image_data = data['image'].split(',')[1]  # base64 string
        recognized_names = recognize_face_from_base64(image_data)

        conn = sqlite3.connect('attendance.db')
        cursor = conn.cursor()

        for name in recognized_names:
            if name != "Unknown":
                now = datetime.now()
                time_str = now.strftime('%H:%M:%S')
                date_str = now.strftime('%Y-%m-%d')
                cursor.execute("INSERT INTO attendance (name, time, date) VALUES (?, ?, ?)", (name, time_str, date_str))
                conn.commit()

        conn.close()
        return jsonify({"recognized": recognized_names})

    except Exception as e:
        print(f"Error in recognize route: {e}")
        return jsonify({"error": str(e)}), 500
=======
# @app.route('/attendance', methods=['POST'])
#  def attendance():
#     selected_date = request.form.get('selected_date')
#     selected_date_obj = datetime.strptime(selected_date, '%Y-%m-%d')
#     formatted_date = selected_date_obj.strftime('%Y-%m-%d')

#     conn = sqlite3.connect('attendance.db')
#     cursor = conn.cursor()

#     cursor.execute("SELECT name, time FROM attendance WHERE date = ?", (formatted_date,))
#     attendance_data = cursor.fetchall()

#     conn.close()

#     if not attendance_data:
#         return render_template('index.html', selected_date=selected_date, no_data=True)
    
#     return render_template('index.html', selected_date=selected_date, attendance_data=attendance_data)
>>>>>>> 3efbd1c8418909bdd3e42274011b5450b381b014

if __name__ == '__main__':
    app.run(debug=True)


