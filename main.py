# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import cv2
import png
import qrcode

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    data = "http://www.google.com"
    image = qrcode.make(data)
    image.save("img1.png")
    array1 = cv2.imread("img1.png")
    print(type(array1))
    qrcodeDetector: cv2.QRCodeDetector = cv2.QRCodeDetector()
    retval, points, straight_qrcode = qrcodeDetector.detectAndDecode(array1)
    print(retval)
    print(f"{points=}")
    print(f"{straight_qrcode=}")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
