# Задание 2.3

## Файлы
`task3.cpp` - основной код
`CMakeLists.txt` - настройка сборки
`result.csv` - таблица результатов
`task3.py` - построение графика
`speedup.png` - график

## Как собрать
```bash
mkdir build && cd build
cmake ..
make
cd ..
```

## Запуск и сохранение результатов
```bash
./build/task3_1 > result_1.csv
./build/task3_2 > result_2.csv
```

## Построение графика
```bash
python task3.py
```