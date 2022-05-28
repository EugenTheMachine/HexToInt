import exch

# в зависимости от того, в какой системе счисления вводится входное значение,
# автоматически вызываются или функции перевода hex -> int, или функции int -> hex
value = input('Enter the value: ')
if value[0] == '0' and value[1] == 'x':
    value_mod = value.replace('0x', '')
    print(exch.hex_to_int_litend(value_mod))
    print(exch.hex_to_int_bigend(value_mod))
else:
    print(exch.bigend_int_to_hex(value))
    print(exch.litend_int_to_hex(value))