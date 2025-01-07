'''
    - Отвечает за загрузку данных об акциях.
    - Содержит функции для извлечения данных об акциях из интернета и расчёта скользящего среднего.
'''

import yfinance as yf  # исторические данные об акциях
import pandas as pd


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

    with open('files/data.csv', encoding='utf-8', mode='w') as file:
        file.write(data.to_csv())
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


def notify_if_strong_fluctuations(data, threshold, ticker, period):  # threshold - порог
    '''
        Уведомление о сильных колебаниях
    '''
    df = pd.DataFrame(data)
    # print(df.loc[:, 'Close'])
    minn = df.loc[:, 'Close'].min()
    maxx = df.loc[:, 'Close'].max()
    if maxx - minn > threshold:
        print(f'Цена акций {ticker} колебалась более чем на {threshold} '
              f'(на {maxx - minn}) за период {period}')
    # print(f'Минимальная цена закрытия за период = {minn}')
    # print(f'Максимальная цена закрытия за период = {maxx}')
    # print(f'Порог = {threshold}')
