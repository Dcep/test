#This is a test function for py.test and jenkins
from funct import funct

def test_run():
	assert funct(1,2) == 2
	assert funct(2,3) == 7

def test_run2():
	assert funct(2,4) == 8
	assert funct(3,4) == 12
#run_test()
