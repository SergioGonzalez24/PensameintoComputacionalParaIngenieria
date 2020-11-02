def pali (t):
    if t[::-1]==t:
        print(1)
        return 1

    else:
        print(0)
        return 0

def main():
    texto=input()
    return pali(texto)

main()