string = "     boA tard2 4migo    "
string2 = "tarde"

print(string.upper())
print(string.lower())
print(string.capitalize())
print(string.strip())
print(string.replace("tarde", "NOITE"))
print(string.swapcase())
print(string.title())
print(string.replace(" ", "_"))
print(string[::-1])
print(string.find(string2))
print(string.count(string2))
print("boa {}".format(string2))
print(f"boa {string2}")
print(string2[-1:])
print(list(string2))
print(string2 * 5)

print(" ".join(string.split()[::-1]))

palavras = string.split()
iniciais = [word[0].upper() for word in palavras]
acronimo = ''.join(iniciais)

print(acronimo)
