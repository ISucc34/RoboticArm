import cv2 as cv




def main():

    cam = cv.VideoCapture(0)

    cv.namedWindow("trackbars")


    def hueUpper(val):
        print(val)

    def hueLower(val):
        print(val)

    def satUpper(val):
        print(val)

    def satLower(val):
        print(val)

    def valUpper(val):
        print(val)

    def valLower(val):
        print(val)
    
    cv.createTrackbar("Hue Upper", "trackbars", 0, 255, hueUpper)  
    cv.createTrackbar("Hue Lower", "trackbars", 0, 255, hueLower)
    cv.createTrackbar("Saturation Upper", "trackbars", 0, 255, satUpper)
    cv.createTrackbar("Saturation Lower", "trackbars", 0, 255, satLower)
    cv.createTrackbar("Value Upper", "trackbars", 0, 255, valUpper)
    cv.createTrackbar("Value Upper", "trackbars", 0, 255, valLower)
    
    while cam.isOpened():
        ret, frame = cam.read()

        cv.imshow("Camera",frame)
        #cv.imshow("trackbars")

        if cv.waitKey(1) == ord('q'):
            break
    
    cv.destroyAllWindows()


        


if __name__ == "__main__":
    main()