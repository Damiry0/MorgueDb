import tkinter as tk
import tkinter.messagebox
import customtkinter
import db_connection
from pandastable import Table, TableModel, config



customtkinter.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"




class App(customtkinter.CTk):
    WIDTH = 840
    HEIGHT = 520

    def __init__(self):
        super().__init__()

        self.title("MorgueDB")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")

        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed

        # ============ create two frames ============

        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # ============ frame_right ============

        # configure grid layout (3x7)
        self.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right.rowconfigure(7, weight=10)
        self.frame_right.columnconfigure((0, 1), weight=1)
        self.frame_right.columnconfigure(2, weight=0)

        self.frame_info = customtkinter.CTkFrame(master=self.frame_right)
        self.frame_info.grid(row=0, column=0, columnspan=2, rowspan=4, pady=20, padx=20, sticky="nsew")

        self.frame_pacjenci = customtkinter.CTkFrame(master=self.frame_right)
        self.frame_pacjenci.grid(row=0, column=0, columnspan=2, rowspan=4, pady=20, padx=20, sticky="nsew")


        # ============ frame_left ============

        # configure grid layout (1x11)
        self.frame_left.grid_rowconfigure(0, minsize=10)  # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(5, weight=1)  # empty row as spacing
        self.frame_left.grid_rowconfigure(8, minsize=20)  # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing

        self.label_1 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="MorgueDB",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_1.grid(row=1, column=0, pady=10, padx=10)

        self.button_1 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Pacjenci",
                                                fg_color=("gray75", "gray30"),  # <- custom tuple-color
                                                command=self.button_pacjenci_another_way)
        self.button_1.grid(row=2, column=0, pady=10, padx=20)

        self.button_2 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Lista Sal",
                                                fg_color=("gray75", "gray30"),  # <- custom tuple-color
                                                command=self.frame_pacjenci.tkraise)
        self.button_2.grid(row=3, column=0, pady=10, padx=20)

        self.button_3 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Grafik",
                                                fg_color=("gray75", "gray30"),  # <- custom tuple-color
                                                command=self.button_pacjenci_another_way)
        self.button_3.grid(row=4, column=0, pady=10, padx=20)

        self.switch_1 = customtkinter.CTkSwitch(master=self.frame_left)
        self.switch_1.grid(row=9, column=0, pady=10, padx=20, sticky="w")

        self.switch_2 = customtkinter.CTkSwitch(master=self.frame_left,
                                                text="Dark Mode",
                                                command=self.change_mode)
        self.switch_2.grid(row=10, column=0, pady=10, padx=20, sticky="w")

        # ============ frame_info ============

        # configure grid layout (1x1)
        self.frame_info.rowconfigure(0, weight=1)
        self.frame_info.columnconfigure(0, weight=1)

        self.frame_info.tkraise()
        # ============ frame_pacjenci ============




        # self.button4 = customtkinter.CTkButton(master=self.frame_pacjenci,
        #                                                 text="dupa",
        #                                                 fg_color=("gray75", "gray30"),  # <- custom tuple-color
        #                                                 command=self.button_event)

        self.frame_info.tkraise()

    def button_event(self):
        print("Button pressed")

    # def button_pacjenci(self):
    #     self.frame_info.tkraise()
    #     x = db_connection.moreguDB()
    #     df = x.test_connection()
    #     pt = Table(self.frame_info,dataframe=df,showtoolbar=True, showstatusbar=True)
    #     options = {'align': 'w',
    #          'cellbackgr': '#F4F4F3',
    #          'cellwidth': 80,
    #          'floatprecision': 2,
    #          'thousandseparator': '',
    #          'font': 'Arial',
    #          'fontsize': 12,
    #          'fontstyle': '',
    #          'grid_color': '#ABB1AD',
    #          'linewidth': 1,
    #          'rowheight': 22,
    #          'rowselectedcolor': '#E4DED4',
    #          'textcolor': 'black'}
    #     config.apply_options(options, pt)
    #
    #     pt.show()

    def button_pacjenci_another_way(self):
        x = db_connection.moreguDB()
        df = x.test_connection().values.tolist()
        self.frame_pacjenci.tkraise()
        self.frame_pacjenci.grid_columnconfigure(1, weight=1)
        tk.Label(master=self.frame_pacjenci, text="Id lekarza", anchor="w").grid(row=0, column=0, sticky="ew")
        tk.Label(master=self.frame_pacjenci, text="Id pracownika", anchor="w").grid(row=0, column=1, sticky="ew")
        tk.Label(master=self.frame_pacjenci, text="Imie", anchor="w").grid(row=0, column=2, sticky="ew")
        tk.Label(master=self.frame_pacjenci, text="Nazwisko", anchor="w").grid(row=0, column=3, sticky="ew")
        tk.Label(master=self.frame_pacjenci, text="Telefon", anchor="w").grid(row=0, column=4, sticky="ew")
        tk.Label(master=self.frame_pacjenci, text="Godziny pracy", anchor="w").grid(row=0, column=5, sticky="ew")
        tk.Label(master=self.frame_pacjenci, text="Szczegóły", anchor="w").grid(row=0, column=6, sticky="ew")
        row=1

        for (id_lekarza, id_pracownika, imie,nazwisko,telefon,godziny_pracy) in df:
            id_lekarza_label = tk.Label(master=self.frame_pacjenci, text=str(id_lekarza), anchor="w")
            id_pracownika_label = tk.Label(master=self.frame_pacjenci, text=str(id_lekarza), anchor="w")
            imie_label = tk.Label(master=self.frame_pacjenci, text=imie, anchor="w")
            nazwisko_label = tk.Label(master=self.frame_pacjenci, text=nazwisko, anchor="w")
            telefon_label = tk.Label(master=self.frame_pacjenci, text=telefon, anchor="w")
            godziny_pracy_label = tk.Label(master=self.frame_pacjenci, text=godziny_pracy, anchor="w")
            action_button = tk.Button(master=self.frame_pacjenci, text="Szczegóły",)

            id_lekarza_label.grid(row=row, column=0, sticky="ew")
            id_pracownika_label.grid(row=row, column=1, sticky="ew")
            imie_label.grid(row=row, column=2, sticky="ew")
            nazwisko_label.grid(row=row, column=3, sticky="ew")
            telefon_label.grid(row=row, column=4, sticky="ew")
            godziny_pracy_label.grid(row=row, column=5, sticky="ew")
            action_button.grid(row=row, column=6, sticky="ew")

            row += 1

    def change_mode(self):
            if self.switch_2.get() == 1:
                customtkinter.set_appearance_mode("dark")
            else:
                customtkinter.set_appearance_mode("light")

    def on_closing(self, event=0):
        self.destroy()

    def start(self):
        self.mainloop()



if __name__ == "__main__":
    app = App()
    app.start()

