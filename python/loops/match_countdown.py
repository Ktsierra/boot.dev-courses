def countdown_to_start():
    for i in range(10, 0, -1) : 
        if (i==1) : print("1...Figth!")
        else : print(f"{i}...")
    return

# Don't edit below this line


def test():
    print("Counting down to match start:")
    countdown_to_start()
    print("=====================================")


def main():
    test()


main()

