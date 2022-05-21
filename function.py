

def sum_and_multiple(*args,**kwargs):
    multiple=1
    for num in args:
        multiple*=num
        print(multiple)
    print(f"Hello {kwargs}")
        