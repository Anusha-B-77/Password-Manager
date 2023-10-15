import tkinter
from tkinter import CENTER,Tk,Label,END,Button,Entry,Frame,Toplevel
from tkinter import ttk
from database_operations import DbOperation

class root_window:
    
    def __init__(self,root,db):
        self.db=db
        self.root=root
        self.root.title("Password Manager")
        self.root.geometry("900x550+40+40")
        head_title =Label(self.root,text="Password Manager",width=40,bg="purple",fg="white"
                          ,font=("Ariel",21),padx=10,pady=10,justify=CENTER,anchor="center").grid(columnspan=4,padx=120,pady=10)
        self.curd_frame=Frame(self.root,highlightbackground="black",highlightthickness=1,padx=10,pady=30)
        self.curd_frame.grid()
        self.create_entry_labels()
        self.create_entry_boxes()
        self.create_curd_buttons()
        self.search_entry=Entry(self.curd_frame,width=30,font=('ariel',12))
        self.search_entry.grid(row=self.row,column=self.col)
        self.col+=1
        Button(self.curd_frame,text="Search",bg="yellow",font=("ariel",12),width=20).grid(row=self.row,column=self.col,padx=5,pady=5) 
        self.create_records_tree() 
        self.save_records_to_file()
             
    def create_entry_labels(self): 
        self.col=0
        self.row=0
        labels_info=('ID','Website','Username','Password')
        for label_info in labels_info:
            Label(self.curd_frame,text=label_info,bg='grey',
            fg='white',font=('ariel',12),padx=5,pady=2).grid(padx=5,pady=2,row=self.row,column=self.col)
            self.col+=1
            
    def create_curd_buttons(self):
        self.row+=1
        self.col=0
        buttons_info=(('Create','green',self.save_record),("Update",'blue',self.update_record),
                 ('delete','red',self.delete_record),('Copy Password','violet',self.copy_password),
                 ('Show All Records','purple',self.show_records),('Save Records to File', 'orange', self.save_records_to_file))
        
        for btn_info in buttons_info:
            if btn_info[0]=='Show All Records':
                self.row+=1
                self.col=0
            Button(self.curd_frame,text=btn_info[0],bg=btn_info[1],
              fg='white',font=('ariel',12),padx=1,pady=1,width=20,command=btn_info[2]).grid(padx=5,pady=10,row=self.row,column=self.col)
            self.col+=1
            
    def create_entry_boxes(self):
        self.entry_boxes=[]
        self.col=0
        self.row+=1
        for i in range(4):
            show=""
            if i == 3:
                show="*"
            entry_box=Entry(self.curd_frame,width=20,bg="lightgrey",font=("Ariel",12),show=show)
            entry_box.grid(row=self.row,column=self.col,padx=5,pady=2)
            self.col+=1
            self.entry_boxes.append(entry_box)
            
    #CURD Functions
    def save_record(self):
        website=self.entry_boxes[1].get()
        username=self.entry_boxes[2].get()
        password=self.entry_boxes[3].get()
        data={'website':website,'username':username,'password':password}
        self.db.create_record(data)
        
    def show_records(self):
        for item in self.records_tree.get_children():
            self.records_tree.delete(item)
        records_list=self.db.show_records()
        for record in records_list:
            self.records_tree.insert('',END,values=(record[0],record[3],[record[4]],record[5]))
        
    def update_record(self):
        ID=self.entry_boxes[0].get()
        website=self.entry_boxes[1].get()
        username=self.entry_boxes[2].get()
        password=self.entry_boxes[3].get()
        data={'ID':ID,'website':website,'username':username,'password':password}
        self.db.update_record(data)
        self.show_records()
        
    def delete_record(self):
        ID=self.entry_boxes[0].get()
        self.db.delete_record(ID)
        self.show_records() 
            
    def create_records_tree(self):
        columns=('ID','Website','Username','Password')
        self.records_tree=ttk.Treeview(self.root,columns=columns,show="headings")
        self.records_tree.grid()
        self.records_tree.heading('ID',text="ID")
        self.records_tree.heading('Website',text="Website_Name")
        self.records_tree.heading('Username',text="Username_Name")
        self.records_tree.heading('Password',text="Password")
        self.records_tree['displaycolumns']=('Website','Username')
        def item_selected(event):
            for selected_item in self.records_tree.selection():
                item=self.records_tree.item(selected_item)
                record=item['values']
                for entry_box,item in zip(self.entry_boxes,record):
                    entry_box.delete(0,END)
                    entry_box.insert(0,item)
        self.records_tree.bind('<<TreeviewSelect>>',item_selected)
        
    def copy_password(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.entry_boxes[3].get())
        message="Password Copied"
        title="Copy"
        if self.entry_boxes[3].get=="":
            message="Box is Empty"
            title="Error"
        self.showmessage(title,message) 
        
    def showmessage(self,title_box:str=None,message:str=None):
        TIME_TO_WAIT=900
        root=Toplevel(self.root)
        background='green'
        if title_box=='Error':
            background="red"
        root.geometry('200x30+600+200')
        root.title(title_box)
        Label(root,text=message,background=background,font=("Ariel",15),fg="white").pack(padx=4,pady=2)
        try:
            root.after(TIME_TO_WAIT,root.destroy)
        except Exception as e:
            print("Error occured",e) 
    def save_records_to_file(self):
        records_list = self.db.show_records()
        with open("password_records.txt", "w") as file:
            for record in records_list:
                file.write(f"ID: {record[0]}\n")
                file.write(f"Website: {record[3]}\n")
                file.write(f"Username: {record[4]}\n")
                file.write(f"Password: {record[5]}\n\n")
         
if __name__=="__main__":
    #create a table if not exists
    db_class=DbOperation()
    db_class.create_table()
    #create a tkinter window 
    root=Tk()
    root_window(root,db_class)
    root.mainloop()