def primes_sieve2(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in xrange(i*i, limit, i):     # Mark factors non-prime
                a[n] = False

if __name__ == '__main__':
    prime = []
    counter = 1
    next_prime = primes_sieve2(100000000)
    while True:
        prime.append(next_prime.next())
        if len(prime) == 10001:
            print prime[-1]
            break
        counter += 1
