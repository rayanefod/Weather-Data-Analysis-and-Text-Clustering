#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import libraries
import sys


# In[4]:


def main():
    mapper = Mapper()
    mapper.map_input(sys.stdin)

class Mapper():
    
    def map_input(self, input_stream) -> list:
       
        output = []

        for item in input_stream:
            mapped_item = self.map(item)
            if mapped_item:
                print(mapped_item)

        return output

    def map(self, item:str) -> str:
        
        # Disregard the file headers
        if item.startswith('Wban Number'):
            return None

        # Disregard the empty lines
        if item == '\n':
            return None

        # Tokenize the input line
        tokens = item.split(',')

        # Get the day's value
        day_value = tokens[1].strip()

        # Get the temperature
        temperature_value = tokens[8].strip()
        
        # Do not process empty temperature values
        if temperature_value == '-':
            return None
        elif temperature_value == '':
            return None
        else:
            temperature_value = int(temperature_value)

        # Return the key and value as a comma seperated string
        return '%s,%s' % (day_value, temperature_value)


# In[3]:


if __name__=="__main__":
    main()

