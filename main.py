from  matplotlib import pyplot as plt
import colorsys
import cv2
import numpy as np
#-------------parte 2

#   1.  Calculo do histograma de imagem

imagem = cv2.imread('D:/Web/python/tarefa1_sm/ajudando.png',-1)
# plt.hist(imagem.ravel(),256,[0,256])
histograma = cv2.calcHist([imagem], [0], None, [256], [0,256])
plt.title('Histograma da imagem')
plt.plot(histograma)
plt.show()


#   2.  Conversao de cores RGB para HSV
(r,g,b) = (255, 255, 255)
(h, s, v) = colorsys.rgb_to_hsv(r, g, b)
print('HSV : ', h,s,v)

#   3.  Conversao de cores RGB para YUV
# m = np.array([[0,29900, -0,16874, 0,50000],
#               [0,58700, -0,33126, -0,41869], 
#               [0,11400, 0,50000, -0,28131 ] ])

# yuv = np.dot((255, 255, 255), m)
# yuv [:, :, 1 :] += 128,0
def rgb_yuv(r,g,b):
    y = 0.299 * r + 0.587 * g + 0.114 * b
    u = -0.147 * r -0.289 * g + 0.436 * b
    v = 0.615 * r -0.515 * g -0.100 * b 
    return y,u,v

(r,g,b) = (255,0,255)
y,u,v = rgb_yuv(r,g,b)
print('yuv : ', y,u,v)