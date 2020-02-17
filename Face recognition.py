import cv2
detect_face=0
detect_eye = 0
detect_smile=0
face_cascade = cv2.CascadeClassifier("C:\haarcascade_frontalcatface.xml")
eye_cascade = cv2.CascadeClassifier("C:\haarcascade_eye_tree_eyeglasses.xml")
smile_cascade= cv2.CascadeClassifier("C:\haarcascade_smile.xml")
cap = cv2.VideoCapture(0)
while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.03, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + (2+w), y + (2+h)), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        detect_face += 1
        eyes = eye_cascade.detectMultiScale(roi_gray,1.01,22)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
            detect_eye+=1
        smiles= smile_cascade.detectMultiScale(roi_gray,1.3,22)
        for (sx,sy,sw,sh) in smiles:
            cv2.rectangle(roi_color, (sx, sy), (sx + sw , sy + sh), (0, 0, 255), 2)
            detect_smile+=1
        if detect_face == detect_eye==detect_smile:
            print("face detected:\t", detect_face)
    cv2.imshow('img, ', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()