""Marks tool - print a short report for a list of marks."""
from config import load_env
from stats import average, highest
MARKS=[72,65,88,91,54]
def main():
    setting=load_env()
    print(settings["APP_NAME"])
    print("count :", len(MARKS))
    print(""Average:", average(MARKS))
    print("Highest:", highest(MARKS))
if__nane__=="__main__":
   main()
