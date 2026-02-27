import time
import functools

def timer(func):
    """
    A Decorator that measures and prints the execution time of a function.
    
    This wraps the original function, records the start time, runs the function,
    records the end time, and prints the difference.
    
    Args:
        func (function): The function to be measured.
        
    Returns:
        function: The wrapper function that executes the original logic + timing.
    """
    @functools.wraps(func) # Preserves the original function's name and identity
    def wrapper(*args, **kwargs):
        # *args and **kwargs allow this decorator to accept ANY arguments
        # that the original function might need.
        
        start = time.time()       # Start the clock
        result = func(*args, **kwargs) # Run the actual function
        end = time.time()         # Stop the clock
        
        # Calculate duration
        duration = end - start
        print(f"--> [Timer] Function '{func.__name__}' finished in {duration:.4f} seconds.")
        
        return result # Return the original result so the program continues normally
    return wrapper