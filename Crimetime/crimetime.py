# Name: Spencer Lawry     
# Course: CPE 101  
# Instructor: Daniel Kauffman
# Assignment: Crimetime 
# Term: Fall 2016        

def main():
   
    time_lines = read_file('times-all.tsv')
    #print time_lines
    crime_lines = read_file('crimes-all.tsv')
    #print crime_lines 
    crime_list = create_entries(crime_lines)
    #print crime_list
    sorted_list = sort_entries(crime_list)
    #print sorted_list
    updated_list = update_entries(sorted_list, time_lines)
    #print updated_list
    write_file('my_robbery_file.tsv', updated_list)

    print_results(updated_list)
def read_file(path):
    f = open(path, 'r')
    line = f.readline()
    lines = []
    while not line == '' :
        line = f.readline().strip()
        lines.append(line)
    f.close()
    return lines

def create_entries(crime_lines):
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
       
    crime_list = []
    for i in range(len(crime_lines) - 1): 
        line_list = crime_lines[i].split()
        crime = Crime(line_list[0], line_list[1],'','','')
        if crime.category == 'ROBBERY' and crime not in crime_list:
            crime_list.append(crime)
    return crime_list
            
def sort_entries(entries): #insertion sort
    for i in range(1, len(entries)):
        pos = i
        current_entry = entries[i]
        while pos > 0 and entries[pos-1].id > current_entry.id:
            entries[pos] = entries[pos-1]
            pos -= 1
        entries[pos] = current_entry

    return entries    


def update_entries(sorted_list, time_lines):
    import calendar
    for i in range(len(sorted_list)):
        id_string = str(sorted_list[i].id)
        for j in range(len(time_lines)):
            time_list = time_lines[j].split()
            if id_string in time_list:
                sorted_list[i].day_of_week = time_list[1]
                sorted_list[i].month =\
                                 calendar.month_name[int(time_list[2][:2])]     
                if int(time_list[3][:2]) > 12:
                    sorted_list[i].hour =\
                                 '{0:d}PM'.format(int(time_list[3][:2]) - 12)
                    break
                elif int(time_list[3][:2]) == 0:
                    sorted_list[i].hour = '12AM'
                    break
                elif int(time_list[3][:2]) == 12:
                    sorted_list[i].hour = '12PM'
                    break
                else:
                    sorted_list[i].hour =\
                                 '{0:d}AM'.format(int(time_list[3][:2]))
                    break

    return sorted_list


def write_file(path, updated_list):
    f = open(path, 'w')
    for i in range(len(updated_list)):
        f.write(str(updated_list[i]))
    f.close()

def print_results(updated_list):
    num_rob = len(updated_list)
    print 'NUMBER OF PROCESSED ROBBERIES: {0}'.format(num_rob) 
    
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',\
           'Saturday']
    biggest = 0
    for i in range(len(days)):
        num = 0
        for j in range(len(updated_list)):
            if days[i] in str(updated_list[j]):
                num += 1
        if num>biggest:
            biggest = num
            most_day = days[i]
    print 'DAY WITH MOST ROBBERIES: {0}'.format(most_day) 
        
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',\
            'August', 'September', 'October', 'November', 'December']
 
    biggest = 0
    for i in range(len(months)):
        num = 0
        for j in range(len(updated_list)):
            if months[i] in str(updated_list[j]):
                num += 1
        if num>biggest:
            biggest = num
            most_month = months[i]
    print 'MONTH WITH MOST ROBBERIES: {0}'.format(most_month) 

    hours = ['12AM',' 1AM',' 2AM','3AM','4AM','5AM','6AM','7AM','8AM','9AM',\
            '10AM','11AM','12PM',' 1PM',' 2PM','3PM','4PM','5PM','6PM','7PM',\
            '8PM','9PM','10PM','11PM']

    biggest = 0
    for i in range(len(hours)):
        num = 0
        for j in range(len(updated_list)):
            if hours[i] in str(updated_list[j]):
                num += 1
        if num>biggest:
            biggest = num
            most_hour = hours[i]
    print 'HOUR WITH MOST ROBBERIES: {0}'.format(most_hour)


if __name__ == "__main__":
    main()
