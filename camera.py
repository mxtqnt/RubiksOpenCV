import cv2

def camera():
    cap = cv2.VideoCapture(0)
    i = 0
    fotos = []

    while True:
        ret, frame = cap.read()
        h, w, _ = frame.shape
        x, y = (w//2)//2, (h//2)//3
        tamanho = w//2
        quadrados = tamanho//3
        rois = [[x                  , y, quadrados],
                [x + quadrados      , y, quadrados],
                [x + quadrados * 2  , y, quadrados],
                  
                [x                  , y + quadrados, quadrados],
                [x + quadrados      , y + quadrados, quadrados],
                [x + quadrados * 2  , y + quadrados, quadrados],
                    
                [x                  , y + quadrados * 2, quadrados],
                [x + quadrados      , y + quadrados * 2, quadrados],
                [x + quadrados * 2  , y + quadrados * 2, quadrados]]
        
        rgb_quadrados = [0, 0, 0, 0, 0, 0, 0, 0, 0]

        for index, roi in enumerate(rois, start = 0): 
            x, y, largura = roi[0], roi[1], roi[2]
            roi = frame[y:y+quadrados, x:x+quadrados]
            rgb = cv2.mean(roi)
            rgb_quadrados[index] = rgb
            frame = cv2.rectangle(frame, (x, y), (x + largura, y + largura), (255, 255, 255), 1) 

        cv2.imshow('Camera', frame)
        key = cv2.waitKey(1)
        if key == 32 and i <= 6:
            print('Foto tirada!')
            fotos.append(rgb_quadrados)
            i += 1
        elif i >= 6:
            break

    cap.release()
    cv2.destroyAllWindows()
    return fotos