# class ShoppingCart:
#     def __init__(self):
#         self.items = []

#     def add_item(self, item_name, qty, price=None):
#         if price is None:
#             for item in self.items:
#                 if item[0] == item_name:
#                     item[1] += qty
#                     return
#             self.items.append((item_name, qty))
#         else:
#             self.items.append((item_name, qty, price))

#     def current_items(self):
#         result = {}
#         for item in self.items:
#             if item[0] in result:
#                 result[item[0]] += item[1]
#             else:
#                 result[item[0]] = item[1]
#         return result

#     def calculate_total(self):
#         total = 0
#         for item in self.items:
#             if len(item) == 3:
#                 total += item[1] * item[2]
#             else:
#                 total += item[1]
#         return total

#     def remove_item(self, item_name):
#         for i in range(len(self.items)):
#             if self.items[i][0] == item_name:
#                 del self.items[i]
#                 break

# cart = ShoppingCart()
# cart.add_item(item_name="პური", qty=2)
# cart.add_item(item_name="კარაქი", qty=1)
# cart.add_item(item_name="წყალი", qty=6)
# cart.add_item(item_name="ზეთი", qty=2)

# print( "ამჟამად კალათშია:", cart.current_items())
# print("პროდუქტების რაოდენობა შეადგენს:",cart.calculate_total())

# cart.remove_item("ზეთი")

# print("განახლების შედეგად კალათშია: ",cart.current_items())
# print("პროდუქტების რაოდენობა შეადგენს: ",cart.calculate_total())