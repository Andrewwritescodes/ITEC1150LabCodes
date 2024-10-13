def main():
    Megabytes = float(input('Please enter number of Megabytes: '))
    Bytes = Megabytes_to_Bytes(Megabytes)
    print(f'{Megabytes} Megabyte(s) is equal to {Bytes} Bytes')

def Megabytes_to_Bytes(Megabytes):
    Bytes = Megabytes * 1000000
    return Bytes

main()