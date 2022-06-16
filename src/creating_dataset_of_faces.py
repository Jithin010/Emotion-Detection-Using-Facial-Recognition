import cv2

with open('C:/Users/hp/OneDrive/Documents/GitHub/S6 MiniProject/Emotion-Detection-Using-Facial-Recognition/src/happy.txt','r') as f:
    images = [line.strip() for line in f]

face_detector = cv2.CascadeClassifier('C:/Users/hp/OneDrive/Documents/GitHub/S6 MiniProject/Emotion-Detection-Using-Facial-Recognition/src/haarcascade_frontalface_default.xml')

# For each Emotion, enter one numeric face id
face_id = input('\n Enter Emotion id end press <return> ==>  ')

count = 0

for image in images:
    img = cv2.imread("C:/Users/hp/OneDrive/Documents/GitHub/S6 MiniProject/Emotion-Detection-Using-Facial-Recognition/src/data_set/happy/"+image)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
        count += 1

        # Save the captured image into the datasets folder
        cv2.imwrite("C:/Users/hp/OneDrive/Documents/GitHub/S6 MiniProject/Emotion-Detection-Using-Facial-Recognition/src/dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
#0 for happy
#1 for sad