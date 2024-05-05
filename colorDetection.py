import cv2
cap=cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)


while True:
    _,img=cap.read()
    hsv_img=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    height, width, _=img.shape

    cx=int(width/2)
    cy=int(height/2)
    img_center=hsv_img[cy,cx]
    hue=img_center[0]

    color="Undefined"

    if hue<10:
          color="RED"
    elif hue<15:
          color="ORANGE"
    elif hue<30:
          color="YELLOW"
    elif hue<40:
          color="LIME"
    elif hue<70:
          color="GREEN"
    elif hue<90:
          color="AQUA"
    elif hue<110:
          color="CYAN"
    
    elif hue<150:
          color="BLUE"
    elif hue<170:
          color="PURPLE"
    else:
          color="RED"
    
    img_color=img[cy,cx]
    b,g,r=int(img_color[0]),int(img_color[1]),int(img_color[2])
    cv2.putText(img,color,(10,70),0,2,(b,g,r),2)

    cv2.circle(img,(cx,cy),5,(25,25,25),3)
    cv2.imshow('cam',img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
            break

cap.release()

cv2.destroyAllWindows()


