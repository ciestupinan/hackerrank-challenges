"""
Read an integer N.
Without using any string methods, try to print: 123...N
Note that ... represents the values in between.

Input Format: The first line contains an integer .

Output Format: Output the answer as explained in the task.

	>>> print_int(3)
	123

	>>> print_int(12)
	123456789101112

	>>> print_int(100)
	123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100

"""


def print_int(n):
    out_num = 0

    for i in range(1,n+1):
        if i < 10 and n < 10:
            num_to_add = (i) * pow(10,n-i)
            out_num += num_to_add

        elif i < 10 and n >= 10:
            num_to_add = (i) * pow(10,10-i)
            out_num += num_to_add

        elif i == 10:
            num_to_add = i
            out_num *= 10
            out_num += num_to_add

        elif i > 10:
            num_to_add = (i)
            num_digits = len(str(i))
            out_num *= pow(10,num_digits)
            out_num += num_to_add
        
    print(out_num)


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED.\n")
