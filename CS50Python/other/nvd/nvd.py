import requests
import sys
import json

#this program gets the current version of nvd cve file

def main():
    file_name = input("Give me a name for the file: ")
    try:
        response = requests.get("https://services.nvd.nist.gov/rest/json/cves/2.0")
    except requests.RequestException:
        sys.exit("bad request")
    o = response.json()
    with open(f"{file_name}.txt", "w") as out_file:
        json.dump(o, out_file, sort_keys = True, indent = 4, ensure_ascii = False)



if __name__ == "__main__":
    main()
