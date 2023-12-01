
"""
Project :  Create Fee Voucher By Ehsanullah Qadeer 
Roll No :  2094
Section :  E1
"""

try:
    from tkinter import * 
    from tkinter import ttk            
    import Voucher
    import Database
    
except:
    print( "One of the required module is missing." )
###  colors to use

color1 = "#666666"   # Grey
color2 = "#F0F0F0"      # White
color3 = "#cc6600"      # Brown
color4 = "#0066ff"     # Blue
color5 = "#66ff33"   # Green
color6 = "#ff99ff"      # Pink
color7 = "#ffff00"       # Yellow
color8 = "#FF8916"    # orange!
color9 = "#ff6600"      # Orange
color10 = "#993300"    # Chocolate
color11="#66ffff"       #cyan
color12='#000000' #Black
color13 = "#52ACEA"     # Blue!
color14 = "#CDE3F1"     # lightBlue



color_head1 = color8
color_head2 = color8
color_head3 = color4
color_regular1 = color4
color_regular2 = color4
color_regular3 = color4
color_back1 = color2
color_back2 = color14
color_back3 = color14

font_style = 'Century Gothic'

LARGE_FONT = ( font_style , 32 )
MEDIUM_FONT = ( font_style , 24 )
SMALL_FONT = ( font_style , 16 )
SMALLER_FONT = ( font_style , 12 )


class MainView( Tk ):
    
    def __init__( self , *args , **kwargs ):
        
        Tk.__init__( self , *args , **kwargs )

        container = Frame( self )     
        container.pack( side = 'top' , fill = 'both' , expand =True)

        self.geometry( "1300x700" )        
        self.title( "Fee Voucher System" )      
        
        self.Frames = { }

        for F in ( Login , Main ):
            page_name = F.__name__
            frame = F( parent = container , controller = self )
            self.Frames[page_name] = frame

            frame.grid( row = 0 , column = 0 , sticky = 'nsew' )

        self.show_frame( 'Login' )

    def show_frame( self , page_name ):
        """
        This method let us display the frame we want to display

        It raises the frame we want to display
        """
        
        frame = self.Frames[page_name]
        frame.tkraise( )


class Login(  Frame ):
    def __init__( self , parent , controller ):
        Frame.__init__( self , parent )   
        self.controller = controller
       
        self.frame = Frame ( self , height = 700 , width = 1300 )     
        self.frame.grid( row=0 , column = 0 , sticky = 'nsew' )
        self.frame.grid_propagate(0)

        self.left_frame = Frame( self.frame , height = 700 , width = 600 , bg = color_back1)     
        self.left_frame.grid( row = 0 , column = 0 , sticky = 'nsew' )
        self.left_frame.grid_propagate(0)

        self.top_heading = Label( self.left_frame , text = "Fee Voucher System" , font = LARGE_FONT , fg = 'red' , bg = color_back1 )
        self.top_heading.grid( row=1 , column = 1 , pady = (200 , 5) , padx = 120)
 
        self.heading = Label( self.left_frame , text = "Log in" , font = MEDIUM_FONT , fg = color_head2 , bg = color_back1 )
        self.heading.grid( row = 2 , column = 1 , pady = (2 , 20) )

        self.info = Frame( self.left_frame  , bg = color_back1)    
        self.info.grid( row = 3 , column = 1 )

        self.label1 = Label( self.info , text = "Username (Ehsan)" , font = SMALL_FONT , fg = color_regular1  , bg = color_back1 )
        self.label1.grid( row=1 , column = 1 , pady = 7 , padx = 3 )

        self.Entry1 = ttk.Entry ( self.info , font = SMALL_FONT)
        self.Entry1.bind ('<Return>' , self.log_in_info)
        self.Entry1.grid( row = 1 , column = 2 , pady = 7 , padx = 3)

        self.label2 = Label( self.info , text = "Password (2094)" , font = SMALL_FONT , fg = color_regular1  , bg = color_back1 )
        self.label2.grid( row=2 , column = 1 )

        self.Entry2 = ttk.Entry ( self.info , font = SMALL_FONT , show = "*" )
        self.Entry2.bind ('<Return>' , self.log_in_info)
        self.Entry2.grid( row = 2 , column = 2 )

        self.mess_lab = Label( self.info , text = " " , bg = color_back1 , fg = "red" )
        self.mess_lab.grid( row = 3 , column = 2 )

        submit = PhotoImage(file='submit.png')
        
        self.submit_b = Button( self.info , image = submit  , command = self.log_in_info , relief=FLAT )
        self.submit_b.image = submit
        self.submit_b.grid( row =4  , column = 2 , ipady = 4 , pady = 8)
        
        self.submit = ttk.Button( self.info , text  = "Submit" , style = 'my.TButton' , command = self.log_in_info)
        self.submit.bind( '<Button-1>' , self.log_in_info )
        

        image1 = PhotoImage( file = 'image1.png' )
        
        self.right_frame = Frame( self.frame , height = 700 , width = 700 , bg = color_back1 )  
        self.right_frame.grid( row = 0 , column = 1 )
        self.right_frame.grid_propagate(0)

        self.Image_1 = Label( self.right_frame , image = image1 )   
        self.Image_1.image = image1
        
        self.Image_1.place( x = 50 , y = 70 )
        

    def log_in_info( self , *args ):
        check = Database.login( self.Entry1.get() , self.Entry2.get() )

        if check:
            self.controller.show_frame( 'Main' )
        else:
            self.mess_lab.configure( text = "* Enter Valid username and password" )



