PARKING_SIZE_S = 0
PARKING_SIZE_M = 1
PARKING_SIZE_L = 2
parking_size = ['S', 'M', 'L']

class ParkingLot:
    def __init__(self):
        self.spots = []
        self.n_spots =0

    def add_parking_spots(self, floor, size, num):
        for i in range(num):
            self.spots.append(ParkingSpot(id=self.n_spots, size=size, floor=floor))
            self.n_spots += 1

    def get_empty_spot_id(self, vehicle_size):
        for size in range(vehicle_size, len(parking_size)):
            #print('#',size, vehicle_size, len(parking_size))
            for spot in self.spots:
                if spot.size == size and spot.is_empty():
                    return spot.id
        return None

    def park_at_spot(self, id):
        self.spots[id].set_full()

    def empty_spot(self, id):
        self.spots[id].set_empty()

class ParkingSpot:
    def __init__(self, id=None, size=None, floor=None):
        self.id = id
        self.size = size
        self.floor = floor
        self.state = 0
        # 0: empty, 1: full, 2: out of service

    def print(self):
        print("id:", self.id, ",size:", parking_size[self.size], ",floor:", self.floor, ",is_empty:", self.is_empty())

    def is_empty(self):
        if self.state == 0:
            return True
        else:
            return False

    def set_empty(self):
        self.state = 0

    def set_full(self):
        self.state = 1

if __name__=='__main__':
    # test
    parking_lot = ParkingLot()
    parking_lot.add_parking_spots(1, PARKING_SIZE_S, 1)
    parking_lot.add_parking_spots(1, PARKING_SIZE_M, 2)
    parking_lot.add_parking_spots(1, PARKING_SIZE_L, 1)
    parking_lot.add_parking_spots(2, PARKING_SIZE_S, 1)
    parking_lot.add_parking_spots(2, PARKING_SIZE_M, 1)
    parking_lot.add_parking_spots(3, PARKING_SIZE_M, 3)
    for spot in parking_lot.spots:
        spot.print()
    print()

    import random
    for i in range(10):
        size = random.randrange(len(parking_size))
        print("{}-size vehicle =>".format(parking_size[size]), end=' ')

        id = parking_lot.get_empty_spot_id(size)
        if id != None:
            print("slot #{:d} at {:d}F".format(id, parking_lot.spots[id].floor))
            parking_lot.park_at_spot(id)
        else:
            print("Parking lot is full")
