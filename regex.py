import re

def regexbuilder():
    print("\n")
    pre = input("Prefix (e.g, 'flag{'): ").strip()
    suf = input("Suffix (e.g, '}'): ").strip()
    
    char_set = {
        1: ('Alphanumeric (A-Za-z0-9)', 'A-Za-z0-9'),
        2: ('Alphanumeric + Underscore', 'A-Za-z0-9_'),
        3: ('Alphanumeric + Hyphen', 'A-Za-z0-9-'),
        4: ('Hexadecimal lowercase (0-9a-f)', '0-9a-f'),
        5: ('Hexadecimal uppercase (0-9A-F)', '0-9A-F'), #1-128?
        6: ('ASCII Printable (all visible char)', r'\x20-\x7E'),
        7: ('Special characters (@#$%!&)', '@#$%!&')
    }
    
    print("\nSelect kar jaldi (comma-separated):")
    print("\n")
    for num, (desc, _) in char_set.items():
        print(f"{num}. {desc}")
    
    charset = ""
    while True:
        choices = input("> ").strip().split(',')
        try:
            choices = [int(c.strip()) for c in choices if c.strip()]
            if all(1 <= num <= 7 for num in choices):
                charset = ''.join(char_set[num][1] for num in choices)
                break
            print("Select from numbers 1-7 👋")
        except ValueError:
            print("Enter comma-separated numbers 👋")

    pozshtive_dhoka = f"[{charset}]+"
    
    negatibe_dhoka = f"^{re.escape(pre)}{pozshtive_dhoka}{re.escape(suf)}$"
    return re.compile(negatibe_dhoka)

def main():
    print("=== Flag Regex Checker ===")
    
    regex = regexbuilder()
    print(f"\nDomain: {regex.pattern}")
    
    print("\nEnter solutionsz for validation (CTRL+C to bunk):")
    while True:
        try:
            tryball = input("> ").strip()
            if regex.fullmatch(tryball):
                print("💚")
            else:
                print("😹") #hekadi
        except KeyboardInterrupt:
            print("\nhairaan")
            break

if __name__ == "__main__":
    main()