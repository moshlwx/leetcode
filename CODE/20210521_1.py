'''
租房信息查询系统
系统设计
'''


class RentingSystem:

    def __init__(self):
        # {id: [room_attr1, roomattr2]}
        self.rooms_dict = {}

    def add_room(self, id: int, area: int, price: int, rooms: int, address) -> bool:
        res = self.rooms_dict.get(id)
        self.rooms_dict[id] = [area, price, rooms, address.copy()]

        return True if not res else False

    def delete_room(self, id: int) -> bool:
        if self.rooms_dict.get(id):
            del(self.rooms_dict[id])
            return True
        else:
            return False

    def query_room(self, area: int, price: int, rooms: int, address, order_by):
        res = []

        for id in self.rooms_dict.keys():
            attr = self.rooms_dict[id]
            area_i = attr[0]
            price_i = attr[1]
            rooms_id = attr[2]
            dist_i = abs(attr[3][0]-address[0]) + \
                abs(attr[3][1]-address[1])

            if area_i >= area and price_i <= price and rooms_id == rooms:
                res.append((id, area_i, price_i, dist_i))
        if not order_by:
            order_by = [[0, 1]]

        res_sorted = sorted(res,
                            key=lambda x:
                            [order_attr[1] * x[order_attr[0]]
                             for order_attr in order_by])

        return [i[0] for i in res_sorted]
