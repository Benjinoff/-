from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    data = pd.read_excel('A:\ЗАГРУЗКИ\ТАКСИ ЗАДАНИЕ 1.xlsx')  # Замените 'путь_к_вашему_файлу.xlsx' на реальный путь к вашему файлу Excel
    return render_template('index.html', tables=[data.to_html(classes='data')], titles=data.columns.values)

if __name__ == '__main__':
    app.run(debug=True)
    # Загрузка данных из Excel файла
    df = pd.read_excel('A:\ЗАГРУЗКИ\ТАКСИ ЗАДАНИЕ 1.xlsx')  # Укажите путь к вашему файлу Excel

    # Вывод данных для проверки
    print(df)

# Пример фильтрации данных по конкретному значению в столбце
filtered_data = df[df['название_столбца'] == 'значение']
print(filtered_data)

# Пример сортировки данных по столбцу
sorted_data = df.sort_values(by='столбец_для_сортировки', ascending=True)  # ascending=False для сортировки по убыванию
print(sorted_data)

# Сохранение данных в новый Excel файл
filtered_data.to_excel('путь_к_новому_файлу.xlsx', index=False)  # Укажите путь для нового файла
