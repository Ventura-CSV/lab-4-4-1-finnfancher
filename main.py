def main():
    """
    ########################################
    Code Your Program here
    ########################################
    """
    num = (int)(input("Input a number: "))
    while(True):
        if(num > 0 and num < 100):
            number = num
            break
        else:
            num = (int)(input("Input a number: "))
            
        

    print(number)

    ########################################
    # Do not delete the return statement
    ########################################
    return number


if __name__ == '__main__':
    main()
