# Скачайте любой датасет с сайта https://www.kaggle.com/datasets
# Загрузите набор данных из CSV-файла в DataFrame.
# Выведите первые 5 строк данных, чтобы получить представление о структуре данных.
# Выведите информацию о данных (.info()) и статистическое описание (.describe()).

# series =pd.Series(data)
# df = pd.DataFrame(data)
# df = pd.read_csv('')
# df = pd.read_excel('')
# print(series)

import pandas as pd

def task1():
    # Загрузка данных из CSV-файла в DataFrame
    file_path = 'Paris Olmypics total medal tally 2024 - Sheet1.csv'
    df = pd.read_csv(file_path)

    # Вывод первых 5 строк данных
    print("Первые 5 строк данных:")
    print(df.head())

    # Вывод информации о данных
    print("\nИнформация о данных:")
    print(df.info())

    # Статистическое описание данных
    print("\nСтатистическое описание данных:")
    print(df.describe())


def task2():
    # Загрузка данных из CSV-файла в DataFrame
    file_path = 'dz.csv'
    df = pd.read_csv(file_path)

    # Проверка наличия необходимых столбцов
    if 'City' in df.columns and 'Salary' in df.columns:
        # Вычисление средней зарплаты по городу
        avg_salary_by_city = df.groupby('City')['Salary'].mean()
        print("\nСредняя зарплата по городу:")
        print(avg_salary_by_city)
    else:
        print("Ошибка: В данных отсутствуют необходимые столбцы 'City' и 'Salary'.")


def main():
    # Запрос у пользователя, какое задание выполнить
    task_number = input("Введите номер задания (1 или 2): ").strip()

    if task_number == '1':
        task1()
    elif task_number == '2':
        task2()
    else:
        print("Ошибка: Неверный номер задания. Пожалуйста, введите 1 или 2.")


if __name__ == "__main__":
    main()