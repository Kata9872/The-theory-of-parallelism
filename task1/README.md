# Задание 1

## Файлы
`task.cpp` — основной код
`CMakeLists.txt` — настройка сборки
`.gitignore` — исключает папки сборки

## Как собрать

### Вариант 1: double (по умолчанию)
```bash
mkdir build && cd build
cmake ..
make
./task
```

### Вариант 2: float
```bash
mkdir build && cd build
cmake -DUSE_FLOAT=ON ..
make
./task
```