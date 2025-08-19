def flight(height): 
    result = 0
    
    if height <= 0: 
        print("Invalid")
        return result
    
    elif height % 2 == 0: 
        result = (height // 2)
        return result
        
    elif height % 2 != 0: 
        result = (height * 3) + 1
        return result
    
flight(15)