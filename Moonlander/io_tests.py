import moonlander


def main():
   moonlander.showWelcome()
   moonlander.getFuel()
   moonlander.getAltitude()
   moonlander.displayLMState(12, 1034.278, -54.3333, 486, 7)
   
   # call twice to test with requesting too much fuel
   rate = moonlander.getFuelRate(45)
   print "rate:", rate
   rate = moonlander.getFuelRate(4)
   print "rate:", rate
   
   # call three times to display each possible comment
   moonlander.displayLMLandingStatus(-.2)
   moonlander.displayLMLandingStatus(-9)
   moonlander.displayLMLandingStatus(-19)


if __name__ == "__main__":
   main()
