import csv

NAME_FILE_TXT1 = "D:\\CodeField\\CODE_PYTHON\\name\\name1.txt"
NAME_FILE_CSV1 = "D:\\CodeField\\CODE_PYTHON\\name\\name1.csv"
NAME_FILE_CSV2 = "D:\\CodeField\\CODE_PYTHON\\name\\name2.csv"

def names_output_txt():
    with open(NAME_FILE_TXT1, "r") as file:
        names = []
        for line in file:
            names.append(line.strip())
        for name in sorted(names):
            if name == "Littorio":
                print(f"Hello, {name} ! You are the best!")
            else:
                print(f"Hello, {name} !")
        print("--------------")
    
def names_input_txt():
    with open(NAME_FILE_TXT1, "a") as file:
        while True:
            name = input("Name: ")
            if name == "" or name.isspace():
                break
            file.write(name + "\n")

def names_output_csv1():
    with open(NAME_FILE_CSV1, "r") as file:

        for line in sorted(file):
            row = line.strip().split(",")
            if row[0] == "Littorio":
                print(f"Hello, {row[0]} from {row[1]} ! You are the best!")
            else:
                print(f"Hello, {row[0]} from {row[1]} !")
        print("--------------")

def names_input_csv1():
    with open(NAME_FILE_CSV1, "a") as file:
        while True:
            line = input("Format: Name,Country: ").strip()
            if line == "" or line.isspace():
                break
            line.split(",")
            if len(line.split(",")) != 2:
                print("Invalid format. Please enter in 'Name,Country' format.")
                continue
            file.write(line + "\n")

def names_output_csv2():
    with open(NAME_FILE_CSV1, "r", newline='') as file:
        reader = csv.reader(file, skipinitialspace = True)
        next(reader, None)
        ships = []
        for name, country in reader:
            ships.append({"name": name.strip(), "country": country.strip()})
        for ship in sorted(ships, key = lambda ships: (ships["country"], ships["name"])):
            print(f"Hello, {ship['name']} from {ship['country']} !")
    print("--------------")

def names_input_csv2():
    with open(NAME_FILE_CSV1, "a", newline='') as file:
        writer = csv.DictWriter(file,fieldnames=["name","country"])
        name = input("Name: ").strip()
        country = input("Country: ").strip()
        if name == "" or name.isspace() or country == "" or country.isspace(): 
            return
        writer.writerow({"name": name, "country": country})
        
def names_output_csv3():
    with open(NAME_FILE_CSV2, "r", newline='') as file:
        reader = csv.reader(file, skipinitialspace = True)
        header = next(reader, None)
        ships = []
        if header is None:
            print("No data in the file.")
            return
        else:
            for row in reader:
                if len(row) != 3:
                    print("Invalid format. Corrupted data.")
                    return
                else:
                    ships.append({"name": row[0].strip(), "country": row[1].strip(), "type": row[2].strip()})
        for ship in sorted(ships, key = lambda ships: (ships["country"], ships["type"], ships["name"])):
            if ship["name"] == "Littorio":
                print(f"Hello, {ship['type']} {ship['name']} from {ship['country']} ! You are the best!")
            else:
                print(f"Hello, {ship['type']} {ship['name']} from {ship['country']} !")
    print("--------------")

def names_input_csv3():
    with open(NAME_FILE_CSV2, "a", newline='') as file:
        writer = csv.DictWriter(file, fieldnames = ["name", "country", "type"])
        while True:
            ip = input("Format: Name,Country,Type(space to stop):")
            if ip == "" or ip.isspace():
                break
            name, country, type = ip.split(",")
            if name == "" or country == "" or type == "":
                print("Invalid format. Please enter in 'Name Country Type' format.")
                continue
            writer.writerow({"name": name, "country": country, "type": type})







def main():
    print("Currently names in the file:")
    names_output_csv3()
    #print("Add new names (press Space to stop):")
    names_input_csv3()
    print("Updated names in the file:")
    names_output_csv3()

if __name__ == "__main__":
    main()