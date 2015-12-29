from Tkinter import *
from sympy import *
from numpy import *
from scipy import *
from sympy.abc import x
from sympy import sympify
class App(Frame):
	def __init__(self, master):
		Frame.__init__(self,master)
		self.grid()
		self.integrator()
	def integrator(self):
		self.instruction1 = Label(self, text = "Function : ")
		self.instruction1.grid(row = 0, column = 0, columnspan  = 2, sticky = W)
		self.instruction1 = Label(self, text = "Lower limit : ")
		self.instruction1.grid(row = 0, column = 1, columnspan  = 2, sticky = W)
		self.instruction3 = Label(self, text = "Upper limit : ")
		self.instruction3.grid(row = 0, column = 2, columnspan  = 2, sticky = W)
		self.function1 = Entry(self)
		self.function1.grid(row = 1, column = 0, sticky = W)
		self.function2 = Entry(self)
		self.function2.grid(row = 1, column = 1, sticky = W)
		self.function3 = Entry(self)
		self.function3.grid(row = 1, column = 2,sticky = W)
		self.submit_button = Button(self, text = "submit", command = self.answer)
		self.submit_button.grid(row =2, column = 0, sticky =W)
		self.text = Text(self, width = 35, height = 5, wrap = WORD)
		self.text.grid(row =3, column =0, sticky = W)
	def answer(self):
		f = str(self.function1.get())
		func = sympify(f)
		r1 = int(self.function2.get())
		r2 = int(self.function3.get())
		x = symbols('x')
		p = linspace(r1,r2,101)
		y = zeros(101)
		for i in range(0,101):
			y[i] = func.subs(x,p[i])
		I = (r2-r1)/200.0*(y[0]+y[100]+2.0*(sum(y,axis =0)-y[0]-y[100]))
		self.text.insert(0.1,I)
		self.text.insert(CURRENT,"is the integrated value of single valued function for given range\n ")


root = Tk()
root.title("integrator")
root.geometry("600x150")
app = App(root)
root.mainloop()		

