import cv2
n = cv2.imread("C:/Users/Tigas/Documents/Estudo/perfilgit.jpg")
if n is None:
    print('Erro ao carregar imagem')
else:
    print('Imagem carregada')
    cv2.imshow('Minha imagem',n)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    imagem_cinza = cv2.cvtColor(n,cv2.COLOR_BGR2GRAY)
    cv2.imshow('Imagem cinza',imagem_cinza)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
