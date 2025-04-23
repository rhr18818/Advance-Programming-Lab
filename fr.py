# import cv2
# import dlib

# # Load the image
# image_path = "D:\\fr\\hih\\taylor.jpg"  # Using double backslashes
# image = cv2.imread(image_path)

# # Check if the image was loaded successfully
# if image is None:
#     print("Error: Could not load image.")
#     exit()

# # Convert the image to grayscale for face detection
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# # Initialize the dlib face detector
# detector = dlib.get_frontal_face_detector()

# # Detect faces in the grayscale image
# faces = detector(gray)

# # Draw rectangles around the detected faces
# for i, face in enumerate(faces):
#     x, y, w, h = (face.left(), face.top(), face.width(), face.height())
#     cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# # Show the output image with faces detected
# cv2.imshow("Face Recognition", image)

# # Wait until a key is pressed and then close the window
# cv2.waitKey(0)
# cv2.destroyAllWindows()
