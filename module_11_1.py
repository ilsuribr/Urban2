import requests
from PIL import Image
from io import BytesIO

# Ссылка на изображение
url = "https://sun9-79.userapi.com/impg/BKBE-ILDRXTIH5Jexx_XumNiEkXb7YqRZyGBgg/d8TuFmSng9M.jpg?size=1080x1920&quality=95&sign=db24ed3e83f4a04434e49f6b45c2de26&type=album"

try:
    # Загрузка изображения через requests
    response = requests.get(url)
    response.raise_for_status()  # Проверяем, успешно ли выполнен запрос

    # Конвертация байтов в изображение с помощью Pillow
    image = Image.open(BytesIO(response.content))
    print("Оригинальный размер:", image.size)

    # Изменение размера изображения
    new_size = (150, 150)
    resized_image = image.resize(new_size)
    print("Новый размер:", resized_image.size)

    # Сохранение обработанного изображения
    resized_image.save("resized_image.png")
    print("Изображение сохранено как 'resized_image.png'")

except requests.exceptions.RequestException as e:
    print("Ошибка при загрузке изображения:", e)
except Exception as e:
    print("Ошибка при обработке изображения:", e)
