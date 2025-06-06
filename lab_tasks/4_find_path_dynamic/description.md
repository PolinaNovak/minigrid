Задача: "Найти путь от стартовой позиции агента до целевой точки при динамическом
изменении карты"

Описание задачи:
Агент должен найти кратчайший путь от начальной точки до целевой
точки на двумерной карте, избегая препятствий. При этом после каждого 
шага агента, изменяются стены на карте. Карта представляет
собой сетку размером N×N, где каждая клетка может быть проходимой
(пустой) или непроходимой (препятствие).

Информация о сгенерированной карте (размеры, координаты агента в начале,
координаты цели) сохраняется в файле config_for_student.json. На данный момент
информация просто выводится в консоль через функцию print_map_info.

Ответом студента должен быть файл под названием student_solution.py. Основная функция
для построения пути должна называться solution(env, task_map). В 
качестве аргументов она принимает task_map - объект с вводными данными
для карты, env - объект окружения minigrid. На основе
этих данных простраивается корректный путь. Ответ функция должна генерировать после
каждого шага агента. Ответом должен быть массив координат следующего шага агента, например:
`[2, 10]`.

У объекта map можно обращаться к следующим полям для получения данных:
- 'grid_size'
- 'agent_start_pos'
- 'agent_start_dir'
- 'max_steps'
- 'goal_pos'
- 'walls'
- 'doors'
- 'keys'