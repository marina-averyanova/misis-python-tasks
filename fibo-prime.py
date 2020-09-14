import time


def fibonacci_divided_generator(divider):
    previous_fibo = 0
    # we use combinatorics definition due to task condition: start fibo with 1
    current_fibo = 1
    while True:
        yield current_fibo
        previous_fibo, current_fibo = current_fibo, (previous_fibo + current_fibo) % divider


def get_primes(n):
    # sieve of Eratosthenes
    primes = {}
    sieve = [True] * (n + 1)
    for num in range(2, n + 1):
        if sieve[num]:
            primes[num] = num
            for i in range(num * num, n + 1, num):
                sieve[i] = False
    return primes


def run(fibo_num, divider):
    # create sieve 0 to divider
    primes = get_primes(divider)
    # create divided fibo generator
    fibonacci_divided = fibonacci_divided_generator(divider)

    # values to define prime pairs
    previous_prime_value = 0
    is_previous_prime = False

    # result containers
    pairs_counter = 0
    first_of_pairs_sum = 0

    for i in range(fibo_num):
        # get current and check if prime
        current_value = next(fibonacci_divided)
        is_current_value_prime = primes.get(current_value) is not None

        if is_current_value_prime:

            # try to define pair and calculate it
            if previous_prime_value != 0 and is_previous_prime:
                pairs_counter += 1
                first_of_pairs_sum += previous_prime_value
                # set values to define pair on next step
                previous_prime_value = current_value
                is_previous_prime = True
            else:
                # set values to define pair on next step
                previous_prime_value = current_value
                is_previous_prime = True

        else:
            # set values to define pair on next step
            is_previous_prime = False

    print("count of pairs: " + str(pairs_counter) + " sum of first elements: " + str(first_of_pairs_sum))

# test


fibo_num = 14
divider = 10
start_time = time.time()
run(fibo_num, divider)
print("--- execution time %s seconds ---" % round(time.time() - start_time, 4))
# count of pairs: 3 sum of first elements: 8
# --- execution time 0.0 seconds ---

fibo_num = 1000
divider = 10000000
start_time = time.time()
run(fibo_num, divider)
print("--- execution time %s seconds ---" % round(time.time() - start_time, 4))
# count of pairs: 7 sum of first elements: 20910638
# --- execution time 2.1774 seconds ---
