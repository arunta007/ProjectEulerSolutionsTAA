#-------------------------------------------------------------------------------
# Author:      ata
# Created:     10-08-2015
#-------------------------------------------------------------------------------

def summation():
    _sum = sum(x for x in range(1000) if (x % 3 == 0 or x % 5 == 0))
    print _sum

if __name__ == '__main__':
    summation()
