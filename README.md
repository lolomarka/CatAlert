Участники: Филатова А.А., Токарчук С.Д, Шеретов М.А.
Группа: АСУ-19-1б

## 1 Введение
### 1.1 Наименование программы
Наименование программы – "Кошачья сигнализация".

### 1.2 Краткая характеристика области применения
Программа предназначена для защиты от вторжения в рабочую зону пользователя инородных биологических организмов семейства кошачих.

## 2 Основания для разработки
Основанием для разработки послужила необходимость создания лабораторный работы - проекта по дисциплине "Интернет вещей".

## 3 Назначение разработки
Программа будет отслеживать появление нежелательных объектов семейства кошачих за рабочим местом пользователя во время его отсутствия. При появление нежелательного субъекта будет включен звук сирены и отправлено предупреждение о вторжение пользователю в мессенджер Telegram.

## 4 Требования к программе или программному изделию
### 4.1 Требования к функциональным характеристикам
Проект: Кошачья сигнализация. 
Во время старта программа помещается в режим ожидания. При возникновении физического контакта с рабочей поверхностью (движение компьютерной мыши) активируется камера(камера ноутбука или  веб-камера) и делает снимок. Снимок анализируется на наличие на нём биологических объектов семейства кошачих. Если объект обнаружен, программа включает аудиосигнал, для того чтобы прогнать объект. И отправляет снимок с объектом пользователю в мессенджер Telegram, также снимок помещается в папку-архив с датой срабатывания в названии. Если объект во время срабатывания триггера не найден, то программа помещает снимок в архив с указанием о ложной тревоге и датой срабатывания в названии и возвращается в начальное состояние.

### 4.2 Условия эксплуатации
Программа запускается на компьютере пользователя. 

Руководство по запуску приложения.

1. Установить python 3.6 и выше

2. Установить зависимости(в консоли). 
mouse (для работы с компьютерной мышью):
```
pip install mouse
```
pygame (используется для воспроизведения звука):
```
pip install pygame
```
OpenCV (используется для работы анализатора):
```
pip install opencv-python
```
TelegramBotAPI:
```
pip install pytelegrambotapi
```

Используется бот доступный по ссылке: https://t.me/detect_cat_bot .
Если есть необходимость, можно создать своего бота через @BotFather и записать сгенерированный token в файл telegramToken.txt

Бот пишет последнему написавшему одну из нижеописанных команд. 
Команды для работы с ботом: 
```
/яглавный } 
/пишимне  } Сообщить боту, что следует отправлять сигналы о тревоге вам.
/start    }
```
Бот работает при включённой программе. Бот может не ответить, если ему написать. При запуске программы он сразу отвечает всем написавшим.
### 4.3 Требования к составу и параметрам технических средств
Компьютер должен включать в себя:
1. процессор x86 с тактовой частотой, не менее 1 ГГц;
2. оперативную память объемом, не менее 1 Гб;
3. монитор, мышь, веб-камера;
4. подключение к Интернету.

## 5 Требования к программной документации
Предварительный состав программной документации:
1. программа;
2. документация в README.

## 6 Стадии и этапы разработки
Разработка должна быть проведена в 3 стадии:
1. анализ задачи;
2. программирование;
3. тестирование.
