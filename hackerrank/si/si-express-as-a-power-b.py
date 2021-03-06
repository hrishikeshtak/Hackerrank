#!/usr/bin/python3

# from math import sqrt

powers = set()


# def sqrt(N):
#     lo = 1
#     hi = N
#     ans = -1
#     while lo <= hi:
#         mid = (lo + hi) // 2
#         if mid * mid <= N:
#             ans = mid
#             lo = mid + 1
#         else:
#             hi = mid - 1
#     return ans


def store_powers():
    global powers
    for i in range(2, int(1e4)):
        p = i
        while p <= int(1e8):
            p = p * i
            powers.add(p)


def express_as_a_power_b(N):
    if N <= 2:
        return "No"

    if N in powers:
        return "Yes"
    else:
        return "No"

    # N_sqrt = int(sqrt(N))
    # count = 0
    # for i in range(2, N_sqrt + 1):
    #     p = i
    #     while p <= N:
    #         count += 1
    #         p *= i
    #         if p == N:
    #             # print("iterations: ", count)
    #             return "Yes"
    # # print("iterations: ", count)
    # return "No"


if __name__ == '__main__':
    # store all power upto 10**6, to avoid TLE
    store_powers()
    # print(powers)
    # print(len(powers))
    # print(max(powers))
    for _ in range(int(input())):
        N = int(input())
        print(express_as_a_power_b(N))
