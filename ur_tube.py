import hashlib, time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.hash_password = User.hash_password(password)
        self.age = age

    def hash_password(password: str) -> str:
        # Преобразуем пароль в хэш-строку с использованием SHA-256
        return hashlib.sha256(password.encode()).hexdigest()

    def __str__(self):
        return f'Nick: {self.nickname}, Age: {self.age}'

    def __repr__(self):
        return f'{self.nickname}-{self.age}'


class UrTube:
    def __init__(self):
        self.current_user = None
        self.users = []
        self.videos = []

    def __contains__(self, user):
        if isinstance(user, User):
            return any(u.nickname == user.nickname for u in self.users)

    def log_in(self, nickname, password):
        find = False
        for user in self.users:
            if user.nickname == nickname and user.hash_password == User.hash_password(password):
                self.current_user = user
                find = True
                break
        if not find:
            print(f'Пользователь {nickname} не найден, либо не правильно введет пароль')

    def log_out(self):
        self.current_user = None

    def register(self, nickname, password, age):

        user = User(nickname, password, age)

        if user in self:
            print(f'Пользователь {user.nickname} уже существует')
        else:
            self.users.append(user)
            self.current_user = user

    def add(self, *args):
        for video in args:
            if video not in self:
                self.videos.append(video)

    def get_videos(self, word):
        result = []
        for video in self.videos:
            if video.title.lower().find(word.lower()) != -1:
                result.append(video.title)

        return result

    def watch_video(self, title_video):
        finded_video = None
        adult_video = False

        if not self.current_user:
            print('Войдите в аккаунт, чтобы посмотреть видео')
        else:
            for video in self.videos:
                if title_video == video.title:
                    finded_video = video
                    break

            if finded_video:
                if finded_video.adult_mode and self.current_user.age < 18:
                    adult_video = True

            if finded_video:
                if not adult_video:
                    for i in range(finded_video.time_now, finded_video.duration):
                        print(i, end=' ')
                        time.sleep(1)
                    print(f'Конец видео "{finded_video.title}"')
                else:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
            else:
                print(f'Видео с названием "{title_video}" не найдено')


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))
print(ur.get_videos('Герой'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)


# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
