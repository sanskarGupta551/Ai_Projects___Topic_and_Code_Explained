import os 

import customtkinter as ctk 
from PIL import Image 
import emoji 





class AI_Toolkit: 
    def __init__(self): 
        # Main_Widget 
        ctk.set_appearance_mode("dark") 
        ctk.set_default_color_theme("green") 
        self.root=ctk.CTk() 
        self.root.title("Ai Comic Generator") 
        self.root.minsize(1920,1080) 
        self.root.resizable(width=False, height=False) 
        self.root.grid_rowconfigure((0), weight=1) 
        self.root.grid_columnconfigure((0), weight=1) 

        # Universal_Variables 
        self.Comic_Generation_Type_Choice=ctk.StringVar(value="") 
        self.Have_Character_Dialogues_bool=ctk.StringVar(value="") 
        self.Keywords_string=ctk.StringVar(value="") 
        self.Keywords_index=ctk.IntVar(value=0) 
        self.Draw_Page_Border_bool=ctk.StringVar(value="") 
        self.Comic_Save_Directory=ctk.StringVar(value="Documents") 
        self.sparkle_emoji=emoji.emojize(":sparkles:") 
        self.shuffle_icon=ctk.CTkImage(Image.open(r"./(Pending)Portfolio_project___Ai_Comic_Generator/shuffle_icon.png"), size=(25,25)) 
        self.delete_icon=ctk.CTkImage(Image.open(r"./(Pending)Portfolio_project___Ai_Comic_Generator/delete_icon.png"), size=(25,25)) 
        
        # Base_GUI 
        self.Build_UI() 
        self.Switch_Comic_Generation_Type_GUI(" Generate New Comics ") 
        self.root.mainloop() 


    
    def Build_UI(self):
        # Heading Label 
        self.Sparkle_Emoji_Label=ctk.CTkLabel(master=self.root, text=self.sparkle_emoji, fg_color="transparent", font=("Comic Sans MS", 54)) 
        self.Sparkle_Emoji_Label.grid(row=0, column=0, padx=(1,880), pady=1, sticky="ne") 
        self.Output_Heading_Label=ctk.CTkLabel(master=self.root, text="Comic Generator ", fg_color="transparent", font=("Comic Sans MS", 108)) 
        self.Output_Heading_Label.grid(row=0, column=0, padx=1, pady=1, sticky="ne") 
        self.Ai_Label=ctk.CTkLabel(master=self.root, text="Ai", fg_color="transparent", font=("Comic Sans MS", 36)) 
        self.Ai_Label.grid(row=0, column=0, padx=(1,900), pady=(85,1), sticky="ne") 
        self.Comic_Generation_Type_Button=ctk.CTkSegmentedButton(master=self.root, height=60, corner_radius=10, values=[" Generate New Comics ", " Generate Sequel "], font=("Comic Sans MS", 24), command=self.Switch_Comic_Generation_Type_GUI) 
        self.Comic_Generation_Type_Button.grid(row=0, column=0, padx=11, pady=(135,11), sticky="nw") 
        self.Save_Location_Label=ctk.CTkLabel(master=self.root, text="Save location : ", fg_color="transparent", font=("Comic Sans MS", 24)) 
        self.Save_Location_Label.grid(row=0, column=0, padx=11, pady=(11,25), sticky="sw") 
        self.Save_Location_Button=ctk.CTkButton(master=self.root, text=self.Comic_Save_Directory.get(), height=60, width=1190, corner_radius=10, font=("Comic Sans MS", 24)) 
        self.Save_Location_Button.grid(row=0, column=0, padx=(200,11), pady=11, sticky="sw") 
        self.Generate_Comics_Button=ctk.CTkButton(master=self.root, text="  Generate Comics  ", height=60, corner_radius=10, font=("Comic Sans MS", 24), command=self.Generate_Comics) 
        self.Generate_Comics_Button.grid(row=0, column=0, padx=11, pady=11, sticky="se") 

        # Story-line Configuration Frame 
        self.Story_line_Configuration_Frame=ctk.CTkFrame(master=self.root, border_width=0.5, border_color="white", fg_color="transparent", corner_radius=5) 
        self.Story_line_Configuration_Frame.grid(row=0, column=0, padx=(11,530), pady=(210,110), sticky="nsew") 
        self.Story_line_Configuration_label=ctk.CTkLabel(master=self.Story_line_Configuration_Frame, text="Story-line", fg_color="transparent", font=("Comic Sans MS", 24)) 
        self.Story_line_Configuration_label.grid(row=0, column=0, padx=11, pady=11, sticky="nw") 
        self.OR_Label=ctk.CTkLabel(master=self.Story_line_Configuration_Frame, text="OR", fg_color="transparent", font=("Comic Sans MS", 20)) 
        self.OR_Label.grid(row=0, column=0, padx=(1140,11), pady=(90,11), sticky="nw") 
        self.Story_Keywords_list_frame=ctk.CTkScrollableFrame(master=self.Story_line_Configuration_Frame, height=450, width=330, label_text="Keywords", border_width=1, fg_color="transparent", corner_radius=5, label_font=("Comic Sans MS", 24)) 
        self.Story_Keywords_list_frame.grid(row=0, column=0, padx=11, pady=(160,11), sticky="nw") 
        self.Story_Keywords_Input=ctk.CTkEntry(master=self.Story_line_Configuration_Frame, placeholder_text="Enter 'Keywords' (optional) ...", width=350, height=60, corner_radius=10, fg_color="transparent", font=("Comic Sans MS", 24)) 
        self.Story_Keywords_Input.grid(row=0, column=0, padx=11, pady=(685,11), sticky="nw") 
        self.Story_Style_Label=ctk.CTkLabel(master=self.Story_line_Configuration_Frame, text="Style : ", fg_color="transparent", font=("Comic Sans MS", 24)) 
        self.Story_Style_Label.grid(row=0, column=0, padx=(420,11), pady=(210,11), sticky="nw") 
        self.Story_Style_Options=ctk.CTkComboBox(master=self.Story_line_Configuration_Frame, height=50, width=320, border_width=1, corner_radius=5, values=["Plot First", "Full Script", "Classic Comic Strip", "Western Comic Style", "Modern Age Styles", "~Pick Any"], font=("Comic Sans MS", 24)) 
        self.Story_Style_Options.grid(row=0, column=0, padx=(520,11), pady=(200,11), sticky="nw") 
        self.Story_Tone_Label=ctk.CTkLabel(master=self.Story_line_Configuration_Frame, text="Tone : ", fg_color="transparent", font=("Comic Sans MS", 24)) 
        self.Story_Tone_Label.grid(row=0, column=0, padx=(420,11), pady=(290,11), sticky="nw") 
        self.Story_Tone_Options=ctk.CTkComboBox(master=self.Story_line_Configuration_Frame, height=50, width=320, border_width=1, corner_radius=5, values=["Joyful", "Serious", "Humorous", "Sad", "Formal", "Informal", "Optimistic", "Pessimistic", "Horror", "~Pick Any"], font=("Comic Sans MS", 24)) 
        self.Story_Tone_Options.grid(row=0, column=0, padx=(520,11), pady=(280,11), sticky="nw") 
        self.Story_Mood_Label=ctk.CTkLabel(master=self.Story_line_Configuration_Frame, text="Mood : ", fg_color="transparent", font=("Comic Sans MS", 24)) 
        self.Story_Mood_Label.grid(row=0, column=0, padx=(420,11), pady=(370,11), sticky="nw") 
        self.Story_Mood_Options=ctk.CTkComboBox(master=self.Story_line_Configuration_Frame, height=50, width=320, border_width=1, corner_radius=5, values=["Cheerful", "Humorous", "Idyllic", "Madness", "Melancholic", "Suspenseful", "Romantic", "Horrrifying", "Inspirational", "~Pick Any"], font=("Comic Sans MS", 24)) 
        self.Story_Mood_Options.grid(row=0, column=0, padx=(520,11), pady=(360,11), sticky="nw") 
        self.Story_Pace_Label=ctk.CTkLabel(master=self.Story_line_Configuration_Frame, text="Pace : ", fg_color="transparent", font=("Comic Sans MS", 24)) 
        self.Story_Pace_Label.grid(row=0, column=0, padx=(940,11), pady=(210,11), sticky="nw") 
        self.Story_Pace_Options=ctk.CTkComboBox(master=self.Story_line_Configuration_Frame, height=50, width=320, border_width=1, corner_radius=5, values=["Fast-paced", "Slow-paced", "Variable pacing", "Steady pacing", "~Pick Any"], font=("Comic Sans MS", 24)) 
        self.Story_Pace_Options.grid(row=0, column=0, padx=(1040,11), pady=(200,11), sticky="nw") 
        self.Story_Theme_Label=ctk.CTkLabel(master=self.Story_line_Configuration_Frame, text="Theme : ", fg_color="transparent", font=("Comic Sans MS", 24)) 
        self.Story_Theme_Label.grid(row=0, column=0, padx=(920,11), pady=(290,11), sticky="nw") 
        self.Story_Theme_Options=ctk.CTkComboBox(master=self.Story_line_Configuration_Frame, height=50, width=320, border_width=1, corner_radius=5, values=["Fantasy", "Reality", "Autobiography", "Humor", "Politics", "Love and Freindship", "Courage and Heroism", "Good vs Evil", "~Pick Any"], font=("Comic Sans MS", 24)) 
        self.Story_Theme_Options.grid(row=0, column=0, padx=(1040,11), pady=(280,11), sticky="nw") 
        self.Have_Character_Dialogues_Switch=ctk.CTkSwitch(master=self.Story_line_Configuration_Frame, text="  Have Character Dialogues", variable=self.Have_Character_Dialogues_bool, onvalue="", offvalue="not ", font=("Comic Sans MS", 24)) 
        self.Have_Character_Dialogues_Switch.grid(row=0, column=0, padx=(980,11), pady=(370,11), sticky="nw") 
        self.Story_Conflict_Label=ctk.CTkLabel(master=self.Story_line_Configuration_Frame, text="Conflict : ", fg_color="transparent", font=("Comic Sans MS", 24)) 
        self.Story_Conflict_Label.grid(row=0, column=0, padx=(420,11), pady=(530,11), sticky="nw") 
        self.Story_Conflict_Input=ctk.CTkEntry(master=self.Story_line_Configuration_Frame, placeholder_text="What will the Comic's narrative 'Revolve Around' (optional) ...", width=820, height=60, corner_radius=10, fg_color="transparent", font=("Comic Sans MS", 24)) 
        self.Story_Conflict_Input.grid(row=0, column=0, padx=(540,11), pady=(520,11), sticky="nw") 
        self.Story_Villain_Label=ctk.CTkLabel(master=self.Story_line_Configuration_Frame, text="Villain : ", fg_color="transparent", font=("Comic Sans MS", 24)) 
        self.Story_Villain_Label.grid(row=0, column=0, padx=(420,11), pady=(610,11), sticky="nw") 
        self.Story_Villain_Input=ctk.CTkEntry(master=self.Story_line_Configuration_Frame, placeholder_text="Your Comic's 'Main Villain' (optional) ...", width=820, height=60, corner_radius=10, fg_color="transparent", font=("Comic Sans MS", 24)) 
        self.Story_Villain_Input.grid(row=0, column=0, padx=(540,11), pady=(600,11), sticky="nw") 
        self.Story_Ending_Label=ctk.CTkLabel(master=self.Story_line_Configuration_Frame, text="Ending : ", fg_color="transparent", font=("Comic Sans MS", 24)) 
        self.Story_Ending_Label.grid(row=0, column=0, padx=(420,11), pady=(690,11), sticky="nw") 
        self.Story_Ending_Input=ctk.CTkEntry(master=self.Story_line_Configuration_Frame, placeholder_text="A 'Desired Ending' to your Comic (optional) ...", width=820, height=60, corner_radius=10, fg_color="transparent", font=("Comic Sans MS", 24)) 
        self.Story_Ending_Input.grid(row=0, column=0, padx=(540,11), pady=(680,11), sticky="nw") 
        
        # Additional Frame 
        self.Additional_Frame=ctk.CTkFrame(master=self.root, border_width=0.5, border_color="white", fg_color="transparent", corner_radius=5) 
        self.Additional_Frame.grid(row=0, column=0, padx=(1410,11), pady=(210,500), sticky="nsew") 

        # Drawing Configuration Frame 
        self.Drawing_Configuration_Frame=ctk.CTkFrame(master=self.root, border_width=0.5, border_color="white", fg_color="transparent", corner_radius=5) 
        self.Drawing_Configuration_Frame.grid(row=0, column=0, padx=(1410,11), pady=(600,110), sticky="nsew") 
        self.Art_style_Configuration_label=ctk.CTkLabel(master=self.Drawing_Configuration_Frame, text="Drawing", fg_color="transparent", font=("Comic Sans MS", 24)) 
        self.Art_style_Configuration_label.grid(row=0, column=0, padx=11, pady=11, sticky="nw") 
        self.Art_style_label=ctk.CTkLabel(master=self.Drawing_Configuration_Frame, text="Art style : ", fg_color="transparent", font=("Comic Sans MS", 24)) 
        self.Art_style_label.grid(row=0, column=0, padx=11, pady=(80,11), sticky="nw") 
        self.Art_style_Options=ctk.CTkComboBox(master=self.Drawing_Configuration_Frame, height=50, width=320, border_width=1, corner_radius=5, values=["Realistic", "Cartoon", "Abstract", "Sketch", "~Pick Any"], font=("Comic Sans MS", 24)) 
        self.Art_style_Options.grid(row=0, column=0, padx=(160,11), pady=(70,11), sticky="nw") 
        self.Page_Count_label=ctk.CTkLabel(master=self.Drawing_Configuration_Frame, text="Page Count : ", fg_color="transparent", font=("Comic Sans MS", 24)) 
        self.Page_Count_label.grid(row=0, column=0, padx=11, pady=(160,11), sticky="nw") 
        self.Page_Count_Options=ctk.CTkComboBox(master=self.Drawing_Configuration_Frame, height=50, width=320, border_width=1, corner_radius=5, values=["24", "32", "48", "64", "96", "Free Art"], font=("Comic Sans MS", 24)) 
        self.Page_Count_Options.grid(row=0, column=0, padx=(160,11), pady=(150,11), sticky="nw") 
        self.Page_Size_label=ctk.CTkLabel(master=self.Drawing_Configuration_Frame, text="Page Size : ", fg_color="transparent", font=("Comic Sans MS", 24)) 
        self.Page_Size_label.grid(row=0, column=0, padx=11, pady=(240,11), sticky="nw") 
        self.Page_Size_Options=ctk.CTkComboBox(master=self.Drawing_Configuration_Frame, height=50, width=320, border_width=1, corner_radius=5, values=["800x1280", "1200x630", "1080x1080", "~Any"], font=("Comic Sans MS", 24)) 
        self.Page_Size_Options.grid(row=0, column=0, padx=(160,11), pady=(230,11), sticky="nw") 
        self.Draw_Page_Border_Switch=ctk.CTkSwitch(master=self.Drawing_Configuration_Frame, text="  Draw Page Border", variable=self.Draw_Page_Border_bool, onvalue="", offvalue="not", font=("Comic Sans MS", 24)) 
        self.Draw_Page_Border_Switch.grid(row=0, column=0, padx=(100,11), pady=(320,11), sticky="nw") 

        # Set value 
        self.Comic_Generation_Type_Button.set(" Generate New Comics ") 
        self.Story_Keywords_Input.bind(sequence="<Return>", command=self.Add_Keywords)
        self.Page_Count_Options.set("Free Art") 


    def Switch_Comic_Generation_Type_GUI(self, value): 
        self.Comic_Generation_Type_Choice.set(value) 
        if value==" Generate New Comics ": 
            try: self.Comic_Prequel_Path_Input.destroy(), self.Browse_Files_Button.destroy() 
            except: pass 
            self.Comic_Idea_Input=ctk.CTkEntry(master=self.Story_line_Configuration_Frame, placeholder_text="Enter your 'Comic Idea' here (optional) ...", width=1110, height=60, corner_radius=10, fg_color="transparent", font=("Comic Sans MS", 24)) 
            self.Comic_Idea_Input.grid(row=0, column=0, padx=11, pady=(70,11), sticky="nw") 
            self.Use_Images_Button=ctk.CTkButton(master=self.Story_line_Configuration_Frame, width=170, height=60, corner_radius=10, text="Use Images", font=("Comic Sans MS", 24), command=self.Generate_Comics) 
            self.Use_Images_Button.grid(row=0, column=0, padx=(1190,11), pady=(70,11), sticky="nw")  
        elif value==" Generate Sequel ": 
            try: self.Comic_Idea_Input.destroy(), self.Use_Images_Button.destroy() 
            except: pass 
            self.Comic_Prequel_Path_Input=ctk.CTkEntry(master=self.Story_line_Configuration_Frame, placeholder_text="Enter your 'Comic Prequel Path' here ...", width=1110, height=60, corner_radius=10, fg_color="transparent", font=("Comic Sans MS", 24)) 
            self.Comic_Prequel_Path_Input.grid(row=0, column=0, padx=11, pady=(70,11), sticky="nw") 
            self.Browse_Files_Button=ctk.CTkButton(master=self.Story_line_Configuration_Frame, width=170, height=60, corner_radius=10, text="Browse Files", font=("Comic Sans MS", 24), command=self.Generate_Comics) 
            self.Browse_Files_Button.grid(row=0, column=0, padx=(1190,11), pady=(70,11), sticky="nw")  



    def Generate_Comics(self): 
        comic_generation_type=self.Comic_Generation_Type_Choice.get() 
        # Get Story-line Inputs 
        comic_idea=self.Comic_Idea_Input.get() 
        style=self.Story_Style_Options.get() 
        tone=self.Story_Tone_Options.get() 
        mood=self.Story_Mood_Options.get() 
        pace=self.Story_Pace_Options.get() 
        theme=self.Story_Theme_Options.get() 
        have_character_dialogues=self.Have_Character_Dialogues_Switch.get() 
        conflict=self.Story_Conflict_Input.get() 
        villain=self.Story_Villain_Input.get() 
        ending=self.Story_Ending_Input.get() 

        # Get Drawing Inputs 
        print(f"""comic_idea: {comic_idea}
              style: {style}
              tone: {tone}
              mood: {mood}
              pace: {pace}
              theme: {theme}
              have_character_dialogues: {have_character_dialogues}
              conflict: {conflict}
              villain: {villain}
              ending: {ending}""") 

        if comic_generation_type==" Generate New Comics ": 
            pass 
        elif comic_generation_type==" Generate Sequel ": 
            pass 



    def Add_Keywords(self, event): 
        # Extracting new Keywords from Input 
        add=self.Story_Keywords_Input.get() 
        add=add.replace(",", " ") 
        new_keywords_list=add.split() 

        # Making a label out of each keywords 
        for _ in new_keywords_list: 
            index=self.Keywords_index.get() 
            self.Keyword_Button=ctk.CTkButton(master=self.Story_Keywords_list_frame, text=_, corner_radius=10, fg_color="black", hover_color="dark gray", font=("Comic Sans MS", 24), command=self.Keyword_controller) 
            self.Keyword_Button.grid(row=index, column=0, padx=1, pady=1, sticky="nw") 
            self.Keywords_index.set(index+1) 
        # Clearing Entry 
        self.Story_Keywords_Input.delete(0, ctk.END) 

        # Updating Keyword string
        keywords_string=self.Keywords_string.get() 
        new_keywords_string=", ".join(new_keywords_list) 
        all_keywords_string=keywords_string+new_keywords_string 
        self.Keywords_string.set(all_keywords_string) 

    def Keyword_controller(self): 
        pass





AI_Toolkit() 