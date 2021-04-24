from PIL import Image
import face_recognition

# image'i yükle
image = face_recognition.load_image_file("image.jpg")

# resimdeki yüzleri bul
face_locations = face_recognition.face_locations(image)
person_image = face_recognition.load_image_file("person.jpg")

bilinen_yuzler = [
    person_face_encoding,
]


print("Fotoğrafta {} adet yüz bulundu".format(len(face_locations)))

for face_location in face_locations:

    # Resimdeki yüzlerin konumlarını yazdır
    top, right, bottom, left = face_location
    print("Yüzün bulunduğu piksel konumu = Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))
    face_recognition.com
    # yüz resminin gerçeğine ulaşılıyor:
    face_image = image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)

    results = face_recognition.compare_faces(bilinen_yuzler, pil_image)
    if results[0]==True:
        pil_image.show()
        break
