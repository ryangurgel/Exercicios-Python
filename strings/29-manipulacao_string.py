string = "     boA tard2 4migo    "
string2 = "tarde"

print("1" + string.upper())
print("2" + string.lower())
print("3" + string.capitalize())
print("4" + string.strip())
print("5" + string.replace("tarde", "NOITE"))
print("6" + string.swapcase())
print("7" + string.title())
print("8" + string.replace(" ", "_"))
print("9" + string[::-1])
print(string.find(string2))
print(string.count(string2))
print("12" + "boa {}".format(string2))
print("13" + f"boa {string2}")
print("14" + string2[-1:])
print(list(string2))
print("16" + string2 * 5)

print("17" + " ".join(string.split()[::-1]))

palavras = string.split()
iniciais = [word[0].upper() for word in palavras]
acronimo = ''.join(iniciais)

print("18" + acronimo)
