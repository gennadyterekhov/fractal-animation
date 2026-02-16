
def make_n_iters(iters: int, iteration_func, entry_data):
    for i in range(iters):
        entry_data = iteration_func(entry_data)
