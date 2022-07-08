# pip install bs4

from tkinter import *
from tkinter.messagebox import *
import requests
import bs4

def f1():
	def f2():
		main_window.deiconify()
		view_window.withdraw()
		main_window_ent_name.focus()
	try:
		country_name=main_window_ent_name.get()
		wa="https://www.worldometers.info/coronavirus/country/"+country_name+"/"
		res=requests.get(wa)
		data= bs4.BeautifulSoup(res.text,'html.parser')
		info = data.find_all('div', {'class':'maincounter-number'})
		total_cases = info[0].span.text
		death_cases=info[1].span.text
		recovered=info[2].span.text
		
		view_window=Toplevel(main_window)
		view_window.title("Count")
		view_window.geometry("600x700+500+50")
		view_window.configure(background='cyan')
		view_window_lbl_total=Label(view_window,text="Total Cases",font=('Calibri',30,'bold'),background='cyan')
		view_window_lbl_total_count=Label(view_window,text=total_cases,font=('Calibri',30,'bold'),background='cyan',foreground='blue')
		view_window_lbl_death=Label(view_window,text="Death Cases",font=('Calibri',30,'bold'),background='cyan')
		view_window_lbl_death_count=Label(view_window,text=death_cases,font=('Calibri',30,'bold'),background='cyan',foreground='red')
		view_window_lbl_recovered=Label(view_window,text="Recovered Cases",font=('Calibri',30,'bold'),background='cyan')
		view_window_lbl_recovered_count=Label(view_window,text=recovered,font=('Calibri',30,'bold'),background='cyan',foreground='green')
		view_window_btn_back=Button(view_window,text="Back",font=('Calibri',30,'bold'),command=f2)
		view_window_lbl_total.pack(pady=20)
		view_window_lbl_total_count.pack(pady=20)
		view_window_lbl_death.pack(pady=20)
		view_window_lbl_death_count.pack(pady=20)
		view_window_lbl_recovered.pack(pady=20)
		view_window_lbl_recovered_count.pack(pady=20)
		view_window_btn_back.pack(pady=20)
		view_window.deiconify()
		main_window.withdraw()
		main_window_ent_name.delete(0,END)
		main_window_ent_name.focus()
	except Exception as e:
		showerror("Error",e)

	
main_window=Tk()
main_window.title("Corona Counter")
main_window.geometry("500x500+500+200")
main_window.configure(background='yellow')

main_window_lbl_name=Label(main_window,text="Enter Country Name",font=('Calibri',30,'bold'),background='yellow')
main_window_ent_name=Entry(main_window,bd=2,font=('Calibri',30,'bold'))
main_window_btn_count=Button(main_window,text="Find",font=('Calibri',30,'bold'),command=f1)


main_window_lbl_name.pack(pady=20)
main_window_ent_name.pack(pady=20)
main_window_btn_count.pack(pady=20)
main_window_ent_name.focus()
main_window.mainloop()
	