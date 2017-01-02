from ib.opt import Connection, message
from ib.ext.Contract import Contract
from ib.ext.Order import Order

def make_contract(symbol, sec_type, exch, prim_exch, curr):
    contract = Contract()
    contract.m_symbol = symbol
    contract.m_secType = sec_type
    contract.m_exchange = exch
    contract.m_primaryExch = prim_exch
    contract.m_currency = curr
    
    return contract


def make_order(action,quantity, price = None):
    order = Order()
    order.m_totalQuantity = quantity
    order.m_action = action

    if price is not None:
        order.m_orderType = 'LMT'
        order.m_lmtPrice = price

    else:
        order = Order()
        order.m_orderType = 'MKT'
        
    return order
    

def error_handler(msg):
    print "Server Error: %s" % msg

def reply_handler(msg):
    print "Server Response: %s, %s" % (msg.typeName, msg)


cid = 303

while __name__ == "__main__":

    conn = Connection.create(port=7497, clientId=3685)
    conn.connect()
    conn.register(error_handler, 'Error')
    conn.registerAll(reply_handler)
    oid = cid
    cont = make_contract('TSLA', 'STK', 'SMART', 'SMART', 'USD')
    offer = make_order('BUY', 1, 200)
    conn.placeOrder(oid, cont, offer)
    conn.disconnect()
    x = raw_input('enter to resend')
    cid += 1