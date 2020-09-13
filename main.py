import time


def generate_fibonacci(fibo_num, divider):
    # we are using combinatorics definition: start with 1
    previous_fibo = 1
    current_fibo = 1

    fibo_list = [previous_fibo, current_fibo]
    for i in range(2, fibo_num):
        previous_fibo, current_fibo = current_fibo, previous_fibo + current_fibo
        fibo_list.append(current_fibo % divider)
    return fibo_list


def sift_numbers(n):
    # sieve of Eratosthenes
    sieve = list(range(n + 1))
    sieve[1] = 0
    for i in sieve:
        if i > 1:
            for j in range(i + i, len(sieve), i):
                sieve[j] = 0
    return sieve


def sift_list(lst, sieve):
    for i in range(len(lst)):
        if sieve[lst[i]] == 0:
            lst[i] = 0


def calculate_pairs(lst):
    pairs_counter = 0
    first_of_pairs_sum = 0
    for i in range(len(lst) - 1):
        current_value = lst[i]
        next_value = lst[i + 1]
        if current_value > 0 and next_value > 0:
            pairs_counter += 1
            first_of_pairs_sum += current_value
    return [pairs_counter, first_of_pairs_sum]


def run(fibo_num, divider):
    # generate divided fibo list
    divided_fibo_list = generate_fibonacci(fibo_num, divider)
    # create sieve 0 to divider
    sieve = sift_numbers(divider)
    # filter non-prime values
    sift_list(divided_fibo_list, sieve)
    # calculate result
    result = calculate_pairs(divided_fibo_list)

    print("count of pairs: " + str(result[0]) + " sum of first elements: " + str(result[1]))


print(generate_fibonacci(1, 1))

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
# --- execution time 3.7871 seconds ---
