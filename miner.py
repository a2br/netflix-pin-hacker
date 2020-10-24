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


print(f"{Colors.HEADER}Miner{Colors.ENDC} # This mode tries every possible code in a defined range")


# INPUTS

start = int(input("| Start at: (0000) ") or "0000")
endStr = input("| End at: (9999) ") or "9999"
code_length = len(endStr)
end = int(endStr or "9999")+1
playing_time = (end-1)-start
if (playing_time != abs(playing_time)) or (start != abs(start)) or (end != abs(end)):
    print(Colors.FAIL + "Invalid inputs." + Colors.ENDC)
    exit()

print(f"{Colors.OKGREEN}Code format is {code_length} digits long{Colors.ENDC}: "
      f"{str(start).zfill(code_length)} ~ {str(end - 1).zfill(code_length)}")

time_between_each_keystroke = float(input("| Time between each keystroke: (0.06) ") or "0.06")
time_between_each_code = float(input("| Time between each code: (0.12) ") or "0.12")
estimated_time = ((time_between_each_keystroke * code_length) * playing_time) + (time_between_each_code * playing_time)\
                 + playing_time * 0.03  # This value may change

# WAITS FOR START
print(f"{Colors.OKGREEN}Estimated time to enter all codes is approximately "
      f"{Colors.BOLD}{round(estimated_time)} seconds{Colors.ENDC} "
      f"({round(estimated_time / 60, 2)} minutes){Colors.ENDC}")
print(f"{Colors.OKCYAN}[SHIFT] Waiting for signal...{Colors.ENDC}")
keyboard.wait("SHIFT")
startsAt = time.time()

# STARTS
for i in range(start, end):
    code = str(i).zfill(code_length)
    time.sleep(time_between_each_code)
    sys.stdout.write(f"{code} | {Colors.WARNING}__{Colors.ENDC}")
    sys.stdout.flush()
    for digit in code:
        keyboard.write(digit)
        time.sleep(time_between_each_keystroke)
    keyboard.write("\n")
    print(f"\r{code} | {Colors.OKCYAN}OK{Colors.ENDC}")

# CONCLUDES
endsAt = time.time()
elapsed_time = endsAt - startsAt
print(f"{Colors.OKBLUE}[DONE] {playing_time} combinations tested in {round(elapsed_time)} seconds "
      f"({round(elapsed_time / 60, 2)} minutes){Colors.ENDC}")
