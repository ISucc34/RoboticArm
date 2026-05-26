import cv2 as cv



def main():

    cam = cv.VideoCapture(0)

    
    while cam.isOpened():
        ret, frame = cam.read()

        cv.imshow("Camera",frame)

        if cv.waitKey(1) == ord('q'):
            break

        


if __name__ == "__main__":
    main()