a, b, c = map(int, input().split())
remainder = 1
global dividend, divisor, gcd1stPair
gcd = 0

if a == 0 and b == 0 and c == 0:
    gcd = 0
elif a == 0 and b == 0 and c != 0:
    gcd = c
elif a == 0 and b != 0 and c == 0:
    gcd = b
elif a != 0 and b == 0 and c == 0:
    gcd = a
elif a == 0 and b != 0 and c != 0:
    if b == c:
        gcd = b
    elif b > c:
        dividend = b
        divisor = c
        while remainder != 0:
            remainder = dividend % divisor
            if remainder == 0:
                gcd = divisor
                break
            else:
                dividend = divisor
                divisor = remainder
    else:
        dividend = c
        divisor = b
        while remainder != 0:
            remainder = dividend % divisor
            if remainder == 0:
                gcd = divisor
                break
            else:
                dividend = divisor
                divisor = remainder
elif a != 0 and b != 0 and c == 0:
    if a == b:
        gcd = b
    elif a > b:
        dividend = a
        divisor = b
        while remainder != 0:
            remainder = dividend % divisor
            if remainder == 0:
                gcd = divisor
                break
            else:
                dividend = divisor
                divisor = remainder
    else:
        dividend = b
        divisor = a
        while remainder != 0:
            remainder = dividend % divisor
            if remainder == 0:
                gcd = divisor
                break
            else:
                dividend = divisor
                divisor = remainder
elif a != 0 and b == 0 and c != 0:
    if a == c:
        gcd = c
    elif a > c:
        dividend = a
        divisor = c
        while remainder != 0:
            remainder = dividend % divisor
            if remainder == 0:
                gcd = divisor
                break
            else:
                dividend = divisor
                divisor = remainder
    else:
        dividend = c
        divisor = a
        while remainder != 0:
            remainder = dividend % divisor
            if remainder == 0:
                gcd = divisor
                break
            else:
                dividend = divisor
                divisor = remainder                
elif a != 0 and b != 0 and c != 0:
    if a == b and b == c:
        gcd = a
    elif a == b and b != c:
        if a > c:
            dividend = a
            divisor = c
            while remainder != 0:
                remainder = dividend % divisor
                if remainder == 0:
                    gcd = divisor
                    break
                else:
                    dividend = divisor
                    divisor = remainder
        else:
            dividend = c
            divisor = a
            while remainder != 0:
                remainder = dividend % divisor
                if remainder == 0:
                    gcd = divisor
                    break
                else:
                    dividend = divisor
                    divisor = remainder            
    elif a == c and a != b:
        if a > b:
            dividend = a
            divisor = b
            while remainder != 0:
                remainder = dividend % divisor
                if remainder == 0:
                    gcd = divisor
                    break
                else:
                    dividend = divisor
                    divisor = remainder
        else:
            dividend = b
            divisor = a
            while remainder != 0:
                remainder = dividend % divisor
                if remainder == 0:
                    gcd = divisor
                    break
                else:
                    dividend = divisor
                    divisor = remainder        
    elif b == c and a != b:
        if b > a:
            dividend = b 
            divisor = a 
            while remainder != 0:
                remainder = dividend % divisor
                if remainder == 0:
                    gcd = divisor
                    break
                else:
                    dividend = divisor
                    divisor = remainder
        else:
            dividend = a
            divisor = b 
            while remainder != 0:
                remainder = dividend % divisor
                if remainder == 0:
                    gcd = divisor
                    break
                else:
                    dividend = divisor
                    divisor = remainder    
    elif a != b and b != c and a != c:
        # First, we need to find gcd(a, b)
        if a > b:
            dividend = a
            divisor = b 
            while remainder != 0:
                remainder = dividend % divisor
                if remainder == 0:
                    gcd1stPair = divisor
                    break
                else:
                    dividend = divisor
                    divisor = remainder 
        else:
            dividend = b
            divisor = a 
            while remainder != 0:
                remainder = dividend % divisor
                if remainder == 0:
                    gcd1stPair = divisor
                    break
                else:
                    dividend = divisor
                    divisor = remainder
        # Then, we find gcd(gcd1stPair, c) which is equivalent to gcd(gcd(a,b), c) = gcd(a, b, c)
        remainder = 1
        if gcd1stPair > c:
            dividend = gcd1stPair
            divisor = c
            while remainder != 0:
                remainder = dividend % divisor
                if remainder == 0:
                    gcd = divisor
                    break
                else:
                    dividend = divisor
                    divisor = remainder
        elif c > gcd1stPair:
            dividend = c
            divisor = gcd1stPair
            while remainder != 0:
                remainder = dividend % divisor
                if remainder == 0:
                    gcd = divisor
                    break
                else:
                    dividend = divisor
                    divisor = remainder   

if gcd == 1:
    print("YES")
else:
    print("NO")
