#-------------------------------------------------------------------------------
# Name:        Reversing a String
# Purpose:     Different ways to reverse a string in python
#
# Author:      Kuldeep Rishi
#
# Created:     22-07-2013
#-------------------------------------------------------------------------------

string = "Hello, World!"
print "Original String","\t"*6,"==>  ", string
print "="*59

# Method 1  :  Define a function
# =================================
def reverse(string):
    result = ""
    for i in xrange(len(string), 0, -1):
        result = result+string[i-1] # i-1 so as to avoid out of index error
    return result

print "Method 1 : (Defining reverse function)","\t"*1,"==>  ", reverse(string)


# Method 2  :  Using Join
# =================================
print "Method 2 : (Using join)","\t"*4,"==>  ", "".join([string[i-1] for i in xrange(len(string), 0, -1)])


# Method 3  :  Using Join
# =================================
print "Method 3 : (Using join with reversed)","\t"*1,"==>  ", "".join(reversed(string))


# Method 4  :  Using Extended Slice
# =================================
print "Method 4 : (Using Extended Slice)","\t"*2,"==>  ", string[::-1]


# Method 5  :  Using Inbuilt function
# =================================
print "Method 5 : (Using Inbuilt function)","\t"*1,"==>  ", reverse(string)

