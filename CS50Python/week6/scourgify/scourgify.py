import sys
import csv

def main():
    if len(sys.argv) != 3:
        sys.exit("incorrect number of args")
    exist = sys.argv[1]
    new = sys.argv[2]
    scourge(exist, new)
    with open(new, "r") as my_file:
                data = my_file.read()
                print(data)

def scourge(in_file, out_file):
    try:
        with open(in_file, "r") as file:
            #in_cont = file.read()
            #line_split = in_cont.splitlines()
            #print(in_cont)
            #print(line_split)
            #print(new_list)
            new_list = []
            #reader is a dictionary with the headers of file as keys (name, house)
            reader = csv.DictReader(file)
            for line in reader:
                #split first and last name on each line and assign to variable.  this works because 'name' and 'house' were assigned as headers
                lname,fname = line["name"].split(",")
                #remove space from beginning
                fname = fname.strip()
                #assign name of house to variable
                house = line["house"]
                #appending the names split from file to list of dicts
                new_list.append({"first": fname, "last": lname, "house": house})
            #print(new_list)
            with open(out_file, "w") as output:
                #takes list of dicts created earlier and puts them into rows
                #dictwriter creates an dictionary as rows object with fieldnames inside 'output' file
                writer = csv.DictWriter(output, fieldnames = ["first", "last", "house"])
                #print(writer)
                #writeheader() prints a row of headers (fieldnames) from dictwriter object
                writer.writeheader()
                #go down each line in list and print row with data for each fieldname
                for line in new_list:
                    writer.writerow(line)


    except FileNotFoundError:
        sys.exit("no such file")
if __name__ == "__main__":
    main()
