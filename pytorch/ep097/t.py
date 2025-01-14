import sys

def average(numbers):
    return sum(numbers) / len(numbers)
    
def real_main():
    print('enter some number, type "done" when done')
    numbers = []
    for line in sys.stdin:
        line = line.strip()
        if line == 'done':
            break
        else:
            numbers.append(line)
    # if not numbers:
    #    print('no numbers were entered')
    # else:            
    print(f'the average is {average(numbers)}')
    return 0

def main():
    try:
        return real_main()
    except Exception as e:
        print(f'unexpected error occurred: {type(e).__name__}:{e}')
        return 1
        
        
if __name__ == '__main__':
    exit(real_main())