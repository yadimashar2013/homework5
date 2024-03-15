my_list=['apple','banana','coconut','orange','pear','peach','melon']
print('List:',my_list)
print('First element:',my_list[0])
print('Last element:',my_list[6])
print('Sublist:',my_list[2:5])
my_list[0]=3
my_list[2]=True
my_list[5]=(1+2**3)
print('Modified list:',my_list)

my_dict={'gift':'дар','work':'работать','yet':'ещё','mission':'миссия'}
print(type(my_dict))
print('Dictionary:',my_dict)
print(my_dict['gift'])
my_dict['work']='спать'
print('Modified dictionary1:',my_dict)
my_dict['interest']='интерес'
print('Modified dictionary2:',my_dict)
