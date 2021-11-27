from typing import List


def writeFlightTime(flightList: List):
  with open("flightTime.txt", "w") as f:
      for flight in flightList:
          f.write(flight.time + "\n")

def writeFlightHour(flightList: List):
    with open("flightTime-hour.txt", "w") as f:
        for flight in flightList:
            formattedDate = flight.date.strftime("%H:%M:%S")
            f.write(formattedDate + "\n")

def writeFlightTotal(flightList: List):
    with open("flightTime-total.txt", "w") as f:
        for flight in flightList:
            together = flight.time + " " + str(flight.date)
            print(together)
            f.write(together + "\n")