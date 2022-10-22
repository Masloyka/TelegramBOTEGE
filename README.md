#### ТЗ Для Лёни
### Формат входных данных
## Формат дорог
Файл со строками, описывающими дороги, ID точек представлены в виде целых чисел, данные идут через пробел
`ID стартовой точки, ID конечной точки, расстояние между ними`, дорога двусторонняя
## Формат первичного расписания
Файл представлен строками, описывающими рейсы, данные идут через пробел
`ID стартовой точки, ID конечной точки, номер рейса, количество пассажиров`
## Требования к алгоритму
У нас есть 30 автобусов вместимостью 100 человек и 10 автобусов вместимостью 50 человек, на выходе нужно представить файл формата:
`Номер рейса, номера автобусов,"привязанных" к этому рейсу, время рейса (в минутах)`
## Предположения по запросам
Нужно уметь пересчитывать оптимальное распределение автобусов в случае, если рейс заканчивается раньше или позже.
В случае, если у нас неожиданный рейс я думаю можно держать в уме, что кейс первоначально про уменьшение количества используемых автобусов, а это значит, что будет свободный автобус.
Автобус после окончания рейса стоит у гейта или на стоянке, не думаю, что он может стоять прямо в поле
## Предложения для формата запросов
Обновление времени
`номер рейса, новое время`
Новый рейс
`номер рейса, ID стартовой точки, ID конечной точки, количество пассажиров`