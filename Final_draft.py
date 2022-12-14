import tkinter as tk
from tkinter import messagebox
import csv
class MYGUI:

    def __init__(self):
        self.root = tk.Tk()
        self.profile = 'Unknown'
        self.root.geometry('800x500')
        self.label = tk.Label(self.root, text= 'Landing Page', font=('Arial', 15))
        self.label.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text= 'Jaden', font=('Arial', 10), command= self.open)
        self.button.place(x=5, y=10, height=60, width= 120)

        self.button2 = tk.Button(self.root, text= 'Roan', font=('Arial', 10), command= self.open2)
        self.button2.place(x=5, y=80, height=60, width= 120)

        self.button3 = tk.Button(self.root, text= 'Keith', font=('Arial', 10))
        self.button3.place(x=5, y=150, height=60, width= 120)

        self.root.mainloop()

    def open(self):
        self.newwindow = FoodNut()

    def open2(self):
        self.newwindow2 = profile()

    def close(self):
        self.newwindow.top.destroy()
        self.newwindow = FoodNut()

class FoodNut:
    def __init__(self):
                                #Initialize nutrition variables
        self.calories = 0 
        self.carbs = 0
        self.protein = 0
        self.fat = 0

                                #Create window and make labels and text entry
        self.top = tk.Toplevel()
        self.top.title('Food Nutrition Calculator')
        self.top.geometry('800x500')

        label = tk.Label(self.top, text= 'Food Nutrition Calculator', font=('Arial', 20))
        label.pack(padx=10, pady=10)

        self.callabel = tk.Label(self.top, text= (f'Calories = {self.calories}'), font=('Arial', 14))
        self.callabel.place(x=30, y=20)

        self.carblabel = tk.Label(self.top, text= (f'Carbs = {self.carbs}  Grams'), font=('Arial', 14))
        self.carblabel.place(x=49, y=50)

        self.proteinlabel = tk.Label(self.top, text= (f'Protein = {self.protein}  Grams'), font=('Arial', 14))
        self.proteinlabel.place(x=40, y=80)

        self.fatlabel = tk.Label(self.top, text= (f'Fat = {self.fat}  Grams'), font=('Arial', 14))
        self.fatlabel.place(x=72, y=110)

        self.label2 = tk.Label(self.top, text= ('-Grams Eaten'), font=('Arial', 10))
        self.label2.place(x=670, y=258)

        self.label3 = tk.Label(self.top, text= ('-Food'), font=('Arial', 10))
        self.label3.place(x=520, y=258)

        self.textentry = tk.Text(self.top, height= 1, font=('Arial', 15))
        self.textentry.pack(padx= 280, pady= 200)

        self.textentry2 = tk.Text(self.top, height= 1, font=('Arial', 15), width=6)
        self.textentry2.place(x=600, y=258)

                            #Create buttons, exit button quits program, entry button sends filled out textbox to update nutrition info
        button = tk.Button(self.top, text= 'exit', font=('Arial', 14), command= self.top.destroy)
        button.place(x= 725, y= 0, height= 35, width= 75)

        self.textbut = tk.Button(self.top, text= 'butt', font=('Arial', 14), command= self.addfoodbutton)
        self.textbut.place(x= 360, y= 300, height= 30, width= 80)


                        #function to add the food nutrition and update information
    def addfoodbutton(self):  
        file_object = open('Foods.csv', mode='r')
        original_text = file_object.read()
        splitlist = original_text.split()
        file_object.close()
        gramsate = int(self.textentry2.get('1.0', tk.END))
        grams_multiplier = gramsate / 100
        if self.textentry.get('1.0', tk.END).strip() in splitlist:
            self.calories += (int(splitlist[splitlist.index(self.textentry.get('1.0', tk.END).strip()) + 1])) * grams_multiplier
            self.fat += (int(splitlist[splitlist.index(self.textentry.get('1.0', tk.END).strip()) + 2])) * grams_multiplier
            self.protein += (int(splitlist[splitlist.index(self.textentry.get('1.0', tk.END).strip()) + 3])) * grams_multiplier
            self.carbs += (int(splitlist[splitlist.index(self.textentry.get('1.0', tk.END).strip()) + 4])) * grams_multiplier
            self.callabel.config(text=f'Calories = {self.calories:.1f}')
            self.fatlabel.config(text=f'Fat = {self.fat:.1f}')
            self.proteinlabel.config(text=f'Protein = {self.protein:.1f}')
            self.carblabel.config(text=f'Carb = {self.carbs:.1f}')
        else:
            print('false')


