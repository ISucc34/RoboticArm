import cv2 as cv
import numpy as np



def main():

    cam = cv.VideoCapture(0)

    cv.namedWindow("trackbars")


    h_Max = 255
    h_Min = 0

    s_Max = 100
    s_Min = 0

    v_Max = 50
    v_Min = 0

    def hueUpper(val):
        global h_Max
        h_Max = val
        print(h_Max)

    def hueLower(val):
        global h_Min
        h_Min = val

    def satUpper(val):
        global s_Max
        s_Max = val

    def satLower(val):
        global s_Min
        s_Min = val

    def valUpper(val):
        global v_Max
        v_Max = val

    def valLower(val):
        global v_Min
        v_Min = val
    
    cv.createTrackbar("Hue Upper", "trackbars", 0, 255, hueUpper)  
    cv.createTrackbar("Hue Lower", "trackbars", 0, 255, hueLower)
    cv.createTrackbar("Saturation Upper", "trackbars", 0, 255, satUpper)
    cv.createTrackbar("Saturation Lower", "trackbars", 0, 255, satLower)
    cv.createTrackbar("Value Upper", "trackbars", 0, 255, valUpper)
    cv.createTrackbar("Value Lower", "trackbars", 0, 255, valLower)
    
    while cam:
        ret, frame = cam.read()

        lower_bound = np.array([h_Min, s_Min, v_Min])
        upper_bound = np.array([h_Max, s_Max, v_Max])

        HSVframe = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

        mask = cv.inRange(HSVframe, lower_bound, upper_bound)

        new = cv.bitwise_and(frame, frame, mask=mask)

        cv.imshow("Camera",frame)
        cv.imshow("Mask", new)


        if cv.waitKey(1) == ord('q'):
            break
    
    cv.destroyAllWindows()


        


if __name__ == "__main__":
    main()