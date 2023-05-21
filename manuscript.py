import easyocr
import cv2
import numpy as np

# Inicie o leitor OCR.
reader = easyocr.Reader(['pt'])

# Abra a webcam.
cap = cv2.VideoCapture(0)

while True:
    # Leia a imagem da webcam.
    ret, frame = cap.read()
    if not ret:
        break

    # Converta a imagem para escala de cinza.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Se a tecla 's' for pressionada, salve a imagem.
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite('snapshot.png', gray)
        print('Imagem salva!')

        # Use o OCR para ler o texto da imagem.
        result = reader.readtext(gray)

        # Exiba o texto.
        detected_text = ""
        for res in result:
            detected_text += res[1] + ' '

        detected_text = detected_text.strip()  # Remova espaços em branco no início e no final.

        print('Texto detectado:', detected_text)

        break  # Interrompe a webcam assim que a imagem é salva.

    # Exiba a imagem.
    cv2.imshow('Webcam Feed', gray)

cap.release()
cv2.destroyAllWindows()
