

def read_list(filename):
    return open(filename).read().strip().split('\n')


def get_seat_id(boarding_pass):
    row = int(boarding_pass[:-3].replace('F', '0').replace('B', '1'), 2)
    col = int(boarding_pass[-3:].replace('L', '0').replace('R', '1'), 2)
    return row * 8 + col


boarding_passes = read_list('input.txt')
seat_ids = [get_seat_id(boarding_pass) for boarding_pass in boarding_passes]
print(max(seat_ids))