import cv2 as cv

img_path = 'C:/Users/alex/Dropbox/repositorio_git/curso_python/imagem_7.jpg'

img = cv.imread(img_path)
cv.imshow('imagem', img)
cv.waitKey(0)

print('FIM')