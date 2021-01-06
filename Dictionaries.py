customer = {
    "name": "Bhagwati Dangi",
    "age": 30,
    "is_verified": True
}
print(customer["name"])
print(customer.get("birthdate"))
print(customer.get("birthdate", "jan 1 1980"))
customer["name"] = "mamta dangi"
print(customer["name"])