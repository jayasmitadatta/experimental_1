# dashboard

import tkinter as tk 

def main():
    
    
    root = tk.Tk() #main window
    
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    
    root.geometry(f"{screen_width}x{screen_height}")
    
    root.title("Dashboard")
    
    # left frame
    
    left_frame = tk.Frame(root, width ="400", bg="white", bd =2, relief = "solid") # creating the frame
    left_frame.pack(side="left", fill = "y") # deciding where to put it, fill = y fills the whole screen
    left_frame.propagate(False) # stops the frme from resizing as per wtv is inside
    
    right_frame = tk.Frame(root, bg ="white", bd =2, relief = "solid") # creating the frame
    right_frame.pack(side="left", fill = "both", expand = True, padx= (5,0)) # deciding where to put it
    right_frame.propagate(False) # stops the frme from resizing as per wtv is inside
    
    # left label 
    
    left_label = tk.Label(left_frame, text= "Essential Shortcuts", font = ("Arial", 18))
    left_label.pack(fill = "x", ipady= 20) # fill = x Stretch this label horizontally until it fills all the available width of its parent
    
    
    right_label = tk.Label(right_frame, text= "Welcome, Jane Doe!", font = ("Arial", 30))
    right_label.pack(fill = "x", ipady= 35)
    
    # creating a top frame for the canvas
    top_frame = tk.Frame(right_frame, bg="white")
    top_frame.pack(fill="x", pady=20) # Create a separate top frame to control the layout. The canvas couldn't move higher because pack() had already placed it below the header.
    
    #lower frame for sub-sections
    bottom_frame = tk.Frame(right_frame, bg ="white", bd =1, relief="solid")
    bottom_frame.pack(fill= "x") # fremes are resizing per what is in them
    
    # sub-frames within bottom frame
    daily_frame = tk.Frame(bottom_frame, width=250, height=400, bg="white", bd=1, relief="solid")
    daily_frame.pack(side="left", padx=(60,60))
    daily_frame.pack_propagate(False)

    monthly_frame = tk.Frame(bottom_frame, width=250, height=400, bg="white", bd=1, relief="solid")
    monthly_frame.pack(side="left", padx=50)
    monthly_frame.pack_propagate(False)

    yearly_frame = tk.Frame(bottom_frame, width=250, height=400, bg="white", bd=1, relief="solid")
    yearly_frame.pack(side="left", padx=50)
    yearly_frame.pack_propagate(False)
    
    #labels for subsections
    daily_label = tk.Label(daily_frame, text="Daily", font =("Arial", 15))
    daily_label.pack(fill="x", ipady= 10)
    
    monthly_label = tk.Label(monthly_frame, text="Monthly", font =("Arial", 15))
    monthly_label.pack(fill="x", ipady= 10)
    
    yearly_label = tk.Label(yearly_frame, text="Yearly", font =("Arial", 15))
    yearly_label.pack(fill="x", ipady= 10)
    
    histogram = tk.Canvas(top_frame, width = 400, height = 250,bd =1, relief= "solid", bg ="white")
    histogram.pack(side = "left", padx = (100,0)) # 30 pixels from lef, 0 pixels from right, 20 pixels from top, 0 pixels from nottom
    
    histogram.create_rectangle(40, 180, 70, 230, fill="blue")
    histogram.create_rectangle(80, 140, 110, 230, fill="blue")
    histogram.create_rectangle(120, 100, 150, 230, fill="blue")
    histogram.create_rectangle(160, 60, 190, 230, fill="blue")
    histogram.create_rectangle(200, 110, 230, 230, fill="blue")
    histogram.create_rectangle(240, 150, 270, 230, fill="blue")
    histogram.create_rectangle(280, 170, 310, 230, fill="blue")
    histogram.create_rectangle(320, 200, 350, 230, fill="blue")
    
    progress_ring = tk.Canvas(top_frame, width = 350, height = 250,bd =1, relief= "solid", bg ="white")
    progress_ring.pack(side = "left", padx = (100,0))
    
    
    progress_ring.create_oval( 60, 35, 240, 215, outline="lightblue", width=20)
    
    progress_ring.create_arc(60, 35, 240, 215, start=90, extent=-240, style="arc", outline="blue", width=20)
    
    progress_ring.create_text( 150, 125, text="67%", font=("Arial", 28, "bold"), fill = "black")
    
    
    
    # left frame sub-sections
    
    shortcut_frame1 = tk.Frame(left_frame, bg = "white", borderwidth= 5, relief= "solid")
    shortcut_frame1.pack(fill="both", expand = True, padx = 15, pady = 15)
    
    navigation_frame = tk.Text(shortcut_frame1, height=3, width=45, bg ="grey", bd = 0.5, relief = "sunken")
    navigation_frame.pack(padx= 40, pady=20)
    
    # 2nd sub-frame sub-sections
    
    shortcut_frame2 = tk.Frame(left_frame, bg = "white", borderwidth= 5, relief = "solid")
    shortcut_frame2.pack(fill="both", expand = False, padx = 15, pady = 15)
    
    tabs_frame = tk.Frame(shortcut_frame2)
    
    tabs_frame.columnconfigure(0, weight=1)
    tabs_frame.columnconfigure(1, weight=1)

    tabs_frame.rowconfigure(0, weight=1) #weight=1 tells the grid cells they are allowed to grow.
    tabs_frame.rowconfigure(1, weight=1)
    
    txt_box1 = tk.Text(tabs_frame, height=15)
    txt_box1.grid(row = 0, column = 0, sticky = "nsew", padx=2, pady=2) #"nsew" tells the widget to stretch in all directions and fill the entire grid cell.

    txt_box2 = tk.Text(tabs_frame, height = 15)
    txt_box2.grid(row = 0, column = 1, sticky = "nsew", padx=2, pady=2)
    
    txt_box3 = tk.Text(tabs_frame, height = 15)
    txt_box3.grid(row = 1, column = 0, sticky = "nsew", padx=2, pady=2)
    
    txt_box4 = tk.Text(tabs_frame, height = 15)
    txt_box4.grid(row = 1, column = 1, sticky = "nsew", padx=2, pady=2)
    
    tabs_frame.pack(fill="x", pady = (5, 100)) #fill="both", expand=True tells tabs_frame itself to use the available space in its parent.
    
    ai_frame = tk.Text(shortcut_frame2, height=5, width=45, bg ="grey", bd = 0.5, relief = "sunken")
    ai_frame.pack(fill = "both", expand = True)
    # 3rd frame sub-section
    
    shortcut_frame3 = tk.Frame(left_frame, bg = "white", borderwidth= 5, relief = "solid")
    shortcut_frame3.pack(fill="both", expand = True, padx = 15, pady = 10)
    
    #ai_frame = tk.Text(shortcut_frame3, height=5, width=45, bg ="grey", bd = 0.5, relief = "sunken")
    #ai_frame.pack(fill = "both", expand = True)
    
    

    root.mainloop()
    
    
    
    
    
    
    
if __name__ =="__main__":
    main()

    


