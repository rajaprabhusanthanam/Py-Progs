
'''
Chicken Fiesta Pizza

Chicken Pepperoni Piza

Indi Chicken Pizza

Pepper Barbeque Pizza

Cheese n Corn Pizza

Veggie Paradise Pizza



#Pizza Ordering Management System

print("\t \t Pizza Ordering Management System")
print()

print("Welcome to SLA Pizza! A delight to your Tongues!")

print("Place your Order.")
print()

class PizzaOrder:
    def __init__(self):
        self.p1 = 0
        self.p2 = 0
        self.p3 = 0
        self.p4 = 0
        self.p5 = 0
        self.p6 = 0
    def CF(self, size, addons1, addons2):
        p1 = 20
        if size == "s":
            p1 += 0
        elif size == "m":
            p1 += 10
        elif size == "l":
            p1 += 20

        if addons1 == "y":
                p1 += 5
        if addons2 == "y":
            p1 += 5
        self.p1 = p1
        return p1
    def CP(self, size, addons1, addons2):
        p2 = 25
        if size == "s":
            p2 += 0
        elif size == "m":
            p2 += 10
        elif size == "l":
            p2 += 20

        if addons1 == "y":
            p2 += 5
        if addons2 == "y":
            p2 += 5
        self.p2 = p2
        return p2
    def IC(self, size, addons1, addons2):
        p3 = 30
        if size == "s":
            p3 += 0
        elif size == "m":
            p3 += 10
        elif size == "l":
            p3 += 20

        if addons1 == "y":
            p3 += 5
        if addons2 == "y":
            p3 += 5
        self.p3 = p3
        return p3
    def PB(self, size, addons1, addons2):
        p4 = 40
        if size == "s":
            p4 += 0
        elif size == "m":
            p4 += 10
        elif size == "l":
            p4 += 20

        if addons1 == "y":
            p4 += 5
        if addons2 == "y":
            p4 += 5
        self.p4 = p4
        return p4
    def CC(self, size, addons1, addons2):
        p5 = 20
        if size == "s":
            p5 += 0
        elif size == "m":
            p5 += 10
        elif size == "l":
            p5 += 20

        if addons1 == "y":
            p5 += 5
        if addons2 == "y":
            p5 += 5
        self.p5 = p5
        return p5
    def VP(self, size, addons1, addons2):
        p6 = 15
        if size == "s":
            p6 += 0
        elif size == "m":
            p6 += 10
        elif size == "l":
            p6 += 20

        if addons1 == "y":
            p6 += 5
        if addons2 == "y":
            p6 += 5
        self.p6 = p6
        return p6
    

po = PizzaOrder()

print("1. Chicken Fiezta - $20 \n2. Chicken Pepperoni Piza - $25 \n3. Indi Chicken Pizza - $30 \n4. Pepper Barbeque Pizza - $40 \n5. Cheese n Corn Pizza - $20 \n6. Veggie Paradise Pizza - $15")
print()
choice = int(input("Enter a Choice (1-6): "))
print()

print("small: + $0 \nmedium : + $10 \nlarge: + $20")
size = input("Enter a size? s, m, l: ")
print()
print("Addon Pepperoni: $5 extra")
addons1 = input("add Cheese? y or n: ")
print()
print("Addon Pepperoni: $5 extra")
addons2 = input("add Pepperoni? y or n: ")
print()

if choice == 1:
    cfp = po.CF(size, addons1, addons2)
    print("The Pizza you have ordered is Chicken Fiesta Pizza")
    print("Total price for the Pizza is: $",cfp)

if choice == 2:
    cpp = po.CP(size, addons1, addons2)
    print("The Pizza you have ordered is Chicken Pepperoni Pizza")
    print("Total price for the Pizza is: $",cpp)

if choice == 3:
    icp = po.IC(size, addons1, addons2)
    print("The Pizza you have ordered is Indi Chicken Pizza")
    print("Total price for the Pizza is: $",icp)

if choice == 4:
    pbp = po.PB(size, addons1, addons2)
    print("The Pizza you have ordered is Pepper Barbeque Pizza")
    print("Total price for the Pizza is: $",pbp)

if choice == 5:
    ccp = po.CC(size, addons1, addons2)
    print("The Pizza you have ordered is Cheese n Corn Pizza")
    print("Total price for the Pizza is: $",ccp)

if choice == 6:
    vpp = po.VP(size, addons1, addons2)
    print("The Pizza you have ordered is veggie Paradise Pizza")
    print("Total price for the Pizza is: $",vpp)


'''


