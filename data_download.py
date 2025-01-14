'''
    - Отвечает за загрузку данных об акциях.
    - Содержит функции для извлечения данных об акциях из интернета и расчёта скользящего среднего.
'''

import yfinance as yf  # исторические данные об акциях
import pandas as pd
import numpy as np


def fetch_stock_data(ticker, period='1mo'):
    '''
        Получает исторические данные об акциях для указанного тикера и временного периода. Возвращает DataFrame с данными.
    '''
    stock = yf.Ticker(ticker)  # уникальный торговый код
    data = stock.history(period=period)
    '''
        Date - Дата
        Open - Открытие	
        High - Максимум	
        Low	- Минимум
        Close - Закрытие	
        Volume - Объем	
        Dividends - Дивиденды	
        Stock Splits - Дробление акций
    '''
    return data


def add_moving_average(data, window_size=5):
    '''
        Добавляет в DataFrame колонку со скользящим средним, рассчитанным на основе цен закрытия.
    '''
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data


def calculate_and_display_average_price(data):
    '''
        Вывод средней цены за период
    '''
    df = pd.DataFrame(data)
    avg = df.loc[:, 'Close'].mean()
    print(f'Средняя цена закрытия за период = {avg}')


def notify_if_strong_fluctuations(data, threshold, ticker, period):
    '''
        Уведомление о сильных колебаниях
    '''
    df = pd.DataFrame(data)
    min = df.loc[:, 'Close'].min()
    max = df.loc[:, 'Close'].max()
    if max - min > threshold:
        print(f'Цена акций {ticker} колебалась более чем на {threshold} (на {max - min}) за период {period} ')


def export_data_to_csv(data, filename):
    '''
        Экспорт данных в CSV
    '''
    headers = ';'.join(str(el) for el in data.columns.to_list())
    np.savetxt(f'files/{filename}.csv', data, fmt='%s', delimiter=';', header=headers)  # fmt='%.4f'
    print(f'Данные сохранены в папку files файл {filename}.csv')
