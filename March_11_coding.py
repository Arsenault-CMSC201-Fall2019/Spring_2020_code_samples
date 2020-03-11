def calculate_root(num, root):

    # a function to calculate the nth root of a number

    r = num**(1/root)
    return r

if __name__ == "__main__":
    x = calculate_root(125,3)
    print(x)