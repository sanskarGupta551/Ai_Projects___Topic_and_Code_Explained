import os
import re
import customtkinter as ctk
from PIL import Image
import emoji





class AI_Toolkit:
    def __init__(self):
        # Main_Widget
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        self.root=ctk.CTk()
        self.root.title("Ai Multi-media Generator")
        self.root.minsize(1920,1080)
        self.root.resizable(width=False, height=False)
        self.root.grid_rowconfigure((0), weight=1)
        self.root.grid_columnconfigure((0), weight=1)

        # Universal_Variables
        self.television_emoji=emoji.emojize(":television:")
        self.Save_Directory=ctk.StringVar(value="Document")
        self.Save_Format_Var=ctk.IntVar(value=1)
        self.Tags_string=ctk.StringVar(value="")

        # Base_GUI
        self.Build_UI()
        self.root.mainloop()



    def Build_UI(self):
        # Heading Label
        self.Sparkle_Emoji_Label=ctk.CTkLabel(master=self.root, text=self.television_emoji, fg_color="transparent", font=("Comic Sans MS", 108))
        self.Sparkle_Emoji_Label.grid(row=0, column=0, padx=(1,1180), pady=1, sticky="ne")
        self.Output_Heading_Label=ctk.CTkLabel(master=self.root, text="Multi-media Generator ", fg_color="transparent", font=("Comic Sans MS", 108))
        self.Output_Heading_Label.grid(row=0, column=0, padx=1, pady=1, sticky="ne")
        self.Ai_Label=ctk.CTkLabel(master=self.root, text="Ai", fg_color="transparent", font=("Comic Sans MS", 54))
        self.Ai_Label.grid(row=0, column=0, padx=(1,1330), pady=(60,11), sticky="ne")
        # Frame 
        self.MainFrame=ctk.CTkFrame(master=self.root, fg_color="transparent", corner_radius=10, border_width=3, border_color="white")
        self.MainFrame.grid(row=0, column=0, padx=11, pady=(160,11), sticky="nsew")
        self.Media_Type_Label=ctk.CTkLabel(master=self.MainFrame, text="Media Type : ", fg_color="transparent", font=("Comic Sans MS", 30))
        self.Media_Type_Label.grid(row=0, column=0, padx=21, pady=21, sticky="nw")
        self.Media_Type_Button=ctk.CTkSegmentedButton(master=self.MainFrame, values=["Image", "Panaroma", "GIF", "Video"], border_width=1, fg_color="white", font=("Comic Sans MS", 30))
        self.Media_Type_Button.grid(row=0, column=0, padx=(220,21), pady=21, sticky="nw")
        self.Media_Type_Button.set("Image")





AI_Toolkit()




