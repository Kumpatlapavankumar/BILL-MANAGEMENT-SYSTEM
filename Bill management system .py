    from tkinter import *
    import math,random,os
    from tkinter import messagebox
    import tkinter as tk
    from tkinter import ttk
    from PIL import Image, ImageTk

    class Bill_App:
        def __init__(self,root):
            self.root=root
            self.root.geometry("15000x1000+0+0")
            self.root.title("Billing Software")
        
            #bg_color = "#9EA1D4"
            bg_color = "#DFEBEB"
            bg_color1="lightgrey"
            
            title=Label(self.root,text="Billing Software",bd=12,relief=GROOVE,bg=bg_color,fg="red",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
            
            #===========variables==========
            
            #==========cosmetics===========
            self.soap=IntVar()
            self.face_cream=IntVar()
            self.face_wash=IntVar()
            self.spray=IntVar()
            self.gell=IntVar()
            self.loshan=IntVar()
            self.hair_wax=IntVar()
            self.room_fresh=IntVar()
            
            #==========grocery===========
            self.rice=IntVar()
            self.food_oil=IntVar()
            self.daal=IntVar()
            self.wheat=IntVar()
            self.sugar=IntVar()
            self.tea=IntVar()
            self.peanut_butter=IntVar()
            self.spices=IntVar()
            
            #==========cold drinks===========
            self.maza=IntVar()
            self.cock=IntVar()
            self.frooti=IntVar()
            self.thumbsup=IntVar()
            self.limca=IntVar()
            self.sprite=IntVar()
            self.red_bull=IntVar()
            self.mountain_dew=IntVar()
            
            #==========total product price & tax variable===========
            self.cosmetic_price=StringVar()
            self.grocery_price=StringVar()
            self.cold_drink_price=StringVar()
            
            self.cosmetic_tax=StringVar()
            self.grocery_tax=StringVar()
            self.cold_drink_tax=StringVar()
            
            #================customer============
            self.c_name=StringVar()
            self.c_phon=StringVar()
            
            self.bill_no=StringVar()
            x=random.randint(1000,9999)
            self.bill_no.set(str(x))
            
            self.search_bill=StringVar()
            
            #==========================customer details frame
            F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details",font=("times new roman",15,"bold"),fg="red",bg=bg_color)
            F1.place(x=0,y=80,relwidth=2)
            
            #==========mistake
            #cname_lbl=Label(F1,text="Customer Name",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
            #cname_txt=Entry(F1,width=15,textvariable=self.c_name.font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=5,pady=10)
            
            cphn_lbl=Label(F1,text="Customer Name",bg=bg_color,fg="black",font=("Impact",18)).grid(row=0,column=0,padx=20,pady=5)
            cphn_txt=Entry(F1,width=15,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=2,padx=5,pady=10)
            
            cphn_lbl=Label(F1,text="Phone No.",bg=bg_color,fg="black",font=("Impact",18)).grid(row=0,column=4,padx=20,pady=5)
            cphn_txt=Entry(F1,width=15,textvariable=self.c_phon,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,padx=5,pady=10)
            
            c_bill_lbl=Label(F1,text="Bill NO",bg=bg_color,fg="black",font=("Impact",18)).grid(row=0,column=7,padx=20,pady=5)
            c_bill_txt=Entry(F1,width=15,textvariable=self.search_bill,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=8,padx=5,pady=10)
            
            bill_btn=Button(F1,text="search",command=self.find_bill,width=10,bd=7,font="arial 12 bold").grid(row=0,column=10,padx=10,pady=10)
            
            #==================cosmetics frame=============
            F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cosmetics",font=("times new roman",15,"bold"),fg="red",bg=bg_color)
            F2.place(x=5,y=180,width=330,height=500)
            
            bath_lbl=Label(F2,text="Bath soap",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=0,column=0,padx=10,pady=10,sticky="w")
            bath_txt=Entry(F2,width=10,textvariable=self.soap,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
            
            Face_cream_lbl=Label(F2,text="Face Cream",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=1,column=0,padx=10,pady=10,sticky="w")
            Face_cream_txt=Entry(F2,width=10,textvariable=self.face_cream,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)
            
            Face_w_lbl=Label(F2,text="Face Wash",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=2,column=0,padx=10,pady=10,sticky="w")
            Face_w_txt=Entry(F2,width=10,textvariable=self.face_wash,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)
            
            
            Hair_s_lbl=Label(F2,text="Hair Spray",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=3,column=0,padx=10,pady=10,sticky="w")
            Hair_s_txt=Entry(F2,width=10,textvariable=self.spray,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)
            
            Hair_g_lbl=Label(F2,text="Hair Gell",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=4,column=0,padx=10,pady=10,sticky="w")
            Hair_g_txt=Entry(F2,width=10,textvariable=self.gell,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)
            
            Body_lbl=Label(F2,text="Body Loshan",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=5,column=0,padx=10,pady=10,sticky="w")
            Body_txt=Entry(F2,width=10,textvariable=self.loshan,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)
            
            Hair_wax_lbl=Label(F2,text="Hair Wax",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=6,column=0,padx=10,pady=10,sticky="w")
            Hair_wax_txt=Entry(F2,width=10,textvariable=self.hair_wax,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=6,column=1,padx=10,pady=10)
            
            Room_lbl=Label(F2,text="Room Freshener",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=7,column=0,padx=10,pady=10,sticky="w")
            Room_txt=Entry(F2,width=10,textvariable=self.room_fresh,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=7,column=1,padx=10,pady=10)
            
            
            #==================Grocery frame=============
            F3=LabelFrame(self.root,bd=10,relief=GROOVE,text="Grocery",font=("times new roman",15,"bold"),fg="red",bg=bg_color)
            F3.place(x=340,y=180,width=325,height=500)
            
            g1_lbl=Label(F3,text="Rice",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=0,column=0,padx=10,pady=10,sticky="w")
            g1_txt=Entry(F3,width=10,textvariable=self.rice,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
            
            g2_lbl=Label(F3,text="Food Oil",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=1,column=0,padx=10,pady=10,sticky="w")
            g2_txt=Entry(F3,width=10,textvariable=self.food_oil,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)
            
            g3_lbl=Label(F3,text="Daal",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=2,column=0,padx=10,pady=10,sticky="w")
            g3_txt=Entry(F3,width=10,textvariable=self.daal,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)
            
            
            g4_lbl=Label(F3,text="Wheat",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=3,column=0,padx=10,pady=10,sticky="w")
            g4_txt=Entry(F3,width=10,textvariable=self.wheat,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)
            
            g5_lbl=Label(F3,text="Sugar",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=4,column=0,padx=10,pady=10,sticky="w")
            g5_txt=Entry(F3,width=10,textvariable=self.sugar,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)
            
            g6_lbl=Label(F3,text="Tea",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=5,column=0,padx=10,pady=10,sticky="w")
            g6_txt=Entry(F3,width=10,textvariable=self.tea,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)
            
            g7_lbl=Label(F3,text="Peanut butter",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=6,column=0,padx=10,pady=10,sticky="w")
            g7_txt=Entry(F3,width=10,textvariable=self.peanut_butter,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=6,column=1,padx=10,pady=10)
            
            g8_lbl=Label(F3,text="spices",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=7,column=0,padx=10,pady=10,sticky="w")
            g8_txt=Entry(F3,width=10,textvariable=self.spices,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=7,column=1,padx=10,pady=10)
            
            #==================Cold Drinks Frame=============
            F4=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cold Drinks",font=("times new roman",15,"bold"),fg="red",bg=bg_color)
            F4.place(x=670,y=180,width=325,height=500)
            
            c1_lbl=Label(F4,text="Maaza",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=0,column=0,padx=10,pady=10,sticky="w")
            c1_txt=Entry(F4,width=10,textvariable=self.maza,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
        
            c2_lbl=Label(F4,text="Coke",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=1,column=0,padx=10,pady=10,sticky="w")
            c2_txt=Entry(F4,width=10,textvariable=self.cock,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)
            
            c3_lbl=Label(F4,text="Frooti",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=2,column=0,padx=10,pady=10,sticky="w")
            c3_txt=Entry(F4,width=10,textvariable=self.frooti,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)
            
            
            c4_lbl=Label(F4,text="Thumbs Up",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=3,column=0,padx=10,pady=10,sticky="w")
            c4_txt=Entry(F4,width=10,textvariable=self.thumbsup,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)
            
            c5_lbl=Label(F4,text="Limca",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=4,column=0,padx=10,pady=10,sticky="w")
            c5_txt=Entry(F4,width=10,textvariable=self.limca,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)
            
            c6_lbl=Label(F4,text="Sprite",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=5,column=0,padx=10,pady=10,sticky="w")
            c6_txt=Entry(F4,width=10,textvariable=self.sprite,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)
            
            c7_lbl=Label(F4,text="Red Bull",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=6,column=0,padx=10,pady=10,sticky="w")
            c7_txt=Entry(F4,width=10,textvariable=self.red_bull,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=6,column=1,padx=10,pady=10)
            
            c8_lbl=Label(F4,text="Mountain Dew",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=7,column=0,padx=10,pady=10,sticky="w")
            c8_txt=Entry(F4,width=10,textvariable=self.mountain_dew,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=7,column=1,padx=10,pady=10)
            
            #============Bill Area=============
            F5=Frame(self.root,bd=10,relief=GROOVE)
            F5.place(x=1010,y=180,width=500,height=500)
            bill_title=Label(F5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
            scrol_y=Scrollbar(F5,orient=VERTICAL)
            self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
            scrol_y.pack(sid=RIGHT,fill=Y)
            scrol_y.config(command=self.txtarea.yview)
            self.txtarea.pack(fill=BOTH,expand=1)
            
            #============ButtonFrame========
            F6=LabelFrame(self.root,bd=10,relief=GROOVE,text="Bill Menu",font=("times new roman",15,"bold"),fg="red",bg=bg_color)
            F6.place(x=0,y=680,relwidth=1,height=140)
            
            m1_lbl=Label(F6,text="Total Cosmetic Price",bg=bg_color,fg="black",font=("Arial Baltic",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
            m1_txt=Entry(F6,width=18,textvariable=self.cosmetic_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)
            
            m2_lbl=Label(F6,text="Total Grocery Price",bg=bg_color,fg="black",font=("Arial Baltic",14,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
            m2_txt=Entry(F6,width=18,textvariable=self.grocery_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)
            
            m3_lbl=Label(F6,text="Total Cold Drinks Price",bg=bg_color,fg="black",font=("Arial Baltic",14,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
            m3_txt=Entry(F6,width=18,textvariable=self.cold_drink_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)
            
            c1_lbl=Label(F6,text="Cosmetic Tax",bg=bg_color,fg="black",font=("Arial Baltic",14,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")
            c1_txt=Entry(F6,width=18,textvariable=self.cosmetic_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)
            
            c2_lbl=Label(F6,text="Grocery Tax",bg=bg_color,fg="black",font=("Arial Baltic",14,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky="w")
            c2_txt=Entry(F6,width=18,textvariable=self.grocery_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)
            
            c3_lbl=Label(F6,text="Cold Drinks Tax",bg=bg_color,fg="black",font=("Arial Baltic",14,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky="w")
            c3_txt=Entry(F6,width=18,textvariable=self.cold_drink_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)
            
            btn_F=Frame(F6,bd=7,relief=GROOVE)
            btn_F.place(x=780,width=730,height=105)
            
            total_btn=Button(btn_F,command=self.total,text="Total",bg=bg_color1,fg="red",bd=2,pady=15,width=10,font="arial 15 bold").grid(row=0,column=0,padx=5,pady=5)
            
            GBill_btn=Button(btn_F,text="Genrate Bill",command=self.bill_area,bg=bg_color1,fg="red",bd=2,pady=15,width=10,font="arial 15 bold").grid(row=0,column=1,padx=5,pady=5)
                
            Clear_btn=Button(btn_F,text="Clear",command=self.clear_data,bg=bg_color1,fg="red",bd=2,pady=15,width=10,font="arial 15 bold").grid(row=0,column=3,padx=5,pady=5)
            
            Exit_btn=Button(btn_F,text="Exit",command=self.Exit_app,bg=bg_color1,fg="red",bd=2,pady=15,width=10,font="arial 15 bold").grid(row=0,column=4,padx=5,pady=5)
            
            Save_btn=Button(btn_F,text="Pay Now",command=self.payment,bg=bg_color1,fg="red",bd=2,pady=15,width=10,font="arial 15 bold").grid(row=0,column=2,padx=5,pady=5)
            
            self.welcome_bill();
        def total(self):
            
            self.c_s_p=self.soap.get()*40
            self.c_fc_p=self.face_cream.get()*120
            self.c_fw_p=self.face_wash.get()*60
            self.c_hs_p=self.spray.get()*180
            self.c_hg_p=self.gell.get()*140
            self.c_bl_p=self.loshan.get()*80
            self.c_hw_p=self.hair_wax.get()*276
            self.c_rf_p=self.room_fresh.get()*84
            
            self.total_cosmetic_price=float(
                                            self.c_s_p+
                                            self.c_fc_p+
                                            self.c_fw_p+
                                            self.c_hs_p+
                                            self.c_hg_p+
                                            self.c_bl_p+
                                            self.c_hw_p+
                                            self.c_rf_p
            
                                        )
            self.cosmetic_price.set("Rs. "+str(self.total_cosmetic_price))
            self.c_tax=round((self.total_cosmetic_price*0.05),2)
            self.cosmetic_tax.set("Rs. "+str(self.c_tax))
            
            self.g_r_p=self.rice.get()*40
            self.g_f_p=self.food_oil.get()*180
            self.g_d_p=self.daal.get()*60
            self.g_w_p=self.wheat.get()*240
            self.g_s_p=self.sugar.get()*45
            self.g_t_p=self.tea.get()*150
            self.g_p_p=self.peanut_butter.get()*300
            self.g_sp_p=self.spices.get()*80
            
            self.total_grocery_price=float(
                                            self.g_r_p+
                                            self.g_f_p+
                                            self.g_d_p+
                                            self.g_w_p+
                                            self.g_s_p+
                                            self.g_t_p+
                                            self.g_p_p+
                                            self.g_sp_p
            
                                        )
            self.grocery_price.set("Rs. "+str(self.total_grocery_price))
            self.g_tax=round((self.total_grocery_price*0.1),2)
            self.grocery_tax.set("Rs. "+str(self.g_tax))
            
            self.d_m_p=self.maza.get()*60
            self.d_c_p=self.cock.get()*60
            self.d_f_p=self.frooti.get()*50
            self.d_t_p=self.thumbsup.get()*45
            self.d_l_p=self.limca.get()*40
            self.d_s_p=self.sprite.get()*60
            self.d_r_p=self.red_bull.get()*120
            self.d_md_p=self.mountain_dew.get()*60
            
            self.total_cold_drink_price=float(
                                            self.d_m_p+
                                            self.d_c_p+
                                            self.d_f_p+
                                            self.d_t_p+
                                            self.d_l_p+
                                            self.d_s_p+
                                            self.d_r_p+
                                            self.d_md_p
            
                                        )
            self.cold_drink_price.set("Rs. "+str(self.total_cold_drink_price))
            self.d_tax=round((self.total_cold_drink_price*0.05),2)
            self.cold_drink_tax.set("Rs. "+str(self.d_tax))
            
            self.Total_bill=float(self.total_cosmetic_price+
                                self.total_grocery_price+
                                self.total_cold_drink_price+
                                self.c_tax+
                                self.g_tax+
                                self.d_tax)
        def welcome_bill(self):
            self.txtarea.delete("1.0",END)
            font_size=("Helvetica",16)
            self.txtarea.insert(END,"\t\tWelcome Webcode Reatil\n","header")
            self.txtarea.insert(END,f"\nBill Number\t:\t\t{self.bill_no.get()}","body")
            self.txtarea.insert(END,f"\n\nCustomer Name\t:\t\t{self.c_name.get()}","hello")
            self.txtarea.insert(END,f"\n\nPhone Number\t:\t\t{self.c_phon.get()}","hell")
            self.txtarea.insert(END,f"\n=======================================================")
            self.txtarea.insert(END,f"\n Products\t\t\tQTY\t\t\tPrice","y")
            self.txtarea.insert(END,f"\n=======================================================")
            self.txtarea.tag_config("header",font=("Impact",16))
            self.txtarea.tag_config("body",font=("Comic Sans MS",16))
            self.txtarea.tag_config("hello",font=("Comic Sans MS",16))
            self.txtarea.tag_config("hell",font=("Comic Sans MS",16))
            self.txtarea.tag_config("y",font=("Impact",16))
        def bill_area(self):
            
            if self.c_name.get()=="" or self.c_phon.get()=="":
                messagebox.showerror("Error","Customer details are must")
            elif self.cosmetic_price.get()=="Rs. 0.0" and self.grocery_price.get()=="Rs. 0.0" and self.cold_drink_price.get()=="Rs. 0.0":
                messagebox.showerror("Error","No Product purchased")
            else:
                self.welcome_bill()

                #===============cosmetics
                if self.soap.get()!=0:
                    self.txtarea.insert(END,f"\n Bath Soap\t\t\t{self.soap.get()}\t\t\t{self.c_s_p}","soap")
                if self.face_cream.get()!=0:
                    self.txtarea.insert(END,f"\n Face Cream\t\t\t{self.face_cream.get()}\t\t\t{self.c_fc_p}","face")
                if self.face_wash.get()!=0:
                    self.txtarea.insert(END,f"\n Face Wash\t\t\t{self.face_wash.get()}\t\t\t{self.c_fw_p}","facewash")
                if self.spray.get()!=0:
                    self.txtarea.insert(END,f"\n Spray\t\t\t{self.spray.get()}\t\t\t{self.c_hs_p}","spray")
                if self.gell.get()!=0:
                    self.txtarea.insert(END,f"\n Hair Gell\t\t\t{self.gell.get()}\t\t\t{self.c_hg_p}","gell")
                if self.loshan.get()!=0:
                    self.txtarea.insert(END,f"\n Body Loshan\t\t\t{self.loshan.get()}\t\t\t{self.c_bl_p}","loshan")
                if self.hair_wax.get()!=0:
                    self.txtarea.insert(END,f"\n Hair Wax\t\t\t{self.hair_wax.get()}\t\t\t{self.c_hw_p}","wax")
                if self.room_fresh.get()!=0:
                    self.txtarea.insert(END,f"\n Room Freshner\t\t\t{self.room_fresh.get()}\t\t\t{self.c_rf_p}","freshner")
                
                
                font_size=("Courier New",12)
                self.txtarea.tag_config("soap",font=font_size)
                self.txtarea.tag_config("face",font=font_size)
                self.txtarea.tag_config("facewash",font=font_size)
                self.txtarea.tag_config("spray",font=font_size)
                self.txtarea.tag_config("gell",font=font_size)
                self.txtarea.tag_config("loshan",font=font_size)
                self.txtarea.tag_config("wax",font=font_size)
                self.txtarea.tag_config("freshner",font=font_size)

                #===============groceery
                if self.rice.get()!=0:
                    self.txtarea.insert(END,f"\n Rice\t\t\t{self.rice.get()}\t\t\t{self.g_r_p}","rice")
                if self.food_oil.get()!=0:
                    self.txtarea.insert(END,f"\n Food Oil\t\t\t{self.food_oil.get()}\t\t\t{self.g_f_p}","food_oil")
                if self.daal.get()!=0:
                    self.txtarea.insert(END,f"\n Daal\t\t\t{self.daal.get()}\t\t\t{self.g_d_p}","daal")
                if self.wheat.get()!=0:
                    self.txtarea.insert(END,f"\n Wheat\t\t\t{self.wheat.get()}\t\t\t{self.g_w_p}","wheat")
                if self.sugar.get()!=0:
                    self.txtarea.insert(END,f"\n Sugar\t\t\t{self.sugar.get()}\t\t\t{self.g_s_p}","sugar")
                if self.tea.get()!=0:
                    self.txtarea.insert(END,f"\n Tea\t\t\t{self.tea.get()}\t\t\t{self.g_t_p}","tea")
                if self.peanut_butter.get()!=0:
                    self.txtarea.insert(END,f"\n Peanut Butter\t\t\t{self.peanut_butter.get()}\t\t\t{self.g_p_p}","peanut_butter")
                if self.spices.get()!=0:
                    self.txtarea.insert(END,f"\n Spices\t\t\t{self.spices.get()}\t\t\t{self.g_sp_p}","spices")
                    
                font_size=("Courier New",12)
                self.txtarea.tag_config("rice",font=font_size)
                self.txtarea.tag_config("food_oil",font=font_size)
                self.txtarea.tag_config("daal",font=font_size)
                self.txtarea.tag_config("wheat",font=font_size)
                self.txtarea.tag_config("sugar",font=font_size)
                self.txtarea.tag_config("tea",font=font_size)
                self.txtarea.tag_config("peanut_butter",font=font_size)
                self.txtarea.tag_config("spices",font=font_size)
                

                #===============cold drinks
                if self.maza.get()!=0:
                    self.txtarea.insert(END,f"\n Maza\t\t\t{self.maza.get()}\t\t\t{self.d_m_p}","maza")
                if self.cock.get()!=0:
                    self.txtarea.insert(END,f"\n Cock\t\t\t{self.cock.get()}\t\t\t{self.d_c_p}","cock")
                if self.frooti.get()!=0:
                    self.txtarea.insert(END,f"\n Frooti\t\t\t{self.frooti.get()}\t\t\t{self.d_f_p}","frooti")
                if self.thumbsup.get()!=0:
                    self.txtarea.insert(END,f"\n Thumbs Up\t\t\t{self.thumbsup.get()}\t\t\t{self.d_t_p}","thumbsup")
                if self.limca.get()!=0:
                    self.txtarea.insert(END,f"\n Limca\t\t\t{self.limca.get()}\t\t\t{self.d_l_p}","limca")
                if self.sprite.get()!=0:
                    self.txtarea.insert(END,f"\n Sprite\t\t\t{self.sprite.get()}\t\t\t{self.d_s_p}","sprite")
                if self.red_bull.get()!=0:
                    self.txtarea.insert(END,f"\n Red Bull\t\t\t{self.sprite.get()}\t\t\t{self.d_r_p}","redbull")
                if self.mountain_dew.get()!=0:
                    self.txtarea.insert(END,f"\n Mountain Dew\t\t\t{self.mountain_dew.get()}\t\t\t{self.d_md_p}","mountain")
                
                font_size=("Courier New",12)
                self.txtarea.tag_config("maza",font=font_size)
                self.txtarea.tag_config("cock",font=font_size)
                self.txtarea.tag_config("frooti",font=font_size)
                self.txtarea.tag_config("thumbsup",font=font_size)
                self.txtarea.tag_config("limca",font=font_size)
                self.txtarea.tag_config("sprite",font=font_size)
                self.txtarea.tag_config("redbull",font=font_size)
                self.txtarea.tag_config("mountain",font=font_size)

                self.txtarea.insert(END,f"\n--------------------------------------------------------")
                if self.cosmetic_tax.get()!="Rs. 0.0":
                    self.txtarea.insert(END,f"\n Cosmetic Tax\t\t\t\t\t{self.cosmetic_tax.get()}","c_tax")
                if self.grocery_tax.get()!="Rs. 0.0":
                    self.txtarea.insert(END,f"\n Grocery Tax\t\t\t\t\t{self.grocery_tax.get()}","g_tax")
                if self.cold_drink_tax.get()!="Rs. 0.0":
                    self.txtarea.insert(END,f"\n Cold Drink Tax\t\t\t\t\t{self.cold_drink_tax.get()}","cd_tax")
                self.txtarea.insert(END,f"\n---------------------------------------------------------")
                self.txtarea.insert(END,f"\n Total Bill  \t\t\t\t\tRs. {self.Total_bill}","t_tax")
                self.txtarea.insert(END,f"\n---------------------------------------------------------")
                
                font_size=("Garamond",16)
                self.txtarea.tag_config("c_tax",font=("Garamond",16))
                self.txtarea.tag_config("g_tax",font=font_size)
                self.txtarea.tag_config("cd_tax",font=font_size)
                self.txtarea.tag_config("t_tax",font=("Futura",16))
                
                self.save_bill()
        def  save_bill(self):
            #if self.c_name.get()=="" or self.c_phon.get()=="":
                #messagebox.showerror("Error","Customer details are must")
            #elif self.cosmetic_price.get()=="Rs. 0.0" and self.grocery_price.get()=="Rs. 0.0" and self.cold_drink_price.get()=="Rs. 0.0":
                #messagebox.showerror("Error","No Product purchased")
            #else:
            op=messagebox.askyesno("Save Bill","Do you Want to save the Bill?")
            if op>0:
                self.bill_data=self.txtarea.get('1.0',END)
                f1=open("E:\Bills/"+str(self.bill_no.get())+".txt","w")
                f1.write(self.bill_data)
                f1.close()
                messagebox.showinfo("Saved",f"Bill no :{self.bill_no.get()} saved succesfully")
            else:
                return 
        def find_bill(self):
            present="no"
            
            for i in os.listdir("E:\Bills/"):
                if i.split('.')[0]==self.search_bill.get():
                    f1=open(f"E:\Bills/{i}","r")
                    self.txtarea.delete('1.0',END)
                    for d in f1:
                        self.txtarea.insert(END,d)
                    f1.close()
                    present="yes"    
            if present=="no":
                    messagebox.showerror("Error","Invalid Bill No");
        def clear_data(self):
            op=messagebox.askyesno("clear","Do you really want to clear?")
            if op>0:
                #==========cosmetics===========
                self.soap.set(0)
                self.face_cream.set(0)
                self.face_wash.set(0)
                self.spray.set(0)
                self.gell.set(0)
                self.loshan.set(0)
                self.hair_wax.set(0)
                self.room_fresh.set(0)

                #==========grocery===========
                self.rice.set(0)
                self.food_oil.set(0)
                self.daal.set(0)
                self.wheat.set(0)
                self.sugar.set(0)
                self.tea.set(0)
                self.peanut_butter.set(0)
                self.spices.set(0)

                #==========cold drinks===========
                self.maza.set(0)
                self.cock.set(0)
                self.frooti.set(0)
                self.thumbsup.set(0)
                self.limca.set(0)
                self.sprite.set(0)
                self.red_bull.set(0)
                self.mountain_dew.set(0)

                #==========total product price & tax variable===========
                self.cosmetic_price.set("")
                self.grocery_price.set("")
                self.cold_drink_price.set("")

                self.cosmetic_tax.set("")
                self.grocery_tax.set("")
                self.cold_drink_tax.set("")

                #================customer============
                self.c_name.set("")
                self.c_phon.set("")
                self.bill_no.set("")
                x=random.randint(1000,9999)
                self.bill_no.set(str(x))
                self.search_bill.set("")
                self.welcome_bill()
        def Exit_app(self):
            op=messagebox.askyesno("Exit","Do you really want to exit?")
            if op>0:
                self.root.destroy()
        def payment(self):
            if self.c_name.get()=="" or self.c_phon.get()=="":
                messagebox.showerror("Error","Customer details are must")
            elif self.cosmetic_price.get()=="Rs. 0.0" and self.grocery_price.get()=="Rs. 0.0" and self.cold_drink_price.get()=="Rs. 0.0":
                messagebox.showerror("Error","No Product purchased")
            else:

                def show_payment_interface(payment_method):
                    for frame in payment_frames.values():
                        frame.grid_remove()

                    payment_frames[payment_method].grid(row=3, column=0, columnspan=2)

                def process_payment():
                     # Show an error message for maintenance
                    messagebox.showinfo("Error", "Under maintenance")

                    selected_payment_method = payment_var.get()

                    if selected_payment_method == "Scanner":
                        display_scanner_image()
                    else:
                        handle_other_payment_methods(selected_payment_method)

                def display_scanner_image():
                    scanner_image = Image.open("E:\scanner_image.jpg")
                    scanner_image = scanner_image.resize((300, 300), Image.ANTIALIAS)
                    scanner_image_tk = ImageTk.PhotoImage(scanner_image)

                    scanner_image_label = ttk.Label(payment_frames["Scanner"], image=scanner_image_tk)
                    scanner_image_label.image = scanner_image_tk
                    scanner_image_label.pack(pady=20)

                def handle_other_payment_methods(payment_method):
                    if payment_method == "Debit Card":
                        card_number = card_number_entry.get()
                        card_name = card_name_entry.get()
                        card_cvv = card_cvv_entry.get()
                        card_result.set(f"Processing payment using {payment_method}\nCard Number: {card_number}\nCard Holder: {card_name}\nCVV: {card_cvv}")
                    else:
                        phone_number = phone_entry.get()
                        name = name_entry.get()
                        payment_result.set(f"Processing payment using {payment_method}\nPhone Number: {phone_number}\nName: {name}")

                root = tk.Tk()
                root.title("Payment Page")
                root.geometry("1500x1000+0+0")  # Set the window size and position
                root.configure(bg="#DFEBEB")

                center_frame = ttk.Frame(root)
                center_frame.pack(expand=True)

                # Payment method selection frame
                selection_frame = ttk.Frame(center_frame, padding=20)
                selection_frame.grid(row=0, column=0, columnspan=2)

                ttk.Label(selection_frame, text="Select Payment Method", font=("Helvetica", 18), foreground="black", background="white").grid(row=0, column=0, columnspan=2, pady=10)

                payment_var = tk.StringVar()
                payment_options = ["Scanner", "PhonePe", "Google Pay", "Paytm", "Debit Card"]

                for i, option in enumerate(payment_options):
                    payment_button = tk.Radiobutton(selection_frame, text=option, variable=payment_var, value=option, font=("Helvetica", 14),
                                                     foreground="black", background="white", selectcolor="#D8E7E3", command=lambda opt=option: show_payment_interface(opt))
                    payment_button.grid(row=i+1, column=0, columnspan=2, pady=5)

                # Payment frames
                payment_frames = {}
                for payment_method in payment_options:
                    payment_frames[payment_method] = ttk.Frame(center_frame, padding=20)
                    payment_frames[payment_method].grid(row=3, column=0, columnspan=2)

                    ttk.Label(payment_frames[payment_method], text=f"{payment_method} Payment Interface", font=("Helvetica", 18), foreground="black", background="white").pack(pady=10)
                    ttk.Button(payment_frames[payment_method], text="Pay Now", command=process_payment, style="TButton").pack(pady=20)

                # PhonePe payment frame
                phone_frame = payment_frames["PhonePe"]

                ttk.Label(phone_frame, text="Enter Phone Number:", font=("Helvetica", 14), foreground="black", background="white").pack(pady=10)
                phone_entry = ttk.Entry(phone_frame, font=("Helvetica", 18))  # Adjust font size
                phone_entry.pack(pady=10)

                ttk.Label(phone_frame, text="Enter Name:", font=("Helvetica", 14), foreground="black", background="white").pack(pady=10)
                name_entry = ttk.Entry(phone_frame, font=("Helvetica",18))  # Adjust font size
                name_entry.pack(pady=10)

                # Google Pay payment frame
                googlepay_frame = payment_frames["Google Pay"]

                ttk.Label(googlepay_frame, text="Enter Phone Number:", font=("Helvetica", 14), foreground="black", background="white").pack(pady=10)
                googlepay_phone_entry = ttk.Entry(googlepay_frame, font=("Helvetica", 18))  # Adjust font size
                googlepay_phone_entry.pack(pady=10)

                ttk.Label(googlepay_frame, text="Enter Name:", font=("Helvetica", 14), foreground="black", background="white").pack(pady=10)
                googlepay_name_entry = ttk.Entry(googlepay_frame, font=("Helvetica", 18))  # Adjust font size
                googlepay_name_entry.pack(pady=10)

                # Paytm payment frame
                paytm_frame = payment_frames["Paytm"]

                ttk.Label(paytm_frame, text="Enter Phone Number:", font=("Helvetica", 14), foreground="black", background="white").pack(pady=10)
                paytm_phone_entry = ttk.Entry(paytm_frame, font=("Helvetica", 18))  # Adjust font size
                paytm_phone_entry.pack(pady=10)

                ttk.Label(paytm_frame, text="Enter Name:", font=("Helvetica", 14), foreground="black", background="white").pack(pady=10)
                paytm_name_entry = ttk.Entry(paytm_frame, font=("Helvetica", 18))  # Adjust font size
                paytm_name_entry.pack(pady=10)

                # Debit Card payment frame
                debit_card_frame = payment_frames["Debit Card"]

                ttk.Label(debit_card_frame, text="Enter Card Number:", font=("Helvetica", 14), foreground="black", background="white").pack(pady=10)
                card_number_entry = ttk.Entry(debit_card_frame, font=("Helvetica",18))  # Adjust font size
                card_number_entry.pack(pady=10)

                ttk.Label(debit_card_frame, text="Enter Card Holder's Name:", font=("Helvetica", 14), foreground="black", background="white").pack(pady=10)
                card_name_entry = ttk.Entry(debit_card_frame, font=("Helvetica", 18))  # Adjust font size
                card_name_entry.pack(pady=10)

                ttk.Label(debit_card_frame, text="Enter Expiry Date (MM/YY):", font=("Helvetica", 14), foreground="black", background="white").pack(pady=10)
                expiry_date_entry = ttk.Entry(debit_card_frame, font=("Helvetica", 18), width=7)  # Adjust font size
                expiry_date_entry.pack(pady=10)

                ttk.Label(debit_card_frame, text="Enter CVV:", font=("Helvetica", 14), foreground="black", background="white").pack(pady=10)
                card_cvv_entry = ttk.Entry(debit_card_frame, show="*", font=("Helvetica", 18), width=5)  # Adjust font size and width
                card_cvv_entry.pack(pady=10)

                show_payment_interface(payment_options[0])

                payment_result = tk.StringVar()
                payment_label = ttk.Label(center_frame, textvariable=payment_result, font=("Helvetica", 14), foreground="#354F52")
                payment_label.grid(row=4, column=0, columnspan=2, pady=20)
            
    root=Tk()
    obj=Bill_App(root)
    root.mainloop()
            
