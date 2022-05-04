'''
4. write a class with method to take 2 possitional arguments, 2 key word arguments with 
	one having default value of 0, args, and kwargs and print the arguments and keyword 
	arguments passed on different conditions

    ex: 	Considering as object created with the class written                obj = <class>
			obj.print_func(1,2,a=4,b=5,"a", "c", 45, m="d", l=5)        
            output = parameters received are 1, 2
					 positional args are 4, 5
					 args are ["a", "c" 45]
			    	 kwargs are {m: "d", l=5}
			
            obj.print_func(1,2,a=4,b=5,"a", "c", 45, m="d", l=5)
			obj.print_func(1,2,a=4,"a", 45, m="d", l=5)
				
'''
class class1:

    def print(self, param1, param2, pos_arg_a, pos_arg_b, arg1, arg2, arg3, kwarg_m, kwarg_l):
        print("parameters received are", param1, param2,
        "positional args are", pos_arg_a, pos_arg_b,
        "args are", [arg1, arg2, arg3]
        "kwargs are", {}        )

        pass