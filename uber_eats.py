import csv
import datetime
import matplotlib.pyplot as plt
from datetime import datetime
from dateutil import parser

class UberEatsData:
    '''
    
    '''

    def __init__(self):
          
          self.eater_data = {'Order Price': [], 'Item Name': [], 'Order Time': []}
          self.day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
          pass
    
    
    def get_csv_columns(self, file_name : str):
        with open(file_name) as csv_file:
        
            # creating an object of csv reader
            # with the delimiter as ,
            csv_reader = csv.reader(csv_file, delimiter = ',')
        
            # list to store the names of columns
            list_of_column_names = []
        
            # loop to iterate through the rows of csv
            for row in csv_reader:
        
                # adding the first row
                list_of_column_names.append(row)
        
                # breaking the loop after the
                # first iteration itself
                break
        
        # printing the result
        print("List of column names : ",
            list_of_column_names[0])
        
        return list_of_column_names[0]
    def open_file(self, file_path : str):
        '''
        
        '''
        with open(file_path) as csvfile:
            reader = csv.DictReader(csvfile)
            # eater_data = {'Order Price': [], 'Item Name': [], 'Order Time': []}
            for row in reader:
                #if row['Order Time'] != '?':
                    self.eater_data['Order Price'].append(float(row['Order Price']))
                    self.eater_data['Item Name'].append(row['Item Name'])
                    self.eater_data['Order Time'].append((row['Order Time']))
        return self.eater_data
    
    def extract_list_from_data(self, eater_data,  list_element : str):
        '''
        
        '''
        return eater_data[list_element]
    
    def unique_days(self, list_of_days : list):
        '''
         
        '''
        return list(set(list_of_days))
    
    
    def simplify_datetime(self, order_time : str , date_object_type : str):
        '''
        
        '''
        #order timne to date time
        date_obj = parser.parse(order_time[:-10])
        # "%A"
        return(date_obj.strftime(date_object_type))
    
    def simplify_date_list(self, list_of_dates : list, date_object_type : str):
        '''
        
        '''
        list_of_days = []
        for date in list_of_dates: 
            simplified_date = self.simplify_datetime(date, date_object_type)    
            list_of_days.append(simplified_date)
        
        return list_of_days 
    
    def sort_days(self, unique_list_of_days : list):
        '''
        
        '''
        sorted_days = sorted(unique_list_of_days, key=lambda x: self.day_order.index(x))

        return sorted_days 
    
    def create_count_of_days(self, weekday_list : list, sorted_days_list : list):
        '''
        
        '''
        count_of_days = []

        for day in sorted_days_list:
            numerical_day = weekday_list.count(day)
            count_of_days.append(numerical_day)

        print(count_of_days)
        return count_of_days 
    
    def plot_bar_graph(self, sorted_days_list : list, count_of_days_list : list):
        '''
        
        '''
        return plt.bar(x=sorted_days_list, height=count_of_days_list)


if __name__ == "__main__":
    data = UberEatsData() 




