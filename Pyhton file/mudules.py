# Function	            वर्णन (Description)	उदाहरण
# os.getcwd()	        सध्याची Working Directory दाखवतो	print(os.getcwd())
# os.listdir(path)	    दिलेल्या path मधील सर्व फाइल्स/फोल्डर्सची यादी देतो	print(os.listdir("."))
# os.mkdir(name)	    नवीन Directory तयार करतो	os.mkdir("NewFolder")
# os.makedirs(path)	    Nested directories तयार करतो	os.makedirs("A/B/C")
# os.rmdir(name)	    रिकामी Directory delete करतो	os.rmdir("NewFolder")
# os.removedirs(path)	Nested directories delete करतो	os.removedirs("A/B/C")
# os.rename(old, new)	फाइल किंवा फोल्डर rename करतो	os.rename("old.txt", "new.txt")
# os.remove(file)	    फाइल delete करतो	os.remove("temp.txt")
# os.chdir(path)	    Working Directory बदलतो	os.chdir("/home/sachin/Documents")
# os.path.exists(path)	दिलेला path अस्तित्वात आहे का ते तपासतो	os.path.exists("data.txt")
# os.path.isfile(path)	path फाइल आहे का तपासतो	os.path.isfile("demo.txt")
# os.path.isdir(path)	path directory आहे का तपासतो	os.path.isdir("my_folder")
# os.environ	        Environment variables access करण्यासाठी	print(os.environ['HOME'])
# os.system(cmd)	    OS commands चालवण्यासाठी	os.system("ls") किंवा os.system("dir") 


## sys module 

# Function / Attribute	वर्णन (Description)	उदाहरण
# sys.version	सध्या वापरात असलेल्या Python ची version माहिती देते	print(sys.version)
# sys.platform	OS कोणता आहे ते सांगते (Windows, Linux, etc.)	print(sys.platform)
# sys.exit()	प्रोग्राम अचानक बंद करण्यासाठी	sys.exit()
# sys.path	Python interpreter कोणत्या path मध्ये modules शोधतो ते दाखवतो	print(sys.path)
# sys.argv	Command line arguments access करण्यासाठी	print(sys.argv)
# sys.maxsize	Python मधील integer ची maximum value दाखवतो	print(sys.maxsize)
# sys.stdin, sys.stdout, sys.stderr	Input, Output, आणि Error streams handle करण्यासाठी	sys.stdout.write("Hello\n")
# sys.getsizeof(obj)	कोणत्याही object चा memory size (bytes मध्ये) दाखवतो	print(sys.getsizeof(100))
# sys.modules	सध्या import झालेले सर्व modules दाखवतो	print(sys.modules.keys())


### stat module 
#statistics

# फंक्शन	वर्णन
# mean(data)	दिलेल्या डेटाची सरासरी काढते
# median(data)	मध्य मूल्य काढते
# mode(data)	सर्वाधिक वारंवार येणारे मूल्य देते
# stdev(data)	Standard deviation काढते
# variance(data)	Variance काढते


# Math Module
# गणितीय functions साठी.

# import math
# print(math.sqrt(16))   
# print(math.pi)         



#import string

# print(string.ascii_letters)   # सर्व लहान आणि मोठे अक्षरे (a-z, A-Z)
# print(string.ascii_lowercase) # लहान अक्षरे (a-z)
# print(string.ascii_uppercase) # मोठी अक्षरे (A-Z)
# print(string.digits)          # 0 ते 9 पर्यंतची अंक
# print(string.punctuation)     # सर्व punctuation चिन्हे



# import random

# print(random.random())       # 0 ते 1 दरम्यान random float
# print(random.randint(1, 10)) # 1 ते 10 दरम्यान random integer
# print(random.uniform(5, 15)) # 5 ते 15 दरम्यान random float
# print(random.choice([10, 20, 30, 40]))  # लिस्टमधून random element निवडतो
