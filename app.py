# from flask import Flask, render_template, request, jsonify
# import sqlite3
# from datetime import datetime
# import face_recognition
# import numpy as np
# import cv2
# import os
# from PIL import Image
# import io
# import base64

# app = Flask(__name__)

# # === Load known faces from "image" folder ===
# known_face_encodings = []
# known_face_names = []

# for filename in os.listdir("image"):
#     path = os.path.join("image", filename)
#     img = face_recognition.load_image_file(path)
#     encodings = face_recognition.face_encodings(img)

#     if encodings:
#         known_face_encodings.append(encodings[0])
#         name = os.path.splitext(filename)[0]
#         known_face_names.append(name)
#     else:
#         print(f"⚠️ No face found in {filename}")


# @app.route('/')
# def index():
#     return render_template('index.html', selected_date='', no_data=False)


# @app.route('/attendance', methods=['POST'])
# def attendance():
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


# @app.route('/recognize', methods=['POST'])
# def recognize():
#     data = request.json
#     image_data = data['image'].split(',')[1]
#     image_bytes = base64.b64decode(image_data)
#     img = Image.open(io.BytesIO(image_bytes))
#     img = np.array(img.convert('RGB'))

#     # Resize for faster processing
#     small_frame = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
#     rgb_small_frame = small_frame[:, :, ::-1]

#     face_locations = face_recognition.face_locations(rgb_small_frame)
#     face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

#     conn = sqlite3.connect('attendance.db')
#     cursor = conn.cursor()

#     recognized_names = []

#     for face_encoding in face_encodings:
#         matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
#         name = "Unknown"
#         if True in matches:
#             match_index = matches.index(True)
#             name = known_face_names[match_index]

#             # Save attendance in database
#             now = datetime.now()
#             time_str = now.strftime('%H:%M:%S')
#             date_str = now.strftime('%Y-%m-%d')
#             cursor.execute("INSERT INTO attendance (name, time, date) VALUES (?, ?, ?)", (name, time_str, date_str))
#             conn.commit()

#         recognized_names.append(name)

#     conn.close()
#     return jsonify({"recognized": recognized_names})


# if __name__ == '__main__':
#     app.run(debug=True)
# #######################################
# from flask import Flask, render_template, request, jsonify
# import sqlite3
# from datetime import datetime
# import os
# import face_recognition
# from PIL import Image
# import io
# import base64
# # from part2 import recognize_face  # Import the recognize_face function from part2.py
# from part2 import recognize_face_from_base64

# app = Flask(__name__)

# # === Load known faces from "image" folder ===
# known_face_encodings = []
# known_face_names = []

# for filename in os.listdir("image"):
#     path = os.path.join("image", filename)
#     img = face_recognition.load_image_file(path)
#     encodings = face_recognition.face_encodings(img)

#     if encodings:
#         known_face_encodings.append(encodings[0])
#         name = os.path.splitext(filename)[0]
#         known_face_names.append(name)
#     else:
#         print(f" No face found in {filename}")

# @app.route('/')
# def index():
#     return render_template('index.html', selected_date='', no_data=False)

# @app.route('/attendance', methods=['POST'])
# def attendance():
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

# @app.route('/recognize', methods=['POST'])
# def recognize():
#     data = request.json
#     image_data = data['image'].split(',')[1]  # Get the image data from the request
#     recognized_names = recognize_face_from_base64(image_data)  # Call the recognize_face function from part2.py



#     conn = sqlite3.connect('attendance.db')
#     cursor = conn.cursor()

#     for name in recognized_names:
#         if name != "Unknown":
#             # Save attendance in database if face recognized
#             now = datetime.now()
#             time_str = now.strftime('%H:%M:%S')
#             date_str = now.strftime('%Y-%m-%d')
#             cursor.execute("INSERT INTO attendance (name, time, date) VALUES (?, ?, ?)", (name, time_str, date_str))
#             conn.commit()

#     conn.close()

#     return jsonify({"recognized": recognized_names})

# if __name__ == '__main__':
#     app.run(debug=True)
# from flask import Flask, render_template, request, jsonify
# import sqlite3
# from datetime import datetime
# from part2 import recognize_face_from_base64  #  modular function

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html', selected_date='', no_data=False)

# @app.route('/attendance', methods=['POST'])
# def attendance():
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

# @app.route('/recognize', methods=['POST'])
# def recognize():
#     data = request.json
#     if not data or 'image' not in data:
#         return jsonify({"error": "No image data provided"}), 400

#     image_data = data['image'].split(',')[1]  # base64 string
#     recognized_names = recognize_face_from_base64(image_data)

#     conn = sqlite3.connect('attendance.db')
#     cursor = conn.cursor()

#     for name in recognized_names:
#         if name != "Unknown":
#             now = datetime.now()
#             time_str = now.strftime('%H:%M:%S')
#             date_str = now.strftime('%Y-%m-%d')
#             cursor.execute("INSERT INTO attendance (name, time, date) VALUES (?, ?, ?)", (name, time_str, date_str))
#             conn.commit()

#     conn.close()
#     return jsonify({"recognized": recognized_names})

# if __name__ == '__main__':
#     app.run(debug=True)
# ############################
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

if __name__ == '__main__':
    app.run(debug=True)


