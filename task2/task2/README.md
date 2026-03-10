# Задание 2.2

## Файлы
`task2.cpp` - основной код
`CMakeLists.txt` - настройка сборки
`result.csv` - таблица результатов
`task2.py` - построение графика
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
./build/task2 > result.csv
```

## Построение графика
```bash
python task2.py
```