#1.Regular Expressions — Extract Emails & Phone Numbers

import re

# Sample multiline text
text = """
Hello, you can reach me at john.doe@example.com or jane_smith123@work.org.
For urgent matters, call +1-202-555-0184 or (202) 555-0173.
Another email: test.email+filter@domain.co.in and phone: 9876543210.
"""

# Regex patterns
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
phone_pattern = r'(\+?\d[\d\-\(\) ]{8,}\d)'

# Extract all matches
emails = re.findall(email_pattern, text)
phones = re.findall(phone_pattern, text)

print("Emails found:", emails)
print("Phone numbers found:", phones)

#2. Recursion — Fibonacci Sequence

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        seq = fibonacci(n-1)
        seq.append(seq[-1] + seq[-2])
        return seq

# Generate first 10 Fibonacci numbers
print("Fibonacci Sequence:", fibonacci(10))


#3.Generators & Iterators — Prime Numbers up to n

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_generator(n):
    for num in range(2, n+1):
        if is_prime(num):
            yield num

# Generate primes up to 30
print("Prime numbers up to 30:", list(prime_generator(30)))

