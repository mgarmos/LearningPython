"""
Comenzando proceso PR_CONSULTA_ESTRUCTURA_ en DEVO, hora: 2018-03-06 09:35
*****************************************
Parámetros de entrada: 
  P_CD_VENDR_IN: 10310721
  P_FX_VIGENCIA: 20200401
P_NOMBRE_VENDR: X Q, K
P_DTDZ: 216 D.T.LA RIOJA
P_CENTRO: 216  D.T.LA RIOJA
P_CD_VENDR_OUT: 10310721
P_AREA_GEO: 00000233 208 Area 8
P_AREA_COMER: 00000521 ÁREA COMERCIAL 6208
P_AREA_VENTA: 00000208 DT/DZ 208
P_ZONA_COMER: 00000208 DT/DZ 208
*****************************************
Parámetros de salida:
  P_IN_RESULT: 0
  P_IN_MSJ_ERROR: 
*****************************************
Proceso PR_CONSULTA_ESTRUCTURA_ terminado 2018-03-06 09:35
Comenzando proceso PR_CONSULTA_ESTRUCTURA_ en DEVO, hora: 2018-03-06 09:36
*****************************************

"""
class Customer(object):
  """Produces objects that represent customers."""
  def __init__(self, customer_id):
    self.customer_id = customer_id

  def display_cart(self):
    print "I'm a string that stands in for the contents of your shopping cart!"

class ReturningCustomer(Customer):
  """For customers of the repeat variety."""
  def display_order_history(self):
    print "I'm a string that stands in for your order history!"

monty_python = ReturningCustomer("ID: 12345")
monty_python.display_cart()
monty_python.display_order_history()