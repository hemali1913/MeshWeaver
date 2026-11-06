import cloudpickle
import cloudpickle

def serialize_task(func, args=None, kwargs=None):
    """
    Python function aur uske arguments/parameters ko cloudpickle 
    ka use karke byte format (binary) me pack (serialize) karta hai.
    """
    if args is None:
        args = ()
    if kwargs is None:
        kwargs = {}
    
    # Function aur arguments ko ek dictionary me pack karte hain
    task_payload = {
        'func': func,
        'args': args,
        'kwargs': kwargs
    }
    
    # cloudpickle.dumps() ka use karke binary bytes me convert karte hain
    return cloudpickle.dumps(task_payload)

if __name__ == "__main__":
    # Ek chota sa test function (Day 2 check ke liye)
    def sample_func(a, b):
        return a + b
    
    serialized_data = serialize_task(sample_func, args=(5, 10))
    print("Serialization Successful! Byte length:", len(serialized_data))