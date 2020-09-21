import os.path

directory = 'C:\\tmp\\'  #Specify the folder to save the file in
filename = 'decorator_logs.txt' 
file_path = os.path.join(directory, filename)
if not os.path.isdir(directory): #This checks if the folder exists, if it does not then it will be created
    os.mkdir(directory)

#Decorator function programme that will take every function and write it to a file on a new line

def log_message(func):
        def write_to_file(*args, **kwargs):
           
            result = func(*args, **kwargs) #Fuction stored in avariable and will be returned later
            f =  open(file_path ,'a')
            f.write(result + "\n") #writes to file and a adds newline after the function is written to the file
            f.close()
            return result
        return write_to_file
        
     
#Using the decorator function
@log_message
def hello():
    return "Hello user " 

@log_message
def language(s):
    return "The programming language you are learning is {}\n".format(s)


@log_message
def job(string=""):
    return "Your current occupation is a " + string



#Example of function calls

hello()
job("Developer")
language('python')
