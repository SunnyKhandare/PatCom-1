from tkinter import *
from tkinter.filedialog import askopenfilename
import driver
import sys

file_names = []
summaries = []
whitelist = set('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ')

def get_file_name():
	
	file_name = askopenfilename()
	file_names.append( file_name )

def clean_output( string ):
	
	string = ''.join(filter(whitelist.__contains__, string ))
	return ' '.join( string.split() )

def get_summaries():
	
	summaries = driver.driver_code( file_names[0] , file_names[1] )
	
	summaries[0] = clean_output( summaries[0] )
	summaries[1] = clean_output( summaries[1] )
	
	summary_window = Tk()
	summary_window.geometry( '800x800' )
	
	text = Text( summary_window )
	
	text.insert( INSERT , "The Summary Of Document 1 is -\n\n" )
	text.insert( INSERT , summaries[0] + '.' )
	text.insert( INSERT, "\n\n")
	text.insert( INSERT , "The Summary Of Document 2 is -\n\n" )
	text.insert( INSERT, summaries[1] + '.' )
	
	text.pack(expand=True, fill=BOTH)
	
	summary_window.mainloop()
	return

if __name__ == '__main__':

	main_window = Tk()
	main_window.title( "Patcom" )
	main_window.geometry( '800x500' )
	main_window.grid_columnconfigure(2, weight=1)

	l1 = Label( main_window , text="PATCOM", fg = "light green", bg = "dark green" , height = 2 , width = 30)
	l1.config(font=("Courier", 60 ))
	l1.place(relx=0.5, rely=0.2, anchor=CENTER)

	bt_1 = Button(main_window, text='Select File 1', command = get_file_name )
	bt_1.place(relx=0.5, rely=0.5, anchor=CENTER)

	bt_2 = Button(main_window, text='Select File 2', command = get_file_name )
	bt_2.place(relx=0.5, rely=0.6, anchor=CENTER)

	generate_summaries = Button(main_window, text='Generate Summaries', command = get_summaries , height = 1 , width = 20 )
	generate_summaries.place(relx=0.5, rely=0.7, anchor=CENTER)

	main_window.mainloop()
