from distutils.cmd import Command
from email import message
from pickle import FRAME
from struct import pack
from textwrap import fill
from tkinter import *
import math
import random
import os
from tkinter import messagebox


class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.title("BILLING SOFTWARE")
        self.root.geometry("1350x700+0+0")
        title = Label(self.root, text="Billing software", bd=2, relief=GROOVE, font=(
            "times new roman", 30, "bold"), pady=2).pack(fill=X)

        # =====================variables=============
    # ===================cosmetics==========
        self.soap = IntVar()
        self.facecream = IntVar()
        self.facewash = IntVar()
        self.hairspray = IntVar()
        self.hairgel = IntVar()
        self.bodywash = IntVar()
        # =================grocery===========
        self.beshan = IntVar()
        self.rice = IntVar()
        self.daal = IntVar()
        self.foodoil = IntVar()
        self.wheat = IntVar()
        self.rajma = IntVar()
        # =======colddrinks==============
        self.maza = IntVar()
        self.coke = IntVar()
        self.pepsi = IntVar()
        self.dew = IntVar()
        self.slice = IntVar()
        self.sting = IntVar()
        # ===============Total product price and tax variables=====
        self.cosmetic_price = StringVar()
        self.grocery_price = StringVar()
        self.cold_drink_price = StringVar()

        self.cosmetic_tax = StringVar()
        self.grocery_tax = StringVar()
        self.cold_drink_tax = StringVar()

        # ======customer=======
        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill = StringVar()


