from tkinter import *

window = Tk()
window.title("BMI CALCULATOR")

my_weight_label = Label(text="Enter Your Weight!", width=25, height=10)
my_weight_label.pack()

my_entry1 = Entry(width=10)
my_entry1.pack()

my_height_label = Label(text="Enter Your Height", width=25, height=10)
my_height_label.pack()

my_entry2 = Entry(width=10)
my_entry2.pack()

result_label = Label()
result_label.pack()

def button_select():
    user_weight = my_entry1.get()
    user_height = my_entry2.get()

    if not user_weight.isdigit() or not user_height.isdigit():
        result_label.config(text="Please enter a number")
        return

    user_weight = int(user_weight)
    user_height = int(user_height) / 100
    bmi = user_weight / (user_height ** 2)
    rounded_bmi = round(bmi, 2)
    result_label.config(text="BMI: " + str(rounded_bmi))

    if rounded_bmi < 18.50:
        result_label.config(text="Underweight: " + str(rounded_bmi))
    elif rounded_bmi < 25.00:
        result_label.config(text="Normal weight: " + str(rounded_bmi))
    elif rounded_bmi < 30.00:
        result_label.config(text="Overweight: " + str(rounded_bmi))
    else:
        result_label.config(text="Obese: " + str(rounded_bmi))

my_button = Button(text="Calculate", width=8, height=1, command=button_select)
my_button.pack(padx=10, pady=10)

window.mainloop()
