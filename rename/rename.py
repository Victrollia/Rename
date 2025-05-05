import os

def main():
    while True:
        vendor = input("Manufacturer:")
        mpn = input("MPN:")
        index = input("Enter the index of the image (for example 1 for _01):")
        img_name = vendor.lower() + '-' + mpn.lower()
        img_name = img_name.replace(" ","-")
        img_name = img_name.replace("'","")
        i = 1
        old_path = os.getcwd() + r'\\upload\\'
        new_path = os.getcwd() + r'\\processed\\'
        for filename in os.listdir(old_path):
            old_name = old_path + filename
            new_name = new_path + img_name + '_0' + index + '.jpg'
            os.rename(old_name, new_name)
            i += 1
        print(str(i-1) + " images got renamed.\n\n")


if __name__ == '__main__':
    main()
