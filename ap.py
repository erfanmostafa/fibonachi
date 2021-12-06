#! /usr/bin/python3
# erfanmostafa
# released under GPLv3+ Licence

def fibo(num):
    if num == 1:
        return 1
    if num == 2:
        return 1
    return fibo(num-1) + fibo(num-2)


def main():
    x = int(input("Enter your number:"))
    print(fibo(x))


if __name__ == "__main__":
    main()
