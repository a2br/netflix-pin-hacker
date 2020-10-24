import keyboard
import time
import sys


# Colors
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


print(f"{Colors.HEADER}Day{Colors.ENDC} # This mode tries every date of the year in the defined format")


# INPUTS
date_format = input("""
| Choose date format: (1)
|     1. DD/MM 
|     2. MM/DD
| Choice [1/2]: """) or "1"
if not (["1", "2"].count(date_format) > 0):
    print(f"{Colors.FAIL}Choice has to be 1 or 2")
    exit()
date_format = int(date_format)
time_between_each_keystroke = float(input("| Time between each keystroke: (0.08) ") or "0.08")
time_between_each_code = float(input("| Time between each code: (0.12) ") or "0.12")


# WAITS FOR START

print(f"{Colors.OKCYAN}[SHIFT] Waiting for signal...{Colors.ENDC}")
keyboard.wait("SHIFT")
startsAt = time.time()


# STARTS
def test_days(mode: int):
    for m in range(1, 12+1):
        month = str(m).zfill(2)
        for d in range(1, 31+1):
            day = str(d).zfill(2)
            if mode == 1:
                code = day+month
            else:
                code = month+day
            time.sleep(time_between_each_code)
            sys.stdout.write(f"{code} | {Colors.WARNING}__{Colors.ENDC}")
            sys.stdout.flush()
            for n in code:
                keyboard.write(n)
                time.sleep(time_between_each_keystroke)
            keyboard.write("\n")
            print(f"\r{code} | {Colors.OKCYAN}OK{Colors.ENDC}")


test_days(date_format)


# CONCLUDES
endsAt = time.time()
elapsed_time = endsAt - startsAt
print(f"{Colors.OKBLUE}[DONE] All dates of the year ({({1: 'DD/MM',2: 'MM/DD'})[date_format]}) tested in {round(elapsed_time)} seconds "
      f"({round(elapsed_time / 60, 2)} minutes){Colors.ENDC}")
