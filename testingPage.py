import api

#print(api.buy("KRW-XRP",100))
#print(api.get_balance())
#print(api.get_currency_balance('ETC'))
print(api.get_order_state("68482e2d-67c2-4894-92e2-8b32cca65c58"))
print(api.get_holds())