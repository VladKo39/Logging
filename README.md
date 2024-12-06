# Домашнее задание по теме "Логирование"
## Цель: 
получить опыт использования простейшего логирования совместно с тестами.
## Задача Логирование бегунов":
В первую очередь скачайте исходный код, который нужно обложить тестами с [GitHub](https://github.com/yanchuki/HumanMoveTest/blob/master/rt_with_exceptions.py).
 (Можно скопировать)

**Основное обновление** - выбрасывание исключений, если передан неверный тип в **`name`**
и если передано отрицательное значение в **`speed`**.

Для решения этой задачи вам понадобиться класс ***RunnerTest** из предыдущей задачи.

В модуле **tests_12_4.py** импортируйте пакет **`logging`** и настройте **`basicConfig`** на следующие параметры:
>
>1. Уровень - **INFO**
>2. Режим - запись с заменой**('w')**
>3. Название файла - **runner_tests.log**
>4. Кодировка - **UTF-8**
>5. Формат вывода - на своё усмотрение, обязательная информация: *уровень логирования*,
*сообщение логирования*.

Дополните методы тестирования в классе ***RunnerTest*** следующим образом:
> **test_walk:**
>>1. Оберните основной код конструкцией ***try-except***.
>>2. При создании объекта **Runner** передавайте отрицательное значение в **speed**.
>>3. В блок **try** добавьте логирование **INFO** с сообщением **`'"test_walk" выполнен успешно'`**
>>4. В блоке **except** обработайте исключение соответствующего типа и логируйте его на уровне
>> **WARNING** с сообщением **`"Неверная скорость для Runner"`**.
>
> **test_run:**
>>1. Оберните основной код конструкцией **try-except**.
>>2. При создании объекта **Runner** передавайте что-то кроме строки в **`name`**.
>>3. В блок **try** добавьте логирование **INFO** с сообщением **`'"test_run" выполнен успешно'`**
>>4. В блоке **except** обработайте исключение соответствующего типа и логируйте его
>>    на уровне **WARNING** с сообщением **`"Неверный тип данных для объекта Runner"`**.
### Пример результата выполнения программы:
**Пример полученного файла логов runner_tests.log**:
[![image](https://github.com/user-attachments/assets/e3973e8e-6a08-44fe-bfc5-3d38656d6aac)
**Файл tests_12_4.py с классами тестов и runner_tests.log с логами тестов
загрузите на ваш GitHub репозиторий. В решении пришлите ссылку на него**.
 
