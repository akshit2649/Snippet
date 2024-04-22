import concurrent.futures



def do_something(seconds):
    print(f'Sleeping {seconds} seconds(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'

with concurrent.futures.ThreadPoolExecutor() as executor:
    f1 = executor.submit(do_something, 1)
    f2 = executor.submit(do_something, 1)
    print(f1.result())
    print(f2.result())


    secs = [5,4,3,2,1]
    results = [ executor.submit(do_something, sec) for sec in secs ]

    for f in concurrent.futures.as_completed(results):
        print(f.result())

    results = executor.map(do_something, 1)

    for result in results:
        print(result)
