import pprint
message = 'Carlos André Cunha de Almeida, Graziela Mota dos Santos, Miguel Mota de Almeida. Nomes de uma grande família feliz!'
count = {}

for character in message:
    count.setdefault(character,0)
    count[character] = count[character] + 1

print(pprint.pformat(count))