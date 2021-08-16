import random
r = random.randint(1, 100)
while True:
	num = input('請猜數字:')
	num =int(num)
	if r == num:
		print('你猜對了')
		break
	else:
		print('錯了!繼續猜')