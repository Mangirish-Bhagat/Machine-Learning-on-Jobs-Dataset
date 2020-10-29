version = '0.0.180'
chrome_version = '81'

project_directory = './'

os = 'linux'

chrome_driver_location = project_directory + 'chromedriver/'+ chrome_version +'/chromedriver'

if os == 'windows':
    chrome_driver_location += '.exe'
elif os == 'linux':
    chrome_driver_location += ''

webscrapping_directory =  project_directory + 'webscrapping/'
machine_learning_directory = project_directory + 'ml/'
download_directory = project_directory + 'data/'

non_preprocessed_dataset = project_directory + 'indeed_results.xlsx'
preprocessed_dataset = project_directory + 'indeed_results_pp_2020-04-27.xlsx'

# for writing on the mongodb
ip_address = '127.0.0.1'
port_no = 27017
db_name = 'jobDB'
col_name = 'webscrappingdata'
spark_mongo_server_connection_string = 'mongodb://' + ip_address + ':' + str(port_no) + '/' + db_name + '.' + col_name
spark_mongo_server_connection_string = 'mongodb://' + ip_address + '/' + db_name + '.' + col_name

PreProcessing_Done = True
Machine_Learning_Done = True
GUI_Done = False

Libraries_Required = [
    'threaded',
    'selenium',
    'scikit-learn',
    'mlxtend',
    'dash',
    'plotly',
    'pyspark'
]