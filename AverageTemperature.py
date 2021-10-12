'''
Program to calculate average temperatures, and returns out number of days above average temperature
'''

class AvgTemp:
    avg = 0
    def __init__(self,days,lisvalues):
        self.days = days
        self.lisvalues = lisvalues
        
    def calc_temp(self):
        self.avg = sum(self.lisvalues)/self.days
        return self.avg
    
    def days_above(self):
        count = 0
        for val in self.lisvalues:
            if val > self.avg :
                count += 1
        return count

ll = []
while True:
    days = input("Enter the number of days!: ")
    if days.isdigit() == False:
        print('Please enter a valid input!')
        continue
    break

count = 1

while count <= int(days):
    inp = input(f'Enter the temperature of day{count}: ')
    if inp.isdigit() == False:
        print('Please enter a valid input!')
        continue
    ll.append(int(inp))
    count +=1

o = AvgTemp(int(days),ll)

print(f'Average temperature is: {o.calc_temp()}')

print(f'{o.days_above()} day/s above average')