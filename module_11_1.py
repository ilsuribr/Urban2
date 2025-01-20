import requests
from PIL import Image
from io import BytesIO

image_url = "https://sun9-79.userapi.com/impg/BKBE-ILDRXTIH5Jexx_XumNiEkXb7YqRZyGBgg/d8TuFmSng9M.jpg?size=1080x1920&quality=95&sign=db24ed3e83f4a04434e49f6b45c2de26&type=album"

try:
    response = requests.get(image_url)
    response.raise_for_status()
    print("GET запрос выполнен успешно. Размер данных:", len(response.content), "байт")

    head_response = requests.head(image_url)
    print("HEAD запрос - заголовки ответа:", head_response.headers)

    post_response = requests.post("https://httpbin.org/post", data={"key": "value"})
    print("POST запрос - статус ответа:", post_response.status_code)

    image = Image.open(BytesIO(response.content))

    resized_image = image.resize((150, 150))
    print("Изменен размер изображения.")

    bw_image = resized_image.convert("L")
    print("Преобразовано в черно-белое изображение.")

    rotated_image = bw_image.rotate(45)
    print("Изображение повёрнуто на 45 градусов.")

    rotated_image.save("processed_image.png")
    print("Обработанное изображение сохранено как 'processed_image.png'.")

except requests.exceptions.RequestException as e:
    print("Ошибка в запросах:", e)
except Exception as e:
    print("Ошибка при обработке изображения:", e)
