'''
import urllib.request
x = urllib.request.urlopen('https://www.google.com')
print(x.read())
'''
'''
x=input('What is your name?\n')
print('Hello',x)
'''
import statistics
example_list=[4,6,2,6,7,8,2,5,6,8,4,6,7,2,2]
x=statistics.stdev(example_list)
print(x)
import statistics
example_list=[4,6,2,6,7,8,2,5,6,8,4,6,7,2,2]
x=statistics.variance(example_list)
print(x)
