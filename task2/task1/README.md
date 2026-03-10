# Задание 2.1

## Файлы
`task1.cpp` - основной код
`CMakeLists.txt` - настройка сборки
`result.csv` - таблица результатов
`task1.py` - построение графика

## Как собрать
```bash
mkdir build && cd build
cmake ..
make
cd ..
```

## Запуск и сохранение результатов
```bash
./build/task1 > result.csv
```

## Построение графика
```bash
python task1.py
```