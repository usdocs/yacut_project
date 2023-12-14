# yacut
[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=ffffff&color=5fe620)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/-Flask-464646?style=flat&logo=Flask&&logoColor=ffffff&color=5fe620)](https://flask.palletsprojects.com/en/latest/)
[![SQLAlchemy](https://img.shields.io/badge/-SQLAlchemy-464646?style=flat&logo=SQLAlchemy&logoColor=ffffff&color=5fe620)](https://www.sqlalchemy.org/)

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

```bash
git clone git@github.com:usdocs/yacut.git
cd yacut
```

Создать и активировать виртуальное окружение:
```bash
python -m venv env
source venv/Scripts/activate
```

Обновить менеджер пакетов pip:
```bash
python -m pip install --upgrade pip
```
Установить зависимости из файла requirements.txt:

```bash
pip install -r requirements.txt
```

Выполнить миграции:
```bash
flask db upgrade
```

Запустить проект:
```bash
flask run
```

Автор: [Балакин Андрей](https://github.com/usdocs)
