first = "Bhagwati"
last = "Dangi"

# how to print this message : Bhagwati [Dangi] is a coder
message = first +" ["+ last +"] is a coder." # but this is not ideal to formated string

# formatted string like below
msg = f'{first} [{last}] is a coder'
print(message)
print(msg)
