import time
def program(target):
    
    letters = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP 
    QRSTUVWXYZ 1234567890, .-;:_!"#%&/()=?@${[]}'''
    string = ""
    count = 0
    for t in target:
        for letter in letters:
            if letter == t:
                string += letter
                break

    print(string)
if __name__ == '__main__': 
    sentences = ["Hello there!", "My name is Prayuj", "I am in BE COMPS"]
    for sentence in sentences:
        start_time = time.time()
        program(sentence)
        print("Time Taken = ",time.time() - start_time)