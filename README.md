# yacut
[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=56C0C0&color=008080)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/-Flask-464646?style=flat&logo=Flask&&logoColor=56C0C0&color=008080)](https://flask.palletsprojects.com/en/latest/)
[![SQLAlchemy](https://img.shields.io/badge/-SQLAlchemy-464646?style=flat&logo=SQLAlchemy&logoColor=56C0C0&color=008080)](https://www.sqlalchemy.org/)

## сервис YaCut
Проект YaCut — это сервис укорачивания ссылок. Его назначение — ассоциировать длинную пользовательскую ссылку с короткой, которую предлагает сам пользователь или предоставляет сервис.
Ключевые возможности сервиса:
* генерация коротких ссылок и связь их с исходными длинными ссылками,
* переадресация на исходный адрес при обращении к коротким ссылкам.

Пользовательский интерфейс сервиса — одна страница с формой. Эта форма состоит из двух полей:
* обязательного для длинной исходной ссылки;
* необязательного для пользовательского варианта короткой ссылки.

## Технологии проекта
* Python — высокоуровневый язык программирования.
* Flask — Фреймворк для создания веб-приложений на языке программирования Python, использующий набор инструментов Werkzeug, а также шаблонизатор Jinja2.
* SQLAlchemy — Программная библиотека на языке Python для работы с реляционными СУБД с применением технологии ORM.

## Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:usdocs/yacut.git
```

```
cd yacut
```

Создать и активировать виртуальное окружение:
```
python -m venv env
```

```
source venv/Scripts/activate
```

Обновить менеджер пакетов pip:
```
python -m pip install --upgrade pip
```
Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```

Автор: [Балакин Андрей](https://github.com/usdocs)
