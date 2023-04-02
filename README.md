## Проект API автотестов
### Используемые технологии
<p  align="center">
<code><img width="5%" title="Python" src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Python.svg/1024px-Python.svg.png"></code>
<code><img width="5%" title="Pycharm" src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/PyCharm_Icon.svg/1200px-PyCharm_Icon.svg.png"></code>
<code><img width="5%" title="Pytest" src="https://upload.wikimedia.org/wikipedia/commons/b/ba/Pytest_logo.svg"></code>
<code><img width="5%" title="Selene" src="https://fs.getcourse.ru/fileservice/file/download/a/159627/sc/264/h/e0cabcb69a2df1e6b1086292c020a4a7.png"></code>
<code><img width="5%" title="Selenium" src="http://www.loadview-testing.com/wp-content/uploads/Selenium_Logo-1.png"></code>
<code><img width="5%" title="Selenoid" src="https://aerokube.com/selenoid/latest/img/og-image.jpg"></code>
<code><img width="5%" title="Requests" src="https://upload.wikimedia.org/wikipedia/commons/a/aa/Requests_Python_Logo.png"></code>
<code><img width="5%" title="Allure Report" src="https://avatars.githubusercontent.com/u/5879127?s=200&v=4"></code>
<code><img width="5%" title="Allure TestOps" src="https://marketplace-cdn.atlassian.com/files/92e2d8c3-2a30-46c0-bf21-2453a4a270d3?fileType=image&mode=full-fit"></code>
<code><img width="5%" title="Jenkins" src="https://avatars.githubusercontent.com/u/2520748?v=4"></code>
<code><img width="5%" title="GitHub" src="https://cdn-icons-png.flaticon.com/512/25/25231.png"></code>
<code><img width="5%" title="Telegram" src="https://cdn.icon-icons.com/icons2/923/PNG/256/telegram_icon-icons.com_72055.png"></code>
</p>
<br> 

### Проекст состоит из двух групп тестов:
<details><summary><b>reqres.in - только api тесты</b></summary>
<ul>
  <li>Создание пользователя</li>
  <li>Обновление пользователя через метод patch</li>
  <li>Получение списка пользователей</li>
</ul>

</details>
<details><summary><b>demowebshop - комбинированные ui+api тесты</b></summary>
<br> 
<ul>
  <li>Успешная авторизация</li>
  <li>Выход из аккаунта</li>
  <li>Просмотр страницы профиля</li>
  <li>Поиск</li>
  <li>Просмотр страницы смены пароля</li>
</ul>
</details>
<br>

## Как запустить
Перед выполнением необходимо:
* в .env определить параметры конфигурации:
```
LOGIN = email пользователя
PASSWORD= пароль пользователя
LOCAL_DEMOQA = url проекта для локального запуска
TEST_DEMOQA = url проекта текстового контура
TEST2_DEMOQA= url проекта текстового контура
PROD_DEMOQA= url проекта продовского контура
LOCAL_REQRESIN = url проекта для локального запуска
TEST_REQRESIN = url проекта текстового контура
TEST2_REQRESIN= url проекта текстового контура
PROD_REQRESIN= url проекта продовского контура

```

### Локально
```
pytest tests/test_reqres.py --env=prod
```

### Удаленно
```
python -m venv .venv
source .venv/bin/activate
pip install poetry 
pytest . --env=prod || true
```


### <img width="3%" title="Jenkins" src="https://avatars.githubusercontent.com/u/2520748?v=4"> [Запуск проекта в Jenkins](https://jenkins.autotests.cloud/job/qa_diplom_api/)
##### При нажатии на "Собрать сейчас" начнется сборка тестов и их прохождение на сервере Jenkins.
![Jenkins_run](/images/jenkins.jpg)

### <img width="3%" title="Allure Report" src="https://avatars.githubusercontent.com/u/5879127?s=200&v=4"> Allure report
##### После прохождения тестов, результаты можно посмотреть в Allure отчете.
![Overview](images/report.jpg)

##### Во вкладке Behaviors находятся собранные тест кейсы, у которых описаны шаги. Для api методов реализованы вложения. Для комбинированных тестов по окончанию теста делается скриншот и сохраняется видеозапись теста.
![Behaviors](images/report_behaviors.jpg)

##### Видео теста просмотра данных пользователя, авторизация происходит по api, проверка полей и данных через ui.
![This is an image](images/test_ui.gif)

В проекте используется встроенный logger - logging:
![This is an image](images/logs.jpg)
##### Так же вся отчетность сохраняется в Allure TestOps, где строятся аналогичные графики.
![Graf](images/testops.jpg)

#### Во вкладке со сьютами, мы можем:
- Управлять всеми тест-кейсами или с каждым отдельно
- Перезапускать каждый тест отдельно от всех тестов
- Настроить интеграцию с Jira
- Добавлять ручные тесты и т.д

![tests](images/testops2.jpg)


### <img width="3%" title="Telegram" src="https://cdn.icon-icons.com/icons2/923/PNG/256/telegram_icon-icons.com_72055.png"> Интеграция с Telegram
##### После прохождения тестов, в Telegram bot приходит сообщение с графиком и небольшой информацией о тестах.

![Telegram](images/telega.jpg)


