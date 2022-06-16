import xlsxwriter

class Excel():
    worksheet: object
    headers: list
    workbook: object
    
    def __init__(self, name: str = './database.xlsx') -> None:
        self.workbook = xlsxwriter.Workbook(f'{name}')
        self.worksheet = self.workbook.add_worksheet()
        data = {
            "name": "",
            "phone": "",
            "website": "",
            "email": "",
            "address": "",
            "thematic": "",
            'city': '',
            'state': '',
            'query': ''
        }
        self.headers = self.generate_headers(data)
        self.print_table_headers()
        
    def generate_headers(self, example_dict):
        '''
        Generates headeers from the data dictionary by capitalizing it's keys.

        Parameters:
                args (object): Object containging CLI arguments passed as they can affect which columns are needed
                example_dict (dict): Data dictionary with keys

        Returns:
                list (list): List of capitalized strings representing headers
        '''

        headers = example_dict.keys()
        
        return [header.capitalize() for header in headers]
    
    def print_table_headers(self):
        '''
        Writes headers to the worksheet.

        Parameters:
                worksheet (worksheet object): Worksheet where headsers should be written
                headers (list): List of headers to vrite
        '''
        col = 0
        for header in self.headers:
            self.worksheet.write(0, col, header)
            col += 1
            
    def write_data_row(self, data, row):
        '''
        Writes data dictionary to row.

        Parameters:
                worksheet (worksheet object): Worksheet where data should be written
                data (dict): Dictionary containing data to write
                row (int): No. of row to write to
        '''
        col = 0
        for key in data:
            self.worksheet.write(row, col, data[key])
            col += 1

    def close(self) -> bool:
        self.workbook.close()
        return True
    

def write_to_excel(database: list, name: str = './database.xlsx') -> int:
    e = Excel(name=name)
    i = 0
    for card in database:
        i += 1
        e.write_data_row(card, i)
    e.close()
    return i   