from modules import api, universe, stream
from datetime import datetime, timedelta
import threading


def main():
    # get accounts numbers for linked accounts
    accountNumbers = api.accounts.accountNumbers().json()
    universe.credentials.encryptedId = accountNumbers[0].get('hashValue')
    print(accountNumbers)

    # get positions for linked accounts
    print(api.accounts.getLinkedAccounts().json())

    # get specific account positions
    print(api.accounts.getAccount().json())

    # get up to 3000 orders for an account for the past week
    print(api.orders.getOrders(3000, datetime.now()-timedelta(days=7), datetime.now()).json())

    # place an order (not being demonstrated for ovbious reasons)
    # api.orders.placeOrder(orderObject)

    # get a specific order
    # api.orders.getOrder(orderID)

    # cancel specific order
    # api.orders.cancelOrder(orderID)

    # replace specific order
    # api.orders.replaceOrder(orderID)

    # get up to 3000 orders for all accounts for the past week
    print(api.orders.getAllOrders(3000, datetime.now()-timedelta(days=7), datetime.now()).json())

    # preview order (not implemented by Schwab yet
    # api.orders.previewOrder(orderObject)

    # get all transactions for an account
    print(api.transactions.transactions(datetime.now()-timedelta(days=7), datetime.now()).json())

    # get details for a specific transaction
    # print(api.transactions.details(transactionId).json())

    # get user preferences for an account
    print(api.userPreference.userPreference().json())

    # get a list of quotes
    print(api.quotes.getList(["AAPL", "AMD"]).json())

    # get a single quote
    print(api.quotes.getSingle("INTC").json())

    # get a option chains
    # print(api.options.chains("AAPL").json()) # there are a lot to print

    #get an option expiration chain
    print(api.options.expirationChain("AAPL").json())

    # get price history for a symbol
    # print(api.pricehistory.getPriceHistory("AAPL").json()) # there are a lot to print

    #get movers for an index
    #print(api.movers.getMovers("$DJI"))

    #get marketHours for a symbol
    print(api.marketHours.getHours("AAPL").json())

    #get marketHours for a market
    print(api.marketHours.byMarket("equity").json())

    #get instruments for a symbol
    print(api.instruments.get("AAPL", "search").json())

    #get instruments for a cusip
    print(api.instruments.byCusip("037833100").json())  # 037833100 = AAPL



if __name__ == '__main__':
    print("Welcome to the unofficial Schwab api interface!\nGithub: https://github.com/tylerebowers/Schwab-API-Python")
    api.initialize()  # checks tokens & loads variables
    api.updateTokensAutomatic() # starts thread to update tokens automatically
    #stream.startManual() # start the stream manually
    main() #call the user code above
