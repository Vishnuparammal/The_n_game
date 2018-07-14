from itertools import cycle
comp = []
user = []
maindict = [comp,user]
data = []

def getData():
	mini = int(raw_input('enter minimum '))
	maxi = int(raw_input('enter maximum '))
	base = int(raw_input('enter base '))
	final = int(raw_input('enter final '))
	start = raw_input('do u wish to play first y/n ? ')
	if maxi<=mini or final<=base+maxi or mini<=0 or maxi<=0 or (start is not 'y' and start is not 'Y' and start is not 'n' and start is not 'N'):
		print "wrong input"				# ERROR check
		getData()
		return
	data.append(mini)					# storing data
	data.append(maxi)
	data.append(base)
	data.append(final)
	data.append(start)
 	return

def play(umove,cmove):						
	if maindict[0][0].count(cmove) is 1:			# to check win in first move when computer plays first		
		print 'computer wins'
		return						
	print "enter number"					# accept number from user
	prev = umove						
	umove = int(raw_input())
	if umove < cmove+data[0] or umove > cmove+data[1]:	# check range of user input number
		print 'play by rules'
		umove = prev
		play(umove,cmove)
		return
	elif maindict[0][0].count(umove) is 1:			# check if player win by entering X number
		print 'user wins'
		return
	elif umove > max(maindict[0][0]):			# special case of computer win when user is fool
		print 'computer wins'
		return	
	else:
		for a in range(data[0],data[1]+1):
			for b in range(len(maindict[0])):
				if maindict[0][b].count(umove+a) is 1:	# check if sum of
					cmove = umove+a			# user number and range [min,max]
					print cmove			# is present in computer moves
					play(umove,cmove)		# if YES , computer plays that number
					return
		cmove = umove + data[0]					# if NO, computer tries to buy time and wait for user's mistake
		print cmove						# computer plays 'base + min' (least possible number)
		play(umove,cmove)
		return
										
def Xnum():							# finding X number
	c_list = []
	a = data[3] - data[0]
	b = data[3]
	for c_no in range(a,b):					# for number in range [ finish - min , finish )
		if c_no >= data[0] + data[2]:			# check number is not less than least possible number(LPN)
			c_list.append(c_no)
	maindict[0].append(c_list)	
			
def treeStore(k,x):						# finding set of winning branch
	exit = 0
	alt = next(x)
	altx = next(x)
	c_list = []
	a = min(maindict[altx][k]) - data[alt]			# C -> U [ C.min - max , C.min -1 ]
	if alt is 0:						# U -> C [ C.min - min , C.max - min ]]	
		b = max(maindict[altx][k]) - data[0]
	elif alt is 1:
		b = min(maindict[altx][k]) - 1
	for c_no in range(a,b+1):
		if maindict[altx][k].count(c_no) is 0 and c_no >= data[0] + data[2]:	# number should be more than LPN
			c_list.append(c_no)			# if number present in previous set, it shouldn't be put in this set
	if len(c_list) is 0:					# check if list is empty,STOP
		return
	elif c_list[0] is data[0] + data[2]:			# if smallest number in list is LPN, append and then STOP
		maindict[alt].append(c_list)
		return
	else:							# if none of above condition is true, simply append
		maindict[alt].append(c_list)			
	if alt is 0:						# controlling value of k (method obtained from exmples)
		k+=1						
	next(x)							# reset cycle for next call						
	treeStore(k,x)
	
def main():	
	running = True						# program runs continuouly till user wants to stop
	while running:
		x = cycle([1,0])
		getData()
		Xnum()
		treeStore(0,x)
		#print comp					# see the computer moves for victory
		#print user					# see the user moves for victory
		#print data					# see game variables 		
		cmove = data[2]					# argument initialized
		if data[4] is 'n' or data[4] is 'N':		# if computer plays first 
			cmove = maindict[0][-1][0]		# it plays least of computer moves
			if cmove > data[1] + data[2]:		# but if above value is more than 'base + max'(largest possible value)
				cmove = data[0]	+ data[2]	# computer plays least possible value
			print cmove
		play(0,cmove)
		restart = raw_input('would you like to play again y/n ? ')
		if restart is not 'y' and restart is not 'Y':
			running = False
		del comp[:]					
		del user[:]					# clear list
		del data[:]	
	print "Good BYE !!!"					# finish game

if __name__ == '__main__':					# game starts here
	main()	
