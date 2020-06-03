import cv2
import numpy as np

#####이미지를 위해서 가공 처리 하기
def nothing(x):
    pass

###Tracking이라는 이미지를 만들기
cv2.namedWindow("Tracking", cv2.WINDOW_NORMAL)
cv2.resizeWindow('Tracking', 400,250)
cv2.createTrackbar("LH", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LS", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LV", "Tracking", 1, 255, nothing)
cv2.createTrackbar("UH", "Tracking", 255, 255, nothing)
cv2.createTrackbar("US", "Tracking", 255, 255, nothing)
cv2.createTrackbar("UV", "Tracking", 255, 255, nothing)
#red : LH : 0 , LS : 153, LV : 0, UH : 5, US : 255, UV : 255
#red : LH : 0 , LS : 137, LV : 123, UH : 7, US : 255, UV : 255
#blue : LH :84, LS : 120, LV : 74, UH : 255, US : 255, UV : 255

cap = cv2.VideoCapture(0) #비디오 찍기
cap.set(cv2.CAP_PROP_FPS, 60) #프레임 속도를 내가 원하는 것으로 설정 (30이상 안되는듯...)
fps = cap.get(cv2.CAP_PROP_FPS) #프레임 속도를 측정
print(fps)
ret, frame = cap.read() #찍은 프레임 하나를 읽어옴

(height, width) = frame.shape[:2] #프레임하나를 읽어와서 해당 높이와 너비를 가져옴
center = height/2 #그러고 높이의 중앙을 가져옴

count = 0 #개수를 0으로 설정
change = 1 #공이 위에 있는지 아래 있는지 측정하여 count가 1개씩만 올라가도록 설정

if not cap.isOpened: #카메라가없을 경우 Error를 띄운다
    print("--(Error)--")
    exit(0)

while True:
    ret, frame = cap.read() #반복문을 돌려서 계속 가져온다!
    
    if frame is None: #만약에 frame이 없으면 없다고 한다
        print("--(NONE)--")
        break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #frame의 색깔을 인식 잘하기 위해서 혹은 hsv랑 같이 연결을 하기 위해서!

    l_h = cv2.getTrackbarPos("LH", "Tracking") #색상 (Hue) : 색의 질
    l_s = cv2.getTrackbarPos("LS", "Tracking") #채도 (Saturation) : 색의 선명도
    l_v = cv2.getTrackbarPos("LV", "Tracking") #명도 (Value) : 색의 밝기

    u_h = cv2.getTrackbarPos("UH", "Tracking")
    u_s = cv2.getTrackbarPos("US", "Tracking")
    u_v = cv2.getTrackbarPos("UV", "Tracking")
    
    
    l_b = np.array([84, 120, 74]) #범위를 결정하기 위해서
    u_b = np.array([255, 255, 255]) #범위를 결정하기 위해서

    mask = cv2.inRange(hsv, l_b, u_b) #마스크 씌우기!

    cv2.imshow("mask", mask) #선택한 색상, 채도, 명도만 나오게 하기!
    
    res = cv2.bitwise_and(frame, frame, mask=mask)
    
    cv2.imshow("mask2", res) 
    #gray = cv2.cvtColor(res, cv2.COLOR_RGB2GRAY)
    #ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY)
    #binary = cv2.bitwise_not(binary)
    #cv2.imshow("sss", binary)

    contours, hierachy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for i in range(len(contours)): #모든역역들 가져오기 위해서!
        if cv2.contourArea(contours[i]) >= 100: #영역의 크기가 500보다 클경우!
            #print(cv2.contourArea(contours[i]))
            #print(contours[i][0][0])# 가장 위에 위치 (x, y)
            
            if contours[i][0][0][1] >= center and change == 0:
                count += 1
                change = 1
            elif contours[i][0][0][1] < center and change == 1:
                change = 0
                
            cv2.drawContours(frame, [contours[i]], 0, (0, 0, 255), 2)
            cv2.putText(frame, str(i), tuple(contours[i][0][0]), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 1)
            
            
    cv2.line(frame, (0, int(center)), (width, int(center)), (0, 255, 0), 2) #중앙선 넘는지 보이기
    cv2.imshow("src", frame)
    print(count)
