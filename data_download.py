'''
    - Отвечает за загрузку данных об акциях.
    - Содержит функции для извлечения данных об акциях из интернета и расчёта скользящего среднего.
'''

import yfinance as yf  # исторические данные об акциях


def fetch_stock_data(ticker, period='1mo'):
    '''
        Получает исторические данные об акциях для указанного тикера и временного периода. Возвращает DataFrame с данными.
    '''
    stock = yf.Ticker(ticker)  # уникальный торговый код
    data = stock.history(period=period)
    return data


def add_moving_average(data, window_size=5):
    '''
        Добавляет в DataFrame колонку со скользящим средним, рассчитанным на основе цен закрытия.
    '''
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data
