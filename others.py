import cv2
import numpy as np
# import pytesseract
from game_player.detect_keyboard_keys import key_check
# ---*---

def roi(img, x, x_w, y, y_h):
    return img[y:y_h, x:x_w]

def on_EVENT_LBUTTONDOWN(event, x, y, flags, param):
    global vertices
    if event == cv2.EVENT_LBUTTONDOWN:
        vertices.append([x, y])
        try:
            cv2.imshow("window", img)
        except NameError:
            pass
    return vertices

def get_xywh(img):
    global vertices
    vertices = []

    print('Press "ESC" to quit. ')
    cv2.namedWindow("window", cv2.WINDOW_NORMAL)
    cv2.setMouseCallback("window", on_EVENT_LBUTTONDOWN)
    while True:
        cv2.imshow("window", img)
        if cv2.waitKey(0)&0xFF==27:
            break
    cv2.destroyAllWindows()

    if len(vertices) != 4:
        print("vertices number not match")
        return -1

    x = min(vertices[0][0], vertices[1][0])
    x_w = max(vertices[2][0], vertices[3][0])
    y = min(vertices[1][1], vertices[2][1])
    y_h = max(vertices[0][1], vertices[3][1])

    cv2.imshow('img', img)
    cv2.imshow('roi(img)', roi(img, x, x_w, y, y_h))

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print(f'\n x={x}, x_w={x_w}, y={y}, y_h={y_h}\n')

# ---------- 以下需要修改 ----------

def get_Self_HP():
    # img = roi(img, x=73, x_w=144, y=432, y_h=464)
    # text2 = pytesseract.image_to_string(img,lang="eng",config=r'--oem 3 --psm 6 outputbase digits')
    # text2=text2.replace('\n', '').replace('\r', '').replace('-','').replace('.','').replace(' ','')
    # if text2=='' or text2== '.' or text2=='-' or text2==None:
    #     return np.float64(0)
    # else:
    #     text2=np.float64(text2)
    #     return text2
    if 'N' in key_check():
        return np.float64(1)
    else:
        return np.float64(0)


def get_Self_Posture():
    # img = roi(img, x=464, x_w=532, y=431, y_h=464)
    # text3 = pytesseract.image_to_string(img,lang="eng",config=r'--oem 3 --psm 6 outputbase digits')
    # text3=text3.replace('\n', '').replace('\r', '').replace('-','').replace('.','').replace(' ','')
    # if text3=='' or text3== '.' or text3=='-' or text3==None:
    #     return np.float64(0)
    # else:
    #     text3=np.float64(text3)
    #     return text3
    if 'M' in key_check():
        return np.float64(1)
    else:
        return np.float64(0)

def get_Target_HP():
    # img = roi(img, x=217, x_w=302, y=431, y_h=464)
    # text4 = pytesseract.image_to_string(img,lang="eng",config=r'--oem 3 --psm 6 outputbase digits')
    # text4=text4.replace('\n', '').replace('\r', '').replace('-','').replace('.','').replace(' ','')
    # if text4=='' or text4== '.' or text4=='-'or text4==None:
    #     return np.float64(0)
    # else:
    #     text4=np.float64(text4)
    #     return text4
    if 'G' in key_check():
        return np.float64(1)
    else:
        return np.float64(0)
# 不够就自己添加，多了就自己删除

def get_status():
    return get_Self_HP(), get_Self_Posture(), get_Target_HP()    # 这里也要改成相应的函数名

# ---------- 以上需要修改 ----------