#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Import libraries 
import sys


# In[6]:


def main():
    reducer = Reducer()
    reducer.reduce_input(sys.stdin, population=True)

class ReducerValues():
    
    def __init__(self, day:str) -> None:
        self.values = []
        self.day = day
        self.max = None
        self.min = None
        self.sum = 0
        self.squared_sum = 0
        self.n = 0

    def add_value(self, value:int) -> None:
        
        # add the value to the collection
        self.values.append(value)

        # update the max and min values
        if self.max is None:
            # initialize the max and min values
            self.max = value
            self.min = value
        else:
            if value > self.max: self.max = value
            if value < self.min: self.min = value

        # update the "running" values
        self.n += 1
        self.sum += value
        self.squared_sum += value * value

    def get_median(self) -> float:
        
        self.values.sort()
        middle = int(self.n / 2)

        if self.n % 2 == 0:
            return (self.values[middle - 1] + self.values[middle]) / 2.0
        else:
            return self.values[middle]

    def get_variance(self, population:bool=True) -> float:
        
        mean = self.sum / float(self.n)

        #    Sample variation (population=True).
        if population:
            return  1.0 / self.n * (self.squared_sum - self.n * mean*mean)
        else:
            return  1.0 / (self.n - 1) * (self.squared_sum - self.n * mean*mean)
        

    def print_output(self, population:bool=True) -> None:
        
        # calculate the mean
        mean = self.sum / float(self.n)

        # print the output
        print('%s,"%d,%d,%.6f,%.1f,%.6f"' % (
            self.day, 
            self.max, 
            self.min,
            mean,
            self.get_median(),
            self.get_variance(population)))


# In[7]:


class Reducer():
   
    def reduce_input(self, input_stream, population:bool=True) -> None:
        
        current_day = ReducerValues(None)

        for item in input_stream:
            if item:
                # get the day and temperature value
                day_value, temperature_value = item.split(',')
                temperature_value = int(temperature_value)

                if current_day.day == day_value:
                    current_day.add_value(temperature_value)
                else:
                    # if the current day exists, show the output
                    if current_day.day:
                        current_day.print_output(population)

                    # the current day has changed, create the new day
                    current_day = ReducerValues(day_value)
                    current_day.add_value(temperature_value)

        # print the last day processed
        if current_day.day == day_value:
            current_day.print_output(population)


# In[8]:


if __name__=="__main__":
    main()


# In[ ]:




