#All python modules and their functions
OS MODULE :
#Manipulating directories:
chdir()
getcwd()
listdir()
mkdir()
makedirs()
rmdir()
removedirs()
#Removing a file:
remove()
#Renaming files/directories:
rename()
#Using more than one process:
system()
popen()
close()
walk()
#User id and process id:
getgid(), os.getuid(), os.getpid()
#More about directories and files:
error
stat()
#Cross-plateform os attributes:
name
#Accessing environment variables:
environ
Random Module:
seed() -	Initialize the random number generator
getstate() -	Returns the current internal state of the random number generator
setstate() -	Restores the internal state of the random number generator
getrandbits() -	Returns a number representing the random bits
randrange() -	Returns a random number between the given range
randint()	- Returns a random number between the given range
choice()	- Returns a random element from the given sequence
choices()	- Returns a list with a random selection from the given sequence
shuffle()	- Takes a sequence and returns the sequence in a random order
sample()	- Returns a given sample of a sequence
random()	- Returns a random float number between 0 and 1
uniform()	- Returns a random float number between two given parameters
triangular() -	Returns a random float number between two given parameters, you can also set a mode parameter to specify the midpoint between the two other parameters
betavariate()	- Returns a random float number between 0 and 1 based on the Beta distribution (used in statistics)
expovariate()	- Returns a random float number based on the Exponential distribution (used in statistics)
gammavariate() - Returns a random float number based on the Gamma distribution (used in statistics)
gauss() -	Returns a random float number based on the Gaussian distribution (used in probability theories)
lognormvariate() -	Returns a random float number based on a log-normal distribution (used in probability theories)
normalvariate() -	Returns a random float number based on the normal distribution (used in probability theories)
vonmisesvariate() -	Returns a random float number based on the von Mises distribution (used in directional statistics)
paretovariate() -	Returns a random float number based on the Pareto distribution (used in probability theories)
weibullvariate() -	Returns a random float number based on the Weibull distribution (used in statistics)
Math module:
math.acos()	Returns the arc cosine of a number
math.acosh()	Returns the inverse hyperbolic cosine of a number
math.asin()	Returns the arc sine of a number
math.asinh()	Returns the inverse hyperbolic sine of a number
math.atan()	Returns the arc tangent of a number in radians
math.atan2()	Returns the arc tangent of y/x in radians
math.atanh()	Returns the inverse hyperbolic tangent of a number
math.ceil()	Rounds a number up to the nearest integer
math.comb()	Returns the number of ways to choose k items from n items without repetition and order
math.copysign()	Returns a float consisting of the value of the first parameter and the sign of the second parameter
math.cos()	Returns the cosine of a number
math.cosh()	Returns the hyperbolic cosine of a number
math.degrees()	Converts an angle from radians to degrees
math.dist()	Returns the Euclidean distance between two points (p and q), where p and q are the coordinates of that point
math.erf()	Returns the error function of a number
math.erfc()	Returns the complementary error function of a number
math.exp()	Returns E raised to the power of x
math.expm1()	Returns Ex - 1
math.fabs()	Returns the absolute value of a number
math.factorial()	Returns the factorial of a number
math.floor()	Rounds a number down to the nearest integer
math.fmod()	Returns the remainder of x/y
math.frexp()	Returns the mantissa and the exponent, of a specified number
math.fsum()	Returns the sum of all items in any iterable (tuples, arrays, lists, etc.)
math.gamma()	Returns the gamma function at x
math.gcd()	Returns the greatest common divisor of two integers
math.hypot()	Returns the Euclidean norm
math.isclose()	Checks whether two values are close to each other, or not
math.isfinite()	Checks whether a number is finite or not
math.isinf()	Checks whether a number is infinite or not
math.isnan()	Checks whether a value is NaN (not a number) or not
math.isqrt()	Rounds a square root number downwards to the nearest integer
math.ldexp()	Returns the inverse of math.frexp() which is x * (2**i) of the given numbers x and i
math.lgamma()	Returns the log gamma value of x
math.log()	Returns the natural logarithm of a number, or the logarithm of number to base
math.log10()	Returns the base-10 logarithm of x
math.log1p()	Returns the natural logarithm of 1+x
math.log2()	Returns the base-2 logarithm of x
math.perm()	Returns the number of ways to choose k items from n items with order and without repetition
math.pow()	Returns the value of x to the power of y
math.prod()	Returns the product of all the elements in an iterable
math.radians()	Converts a degree value into radians
math.remainder()	Returns the closest value that can make numerator completely divisible by the denominator
math.sin()	Returns the sine of a number
math.sinh()	Returns the hyperbolic sine of a number
math.sqrt()	Returns the square root of a number
math.tan()	Returns the tangent of a number
math.tanh()	Returns the hyperbolic tangent of a number
math.trunc()	Returns the truncated integer parts of a number
Math Constants
Constant	Description
math.e	Returns Euler's number (2.7182...)
math.inf	Returns a floating-point positive infinity
math.nan	Returns a floating-point NaN (Not a Number) value
math.pi	Returns PI (3.1415...)
math.tau	Returns tau (6.2831...)
Time Module:
time.time()
time.sleep()
time.ctime()
time.localtime()
time.mktime()
time.gmtime()
time.strptime()
time.strftime()
time.asctime()
Sys Module:
sys.argv
sys.executable
sys.exit
sys.modules
sys.path
sys.platform
sys.stdin/stdout/stderr
Collections module:
Counter
defaultdict
OrderedDict
deque
ChainMap
namedtuple()
Statistics module:
mean()	mean	mean or average	mean([1,4,5,5])	3.75
median()	median	middle value	median([1,4,5,5])	4.5
mode()	mode	most often	mode([1,4,5,5])	5
stdev()	standard deviation	spread of data	stdev([1,4,5,5])	1.892
