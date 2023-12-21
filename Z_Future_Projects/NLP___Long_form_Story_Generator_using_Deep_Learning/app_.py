import os
import re
import customtkinter as ctk
from PIL import Image
import emoji





class AI_Toolkit:
    def __init__(self):
        # Main_Widget
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")
        self.root=ctk.CTk()
        self.root.title("Ai Long-form Story Generator")
        self.root.minsize(1920,1080)
        self.root.resizable(width=False, height=False)
        self.root.grid_rowconfigure((0), weight=1)
        self.root.grid_columnconfigure((0), weight=1)

        # Universal_Variables
        self.sparkle_emoji=emoji.emojize(":sparkles:")
        self.Save_Directory=ctk.StringVar(value="Document")
        self.Save_Format_Var=ctk.IntVar(value=1)
        self.Tags_string=ctk.StringVar(value="")

        # Base_GUI
        self.Build_UI()
        self.root.mainloop()



    def Build_UI(self):
        # Heading Label
        self.Sparkle_Emoji_Label=ctk.CTkLabel(master=self.root, text=self.sparkle_emoji, fg_color="transparent", font=("Comic Sans MS", 36))
        self.Sparkle_Emoji_Label.grid(row=0, column=0, padx=(1,1440), pady=11, sticky="ne")
        self.Output_Heading_Label=ctk.CTkLabel(master=self.root, text="Long-form Story Generator ", fg_color="transparent", font=("Comic Sans MS", 108))
        self.Output_Heading_Label.grid(row=0, column=0, padx=1, pady=1, sticky="ne")
        self.Ai_Label=ctk.CTkLabel(master=self.root, text="Ai", fg_color="transparent", font=("Comic Sans MS", 36))
        self.Ai_Label.grid(row=0, column=0, padx=(1,1450), pady=(80,11), sticky="ne")
        # Entry
        self.Entry_Frame=ctk.CTkFrame(master=self.root, border_width=0.5, border_color="white", fg_color="transparent", corner_radius=5)
        self.Entry_Frame.grid(row=0, column=0, padx=21, pady=(210,21), sticky="nw")
        self.Title_label=ctk.CTkLabel(master=self.Entry_Frame, text="Story Title : ", fg_color="transparent", font=("Comic Sans MS", 24))
        self.Title_label.grid(row=0, column=0, padx=(21,11), pady=(30,11), sticky="nw")
        self.Title_Entry=ctk.CTkEntry(master=self.Entry_Frame, placeholder_text="Enter your 'Comic Idea' here (optional) ...", width=1210, height=60, corner_radius=10, fg_color="transparent", font=("Comic Sans MS", 24))
        self.Title_Entry.grid(row=0, column=0, padx=(180,11), pady=(20,11), sticky="nw")
        self.Context_label=ctk.CTkLabel(master=self.Entry_Frame, text="Context : ", fg_color="transparent", font=("Comic Sans MS", 24))
        self.Context_label.grid(row=0, column=0, padx=(21,11), pady=(110,11), sticky="nw")
        self.Context_Entry=ctk.CTkEntry(master=self.Entry_Frame, placeholder_text="Enter your 'Comic Idea' here (optional) ...", width=1210, height=60, corner_radius=10, fg_color="transparent", font=("Comic Sans MS", 24))
        self.Context_Entry.grid(row=0, column=0, padx=(180,11), pady=(100,11), sticky="nw")
        self.Beginning_label=ctk.CTkLabel(master=self.Entry_Frame, text="Beginning : ", fg_color="transparent", font=("Comic Sans MS", 24))
        self.Beginning_label.grid(row=0, column=0, padx=(21,11), pady=(190,11), sticky="nw")
        self.Beginning_Entry=ctk.CTkEntry(master=self.Entry_Frame, placeholder_text="Enter your 'Comic Idea' here (optional) ...", width=1210, height=60, corner_radius=10, fg_color="transparent", font=("Comic Sans MS", 24))
        self.Beginning_Entry.grid(row=0, column=0, padx=(180,11), pady=(180,11), sticky="nw")
        self.Ending_label=ctk.CTkLabel(master=self.Entry_Frame, text="Ending : ", fg_color="transparent", font=("Comic Sans MS", 24))
        self.Ending_label.grid(row=0, column=0, padx=(21,11), pady=(270,11), sticky="nw")
        self.Ending_Entry=ctk.CTkEntry(master=self.Entry_Frame, placeholder_text="Enter your 'Comic Idea' here (optional) ...", width=1210, height=60, corner_radius=10, fg_color="transparent", font=("Comic Sans MS", 24))
        self.Ending_Entry.grid(row=0, column=0, padx=(180,11), pady=(260,11), sticky="nw")
        self.Conflict_label=ctk.CTkLabel(master=self.Entry_Frame, text="Conflict : ", fg_color="transparent", font=("Comic Sans MS", 24))
        self.Conflict_label.grid(row=0, column=0, padx=(21,11), pady=(350,11), sticky="nw")
        self.Conflict_Entry=ctk.CTkEntry(master=self.Entry_Frame, placeholder_text="Enter your 'Comic Idea' here (optional) ...", width=1210, height=60, corner_radius=10, fg_color="transparent", font=("Comic Sans MS", 24))
        self.Conflict_Entry.grid(row=0, column=0, padx=(180,11), pady=(340,20), sticky="nw")
        # Tags
        self.Tags_Frame=ctk.CTkFrame(master=self.root, border_width=0.5, border_color="white", fg_color="transparent", corner_radius=5)
        self.Tags_Frame.grid(row=0, column=0, padx=21, pady=21, sticky="sw")
        self.Genre_label=ctk.CTkLabel(master=self.Tags_Frame, text="Genre : ", fg_color="transparent", font=("Comic Sans MS", 24))
        self.Genre_label.grid(row=0, column=0, padx=11, pady=(30,11), sticky="nw")
        self.Genre_Options=ctk.CTkComboBox(master=self.Tags_Frame, height=50, width=320, border_width=1, corner_radius=5, values=['action', 'adult comedy', 'alternate history', 'alternate reality', 'blaxploitation', 'christian film', 'horror', 'mystery', 'non fiction', 'paranormal', 'pornographic', 'sci-fi', 'western'], font=("Comic Sans MS", 24))
        self.Genre_Options.grid(row=0, column=0, padx=(120,11), pady=(20,11), sticky="nw")
        self.Style_label=ctk.CTkLabel(master=self.Tags_Frame, text="Style : ", fg_color="transparent", font=("Comic Sans MS", 24))
        self.Style_label.grid(row=0, column=0, padx=11, pady=(110,11), sticky="nw")
        self.Style_Options=ctk.CTkComboBox(master=self.Tags_Frame, height=50, width=320, border_width=1, corner_radius=5, values=['avant garde', 'boring', 'grindhouse film', 'humor', 'insanity', 'intrigue', 'magical realism', 'melodrama', 'murder', 'neo noir', 'plot twist', 'psychedelic', 'queer', 'realism', 'satire', 'sentimental', 'storytelling'], font=("Comic Sans MS", 24))
        self.Style_Options.grid(row=0, column=0, padx=(120,11), pady=(100,11), sticky="nw")
        self.Tone_label=ctk.CTkLabel(master=self.Tags_Frame, text="Tone : ", fg_color="transparent", font=("Comic Sans MS", 24))
        self.Tone_label.grid(row=0, column=0, padx=11, pady=(190,11), sticky="nw")
        self.Tone_Options=ctk.CTkComboBox(master=self.Tags_Frame, height=50, width=320, border_width=1, corner_radius=5, values=['absurd', 'allegory', 'anti war', 'autobiographical', 'bleak', 'brainwashing', 'dark', 'depressing', 'dramatic', 'entertaining', 'feel-good', 'historical fiction', 'inspiring', 'thought-provoking', 'whimsical'], font=("Comic Sans MS", 24))
        self.Tone_Options.grid(row=0, column=0, padx=(120,11), pady=(180,11), sticky="nw")
        self.Mood_label=ctk.CTkLabel(master=self.Tags_Frame, text="Mood : ", fg_color="transparent", font=("Comic Sans MS", 24))
        self.Mood_label.grid(row=0, column=0, padx=11, pady=(270,11), sticky="nw")
        self.Mood_Options=ctk.CTkComboBox(master=self.Tags_Frame, height=50, width=320, border_width=1, corner_radius=5, values=['atmospheric', 'claustrophobic', 'haunting', 'historical', 'home movie', 'philosophical', 'prank', 'psychological', 'sadist', 'stupid', 'suspenseful', 'violence'], font=("Comic Sans MS", 24))
        self.Mood_Options.grid(row=0, column=0, padx=(120,11), pady=(260,11), sticky="nw")
        self.Theme_label=ctk.CTkLabel(master=self.Tags_Frame, text="Theme : ", fg_color="transparent", font=("Comic Sans MS", 24))
        self.Theme_label.grid(row=0, column=0, padx=11, pady=(350,11), sticky="nw")
        self.Theme_Options=ctk.CTkComboBox(master=self.Tags_Frame, height=50, width=320, border_width=1, corner_radius=5, values=['clever', 'comedy', 'comic', 'cruelty', 'cult', 'cute', 'fantasy', 'flashback', 'good versus evil', 'gothic', 'revenge', 'romantic', 'suicidal', 'tragedy'], font=("Comic Sans MS", 24))
        self.Theme_Options.grid(row=0, column=0, padx=(120,11), pady=(340,11), sticky="nw")
        # Keywords
        self.Keywords_Frame=ctk.CTkScrollableFrame(master=self.root, label_text="   Keywords", label_fg_color="transparent", label_anchor="nw", label_font=("Comic Sans MS", 24), border_width=0.5, border_color="white", fg_color="transparent", corner_radius=5)
        self.Keywords_Frame.grid(row=0, column=0, padx=(1450,21), pady=(210,450), sticky="nsew")
        self.Edit_Keyword_Button=ctk.CTkButton(master=self.root, corner_radius=10, text="Edit", font=("Comic Sans MS", 24))
        self.Edit_Keyword_Button.grid(row=0, column=0, padx=(21,50), pady=(220,21), sticky="ne")
        # Length and Save Location + Format
        self.Extra_Frame=ctk.CTkFrame(master=self.root, border_width=0.5, border_color="white", fg_color="transparent", corner_radius=5)
        self.Extra_Frame.grid(row=0, column=0, padx=(500,21), pady=(656,10), sticky="new")
        self.Length_Label=ctk.CTkLabel(master=self.Extra_Frame, text="Story Length : ", fg_color="transparent", font=("Comic Sans MS", 24))
        self.Length_Label.grid(row=0, column=0, padx=21, pady=(20,11), sticky="nw")
        self.Length_Slider=ctk.CTkSlider(master=self.Extra_Frame, from_=1000, to=100000, number_of_steps=99, height=30, width=1050, command=self.Display_Length_Value)
        self.Length_Slider.grid(row=0, column=0, padx=(210,11), pady=(25,11), sticky="nw")
        self.Length_Slider.set(10000)
        self.Length_Value_Label=ctk.CTkLabel(master=self.Extra_Frame, text=int(self.Length_Slider.get()), fg_color="transparent", font=("Comic Sans MS", 24))
        self.Length_Value_Label.grid(row=0, column=0, padx=(1280,11), pady=(20,11), sticky="nw")
        self.Save_Location_Label=ctk.CTkLabel(master=self.Extra_Frame, text="Save Location : ", fg_color="transparent", font=("Comic Sans MS", 24))
        self.Save_Location_Label.grid(row=0, column=0, padx=21, pady=(100,11), sticky="nw")
        self.Save_Location_Button=ctk.CTkButton(master=self.Extra_Frame, corner_radius=10, text=self.Save_Directory.get(), height=50, width=1140, font=("Comic Sans MS", 24))
        self.Save_Location_Button.grid(row=0, column=0, padx=(210,11), pady=(95,11), sticky="nw")
        self.Save_Format_Label=ctk.CTkLabel(master=self.Extra_Frame, text="Save Format : ", fg_color="transparent", font=("Comic Sans MS", 24))
        self.Save_Format_Label.grid(row=0, column=0, padx=21, pady=(180,11), sticky="nw")
        self.PDF_Format_Radio_Button=ctk.CTkRadioButton(master=self.Extra_Frame, corner_radius=10, text="PDF", variable=self.Save_Format_Var, value=0, font=("Comic Sans MS", 24))
        self.PDF_Format_Radio_Button.grid(row=0, column=0, padx=(220,11), pady=(180,21), sticky="nw")
        self.txt_Format_Radio_Button=ctk.CTkRadioButton(master=self.Extra_Frame, corner_radius=10, text=".txt", variable=self.Save_Format_Var, value=1, font=("Comic Sans MS", 24))
        self.txt_Format_Radio_Button.grid(row=0, column=0, padx=(330,11), pady=(180,21), sticky="nw")
        # Progress Bar
        self.Progress_Frame=ctk.CTkFrame(master=self.root, border_width=0.5, border_color="white", height=60, width=1085, fg_color="transparent", corner_radius=5)
        self.Progress_Frame.grid(row=0, column=0, padx=(500,21), pady=(11,80), sticky="sw")
        self.Generate_Story_Button=ctk.CTkButton(master=self.root, corner_radius=10, text="Generate Story", height=60, font=("Comic Sans MS", 36))
        self.Generate_Story_Button.grid(row=0, column=0, padx=21, pady=(11,80), sticky="se")
        self.Progress_Label=ctk.CTkLabel(master=self.root, text="Progress : ", fg_color="transparent", font=("Comic Sans MS", 24))
        self.Progress_Label.grid(row=0, column=0, padx=(500,21), pady=21, sticky="sw")
        self.Progress_Bar=ctk.CTkProgressBar(master=self.root, orientation="horizontal", width=700, height=24)
        self.Progress_Bar.grid(row=0, column=0, padx=(650,21), pady=24, sticky="sw")
        self.Progress_Info_Label=ctk.CTkLabel(master=self.root, text="...", fg_color="transparent", font=("Comic Sans MS", 24))
        self.Progress_Info_Label.grid(row=0, column=0, padx=(1390,21), pady=21, sticky="sw")
        self.Progress_Bar.set(0)
        
    
    
    def Display_Length_Value(self, value): 
        self.Length_Value_Label.configure(text=int(value))





AI_Toolkit()




