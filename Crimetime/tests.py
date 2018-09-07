class Crime:
    def __init__(self, ID, category, day_of_week, month, hour): 
        self.id = int(ID)                                                            
        self.category = category                                                
        self.day_of_week = day_of_week                                          
        self.month = month                                                      
        self.hour = hour                                                        
                           
    def __repr__(self):
        fmt_str = "{0:9d} {1:7} {2:9} {3:9} {4:4}\n"  
        return fmt_str.format(self.id, self.category, self.day_of_week,\
               self.month, self.hour)

    def __eq__(self, other):
        return self.id == other.id

    def __ne__(self, other):
        return not self == other


crime1 = Crime(420955555, 'Robbery','','','')
#print crime1
crime1.day_of_week = 'Wednesday'
crime1.month = 'February'
crime1.hour = '12PM'
#print crime1


#Tests from crimetime.py

import crimetime
crime_lines1 = '100\tROBBERY\tSTOLEMAHWALLET', '750\tDRUGS\tDEALINCRACK', \
               '500\tASSAULT\tSTABBEDSOMEONE', '10\tROBBERY\tTOOKSTUFF', ''

crime_lines2 = '100\tROBBERY\tSTOLEMAHWALLET', '750\tDRUGS\tDEALINCRACK', \
               '500\tASSAULT\tSTABBEDSOMEONE', '' 

crime_lines3 = '750\tDRUGS\tDEALINCRACK', \
               '500\tASSAULT\tSTABBEDSOMEONE', '' #filters out '' at end

#create_entries test
crime_list1 = crimetime.create_entries(crime_lines1)
crime_list2 = crimetime.create_entries(crime_lines2)
crime_list3 = crimetime.create_entries(crime_lines3)

assert len(crime_list1) == 2 
assert len(crime_list2) == 1
assert len(crime_list3) == 0

#sort_entries test

entries_1 = [Crime(55,'','','',''), Crime(11,'','','',''),\
            Crime(21,'','','',''),Crime(50,'','','',''),\
            Crime(17,'','','','')]
#print entries_1
entries_2 = [Crime(5,'','','',''), Crime(111,'','','',''),\
            Crime(29,'','','',''),Crime(52,'','','',''),\
            Crime(73,'','','','')]
#print entries_2
entries_3 = [Crime(1,'','','',''), Crime(2,'','','',''),\
            Crime(3,'','','',''),Crime(5,'','','',''),\
            Crime(4,'','','','')]
#print entries_3

assert crimetime.sort_entries(entries_1) == [Crime(11,'','','',''),\
                                            Crime(17,'','','',''),\
                                            Crime(21,'','','',''),\
                                            Crime(50,'','','',''),\
                                            Crime(55,'','','','')]

assert crimetime.sort_entries(entries_2) == [Crime(5,'','','',''),\
                                            Crime(29,'','','',''),\
                                            Crime(52,'','','',''),\
                                            Crime(73,'','','',''),\
                                            Crime(111,'','','','')]

assert crimetime.sort_entries(entries_3) == [Crime(1,'','','',''),\
                                            Crime(2,'','','',''),\
                                            Crime(3,'','','',''),\
                                            Crime(4,'','','',''),\
                                            Crime(5,'','','','')]


#update_entries test
time_list1 = ['10\tMonday\t01/10/2015\t05:40']
assert 'Monday' in str(crimetime.update_entries(crime_list1,time_list1)[1])                       
assert 'January' in str(crimetime.update_entries(crime_list1,time_list1)[1]) 
assert '5AM' in str(crimetime.update_entries(crime_list1,time_list1)[1]) 

