import cold_start_soln
import collab_filter2

import array
num = input("enter the value 0 for NEW USER \n1 for NOT a new user.....\n then enter the service name")

def main():
  if num == '0':
    cold_start_soln.main()
  elif num == '1':
      collab_filter2.main()



if __name__ == "__main__" :
    main()
