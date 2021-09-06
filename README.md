# Тестовое задание
## Описание
Данный проект реализован исключительно в учебных целях.  
Реализация выполнена в виде автоматизированного теста.
Задача данного проекта:
* Авторизация на сайте https://mail.yandex.ru;
* Подсчет количества сообщений на тему "Simbirsoft Тестовое задание";
* Отправка сообщения, в котором указано количество сообщений на данную тему, а также фамилия.  
## Установка
Проект реализован на языке программирования Python, поэтому для его запуска Вам понадобится интерпретатор Python.
Скачать его можно на [здесь](https://www.python.org).  
Поскольку проект реализован в виде теста, необходимо установить Selenium.  
Сделать это можно выполнив команду в комндной строке cmd:
```
pip install selenium
```
После устанавливаем модуль unittest:
```
pip install unittest
```
Также для запуска тестов Вам понадобится [selenium grid](https://www.selenium.dev/downloads/).  
На момент написания данных инструкций версия selenium grid 3.141.59.  
После скачивания, его необходимо скопировать на диск C и выполнить команду в cmd:
```
C:\>java -jar selenium-server-standalone-3.141.59.jar -role hub -port 8090
```
Для того, чтобы проверить что все заработало, необходимо в адресной строке браузера набрать:
```
http://localhost:8090/grid/console
```
Если у Вы все сделали правильно, то вы увидите следующее:
![Grid console](images/Снимок.PNG)
Драйверы, приложенные к проекту тоже необходимо скопировать на диск С.  
Далее необходимо настроить узлы selenium grid. Для этого каждую следующую комнду необходимо выполнять в новой консоли cmd.  
Настраиваем веб-драйверы для браузеров.  
Opera:
```
java -jar selenium-server-standalone-3.141.59.jar -role webdriver -hub http://localhost:8090/grid/register -port 5556 -browser browserName=opera
```  
Chrome:
```
java -Dwebdriver.chrome.driver=chromedriver.exe -jar selenium-server-standalone-3.141.59.jar -role webdriver -hub http://localhost:8090/grid/register -port 5558 -browser browserName=chrome
```
Firefox:
```
java -jar selenium-server-standalone-3.141.59.jar -role webdriver -hub http://localhost:8090/grid/register -port 5559 -browser browserName=firefox
```
Обновив страницу браузера, в которой находится selenium grid console, Вы должны увидеть следующее:
![Grid console with webdrivers](images/Снимок2.PNG)
## Запуск
Для запуска теста необходимо в папке проекта перейти в папку Support, найти в нем модуль Authorization.py и открыть его с помошью любимого редактора.
В строке 
```
login.send_keys('login')
``` 
вместо слова login необходимо указать свой адрес электронной почты.
В строке 
```
password.send_keys('password')
``` 
вместо слова password указать свой пароль.  
Сохраните и закройте.  
После, Вам необходимо запустить еще одну консоль cmd и перейти в директорию с данным проектом.
Запустите тест с помощью команды:
```
python main.py "browserName" "host"
```
где browserName - это имя одного из трех браузеров, а host - это это адрес одного из узлов selenium grid.
Например, запуск для браузера opera будет выглядеть так:
```
python main.py "opera" "http://192.168.0.101:5556/wd/hub"
```
В случае успешного завершения теста Вы увидите примерно следующую картину:
![Successful completion of the test ](images/Снимок3.PNG)