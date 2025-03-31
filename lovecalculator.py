name = str( input( 'input your name \n ' ) )
theirname = str(input('input their name \n '))
lowercase = name.lower( )
lowerthiers = theirname.lower()
t = lowercase.count('t') + lowerthiers.count('t')
r = lowercase.count('r') + lowerthiers.count('r')
u = lowercase.count('u') + lowerthiers.count('u')
e = lowercase.count('e') + lowerthiers.count('e')
l = lowercase.count('l') + lowerthiers.count('e')
o = lowercase.count('o') + lowerthiers.count('o')
v = lowercase.count('v') + lowerthiers.count('o')
total_add = str(t + r + u + e) + str(l + o + v + e )
total_int = int( total_add)
if total_int < 10 or total_int > 90 :
    print(f'Your score is {total_int}%,you guys go together like coke and mentos ' )
elif 40 <= total_int <= 50:
    print(f'your score is {total_int}%,you are alright together' )
else:
    print(f'your score is {total_int}%')
print('Thanks for using our LOVE CALCULATOR')
input('press ENTER to exit ' )






