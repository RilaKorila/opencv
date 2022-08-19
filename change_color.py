import cv2

img = cv2.imread("./imgs/ajisai.png")

def change_color():
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    show_img(gray)


# 表示
def show_img(img):
    cv2.imshow("OpenCV", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    change_color()
