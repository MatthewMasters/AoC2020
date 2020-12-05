

def read_list(filename):
    return open(filename).read().strip().split('\n')


def get_seat_id(boarding_pass):
    row = int(boarding_pass[:-3].replace('F', '0').replace('B', '1'), 2)
    col = int(boarding_pass[-3:].replace('L', '0').replace('R', '1'), 2)
    return row * 8 + col

boarding_passes = read_list('input.txt')
seat_ids = sorted([get_seat_id(boarding_pass) for boarding_pass in boarding_passes])
first_id = seat_ids[0]

for a, b in enumerate(seat_ids):
    if a + first_id != b:
        print(b-1)
        break