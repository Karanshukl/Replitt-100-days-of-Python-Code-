# If you have queries regarding any codes or your personal project DM/Comment me.

RED = "\033[031m"
BLUE = "\033[034m"
WHITE = "\033[1;37m"
END="\033[0m"
YELLOW = "\033[1;33m"
GREEN = "\033[0;32m"
PINK = "\033[1;35m"

def musicPlayer ():
  songname = 'Radio Gaga'
  singer = 'Queen'
  tittle = f'{RED}={WHITE}={BLUE}={YELLOW} { "Music App" } {YELLOW} {BLUE}={WHITE}={RED}='
  print(f"{tittle:>90}")
  print()
  print()
  print(f"🔥▶️{WHITE}       {songname}")
  print(f"{YELLOW}          {singer}") 
  print()
  prev = 'PREV'
  NEXT = 'NEXT'
  pause = 'PAUSE'
  print(f"{WHITE}{prev}")
  print(f"{GREEN}{NEXT:^20}")
  print(f"{PINK} {pause:^40}")
  print()

def playerstation():
  Head = 'WELCOME TO'
  title1 = 'ARMBOOK'
  line1 = 'Definetly not a rip off of'
  line2 = 'a certain other social'
  line3 = 'networking site'
  title2 = 'Homest'
  user = 'Username'
  pas = 'Password'
  print(f"{WHITE} {Head:^60}")
  print(f"{BLUE} {title1:^60}")
  print()
  print(f"{YELLOW} {line1:>60}")
  print(f"{YELLOW} {line2:>60}")
  print(f"{YELLOW} {line3:>60}")
  print()
  print(f"{RED} {title2:^60}")
  print()
  print(f"{WHITE} {user:^60}")
  print(f"{WHITE} {pas:^60}")
  
musicPlayer()
playerstation()