class aggregation(Database.composition ):
    """
    It is a class in which aggregation is used
    """
    
    def __init__( self , obj ):
         self.obj=obj
        

    def view(self):
        
        return self.obj
    def total(self,roll_no):
        super().__init__(roll_no)
        return super().total()
        
voucher=Database.vouch()
aggr=aggregation(voucher)
#print(aggr.view())

class Main( Frame ):
    def __init__( self , parent , controller,Arg=aggr ):
        Frame.__init__( self , parent )

        self.controller = controller
        
        self.frame = Frame( self , height = 700 , width = 1300 )    #   main frame
        self.frame.grid( row = 0 , column = 0 , sticky = 'nsew')
              
        self.left_frame = Frame(self.frame , height = 700 , width = 250 , bg = color_back1 )    #   left sub frame 
        self.left_frame.grid( row = 1 , column = 1 , sticky ='nsew'  )
        self.left_frame.grid_propagate(0)
        self.Arg=Arg.view()
        self.arg=Arg

        #  used to close frames not in use
        
        self.flag1 = True
        self.flag2 = True
        self.flag3 = True
        self.flag4 = True
        self.flag5 = True

        but1=PhotoImage(file='insert.png')
        but5=PhotoImage(file='show.png')
        but6=PhotoImage(file='vouch.png')

        self.img1=PhotoImage(file='confirm.png')
        self.img2=PhotoImage(file='cancel.png')
        self.img3=PhotoImage(file='submit_small.png')
    
        self.button1 = Button( self.left_frame , image=but1  , command= self.insert, relief=FLAT )
        self.button1.image=but1
        self.button1.grid( row = 1 , column = 1 , padx = 15 , pady = ( 30 , 0 ))
        self.button5 = Button( self.left_frame , image=but5 , command = self.show_all , relief=FLAT )
        self.button5.image=but5
        self.button5.grid( row = 17 , column = 1 , padx = 15 , pady = 10)
        self.button6 = Button( self.left_frame , image=but6 , command = lambda :self.sub_frame_1.lift( ) , relief=FLAT )
        self.button6.image=but6
        self.button6.grid( row = 20 , column = 1 , padx = 15 , pady = 10)

     
        self.right_frame = Frame(self.frame , height = 700 , width = 1050 )   #  right sub frame
        self.right_frame.grid( row = 1 , column = 2 )
        self.right_frame.grid_propagate(0)
 
        self.up_frame = Frame( self.right_frame , height = 140  , width = 1050 , bg = '#376092' )   #   header of right side
        self.up_frame.grid( row = 1 , column = 2 , pady = 5)
        self.up_frame.grid_propagate(0)
      
        self.up1 = Frame( self.up_frame , height = 140 , width = 250 )
        self.up1.grid( row = 1 , column = 1 , padx = (70 , 35) )
        self.up2 = Frame( self.up_frame , height = 140 , width = 250 , bg = color_back1 )
        self.up2.grid( row = 1 ,  column = 2 , padx = 35)
        self.up3 = Frame( self.up_frame , height = 140 , width = 250 , bg = color_back1 )
        self.up3.grid( row = 1 ,  column = 3 , padx = (35 , 70))

        up_image1 = PhotoImage( file = 'upimg2.png' )
        
        logo1=Label(self.up1, image=up_image1)
        logo1.image = up_image1
        logo1.place(x=0,y=0)

        up_image2 = PhotoImage( file = 'upimg1.gif' )
        
        logo2=Label(self.up2, image=up_image2)
        logo2.image = up_image2
        logo2.place(x=0,y=0)

        up_image3 = PhotoImage( file = 'upimg3.png' )
        
        logo3=Label(self.up3, image=up_image3)
        logo3.image = up_image3
        logo3.place(x=0,y=0)
        
        
        self.down_frame = Frame( self.right_frame , height = 550 , width = 1050 ,  bg = color_back2 )   #   body of right side
        self.down_frame.grid( row = 2 , column = 2 )
        self.down_frame.grid_propagate(0)

        self.sub_frame = Frame( self.down_frame , height = 550 , width = 1050 )  #   main display of body
        self.sub_frame.grid( row = 1 , column = 0 )
        self.sub_frame.grid_propagate(0)
 
        self.sub_frame_1 = Frame( self.sub_frame , height = 550 , width = 1050 , bg = color_back2 )  #  frame 1
        self.sub_frame_1.grid( row = 0 , column = 0 )
        self.sub_frame_1.grid_propagate(0)

        self.sub1_in = Frame( self.sub_frame_1 , height = 550 , width = 900 , bg = color_back2 )
        self.sub1_in.place( x = 250, y  = 80 )

        self.lab1 = Label( self.sub1_in , text = 'Enter Roll No' , font = SMALLER_FONT , fg = color_regular3 , bg = color_back2 )
        self.lab1.grid( row = 0 , column = 0 , pady = 5 )

        self.lab2 = Label( self.sub1_in , text = 'Enter Year' , font = SMALLER_FONT , fg = color_regular3 , bg = color_back2 )
        self.lab2.grid( row = 1 , column = 0 , pady = 5 )
       
        self.lab3 = Label( self.sub1_in , text = 'Select Month' , font = SMALLER_FONT , fg = color_regular3 , bg = color_back2 )
        self.lab3.grid( row = 2 , column = 0 , pady = 5 )

        self.lab4 = Label( self.sub1_in , text = 'Select Issue Date' , font = SMALLER_FONT , fg = color_regular3 , bg = color_back2 )
        self.lab4.grid( row = 3 , column = 0 , pady = 5 )

        self.lab5 = Label( self.sub1_in , text = 'Select Due Date'  , font = SMALLER_FONT  , fg = color_regular3 , bg = color_back2 )
        self.lab5.grid( row = 4 , column = 0 , pady = 5 )

        self.lab6 = Label( self.sub1_in , text = 'Select Month'  , font = SMALLER_FONT , fg = color_regular3 , bg = color_back2 )
        self.lab6.grid( row = 5 , column = 0 , pady = 5 )

        self.Ent1 = ttk.Entry ( self.sub1_in , font = SMALL_FONT)
        self.Ent1.bind ('<Return>' , self.voucher)
        self.Ent1.grid( row = 0 , column = 1 , pady = 7 , padx = 3)

        self.Ent2 = ttk.Entry ( self.sub1_in , font = SMALL_FONT)
        self.Ent2.bind ('<Return>' , self.voucher)
        self.Ent2.grid( row = 1 , column = 1 , pady = 7 , padx = 3)

        self.var2 = StringVar( self.sub1_in )
        self.option2 = [ 'January' , 'Feburary' , 'March' , 'April' , 'May' , 'June' , 'July' , 'August' , 'September' , 'October' , 'November' , 'December' ]
        self.popmenu2 = ttk.Combobox( self.sub1_in , textvariable = self.var2 , values = self.option2 , width = 30  )
        self.popmenu2.grid( row = 2 , column = 1 , padx = 5 , ipadx = 22 , ipady = 4)
        self.popmenu2.bind('<<ComboboxSelected>>' , self.voucher )
       
        self.var3 = StringVar( self.sub1_in )
        self.option3 = [ ]
        for x in range( 1 , 32 ):
            self.option3.append( x )
        self.popmenu3 = ttk.Combobox( self.sub1_in , textvariable = self.var3 , values = self.option3 , width = 30  )
        self.popmenu3.grid( row = 3 , column = 1 , padx = 5 , ipadx = 22 , ipady = 4)
        self.popmenu3.bind('<<ComboboxSelected>>' , self.voucher )

        self.var4 = StringVar( self.sub1_in )
        self.option4 = self.option3
        self.popmenu4 = ttk.Combobox( self.sub1_in , textvariable = self.var4 , values = self.option4 , width = 30  )
        self.popmenu4.grid( row = 4 , column = 1 , padx = 5 , ipadx = 22 , ipady = 4)
        self.popmenu4.bind('<<ComboboxSelected>>' , self.voucher )

        self.var5 = StringVar( self.sub1_in )
        self.option5 = [ 'January' , 'Feburary' , 'March' , 'April' , 'May' , 'June' , 'July' , 'August' , 'September' , 'October' , 'November' , 'December' ]
        self.popmenu5 = ttk.Combobox( self.sub1_in , textvariable = self.var5 , values = self.option5 , width = 30  )
        self.popmenu5.grid( row = 5 , column = 1 , padx = 5 , ipadx = 22 , ipady = 4)
        self.popmenu5.bind('<<ComboboxSelected>>' , self.voucher )

        self.empty = Label( self.sub1_in , bg = color_back2 )
        self.empty.grid(row = 9 , column = 0)

        but8=PhotoImage( file='gensing.png' )

        self.butt2 = Button( self.sub1_in , image=but8 , command = self.voucher , relief=FLAT , bg = color14)
        self.butt2.image=but8
        self.butt2.grid( row =10  , column = 1)

    def insert ( self ):
        """This is a method to insert new records of students."""
        
        if self.flag1:
            self.flag1 = False
            self.insert_frame = Frame( self.left_frame , height = 70 , width = 220 , bg = color_back3 )
            self.insert_frame.grid( row = 2 , column = 1 , rowspan = 2 )
               
            self.insert_class = Label( self.insert_frame , text = 'Select Class' , bg = color_back3 , fg = color_head3 )
               
            self.insert_class.place( x = 10 , y = 10 )

            self.var = StringVar( self.insert_frame )

            self.options = ['5th M1' ,'5th M2' ,'5th M3' , '5th E1' , '5th E2' , ]
               
            self.popmenu = ttk.Combobox( self.insert_frame , textvariable = self.var , values = self.options , width = 25  )
            self.popmenu.place( x = 10 , y = 35 )
            self.popmenu.bind('<<ComboboxSelected>>', self.enter_record)
        else :
            self.flag1 = True
            self.insert_frame.destroy( ) 
       
    
    def show_all( self ):
        self.sub_frame_2 = Frame(self.sub_frame, height=550, width=1000)  # frame 4
        self.sub_frame_2.grid(row=0, column=0)
        self.sub_frame_2.grid_propagate(0)

        self.sub2_in = Frame(self.sub_frame_2 , height=550, width=500, bg=color_back2)
        self.sub2_in.place(x=0, y=0)

        tree = ttk.Treeview(self.sub2_in , height='122',column=("column1", "column2", "column3","column4", "column5", "column6","column7", "column8"), show='headings')
        tree.heading("#1", text="NAME")
        tree.column('#1',minwidth=0,width=150)
        tree.heading("#2", text="FATHER NAME")
        tree.column('#2', minwidth=0, width=150)
        tree.heading("#3", text="CLASS")
        tree.column('#3', minwidth=0, width=90)
        tree.heading("#4", text="DATE OF BIRTH")
        tree.column('#4', minwidth=0, width=150)
        tree.heading("#5", text="ROLL NO")
        tree.column('#5', minwidth=0, width=96)
        tree.heading("#6", text="TUTION FEE")
        tree.column('#6', minwidth=0, width=120)
        tree.heading("#7", text="ANNUAL FEE")
        tree.column('#7', minwidth=0, width=120)
        tree.heading("#8", text="EXAMINATION FEE")
        tree.column('#8', minwidth=0, width=120)
        tree.pack(fill='x')

        for row in Database.get_students():
            tree.insert("",END,values=row)
        self.sub_frame_2.lift()
     

    def show_after_change(self):
        self.show_all( )


    def enter_record ( self , *args ):
        self.window = Tk ( )    #  creating new window

        self.window.geometry( "600x500" )
        self.window.title( "Insert Information" )

        self.frame = Frame( self.window , height = 500 , width = 600 , bg = color_back1 )
        self.frame.pack( )
        self.frame.pack_propagate(0)
        
        Heading = Label ( self.frame , text = 'Enter Information' , font = LARGE_FONT , fg = color_head1 , bg = color_back1 )
        Heading.grid( row = 1 , column = 1 , columnspan = 2 , padx = 100 , pady = ( 20 , 28 ))

        label1 = Label ( self.frame , text = 'Name' , font = SMALL_FONT , fg = color_regular1 , bg = color_back1 )
        label1.grid( row = 2 , column = 1 , pady = ( 1,8 ))

        label2 = Label ( self.frame , text = 'Father Name' , font = SMALL_FONT , fg = color_regular1 , bg = color_back1 )
        label2.grid( row = 3 , column = 1  , pady = ( 1,8 ))

        label3 = Label ( self.frame , text = 'Roll no' , font = SMALL_FONT , fg = color_regular1 , bg = color_back1 )
        label3.grid( row = 4 , column = 1  , pady = ( 1,8 ))

        label4 = Label ( self.frame , text = 'Date of Birth' , font = SMALL_FONT , fg = color_regular1 , bg = color_back1 )
        label4.grid( row = 5 , column = 1  , pady = ( 1,8 ))

        label5 = Label ( self.frame , text = 'Tuition Fee' , font = SMALL_FONT , fg = color_regular1 , bg = color_back1 )
        label5.grid( row = 6 , column = 1  , pady = ( 1,8 ))

        label6 = Label ( self.frame , text = 'Annual Fee' , font = SMALL_FONT , fg = color_regular1 , bg = color_back1 )
        label6.grid( row = 7 , column = 1  , pady = ( 1,8 ))

        self.label7 = Label ( self.frame , text = 'Examination Fee' , font = SMALL_FONT , fg = color_regular1 , bg = color_back1 )
        self.label7.grid( row = 8 , column = 1  , pady = ( 1,8 ))

        self.Entry1 = Entry ( self.frame , font = SMALL_FONT)
        self.Entry1.grid( row = 2 , column = 2 , padx = (0 , 100) )

        self.Entry2 = Entry ( self.frame , font = SMALL_FONT )
        self.Entry2.grid( row = 3 , column = 2 , padx = (0 , 100) )

        self.Entry3 = Entry ( self.frame , font = SMALL_FONT )
        self.Entry3.grid( row = 4 , column = 2 , padx = (0 , 100) )

        self.Entry4 = Entry ( self.frame , font = SMALL_FONT )
        self.Entry4.grid( row = 5 , column = 2 , padx = (0 , 100) )

        self.Entry5 = Entry ( self.frame , font = SMALL_FONT )
        self.Entry5.grid( row = 6 , column = 2 , padx = (0 , 100) )

        self.Entry6 = Entry ( self.frame , font = SMALL_FONT )
        self.Entry6.grid( row = 7 , column = 2 , padx = (0 , 100) )

        self.Entry7 = Entry ( self.frame , font = SMALL_FONT )
        self.Entry7.grid( row = 8 , column = 2 , padx = (0 , 100) )

        Button_sub = Button( self.frame , text = 'SUBMIT' , command = self.enter_in_record , bg = color8 , fg = 'white' , relief = GROOVE )
        Button_sub.grid( row = 10 , column = 1 , pady = 30 , padx = (180 , 1) , ipadx = 10)

        Button_cancel = Button( self.frame , text = "CANCEL" ,  command = self.not_record ,bg = color8 , fg = 'white' , relief = GROOVE )
        Button_cancel.grid( row = 10 , column = 2 , pady = 30 , padx = ( 1,180 ), ipadx = 10)

        self.window.mainloop( )

    
    
    def enter_in_record( self ):
        """This is a method to record data in database."""

        list_roll = Database.vouch( )
        flag = 0
        for j in list_roll:
            if j == self.Entry3.get( ):
                flag = 1
        if flag == 0 :
            Database.insert( self.Entry1.get( ) , self.Entry2.get( ) , self.var.get( ) , self.Entry4.get( ) , self.Entry3.get( ) , self.Entry5.get( ) , self.Entry6.get( ) , self.Entry7.get( ))
            self.show_after_change( )
            self.window.destroy( )
        else :            
            self.label8 = Label ( self.frame , text = '* Roll no should be unique.' , font = SMALL_FONT , fg = 'red' , bg = color_back1 )
            self.label8.grid( row = 9 , column = 1  , pady = ( 1,8 ))
         


    def not_record( self ):
        self.window.destroy( )
        

    def voucher( self , *args ):
        Total = self.arg.total(self.Ent1.get( ))
        a,b,c,d,e,f,g,h = Database.search_voucher( self.Ent1.get( ) )
        
        voucher = Voucher.Generate_Voucher(  a , b , e , c , self.var2.get() , f , h , Total , "{}/{}/{}".format(self.var3.get(),self.var2.get(),self.Ent2.get()),"{}/{}/{}".format(self.var4.get(),self.var5.get(),self.Ent2.get()) )



  

#  program runs if we are accessing it directly( without import )

if __name__ == "__main__":                           
    """Condition which be satisfied if file is accessed directly."""

    obj = MainView( )
    
    obj.mainloop()