class profile:
    def __init__(self,dict=None):

        self.root2 = tk.Tk()
        self.root2.geometry('800x500')
        self.label = tk.Label(self.root2, text= 'Profile Creator', font=('Arial', 15))
        self.label.pack(padx=10, pady=10)


        self.name = 'Not defined'
        self.age = 'Not defined'
        self.height = 'Not defined'
        self.w_circ = 'Not defined'
        self.weight = 'Not defined'


        self.agel = tk.Label(self.root2, text= (f'Your age is: {self.age}'), font=('Arial', 12))
        self.agel.place(x=30, y=20)

        self.w_circl = tk.Label(self.root2, text= (f'Your waist circumference is: {self.w_circ}'), font=('Arial', 12))
        self.w_circl.place(x=30, y=50)

        self.heightl = tk.Label(self.root2, text= (f'Your height is: {self.height}'), font=('Arial', 12))
        self.heightl.place(x=30, y=80)

        self.weightl = tk.Label(self.root2, text= (f'Your weight is: {self.weight}'), font=('Arial', 12))
        self.weightl.place(x=30, y=110)

        self.namel = tk.Label(self.root2, text= (f'Your name is: {self.name}'), font=('Arial', 12))
        self.namel.place(x=30, y=140)

#
        self.agelabel = tk.Label(self.root2, text= ('name'), font=('Arial', 9))
        self.agelabel.place(x=145, y=230)

        self.w_circlabel = tk.Label(self.root2, text= ('waist circumference(inch)'), font=('Arial', 9))
        self.w_circlabel.place(x=205, y=230)

        self.heightlabel = tk.Label(self.root2, text= ('height(inch)'), font=('Arial', 9))
        self.heightlabel.place(x=360, y=230)

        self.weightlabel = tk.Label(self.root2, text= ('weight'), font=('Arial', 9))
        self.weightlabel.place(x=495, y=230)

        self.namelabel = tk.Label(self.root2, text= ('age'), font=('Arial', 9))
        self.namelabel.place(x=620, y=230)


        self.button = tk.Button(self.root2, text= 'Update Information', font=('Arial', 10), command= self.profileupdate)
        self.button.place(x=350, y=300, height=60, width= 120)


        self.ptextentry5n = tk.Text(self.root2, height= 1, font=('Arial', 15))
        self.ptextentry5n.place(x=120, y=200, height=30, width= 80)

        self.ptextentry2w_ = tk.Text(self.root2, height= 1, font=('Arial', 15))
        self.ptextentry2w_.place(x=240, y=200, height=30, width= 80)

        self.ptextentry3h = tk.Text(self.root2, height= 1, font=('Arial', 15))
        self.ptextentry3h.place(x=360, y=200, height=30, width= 80)

        self.ptextentry4w = tk.Text(self.root2, height= 1, font=('Arial', 15))
        self.ptextentry4w.place(x=480, y=200, height=30, width= 80)

        self.ptextentryage = tk.Text(self.root2, height= 1, font=('Arial', 15))
        self.ptextentryage.place(x=600, y=200, height=30, width= 80)
        self.ptextentry2w_.get('1.0', tk.END)
        
        self.root2.mainloop()
    def profileupdate(self):
        self.name = self.ptextentry5n.get('1.0', tk.END)
        self.age = self.ptextentryage.get('1.0', tk.END)
        self.w_circ = self.ptextentry2w_.get('1.0', tk.END)
        self.height = self.ptextentry3h.get('1.0', tk.END)
        self.weight = self.ptextentry4w.get('1.0', tk.END)
        self.namel.config(text=(f'Your name is: {self.name}'), font=('Arial', 12))
        self.w_circl.config(text=(f'Your waist circumference is: {self.w_circ}'), font=('Arial', 12))
        self.heightl.config(text=(f'Your height is: {self.height}'), font=('Arial', 12))
        self.agel.config(text=(f'Your age is: {self.age}'), font=('Arial', 12))
        self.weightl.config(text=(f'Your weight is: {self.weight}'), font=('Arial', 12))
        self.toCsv()


    def toCsv(self):
        name = self.name.lower().strip()
        filename = f'{name}.csv'
        with open(filename, mode='w') as profile_file:
            profile_writer = csv.writer(profile_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            #Format: row is data name followed by data
            profile_writer.writerow(['age', self.age.strip()])
            #in inches
            #Format: row is data name followed by data        
            #in cm
            profile_writer.writerow(['w_circ', self.w_circ.strip()])
            #in cm, converted to meters in fromCsv
            profile_writer.writerow(['height', self.height.strip()])
            #in lbs
            #in kg
            profile_writer.writerow(['weight', self.weight.strip()])




root = MYGUI()