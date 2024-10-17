CUSTOMERS = [
    {
        "id": 1,
        "name": "Bever Hopox"
    },
    {
      "id": 2,
      "name": "Chico Hands"
    }
]

def get_all_customers():
  return CUSTOMERS

def get_single_customer(id):
  requested_animal = None

  for customer in CUSTOMERS:
    if customer["id"] == id:
     requested_customer = customer

    return requested_customer
