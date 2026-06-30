from tradingview_ta import TA_Handler, Interval
from symbols import TV_SYMBOLS


def get_tv_prices():

    result = {}

    for key, (exchange, symbol) in TV_SYMBOLS.items():

        try:

            handler = TA_Handler(
                symbol=symbol,
                exchange=exchange,
                screener="crypto" if exchange == "BINANCE" else "forex",
                interval=Interval.INTERVAL_1_MINUTE,
            )

            analysis = handler.get_analysis()

            result[key] = {
                "price": str(round(analysis.indicators["close"], 2)),
                "change": analysis.indicators.get("change", 0)
            }

        except Exception as e:

            print(f"TradingView Error ({key}) -> {e}")

            result[key] = {
                "price": "ERROR",
                "change": 0
            }

    return result
