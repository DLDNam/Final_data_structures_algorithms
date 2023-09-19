class PrimeNumbers:
    def __init__(self, n):
        self.n = n
        self.primes = self.sieve_of_eratosthenes()

    def sieve_of_eratosthenes(self):
        primes = [True] * (self.n+1)
        primes[0] = primes[1] = False
        for p in range(2, int(self.n**0.5)+1):
            if primes[p]:
                for i in range(p*p, self.n+1, p):
                    primes[i] = False
        return [i for i in range(2, self.n+1) if primes[i]]

    def __str__(self):
        return "Cac so nguyen to nho hon hoac bang {} la: \n{}".format(self.n, self.primes)

n = int(input("Nhap n: "))
primes = PrimeNumbers(n)
print(primes)