class PizzaOrder:

    def __init__(self):
        self.p1 = 0
        self.p2 = 0
        self.p3 = 0
        self.p4 = 0
        self.p5 = 0
        self.p6 = 0
    def CF(self, size, addons1, addons2):
        p1 = 20
        if size == "s":
            p1 += 0
        elif size == "m":
            p1 += 10
        elif size == "l":
            p1 += 20

        if addons1 == "y":
                p1 += 5
        if addons2 == "y":
            p1 += 5
        self.p1 = p1
        return p1
    def CP(self, size, addons1, addons2):
        p2 = 25
        if size == "s":
            p2 += 0
        elif size == "m":
            p2 += 10
        elif size == "l":
            p2 += 20

        if addons1 == "y":
            p2 += 5
        if addons2 == "y":
            p2 += 5
        self.p2 = p2
        return p2
    def IC(self, size, addons1, addons2):
        p3 = 30
        if size == "s":
            p3 += 0
        elif size == "m":
            p3 += 10
        elif size == "l":
            p3 += 20

        if addons1 == "y":
            p3 += 5
        if addons2 == "y":
            p3 += 5
        self.p3 = p3
        return p3
    def PB(self, size, addons1, addons2):
        p4 = 40
        if size == "s":
            p4 += 0
        elif size == "m":
            p4 += 10
        elif size == "l":
            p4 += 20

        if addons1 == "y":
            p4 += 5
        if addons2 == "y":
            p4 += 5
        self.p4 = p4
        return p4
    def CC(self, size, addons1, addons2):
        p5 = 20
        if size == "s":
            p5 += 0
        elif size == "m":
            p5 += 10
        elif size == "l":
            p5 += 20

        if addons1 == "y":
            p5 += 5
        if addons2 == "y":
            p5 += 5
        self.p5 = p5
        return p5
    def VP(self, size, addons1, addons2):
        p6 = 15
        if size == "s":
            p6 += 0
        elif size == "m":
            p6 += 10
        elif size == "l":
            p6 += 20

        if addons1 == "y":
            p6 += 5
        if addons2 == "y":
            p6 += 5
        self.p6 = p6
        return p6
    
def display_menu():
    print("Menu:")
    print("1. Chicken Fiesta Pizza - $20")
    print("2. Chicken Pepperoni Pizza - $25")
    print("3. Indi Chicken Pizza - $30")
    print("4. Pepper Barbeque Pizza - $40")
    print("5. Cheese n Corn Pizza - $20")
    print("6. Veggie Paradise Pizza - $15")

def main():
    print("\t \t Pizza Ordering Management System")
    print()
    print("Welcome to SLA Pizza! A Delight to Your Tongues!")
    print("Place your Order.")
    print()

    po = PizzaOrder()
    total_cost = 0

    while True:
        display_menu()
        choice = int(input("Enter a Choice (1-6): "))

        if choice < 1 or choice > 6:
            print("Invalid choice. Please choose a valid option.")
            continue

        size = input("Enter a size? s, m, l: ")
        addons1 = input("Add Cheese? y or n: ")
        addons2 = input("Add Pepperoni? y or n: ")

        if choice == 1:
            total_cost += po.CF(size, addons1, addons2)
            pizza_name = "Chicken Fiesta Pizza"
        elif choice == 2:
            total_cost += po.CP(size, addons1, addons2)
            pizza_name = "Chicken Pepperoni Pizza"
        elif choice == 3:
            total_cost += po.IC(size, addons1, addons2)
            pizza_name = "Indi Chicken Pizza"
        elif choice == 4:
            total_cost += po.PB(size, addons1, addons2)
            pizza_name = "Pepper Barbeque Pizza"
        elif choice == 5:
            total_cost += po.CC(size, addons1, addons2)
            pizza_name = "Cheeze n Corn Pizza"
        else:
            total_cost += po.VP(size, addons1, addons2)
            pizza_name = "Veggie Paradise Pizza"
        
        
        print(f"The Pizza you have ordered is {pizza_name}")
        print(f"Total price for the Pizza is: ${total_cost:.2f}")

        another_order = input("Do you want to order another pizza? (y/n): ")
        if another_order.lower() != 'y':
            break

    print(f"Your total order cost is: ${total_cost:.2f}")
    print("Thank you for ordering from SLA Pizza!")

if __name__ == "__main__":
    main()
