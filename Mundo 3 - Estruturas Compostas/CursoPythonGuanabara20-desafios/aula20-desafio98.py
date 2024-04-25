from time import sleep

print("PROGRAM STARTED.")
print("=" * 50)

def counter(start, end, step):
    if step < 0:
        step *= -1
    if step == 0:
        step = 1

    print("=" * 50)
    print(f'Counting from {start} to {end} in {step} steps')
    sleep(1.5)

    if start < end:
        count = start
        while count <= end:
            print(f'{count} ', end='', flush=True)
            sleep(0.5)
            count+= step
        print('COUNTING ENDED')
    else:
        count = start
        while count >= end:
            print(f'{count} ', end='', flush=True)
            sleep(0.5)
            count-= step
        print('COUNTING ENDED')

counter(1, 10, 1)
counter(10, 0, 2)

print('=' * 30)
print("Your turn")
stt = int(input("Start value: "))
end = int(input("End value: "))
stp = int(input("Step value: "))

counter(stt, end, stp)

print("=" * 50)
print("PROGRAM ENDED.")
