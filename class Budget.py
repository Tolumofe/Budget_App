#Create a Budget class
class Budget:
    def __init__(self, name, amount):
        self.amount = amount
        self.name = name

#Deposit instance
    def deposit(self):
        deposit = int(input('how much to deposit? \n'))
        self.amount += deposit
        print('Deposit successful')
        print(f'The {self.name} balance is now {self.amount}')

#Withdrawal Instance
    def withdrawal(self):
        withdrawal = int(input('how much to withdraw? \n'))
        self.amount -= withdrawal
        print('Withdrawal successful')
        print(f'The {self.name} balance is now {self.amount}')

#Balance Checking instance
    def balance(self):
        # return self.amount
        print(f'The {self.name} balance is {self.amount}')

#Transfer out instance
    def transfer_out(self, category):
        amount_transfer = int(input('how much to transfer? \n'))
        self.amount -= amount_transfer
        category.amount += amount_transfer
        print(f'The {self.name} balance is now {self.amount}')
        print(f'The {category.name} balance is now {category.amount}')


#Database for Food, Clothing and Entertainment
food = Budget('Food', 1000)
clothing = Budget('Clothing', 3000)
entertainment = Budget('Entertainment', 5000)


def action_selection():
    print('Please select an action')
    print('1. Deposit')
    print('2. Withdrawal')
    print('3. Balance')
    print('4. Transfer \n')
    action = int(input())
    return action


def category_selection():
    print('Please select a category')
    print('1. Food')
    print('2. Clothing')
    print('3. Entertainment')
    answer = int(input())
    return answer


def food_selection():
    ans = int(action_selection())
    if ans == 1:
        food.deposit()
    elif ans == 2:
        food.withdrawal()
    elif ans == 3:
        food.balance()
    elif ans == 4:
        print('You have chosen to transfer from food account')
        print('1. Clothing')
        print('2. Entertainment')
        answer = int(input())
        if answer == 1:
            food.transfer_out(clothing)
        elif answer == 2:
            food.transfer_out(entertainment)
        else:
            print('Wrong Selection')
            food_selection()
    else:
        print('Wrong Selection')
        food_selection()


def clothing_selection():
    ans = int(action_selection())
    if ans == 1:
        clothing.deposit()
    elif ans == 2:
        clothing.withdrawal()
    elif ans == 3:
        clothing.balance()
    elif ans == 4:
        print('You have chosen to transfer from clothing account')
        print('1. Food')
        print('2. Entertainment')
        answer = int(input())
        if answer == 1:
            clothing.transfer_out(food)
        elif answer == 2:
            clothing.transfer_out(entertainment)
        else:
            print('Wrong Selection')
            clothing_selection()
    else:
        print('Wrong Selection')
        clothing_selection()


def entertainment_selection():
    ans = int(action_selection())
    if ans == 1:
        entertainment.deposit()
    elif ans == 2:
        entertainment.withdrawal()
    elif ans == 3:
        entertainment.balance()
    elif ans == 4:
        print('You have chosen to transfer from entertainment account')
        print('1. Food')
        print('2. Clothing')
        answer = int(input())
        if answer == 1:
            entertainment.transfer_out(food)
        elif answer == 2:
            entertainment.transfer_out(clothing)
        else:
            print('Wrong Selection')
            entertainment_selection()
    else:
        print('Wrong Selection')
        entertainment_selection()


def main():
    answer = int(category_selection())
    if answer == 1:
        food_selection()

    elif answer == 2:
        clothing_selection()

    elif answer == 3:
        entertainment_selection()
    else:
        print('Wrong input')
        main()


main()



# food.withdrawal()
# print(food.amount)
#
# food.transfer_out(clothing)
# print(food.amount)
# print(clothing.amount)







# def deposit(self):
#    deposit = int('How much would you like to deposit?')
#    return deposit


# print(foo.deposit)


# # print(starting_Balance.food)
#
#

#
# if answer == 1:
#     return 'food'
#     #     elif answer == 2:
#     #         return 'clothing'
#     #
#     #     elif answer == 3:
#     #         return 'entertainment'
#     #
#     #
#     print('Please select a category')
#
# category_selection()
#

# #
# # def deposit(self, category):
# #     deposit = int('How much would you like to deposit?')
# #     return deposit
# #
# # def withdrawal(self, category):
# #     withdrawal = int('How much would you like to deposit?')
# #     return withdrawal
# #
# # def compute_balances(self, category):
# #     print('The current balance for food is')
# #     print('The current balance for clothing is')
# #     print('The current balance for entertainment is')
# #
# # def transfer(self):
# #     print('Please select a category')
# #     print('1. Food')
# #     print('2. Clothing')
# #     print('3. Entertainment')
# #     print('4. Transfer')
# #     transfer_from = input()
# #     print('Please select a category')
# #     print('1. Food')
# #     print('2. Clothing')
# #     print('3. Entertainment')
# #     transfer_to = input()
# #     amount = input('Please select how much you want to move')
# #     return transfer_from, transfer_to, amount
#
# #  3print(category_selection(self))
#
#
# # 1.  Depositing funds to each of the categories
# # 2.  Withdrawing funds from each category
# # 3.  Computing category balances
# # 4.  Transferring balance amounts between categories
