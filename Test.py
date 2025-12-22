key = ('....',
   'X..X',
   '.X..',
   '...X')
value = ('xhwc',
   'rsqx',
   'xqzz',
   'fyzr')
password = ''
key_turn = list(key)
for i in range(4):
    password += ''.join(ep for eg, ep in zip(''.join(key_turn), ''.join(value)) if eg == 'X')
    key_turn = [''.join(tpl) for tpl in zip(*key_turn[::-1])]
print(password)

