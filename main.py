'''
    - Является точкой входа в программу.
    - Запрашивает у пользователя тикер акции и временной период, загружает данные, обрабатывает их
    и выводит результаты в виде графика.
'''

import data_download as dd
import data_plotting as dplt


def main():
    print("Добро пожаловать в инструмент получения и построения графиков биржевых данных.")
    print("Вот несколько примеров биржевых тикеров, которые вы можете рассмотреть: "
          "AAPL (Apple Inc), GOOGL (Alphabet Inc), MSFT (Microsoft Corporation), "
          "AMZN (Amazon.com Inc), TSLA (Tesla Inc).")
    print("Общие периоды времени для данных о запасах включают: "
          "1д, 5д, 1мес, 3мес, 6мес, 1г, 2г, 5г, 10л, с начала года, макс. "
          "('1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max')")

    ticker = input("Введите тикер акции (например, «AAPL» для Apple Inc):»")
    period = input("Введите период для данных (например, '1mo' для одного месяца): ")
    threshold = 'a'
    while not isinstance(threshold, float):
        try:
            threshold = float(threshold)
        except:
            threshold = input("Введите максимально допустимый порог колебаний цены (например, 1): ")

    # Fetch stock data - получение исторических данных
    stock_data = dd.fetch_stock_data(ticker, period)

    # Add moving average to the data - расчёт скользящего среднего
    stock_data = dd.add_moving_average(stock_data)

    # Plot the data - создание и сохранение графика
    dplt.create_and_save_plot(stock_data, ticker, period)

    # Вывод средней цены за период
    dd.calculate_and_display_average_price(stock_data)

    # Уведомление о сильных колебаниях
    dd.notify_if_strong_fluctuations(stock_data, threshold, ticker, period)

    # Экспорт данных в CSV
    dd.export_data_to_csv(stock_data, f'{ticker}_{period}_data')


if __name__ == "__main__":
    main()
