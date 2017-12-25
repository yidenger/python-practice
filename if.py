# age = 18
# if age >= 20:
# 	print('your age is', age)
# 	print('adult')
# else:
# 	print('your age is', age)
# 	print('teenager')

# s = input('birth: ')
# birth = int(s)
# if birth < 2000:
# 	print('00前')
# else:
# 	print('00后')

height = float(input('请输入你的身高: '))
weight = float(input('请输入你的体重: '))

bmi = weight / height
print('bmi: ', bmi)
msg = None;
if bmi < 18.3:
	msg = '过轻'
elif bmi >= 18.5 and bmi < 28:
	msg = '正常'
elif bmi >= 28 and bmi < 32:
	msg = '肥胖'
elif bmi >= 32:
	msg = '严重肥胖'

print(msg)