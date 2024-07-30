import datetime
from datetime import date
import sys
import inflect

def main():
    bday = validate(input("Date of Birth: "))
    minutes = math_it(bday)
    text = text_it(minutes)
    final_text = format_it(text)
    print(f"{final_text} minutes")

def validate(my_date):
    try:
        return datetime.date.fromisoformat(my_date)
    except ValueError:
        sys.exit("incorrect date format, YYYY-MM-DD")

def math_it(my_date):
    today = date.today()
    difference = today - my_date
    return (difference.total_seconds() / 60)

def text_it(numbers):
    p = inflect.engine()
    words = p.number_to_words(int(numbers))
    return words

def format_it(text):
    my_list = text.split(" and")
    #print(my_list)
    my_string = ''.join(my_list)
    return my_string.capitalize()

if __name__ == "__main__":
    main()
