You may have probably played __ The '21' game:

That exact game has been generalized taking it to an extreme level.

Better warm up 'coz this program's gonna beat you.

Open game on terminal using command:

		'python The_n_game.py'

	Rules of the game:

You will be asked 4 numbers in order to create the game. They are:
minimum, maximum, base and final.

minimum - the least number of 'numbers' you need to go ahead
maximum - the most number of 'numbers' you are allowed to go upto.
base - decides the number from which to start the game.
final - the one who reaches/crosses the final, loses the game.

	I'll explain it with an example:

minimum	3
maximum	5
base	10	{this is 0  for The '21' game}
final	30	{this is 21 for The '21' game}
do you wish to start first (y/n) ? y

enter number
		now, its your turn to enter the number
		since the base is 10, you can start counting from 11
		since minimum is 3 and maximum is 5
		you need to count upto atleast 3 and atmost 5 numbers.
		lets count...11,12,13(minimum)
		or... 11,12,13,14
		or...11,12,13,14,15(maximum)
		This means you can enter any of these numbers: 13/14/15 
		you cannot enter 11,12 or any number more than 15 or less than base. 
		You will be asked to re-enter if your number is out of bounds of rule.
		so, as an example, lets put 14.
		
enter number
14

		now its program's turn to play.
		program will enter any among these numbers 17/18/19
		as per the rules explained above.
		lets say it enters 19
		
19
		and so the game continues
enter number
22		{user input}
26		{program input}
enter number	
		now its time for the final move
		you can enter one among these numbers 29/30/31
		
		if you enter 29:
		on the program's next move, it will count this way:
		30,31,32 (minimum)
		or 30,31,32,33
		or 30,31,32,33,34 (maximum)
		
		since, in all the above conditions
		you have forced the program to cross the number 30
		which means you win
		
enter number
29
USER WINS
		an interesting thing to note here is that
		you would win even if the final was 31/32
		beacuse the program was forced to count upto or cross those numbers.
		but if you had entered 30/31 in the last turn
		you would have lost

	enter number	
	30
	COMP WINS
	
You can try every combination of minimum, maximum, base and final
Try out negative bases and final (final should be more than base)
if you want longer games, increase the gap between base and final.
try out long games with short min/max for more challenging gameplay.

!!!!! Hope you enjoy !!!!!
