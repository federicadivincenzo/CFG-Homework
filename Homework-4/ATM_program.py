"""
Simple ATM program**
  - Using exception handling code blocks such as try/ except / else / finally, write a program that simulates an
   ATM machine to withdraw money. (NB: the more code blocks the better, but try to use at least two key words e.g.
  try/except)
  - Tasks:
    1. Prompt user for a pin code
     2. If the pin code is correct then proceed to the next step, otherwise ask a user to type in a password again. 
        You can give a user a maximum of 3 attempts and then exit a program. 
     3. Set account balance to 100. 
     4. Now we need to simulate cash withdrawal 
     5. Accept the withdrawal amount 
     6. Subtract the amount from the account balance and display the remaining balance 
        (NOTE! The balance cannot be negative!)
     7. However, when a user asks to ‘withdraw’ more money than they have on their account, 
        then you need to raise an error an exit the program.
"""

pin_is_successful = False
withdrawal_is_successful = False
account_balance = 100
user_pin = '1234'
pin_attempt = 3

def pin_validated(pin):
    if any(c.isalpha() for c in pin):
        raise SyntaxError('Pin needs to be all number')

    if not pin == user_pin:
        raise ValueError('Pin not match. Please, try again!')

    assert pin == user_pin

    return True


def withdrawal_validated(withdraw):
    if withdraw < 0:
        raise ValueError("Value can't be negative")

    assert (account_balance - withdraw) > 0
    return True


try:
    pin = input("Please enter your pin >> ")
    if pin_validated(pin):
        try:
            withdraw = int(input("How much do you want to to withdraw >> "))
            withdrawal_validated(withdraw)
        except ValueError as exc:
            print(exc)
        except AssertionError:
            print("Withdraw exceeds account balance.")
        else:
            withdrawal_is_successful = True
except SyntaxError as exc:
    print(exc)
except ValueError as exc:
    print(exc)
else:
    pin_is_successful = True
finally:
    if withdrawal_is_successful and pin_is_successful:
        print(f"You successfully withdrew {withdraw}$ 🥳 ")
        pin_attempt = 3
    else:
        print("Sorry something went wrong. Please try again.")





