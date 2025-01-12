'''
    - Отвечает за визуализацию данных.
    - Содержит функции для создания и сохранения графиков цен закрытия и скользящих средних.
'''

import matplotlib.pyplot as plt     # для построения графиков
import pandas as pd     # для работы с таблицами


def create_and_save_plot(data, ticker, period, filename=None):
    '''
        Создаёт график, отображающий цены закрытия и скользящие средние.
        Предоставляет возможность сохранения графика в файл.
        Параметр filename опционален; если он не указан, имя файла генерируется автоматически.
    '''

    plt.figure(figsize=(10, 6))     # контейнер для хранения графиков

    if 'Date' not in data:  # если нет столбца Дата
        if pd.api.types.is_datetime64_any_dtype(data.index):    # проверка типа данных, если дата тайм
            dates = data.index.to_numpy()   # дата для X
            plt.plot(dates, data['Close'].values, label='Close Price')  # X, Y - дата закрытия и название
            plt.plot(dates, data['Moving_Average'].values, label='Moving Average')  # X, Y - Скользящая средняя (при наличии)
        else:
            print("Информация о дате отсутствует или не имеет распознаваемого формата.")
            return
    else:    # если есть столбец Дата
        if not pd.api.types.is_datetime64_any_dtype(data['Date']):
            data['Date'] = pd.to_datetime(data['Date'])
        plt.plot(data['Date'], data['Close'], label='Close Price')
        plt.plot(data['Date'], data['Moving_Average'], label='Moving Average')

    plt.title(f"{ticker} Цена акций с течением времени")
    plt.xlabel("Дата")
    plt.ylabel("Цена")
    plt.legend()    # инициирует отображение названия графика и различных надписей на нём

    if filename is None:
        filename = f"{ticker}_{period}_stock_price_chart.png"

    plt.savefig(f'png/{filename}')  # сохранение
    print(f"График сохранен как {filename}")
