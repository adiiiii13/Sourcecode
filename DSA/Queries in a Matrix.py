# Python3 implementation of program

# Fills initial values in rows[] and cols[]
def preprocessMatrix(rows, cols, m, n):

	# Fill rows with 1 to m-1
	for i in range(m):
		rows[i] = i;

	# Fill columns with 1 to n-1
	for i in range(n):
		cols[i] = i;

# Function to perform queries on matrix
# m --> number of rows
# n --> number of columns
# ch --> type of query
# x --> number of row for query
# y --> number of column for query
def queryMatrix(rows, cols, m, n, ch, x, y):

	# perform queries
	tmp = 0;
	
	if ch == 'R':

		# swap row x with y
		rows[x-1], rows[y-1] = rows[y-1], rows[x-1];

	elif ch == 'C':

		# swap column x with y
		cols[x-1], cols[y-1] = cols[y-1],cols[x-1];

	elif ch == 'P':

		# Print value at (x, y)
		print('value at (',x,',',y,') = ',rows[x-1]*n + cols[y-1]+1, sep='');
		
	return ;

# Driver program to run the case
m = 1234
n = 5678;

# row[] is array for rows and cols[]
# is array for columns
rows = [0 for i in range(m)]
cols = [0 for i in range(n)];

# Fill initial values in rows[] and cols[]
preprocessMatrix(rows, cols, m, n);

queryMatrix(rows, cols, m, n, 'R', 1, 2);
queryMatrix(rows, cols, m, n, 'P', 1, 1);
queryMatrix(rows, cols, m, n, 'P', 2, 1);
queryMatrix(rows, cols, m, n, 'C', 1, 2);
queryMatrix(rows, cols, m, n, 'P', 1, 1);
queryMatrix(rows, cols, m, n, 'P', 2, 1);

# This code is contributed by rutvik_56.