# =====customer details=========
        F1 = LabelFrame(self.root, bd=10, text="Customer details", font=(
            "times new roman", 15, "bold"), fg="yellow", bg="black")
        F1.place(x=0, y=60, relwidth=1)

        cname_lb1 = Label(F1, text="Customer Name", font=(
            "times new roman", 18, "bold"), bg="black", fg="white").grid(row=0, column=0, padx=20, pady=5)
        cname_txt = Entry(F1, width=15, textvariable=self.c_name, font="arial 15", bd=7, relief=SUNKEN).grid(
            row=0, column=1, pady=5, padx=10)

        cphone_lb1 = Label(F1, text=" Phone N0.", font=("times new roman", 18, "bold"), bg="black", fg="white").grid(
            row=0, column=2, padx=20, pady=5)
        cphone_txt = Entry(F1, width=15, textvariable=self.c_phone, font="arial 15", bd=7, relief=SUNKEN).grid(
            row=0, column=3, pady=5, padx=10)

        cbill_lb1 = Label(F1, text="Bill Number", font=("times new roman", 18, "bold"), bg="black", fg="white").grid(
            row=0, column=4, padx=20, pady=5)
        cbill_txt = Entry(F1, width=15, textvariable=self.bill_no, font="arial 15", bd=7, relief=SUNKEN).grid(
            row=0, column=5, pady=5, padx=10)

        bill_btn = Button(F1, text="Search", width=10, bd=7, font=(
            "arial", 12, "bold")).grid(row=0, column=20, padx=30, pady=10)
       # ==============cosmetics Frames==============
        F2 = LabelFrame(self.root, bd=10, text="Cosmetics", font=(
            "times new roman", 15, "bold"), fg="yellow", bg="black")
        F2.place(x=5, y=170, width=325, height=380)

        bath_lb1 = Label(F2, text="bath soap", font=(
            "times new roman", 18, "bold"), bg="black", fg="white").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        bath_txt = Entry(F2, width=10, textvariable=self.soap, font="arial 15", bd=7, relief=SUNKEN).grid(
            row=0, column=1, pady=10, padx=10)

        facecream_lb2 = Label(F2, text="facecream", font=(
            "times new roman", 18, "bold"), bg="black", fg="white").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        facecream_txt = Entry(F2, width=10, textvariable=self.facecream, font="arial 15", bd=7, relief=SUNKEN).grid(
            row=1, column=1, pady=10, padx=10)

        facewash_lb1 = Label(F2, text="fashwash", font=(
            "times new roman", 18, "bold"), bg="black", fg="white").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        facewash_txt = Entry(F2, width=10, textvariable=self.facewash, font="arial 15", bd=7, relief=SUNKEN).grid(
            row=2, column=1, pady=10, padx=10)

        hair_s_lb1 = Label(F2, text="hair spray", font=(
            "times new roman", 18, "bold"), bg="black", fg="white").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        hair_s_txt = Entry(F2, width=10, textvariable=self.hairspray, font="arial 15", bd=7, relief=SUNKEN).grid(
            row=3, column=1, pady=10, padx=10)

        hair_g_lb1 = Label(F2, text="hair gel", font=(
            "times new roman", 18, "bold"), bg="black", fg="white").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        hair_g_txt = Entry(F2, width=10, textvariable=self.hairgel, font="arial 15", bd=7, relief=SUNKEN).grid(
            row=4, column=1, pady=10, padx=10)

        body_lb1 = Label(F2, text="body wash", font=(
            "times new roman", 18, "bold"), bg="black", fg="white").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        body_txt = Entry(F2, width=10, textvariable=self.bodywash, font="arial 15", bd=7, relief=SUNKEN).grid(
            row=5, column=1, pady=10, padx=10)

        # ==============grocery Frames==============
        F3 = LabelFrame(self.root, bd=10, text="grocery items", font=(
            "times new roman", 15, "bold"), fg="yellow", bg="black")
        F3.place(x=370, y=170, width=325, height=380)

        g1_lb1 = Label(F3, text="beshan", font=(
            "times new roman", 18, "bold"), bg="black", fg="white").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        g1_txt = Entry(F3, width=10, textvariable=self.beshan, font="arial 15", bd=7, relief=SUNKEN).grid(
            row=0, column=1, pady=10, padx=10)

        g2_lb2 = Label(F3, text="rice", font=(
            "times new roman", 18, "bold"), bg="black", fg="white").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        g2_txt = Entry(F3, width=10, textvariable=self.rice, font="arial 15", bd=7, relief=SUNKEN).grid(
            row=1, column=1, pady=10, padx=10)

        g3_lb1 = Label(F3, text="daal", font=(
            "times new roman", 18, "bold"), bg="black", fg="white").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        g3_txt = Entry(F3, width=10, textvariable=self.daal, font="arial 15", bd=7, relief=SUNKEN).grid(
            row=2, column=1, pady=10, padx=10)

        g4_s_lb1 = Label(F3, text="food oil", font=(
            "times new roman", 18, "bold"), bg="black", fg="white").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        g4_s_txt = Entry(F3, width=10, textvariable=self.foodoil, font="arial 15", bd=7, relief=SUNKEN).grid(
            row=3, column=1, pady=10, padx=10)

        g5_lb1 = Label(F3, text="wheat", font=(
            "times new roman", 18, "bold"), bg="black", fg="white").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        g5_txt = Entry(F3, width=10, textvariable=self.wheat, font="arial 15", bd=7, relief=SUNKEN).grid(
            row=4, column=1, pady=10, padx=10)

        g6_lb1 = Label(F3, text="rajma", font=(
            "times new roman", 18, "bold"), bg="black", fg="white").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        g6_txt = Entry(F3, width=10, textvariable=self.beshan, font="arial 15", bd=7, relief=SUNKEN).grid(
            row=5, column=1, pady=10, padx=10)

        # ==============colddrink Frames==============
        F4 = LabelFrame(self.root, bd=10, text="cold drinks", font=(
            "times new roman", 15, "bold"), fg="yellow", bg="black")
        F4.place(x=730, y=170, width=325, height=380)

        c1_lb1 = Label(F4, text="Maza", font=(
            "times new roman", 18, "bold"), bg="black", fg="white").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        c1_txt = Entry(F4, width=10, textvariable=self.maza, font="arial 15", bd=7, relief=SUNKEN).grid(
            row=0, column=1, pady=10, padx=10)

        c2_lb2 = Label(F4, text="coke", font=(
            "times new roman", 18, "bold"), bg="black", fg="white").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        c2_txt = Entry(F4, width=10, textvariable=self.coke, font="arial 15", bd=7, relief=SUNKEN).grid(
            row=1, column=1, pady=10, padx=10)

        c3_lb1 = Label(F4, text="pepsi", font=(
            "times new roman", 18, "bold"), bg="black", fg="white").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        c3_txt = Entry(F4, width=10, textvariable=self.pepsi, font="arial 15", bd=7, relief=SUNKEN).grid(
            row=2, column=1, pady=10, padx=10)

        c4_s_lb1 = Label(F4, text="dew", font=(
            "times new roman", 18, "bold"), bg="black", fg="white").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        c4_s_txt = Entry(F4, width=10, textvariable=self.dew, font="arial 15", bd=7, relief=SUNKEN).grid(
            row=3, column=1, pady=10, padx=10)

        c5_lb1 = Label(F4, text="slice", font=(
            "times new roman", 18, "bold"), bg="black", fg="white").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        c5_txt = Entry(F4, width=10, textvariable=self.slice, font="arial 15", bd=7, relief=SUNKEN).grid(
            row=4, column=1, pady=10, padx=10)

        c6_lb1 = Label(F4, text="sting ", font=(
            "times new roman", 18, "bold"), bg="black", fg="white").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        c6_txt = Entry(F4, width=10, textvariable=self.sting, font="arial 15", bd=7, relief=SUNKEN).grid(
            row=5, column=1, pady=10, padx=10)

        # =====Bill area==========
        F5 = Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=1100, y=180, width=380, height=370)
        bill_title = Label(F5, text="bill area", font=(
            "arial", 18, "bold"), bd=7, relief=GROOVE).pack(fill=X)
        scrol_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        # scrol_y.config(Command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

        # ========button frame======
        F6 = LabelFrame(self.root, bd=10, text="button frames", font=(
            "times new roman", 15, "bold"), fg="yellow", bg="black")
        F6.place(x=0, y=560, relwidth=1, height=230)
        m1_lb1 = Label(F6, text="Total cosmetic price", font=("times new roman", 14, "bold"),
                       bg="black", fg="white").grid(row=0, column=0, padx=20, pady=1, sticky="w")
        m1_txt = Entry(F6, width=10, textvariable=self.cosmetic_price, font="arial 15", bd=7, relief=SUNKEN).grid(
            row=0, column=1, pady=10, padx=10)

        m2_lb1 = Label(F6, text="Total Grocery price", font=(
            "times new roman", 14, "bold"), bg="black", fg="white").grid(row=1, column=0, padx=20, pady=1, sticky="w")
        m2_txt = Entry(F6, width=10, textvariable=self.grocery_price, font="arial 15 ", bd=7, relief=SUNKEN).grid(
            row=1, column=1, pady=10, padx=10)

        m3_lb1 = Label(F6, text="Total coldDrink price", font=("times new roman", 14, "bold"),
                       bg="black", fg="white").grid(row=2, column=0, padx=20, pady=1, sticky="w")
        m3_txt = Entry(F6, width=10, textvariable=self.cold_drink_price, font="arial 15", bd=7, relief=SUNKEN).grid(
            row=2, column=1, pady=10,  padx=10)

        c1_lb1 = Label(F6, text=" Cosmetic Tax", font=("times new roman", 14, "bold"),
                       bg="black", fg="white").grid(row=0, column=2, padx=20, pady=1, sticky="w")
        c1_txt = Entry(F6, width=10, textvariable=self.cosmetic_tax, font="arial 15",
                       bd=7, relief=SUNKEN).grid(row=0, column=3, pady=10, padx=10)

        c2_lb1 = Label(F6, text=" Grocery Tax", font=("times new roman", 14, "bold"),
                       bg="black", fg="white").grid(row=1, column=2, padx=20, pady=1, sticky="w")
        c2_txt = Entry(F6, width=10, textvariable=self.grocery_tax, font="arial 15",
                       bd=7, relief=SUNKEN).grid(row=1, column=3, pady=10, padx=10)

        c3_lb1 = Label(F6, text=" coldDrink Tax", font=("times new roman", 14, "bold"),
                       bg="black", fg="white").grid(row=2, column=2, padx=20, pady=1, sticky="w")
        c3_txt = Entry(F6, width=10, textvariable=self.cold_drink_tax, font="arial 15",
                       bd=7, relief=SUNKEN).grid(row=2, column=3, pady=10, padx=10)

        btn_f = Frame(F6, bd=7, relief=GROOVE)
        btn_f.place(x=740, width=750, height=200)

        total_btn = Button(btn_f, command=self.total, text="Total", bg="black", fg="white", pady=15, width=10, bd=5, font=(
            "arial", 15, "bold")).grid(row=0, column=0, padx=5, pady=50)

        Gbill_btn = Button(btn_f, text="Generate Bill", command=self.bill_area, bg="black", fg="white", pady=15, width=10, bd=5, font=(
            "arial", 15, "bold")).grid(row=0, column=1, padx=20, pady=50)

        clear_btn = Button(btn_f, text="Clear", bg="black", fg="white", pady=15, width=10, bd=5, font=(
            "arial", 15, "bold")).grid(row=0, column=2, padx=20, pady=50)

        exit_btn = Button(btn_f, text="Exit", bg="black", fg="white", pady=15, width=10, bd=5, font=(
            "arial", 15, "bold")).grid(row=0, column=3, padx=20, pady=50)

        self.welcome_bill()

    def total(self):
        self.c_s_p = self.soap.get()*40
        self.c_fc_p = self.facecream.get()*120
        self.c_fw_p = self.facewash.get()*60
        self.c_hs_p = self.hairspray.get()*180
        self.c_hg_p = self.hairgel.get()*140
        self.c_bl_p = self.bodywash.get()*180
        self.total_cosmetic_price = float(
            self.c_s_p +
            self.c_fc_p +
            self.c_fw_p +
            self.c_hs_p +
            self.c_hg_p +
            self.c_bl_p
        )
        self.cosmetic_price.set("Rs"+str(self.total_cosmetic_price))
        self.c_tax = round((self.total_cosmetic_price*0.05), 2)
        self.cosmetic_tax.set(
            "Rs"+str(self.c_tax))

        self.g_b_p = self.beshan.get()*80
        self.g_r_p = self.rice.get()*80
        self.g_d_p = self.daal.get()*60
        self.g_f_p = self.foodoil.get()*180
        self.g_w_p = self.wheat.get()*240
        self.g_rj_p = self.rajma.get()*150

        self.total_grocery_price = float(

            self.g_b_p +
            self.g_r_p +
            self.g_d_p +
            self.g_f_p +
            self.g_w_p +
            self.g_rj_p
        )
        self.grocery_price.set("Rs"+str(self.total_grocery_price))
        self.g_tax = round((self.total_grocery_price*0.01), 2)
        self.grocery_tax.set(
            "Rs"+str(self.g_tax))

        self.d_m_p = self.maza.get()*40
        self.d_c_p = self.coke.get()*40
        self.d_p_p = self.pepsi.get()*40
        self.d_dw_p = self.dew.get()*40
        self.d_sl_p = self.slice.get()*40
        self.d_st_p = self.sting.get()*20

        self.total_cold_drink_price = float(
            self.d_m_p +
            self.d_c_p +
            self.d_p_p +
            self.d_dw_p +
            self.d_sl_p +
            self.d_st_p
        )
        self.cold_drink_price.set("Rs"+str(self.total_cold_drink_price))
        self.d_tax = round((self.total_cold_drink_price*0.05), 2)
        self.cold_drink_tax.set(
            "Rs"+str(self.d_tax))

        self.Total_bill = float(self.total_cosmetic_price +
                                self.total_grocery_price +
                                self.total_cold_drink_price +
                                self.c_tax +
                                self.g_tax +
                                self.d_tax)

    def welcome_bill(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, "\tWelcome robin's retail")
        self.txtarea.insert(END, f"\nBill Number:{self.bill_no.get()}")
        self.txtarea.insert(END, f"\nCustomer Name:{self.c_name.get()}")
        self.txtarea.insert(END, f"\nPhone Number:{self.c_phone.get()}")
        self.txtarea.insert(
            END, f"\n==========================================")
        self.txtarea.insert(END, f"\nproducts\t\tQTY\t\tprice")
        self.txtarea.insert(
            END, f"\n==========================================")

    def bill_area(self):
        if self.c_name.get() == "" or self.c_phone.get() == "":
            messagebox.showerror("Error", "customer details are must")
        elif self.cosmetic_price.get() == "Rs.0.0" and self.grocery_price.get() == "Rs.0.0" and self.cold_drink_price.get() == "Rs.0.0":
            messagebox.showerror("Error", "no product selected")
        else:
            self.welcome_bill()
            # =========cosmetics=======
            if self.soap.get() != 0:
                self.txtarea.insert(
                    END, f"\n Bath Soap\t\t{self.soap.get()}\t\t{self.c_s_p}")
            if self.facecream.get() != 0:
                self.txtarea.insert(
                    END, f"\n Face Cream\t\t{self.facecream.get()}\t\t{self.c_fc_p}")
            if self.facewash.get() != 0:
                self.txtarea.insert(
                    END, f"\n Fcae Wash\t\t{self.facewash.get()}\t\t{self.c_fw_p}")
            if self.hairspray.get() != 0:
                self.txtarea.insert(
                    END, f"\n Hair Spray\t\t{self.hairspray.get()}\t\t{self.c_hs_p}")
            if self.hairgel.get() != 0:
                self.txtarea.insert(
                    END, f"\n Hair Gel\t\t{self.hairgel.get()}\t\t{self.c_hg_p}")
            if self.bodywash.get() != 0:
                self.txtarea.insert(
                    END, f"\n Body Wash\t\t{self.bodywash.get()}\t\t{self.c_bl_p}")

            # =========grocery=======
            if self.beshan.get() != 0:
                self.txtarea.insert(
                    END, f"\n Beshan \t\t{self.beshan.get()}\t\t{self.g_b_p}")
            if self.rice.get() != 0:
                self.txtarea.insert(
                    END, f"\n Rice\t\t{self.rice.get()}\t\t{self.g_r_p}")
            if self.daal.get() != 0:
                self.txtarea.insert(
                    END, f"\n Daal\t\t{self.daal.get()}\t\t{self.g_d_p}")
            if self.foodoil.get() != 0:
                self.txtarea.insert(
                    END, f"\n Food Oil\t\t{self.foodoil.get()}\t\t{self.g_f_p}")
            if self.wheat.get() != 0:
                self.txtarea.insert(
                    END, f"\n Wheat\t\t{self.wheat.get()}\t\t{self.g_w_p}")
            if self.rajma.get() != 0:
                self.txtarea.insert(
                    END, f"\n Rajma \t\t{self.rajma.get()}\t\t{self.g_rj_p}")

            # =========cold drinks=======
            if self.maza.get() != 0:
                self.txtarea.insert(
                    END, f"\n Maza\t\t{self.maza.get()}\t\t{self.d_m_p}")
            if self.coke.get() != 0:
                self.txtarea.insert(
                    END, f"\n Coke\t\t{self.coke.get()}\t\t{self.d_c_p}")
            if self.pepsi.get() != 0:
                self.txtarea.insert(
                    END, f"\n Pepsi\t\t{self.pepsi.get()}\t\t{self.d_p_p}")
            if self.dew.get() != 0:
                self.txtarea.insert(
                    END, f"\n DEW \t\t{self.dew.get()}\t\t{self.d_dw_p}")
            if self.slice.get() != 0:
                self.txtarea.insert(
                    END, f"\n SLICE \t\t{self.slice.get()}\t\t{self.d_sl_p}")
            if self.sting.get() != 0:
                self.txtarea.insert(
                    END, f"\n STING \t\t{self.sting.get()}\t\t{self.d_st_p}")

            self.txtarea.insert(
                END, f"\n------------------------------------------")
            if self.cosmetic_tax.get() != " Rs 0.0":
                self.txtarea.insert(
                    END, f"\n Cosmetic Tax\t\t\t{self.cosmetic_tax.get()}")
            if self.grocery_tax.get() != " Rs 0.0":
                self.txtarea.insert(
                    END, f"\n Grocery Tax\t\t\t{self.grocery_tax.get()}")
            if self.cold_drink_tax.get() != " Rs 0.0":
                self.txtarea.insert(
                    END, f"\n Cosmetic Tax\t\t\t{self.cold_drink_tax.get()}")

            self.txtarea.insert(
                END, f"\n Total Bill\t\t\t Rs. {str(self.Total_bill)}")
            self.txtarea.insert(
                END, f"\n------------------------------------------")
            self.save_bill()

    def save_bill(self):
        op = messagebox.askyesno("Save Bill", "Do you want to save the bill")
        if op > 0:
            self.bill_data = self.txtarea.get('1.0', END)
            f1 = open("billssave/"+str(self.bill_no.get())+".txt", "w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("saved")
        else:
            return


root = Tk()
obj = Bill_App(root)

root.config(bg="black")
root.mainloop()
