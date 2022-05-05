'''
4. write a class with method to take 2 possitional arguments, 2 key word arguments with 
	one having default value of 0, args, and kwargs and print the arguments and keyword 
	arguments passed on different conditions

    ex: 	Considering as object created with the class written                
            obj = <class>
			obj.print_func(1,2,a=4,b=5,"a", "c", 45, m="d", l=5)        

            output = parameters received are 1, 2
					 positional args are 4, 5
					 args are ["a", "c" 45]
			    	 kwargs are {m: "d", l=5}
			
            obj.print_func(1,2,a=4,b=5,"a", "c", 45, m="d", l=5)
			obj.print_func(1,2,a=4,"a", 45, m="d", l=5)
				
'''
class obj:

    def __init__(self, parameter1, parameter2, positional_argument_a, positional_argument_b, *args, **kwargs):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.positional_argument_a = positional_argument_a
        self.positional_argument_b = positional_argument_b
        self.args = args
        self.kwargs = kwargs


    def print_func(self):
        print("parameters received are", self.parameter1,",", self.parameter2)
        print("positional args are", self.positional_argument_a,",",self.positional_argument_b)
        print("args are", self.args)
        print("kwargs are", self.kwargs)
        
        

a = obj(1,2,a=4,b=5,"a","c",45, m = "d", l = 5)
a = obj(1,2,"a","c",45, a=4,b=5,m = "d", l = 5)

#a=4,b=5,"a", "c", 45, m="d", l=5)
a.print_func()
        