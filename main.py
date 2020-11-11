from kivmob import KivMob, RewardedListenerInterface

from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.graphics import Canvas
from kivy.graphics.vertex_instructions import Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics.context_instructions import Color
from kivy.properties import ListProperty,NumericProperty,ObjectProperty
import random, time
from kivymd.uix.dialog import MDDialog
from kivy.uix.gridlayout import GridLayout
from kivymd.uix.bottomsheet import MDGridBottomSheet
import webbrowser
from kivy.core.window import Window

# Specifying the version name
__version__ = '1.0.0'

#class for credits to the artist
class Credit(Screen):

    def Rawpixel(self):
        webbrowser.open("https://www.freepik.com/rawpixel-com")

    def Viznezh(self):
        webbrowser.open("https://www.freepik.com/visnezh")

#Class for About Me !!
class AboutScreen(Screen):

    def references(self,site):
        sites_dict = {
            "Facebook":"https://www.facebook.com/Akgupta077",
            "InstaGram":"https://www.instagram.com/abhaygupta1609/",
            "Gmail":"https://Akgupta0777@gmail.com",
            "LinkedIn":"https://www.linkedin.com/in/abhay-gupta-88bb67188/"
        }
        give = sites_dict.get(site)
        webbrowser.open(give)

    def Follow(self):
        Follow_Sheet = MDGridBottomSheet()
        data = {
            "Facebook": "facebook-box",
            "InstaGram": "instagram",
            "Gmail": "gmail",
            "LinkedIn": "linkedin-box"
        }
        for item in data.items():
            Follow_Sheet.add_item(item[0],lambda x,y = item[0]: self.references(y),icon_src=item[1])
        Follow_Sheet.open()

#Main class that is returning from App Build Method
class intro(ScreenManager):
    screen_mgr = ObjectProperty(None)
    previous = "Menu"
    def __init__(self,**kwargs):
        super(intro,self).__init__(**kwargs)

    def Change_Screen(self,first):
        self.current = first
        Window.bind(on_keyboard = self.back)

    def back(self,window,key,*largs):
        if(key == 27):
            if(self.previous == "CLevel" or self.previous == "Level"):
                return True
            else:
                self.current = self.previous
                return True

#Class for instructions of Game
class Instructions(Screen):
    pass

#class for Online Multiplayer
class Multiplayer(Screen):
    pass

#class for Start options(Default Slips,Custom Slips)
class StartOptions(Screen):
    pass

#Class for Custom Slips entries
class CustomSlips(Screen):
    customslips = []

    #Every time it cleares the list of slip entries
    def on_pre_enter(self):
        self.customslips.clear()

#class for Hardest Challenge
class Challenge(Screen):
    pass

#Class for Hardest Custom Screen
class ChallengeC(Screen):
    pass

#Class for Default Slips (Buttons including flowers animals car etc)
class DefaultSlips(Screen):
    playlist = ["","","",""]

    @classmethod
    def Flowerscopy(cls):
        Flower = ["Rose", "Tulips", "Sunflower", "Marigold"]
        cls.playlist = Flower

    @classmethod
    def AnimalsCopy(cls):
        Animals = ["Lion", "Elephant", "Horse", "Bear"]
        cls.playlist = Animals

    @classmethod
    def CartoonCopy(cls):
        Cartoon = ["Tom", "Jerry", "Jack", "Oggy"]
        cls.playlist = Cartoon

    @classmethod
    def FruitsCopy(cls):
        Fruits = ["Apple", "Mango", "Banana", "Strawberry"]
        cls.playlist = Fruits

    @classmethod
    def CarsCopy(cls):
        Cars = ["Audi", "Ferrari", "Mercedes", "Rolls Royce"]
        cls.playlist = Cars

#Choosing Difficult Level
class difficulty(Screen):
    count = 0
    @classmethod
    def easy(cls):
        cls.count = 1
    @classmethod
    def hard(cls):
        cls.count = 2

#Class for choosing difficulty for custom screen
class difficulty_custom(Screen):
    count = 0
    @classmethod
    def easy(cls):
        cls.count = 1
    @classmethod
    def hard(cls):
        cls.count = 2

#Main class for playing arena of Game
class PlayScreen(Screen):
    slips = ListProperty([''] * 4)
    player_1 = ListProperty([''] * 4)
    player_2 = ListProperty([''] * 4)
    player_3 = ListProperty([''] * 4)
    player_4 = ListProperty([''] * 4)
    chosen_slip = ""
    sumlist = []
    confirm = 0
    level = 0
    count_hard = 0

    def __init__(self, **kw):
        super().__init__(**kw)
        self.app = MDApp.get_running_app()


#Function for making actual 16 slips from 4 slips
    def input_append(self):
        for i in range(0, 4):
            for j in range(0, 3):
                self.slips.append(self.slips[i])

# Function that distribute among 4 players
    def distribute(self):
        self.player_1.clear()
        self.player_2.clear()
        self.player_3.clear()
        self.player_4.clear()
        for i in range(0, 4):
            self.player_1.append(random.choice(self.slips))
            self.slips.remove(self.player_1[i])
            self.player_2.append(random.choice(self.slips))
            self.slips.remove(self.player_2[i])
            self.player_3.append(random.choice(self.slips))
            self.slips.remove(self.player_3[i])
            self.player_4.append(random.choice(self.slips))
            self.slips.remove(self.player_4[i])
        self.player_1.append("")

# The Function that will be called each time when this screen is called
    def on_pre_enter(self):
        self.slips = DefaultSlips.playlist
        self.level = difficulty.count
        self.confirm = 0
        self.count_hard = 0
        print("on pre enter Play Screen",self.level)
        print("on pre enter ",self.slips)
        self.input_append()
        print("After inputappend",self.slips)
        self.distribute()
        print("after distribute",self.slips)
        print("Player 1",self.player_1)
        print("player 2",self.player_2)
        print("player 3",self.player_3)
        print("player 4",self.player_4)
        SlipsApp.ads.request_interstitial()

#Function that will Pass the slip from one player to another
    def pass_slip(self,chosen_slip,sender= [],reciever = []):
        reciever.append(reciever[3])
        reciever[3] = self.chosen_slip
        sender.remove(self.chosen_slip)

#Function to check the player wins or not
    def iswinner(self,player = [],Whoiswinner = ""):
        if(player.count(player[0])==4):
            print(Whoiswinner + " Won the game")
            self.confirm = 1
            self.show_winner(Whoiswinner)

#Function that will choose the slip according to algorithms
    def choose(self,chooser = []):
        if self.level == 2:
            if(self.count_hard < 15):
                self.level = 1
                self.choose(chooser)
            for i in range(0,len(chooser)):
                self.sumlist.append(chooser.count(chooser[i]))
            self.chosen_slip = chooser[self.sumlist.index(min(self.sumlist))]
            self.sumlist.clear()

        elif self.level == 1:
            if(self.count_hard < 15):
                self.count_hard +=1
                self.chosen_slip = random.choice(chooser)
            else:
                self.level = 2
                self.choose(chooser)
        else:
            print("Hardest Removed")

#Popup funcion for showing winner
    def show_winner(self,winner = ""):
        my_dialog = MDDialog(title = "Game Over",text = winner+" Won The Game",size_hint = [1,.3],auto_dismiss = False,events_callback = self.ExitCallback)
        my_dialog.open()

    def ExitButton(self):
        Exit_dialogue = MDDialog(title = "Leave Game", text = "Are you sure!! you want to leave the game",size_hint = [1,0.3],auto_dismiss = False,
                                 events_callback = self.Exittoapp,text_button_ok = "No",text_button_cancel = "Yes")
        Exit_dialogue.open()

#Function that will Exit Game when the game overs
    def ExitCallback(self,text_of_selection,popup_widget):
        self.parent.current = "StartOptions"
        pass

    def mycallback(self,text_of_selection,popup_widget):
        print(self.app)
        SlipsApp.decrement(self.app)
        print("My callback Playscreen",self.app)
        print("self",self)

# Function for display sneak peak (Ad Advantage)
    def sneak_peak(self):
        sneak_dialog = MDDialog(title = "Sneak Peak",text = "You = [ "+str(self.player_1[0])+" "+str(self.player_1[1])+" "+str(self.player_1[2])+" "+str(self.player_1[3])+" ]\n\n"
                                +"Player 2 = [ "+str(self.player_2[0])+" "+str(self.player_2[1])+" "+str(self.player_2[2])+" "+str(self.player_2[3])+" ]\n\n"
                                +"Player 3 = [ "+str(self.player_3[0])+" "+str(self.player_3[1])+" "+str(self.player_3[2])+" "+str(self.player_3[3])+" ]\n\n"
                                +"Player 4 = [ "+str(self.player_4[0])+" "+str(self.player_4[1])+" "+str(self.player_4[2])+" "+str(self.player_4[3])+" ]\n\n"
                                ,size_hint = [1,.6],pos_hint = {"top":0.8},auto_dismiss = False,events_callback =self.mycallback)
        sneak_dialog.open()

    def VideoAdPopup(self):
        video_dialog = MDDialog(title = "Watch an Ad",text = "Watch a small video Ad In Exchange of Reward",size_hint = [1,0.3],
                                auto_dismiss = False,text_button_ok = "Ok",text_button_cancel = "Cancel",events_callback = self.videocallback)
        video_dialog.open()

    def videocallback(self,text_of_Selection,popup_widget):
        if(text_of_Selection == "Ok"):
            SlipsApp.ads.show_rewarded_ad()
        else:
            print("User did not want to watch ad")

#Function for exiting Game when the user wants to leave between the play
    def Exittoapp(self,text_of_selection,popup_widget):
        if(text_of_selection == "Yes"):
            self.parent.current = "StartOptions"
        else:
            print("user didn't leave the match")

#The Whole process that loopes after User sends the slip
    def CPU_operate(self):
        self.choose(self.player_2)
        self.pass_slip(self.chosen_slip,self.player_2,self.player_3)
        self.iswinner(self.player_2,"Player 2")
        if self.confirm == 1:
            return
        self.choose(self.player_3)
        self.pass_slip(self.chosen_slip, self.player_3, self.player_4)
        self.iswinner(self.player_3,"Player 3")
        if self.confirm == 1:
            return
        self.choose(self.player_4)
        self.pass_slip(self.chosen_slip, self.player_4, self.player_1)
        time.sleep(0.5)
        self.iswinner(self.player_4,"Player 4")
        if self.confirm == 1:
            return
        self.iswinner(self.player_1,"You")
        if self.confirm == 1:
            return

    def on_pre_leave(self):
        SlipsApp.ads.show_interstitial()

#Main App for Custom screen play Arena
class Customscreen(Screen):
    Cslips = ListProperty([''] * 4)
    Player_1 = ListProperty([''] * 4)
    Player_2 = ListProperty([''] * 4)
    Player_3 = ListProperty([''] * 4)
    Player_4 = ListProperty([''] * 4)
    chose_slip = []
    sumlist = []
    confirm = 0
    level = 0
    count_hard = 0

    def __init__(self, **kw):
        super().__init__(**kw)
        self.app = MDApp.get_running_app()

    def Input_append(self):
        for i in range(0, 4):
            for j in range(0, 3):
                self.Cslips.append(self.Cslips[i])

    def Distribute(self):
        self.Player_1.clear()
        self.Player_2.clear()
        self.Player_3.clear()
        self.Player_4.clear()
        for i in range(0, 4):
            self.Player_1.append(random.choice(self.Cslips))
            self.Cslips.remove(self.Player_1[i])
            self.Player_2.append(random.choice(self.Cslips))
            self.Cslips.remove(self.Player_2[i])
            self.Player_3.append(random.choice(self.Cslips))
            self.Cslips.remove(self.Player_3[i])
            self.Player_4.append(random.choice(self.Cslips))
            self.Cslips.remove(self.Player_4[i])
        self.Player_1.append("")

    def on_pre_enter(self):
        self.Cslips = CustomSlips.customslips
        self.level = difficulty_custom.count
        self.confirm = 0
        self.count_hard = 0
        print("count_hard",self.count_hard)
        print("on pre enter",self.Cslips)
        self.Input_append()
        print("After inputappend",self.Cslips)
        self.Distribute()
        print("after Distribute",self.Cslips)
        print("Player 1",self.Player_1)
        print("player 2",self.Player_2)
        print("player 3",self.Player_3)
        print("player 4",self.Player_4)
        SlipsApp.ads.request_interstitial()

    def Pass_slip(self,chose_slip,sender= [],reciever = []):
        reciever.append(reciever[3])
        reciever[3] = self.chose_slip
        sender.remove(self.chose_slip)

    def Iswinner(self,player = [],whoiswinner=" "):
        if(player.count(player[0])==4):
            print(whoiswinner + " Won")
            self.confirm = 1
            print(whoiswinner)
            self.Show_Winner(whoiswinner)

    def Show_Winner(self,winner = " "):
        my_dialog = MDDialog(title="Game Over", text=winner + " Won The Game", size_hint=[1, .4], auto_dismiss=False,
                             events_callback=self.ExitCallback)
        my_dialog.open()

    def ExitCallback(self,text_of_selection,popup_widget):
        self.parent.current = "StartOptions"
        pass

    def Choose(self,Chooser = []):
        if self.level == 2:
            if (self.count_hard < 15):
                self.level = 1
                self.Choose(Chooser)
            for i in range(0, len(Chooser)):
                self.sumlist.append(Chooser.count(Chooser[i]))
            self.chose_slip = Chooser[self.sumlist.index(min(self.sumlist))]
            self.sumlist.clear()

        elif self.level == 1:
            if (self.count_hard < 15):
                self.count_hard += 1
                self.chose_slip = random.choice(Chooser)
            else:
                self.level = 2
                self.Choose(Chooser)
        else:
            print("Hardest Removed")

    def Default_operate(self):
        self.Choose(self.Player_2)
        self.Pass_slip(self.chose_slip,self.Player_2,self.Player_3)
        self.Iswinner(self.Player_2,"Player 2")
        if self.confirm == 1:
            return
        self.Choose(self.Player_3)
        self.Pass_slip(self.chose_slip, self.Player_3, self.Player_4)
        self.Iswinner(self.Player_3,"Player 3")
        if self.confirm == 1:
            return
        self.Choose(self.Player_4)
        self.Pass_slip(self.chose_slip, self.Player_4, self.Player_1)
        time.sleep(0.5)
        self.Iswinner(self.Player_4,"Player 4")
        if self.confirm == 1:
            return
        self.Iswinner(self.Player_1,"You")
        if self.confirm == 1:
            return

    def Sneak_Peak(self):
        sneak_dialog = MDDialog(title = "Sneak Peak",text = "You = [ "+str(self.Player_1[0])+" "+str(self.Player_1[1])+" "+str(self.Player_1[2])+" "+str(self.Player_1[3])+" ]\n\n"
                                +"Player 2 = [ "+str(self.Player_2[0])+" "+str(self.Player_2[1])+" "+str(self.Player_2[2])+" "+str(self.Player_2[3])+" ]\n\n"
                                +"Player 3 = [ "+str(self.Player_3[0])+" "+str(self.Player_3[1])+" "+str(self.Player_3[2])+" "+str(self.Player_3[3])+" ]\n\n"
                                +"Player 4 = [ "+str(self.Player_4[0])+" "+str(self.Player_4[1])+" "+str(self.Player_4[2])+" "+str(self.Player_4[3])+" ]\n\n"
                                ,size_hint = [1,.6],pos_hint = {"top":0.8},auto_dismiss = False,events_callback =self.mycallback)
        sneak_dialog.open()

    def mycallback(self,text_of_selection,popup_widget):
        SlipsApp.decrement(self.app)
        print("Custom Slips app",self.app)
        print("Screen self",self)

    def VideoAdPopup(self):
        video_dialog = MDDialog(title = "Watch an Ad",text = "Watch a small video Ad In Exchange of Reward",size_hint = [1,0.3],
                                auto_dismiss = False,text_button_ok = "Ok",text_button_cancel = "Cancel",events_callback = self.videocallback)
        video_dialog.open()

    def videocallback(self,text_of_Selection,popup_widget):
        if(text_of_Selection == "Ok"):
            SlipsApp.ads.show_rewarded_ad()
        else:
            print("User did not want to watch ad")

    def Exit_Button(self):
        Exit_Dialogue = MDDialog(title="Leave Game", text="Are you sure!! you want to leave the game",
                                 size_hint=[1, 0.3], auto_dismiss=False,
                                 events_callback=self.Exit_to_app, text_button_ok="No", text_button_cancel="Yes")
        Exit_Dialogue.open()

    def Exit_to_app(self,text_of_selection,popup_widget):
        if (text_of_selection == "Yes"):
            self.parent.current = "StartOptions"
        else:
            print("user didn't leave the match")

    def on_pre_leave(self, *args):
        SlipsApp.ads.show_interstitial()

#The first Screen That appear on the screen
class MenuScreen(Screen):

    def ExitDialog(self):
        Exit_dialog = MDDialog(title = "Exit Game", text = "Are You Sure! You Want To Exit",size_hint = [1,0.3],auto_dismiss = False,
                               events_callback = self.ExitGame,text_button_cancel = "Yes",text_button_ok = "No")
        Exit_dialog.open()

    def ExitGame(self,text_of_selection,popup_widget):
        if(text_of_selection == "Yes"):
            print(text_of_selection)
            MDApp.get_running_app().stop()
        else:
            print("No Button Pressed")

#The Main Kv file included in the python
Builder.load_string('''
#:import SlideTransition kivy.uix.screenmanager.SlideTransition
#.import MDRectangleFlatIconButton kivymd.uix.button.MDRectangleFlatIconButton
#.import MDRectangleFlatButton kivymd.uix.button.MDRectangleFlatButton
#.import MDTextField kivymd.textfields.MDTextField
#.import MaterialLabel kivymd.uix.label 
#.import MDTextButton kivymd.uix.button.MDTextButton
#.import MDIconButton kivymd.uix.button.MDIconButton

<intro>:
    id : screen_mgr
    MenuScreen:
    Instructions:
    Multiplayer:
    StartOptions:
    CustomSlips:
    DefaultSlips:
    PlayScreen:
    Customscreen:
    difficulty:
    difficulty_custom:
    AboutScreen:
    Credit:
    Challenge:
    ChallengeC:
<MenuScreen>:
    name:"Menu"
    FloatLayout:
        canvas:
            Rectangle:
                pos: self.pos
                size: self.size
                source: "paper white.png"
            
        BoxLayout:
            orientation: "vertical"
            pos_hint: {'center_x': 0.4, 'top':0.70}
            size_hint: 0.80, 0.55
            MDRectangleFlatIconButton:
                text:"Play Game"
                icon:"gamepad-variant"
                #font_size: 0.10*self.height
                theme_text_color:"Custom"
                text_color : [0,0,0,1]
                size_hint: 0.7,4.0
                pos_hint:{"center_x":0.5}
                on_release:
                    app.root.transition = SlideTransition(direction = "left")
                    #app.root.current = "StartOptions"
                    app.root.previous = "Menu"
                    app.root.Change_Screen("StartOptions")

            Label:

            MDRectangleFlatIconButton:
                text: "How To Play"
                icon:"cellphone-information"
                #font_size: 0.10*self.height
                theme_text_color:"Custom"
                text_color : [0,0,0,1]
                size_hint: 0.7,4.0
                pos_hint:{"center_x":0.5}
                on_release:
                    app.root.transition = SlideTransition(direction = "left")
                    #app.root.current = "Instruction"
                    app.root.previous = "Menu"
                    app.root.Change_Screen("Instruction")
            Label:
                    
            MDRectangleFlatIconButton:
                text: "Multiplayer"
                icon:"account-group"
                #font_size: 0.10*self.height
                theme_text_color:"Custom"
                text_color : [0,0,0,1]
                size_hint: 0.7,4.0
                pos_hint:{"center_x":0.5}
                on_release:
                    app.root.transition = SlideTransition(direction = "left")
                    #app.root.current = "Multiplayer"
                    app.root.previous = "Menu"
                    app.root.Change_Screen("Multiplayer")
            Label:
                
            MDRectangleFlatIconButton:
                text:"About Us"
                icon:"account-card-details-outline"
                #font_size: 0.10*self.height
                theme_text_color: "Custom"
                text_color: [0,0,0,1]
                size_hint: 0.7,4.0
                pos_hint:{"center_x":0.50}
                on_release:
                    app.root.transition = SlideTransition(direction = "left")
                    #app.root.current = "About"
                    app.root.previous = "Menu"
                    app.root.Change_Screen("About")
            Label:
            
            MDRectangleFlatIconButton:
                text:"Credits"
                icon:"account-heart"
                #font_size: 0.10*self.height
                theme_text_color: "Custom"
                text_color: [0,0,0,1]
                size_hint: 0.7,4.0
                pos_hint:{"center_x":0.50}
                on_release:
                    app.root.transition = SlideTransition(direction = "left")
                    #app.root.current = "Credit"
                    app.root.previous = "Menu"
                    app.root.Change_Screen("Credit")
            Label:
            
            MDRectangleFlatIconButton:
                text:"Exit Game"
                icon:"exit-run"
                #font_size: 0.10*self.height
                theme_text_color: "Custom"
                text_color: [0,0,0,1]
                size_hint: 0.7,4.0
                pos_hint:{"center_x":0.5}
                on_release:
                    root.ExitDialog()
                
<AboutScreen>:
    name:"About"
    FloatLayout:
        canvas.before:
            Rectangle:
                pos:self.pos
                size: self.size
                source: "About.png"
        MDRectangleFlatIconButton:
            text:"Follow"
            icon:"heart-multiple"
            pos_hint:{"center_x": 0.7,"top":0.15}
            size_hint: 0.35,0.05
            on_release:
                root.Follow()
        MDIconButton:
            icon:"keyboard-backspace"
            pos_hint: {"center_x":0.15,"top":0.98}
            on_release:
                app.root.transition = SlideTransition(direction = "right")
                app.root.current = "Menu"

<Credit>:
    name: "Credit"
    FloatLayout:
        canvas.before:
            Rectangle:
                size:self.size
                pos: self.pos
                source:"credits.png"
        MDTextButton:
            text:"Back"
            #font_size: 30
            pos_hint: {"center_x":0.4,"top": 0.3} 
            on_release:
                app.root.transition = SlideTransition(direction = "right")
                app.root.current = "Menu"

    BoxLayout:
        orientation:"vertical"
        pos_hint: {'center_x': 0.4, 'top':0.65}
        size_hint: 0.40, 0.3
        spacing:30   
        MDTextButton:
            text:"RawPixel"
            #font_size: 30
            pos_hint :{"center_x":0.5,"top":0.6}
            on_release: root.Rawpixel()
        
        MDTextButton:
            text:"Viznezh"
            #font_size: 30
            pos_hint :{"center_x":0.5,"top":0.3}
            on_release: root.Viznezh()
                      
<Instructions>:
    name: "Instruction"
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size 
            source: "howtoplay.png"
    Label:
        text: "Back"
        color: 0,0,0,1
        #font_size: 20
        pos_hint: {"center_x":0.90,"top": 0.90}
        size_hint: 0.2,0.2
        on_touch_down:
            app.root.transition = SlideTransition(direction = "right")
            app.root.current = "Menu"
            
<Multiplayer>:
    name:"Multiplayer"
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: "multiplayer.png"
    Label:
        text: "Back"
        color: 0,0,0,1
        #font_size: 20
        pos_hint: {"center_x":0.90,"top": 0.99}
        size_hint: 0.2,0.2
        on_touch_down:
            app.root.transition = SlideTransition(direction = "right")
            app.root.current = "Menu"  
                              
<StartOptions>:
    name: "StartOptions"
    canvas:
        Color:
            rgba: 0,0,0,1
        Rectangle:
            pos: self.pos
            size: self.size
    BoxLayout:
        orientation: "vertical"
        pos_hint: {'center_x':0.4,'top': 0.8}
        size_hint: 0.60,0.50
        MDRectangleFlatIconButton:
            text:"Custom Slips"
            icon:"cards-outline"
            size_hint:1,0.9
            pos_hint:{'center_x':0.5,'top': 0.75}
            #font_size:0.35*self.height
            md_bg_color:[0,0,0,1]
            on_release:
                app.root.transition = SlideTransition(direction ='left')
                #app.root.current = "CustomSlips"
                app.root.previous = "StartOptions"
                app.root.Change_Screen("CustomSlips")
        Label:

        MDRectangleFlatIconButton:
            text:"Default Slips"
            icon:"cards-playing-outline"
            size_hint:1,0.9
            pos_hint:{"center_x":0.5,"top":0.65}
            #font_size:0.35*self.height
            md_bg_color:[0,0,0,1]
            on_release:
                app.root.transition = SlideTransition(direction = "left")
                #app.root.current = "DefaultSlips"
                app.root.previous = "StartOptions"
                app.root.Change_Screen("DefaultSlips")
        Label:

        MDRectangleFlatIconButton:
            text: "Go Back"
            icon:"keyboard-backspace"
            size_hint:1,0.9
            pos_hint:{"center_x":0.5,"top":0.55}
            #font_size:0.35*self.height
            md_bg_color:[0,0,0,1]
            on_release:
                app.root.transition = SlideTransition(direction = "right")
                app.root.current = "Menu"

<CustomSlips>:
    name: "CustomSlips"
    canvas.before:
        Color:
            rgba: 0,0,0,1
        Rectangle:
            pos: self.pos
            size: self.size
    BoxLayout:
        orientation: "vertical"
        size_hint: 0.75,0.75
        pos_hint :{"center_x":0.5,"top":0.9}
        MDTextField:
            hint_text:"Slip 1"
            helper_text:"This Field is required"
            helper_text_mode:"on_error"
            required: True
            active_color: [0,0,0,.2980392156862745]
            id: slip1
            size: 50,50
            #font_size:25
            multiline : False
       
        MDTextField:
            hint_text:"Slip 2"
            helper_text:"This Field is required"
            helper_text_mode:"on_error"
            required: True
            active_color: [0,0,0,.2980392156862745]
            id: slip2
            size: 50,50
            #font_size:25
            multiline : False
        
        MDTextField:
            hint_text:"Slip 3"
            helper_text:"This Field is required"
            helper_text_mode:"on_error"
            required: True
            active_color: [0,0,0,.2980392156862745]
            id: slip3
            size: 50,50
            #font_size:25
            multiline : False

        MDTextField:
            hint_text:"Slip 4"
            helper_text:"This Field is required"
            helper_text_mode:"on_error"
            required: True
            theme_text_color:"Custom"
            text_color: 0,0,1,1
            active_color: [0,0,0,.2980392156862745]
            id: slip4
            size: 50,50
            #font_size:25
            multiline : False
        MDLabel:
            text:"Each Slip Must Be Distinct and Unique"
            theme_text_color:"Custom"
            text_color: 255,28,110,1
            font_size: 14
            
        MDRectangleFlatIconButton:
            pos_hint: {"center_x":0.5,"top":0.4}
            size_hint: 0.7,1.1
            text:"Write On Slips"
            icon:"typewriter"
            on_release:
                root.customslips.append(slip1.text)
                root.customslips.append(slip2.text)
                root.customslips.append(slip3.text)
                root.customslips.append(slip4.text)
                print(root.customslips)
                app.root.transition = SlideTransition(direction = 'left')
                #app.root.current = "CLevel"
                app.root.previous = "CustomSlips"
                app.root.Change_Screen("CLevel")

        Label:

        MDRectangleFlatIconButton:
            text: "Go Back"
            icon: "keyboard-backspace"
            pos_hint: {"center_x":0.5,"top":0.1}
            size_hint: 0.7,1.1
            on_release:
                app.root.transition = SlideTransition(direction = "right")
                app.root.current = "StartOptions"
                
<DefaultSlips>:
    name: "DefaultSlips"
    canvas.before:
        Color:
            rgba: 0,0,0,1
        Rectangle:
            pos: self.pos
            size: self.size
    BoxLayout:
        orientation: "vertical"
        size_hint: 0.65,0.50
        pos_hint:{"center_x":0.4,"top":0.80}
        
        MDRectangleFlatIconButton:
            text: "Flowers"
            icon: "flower"
            size_hint: 0.7,4
            pos_hint:{"center_x":0.5}
            on_release:
                root.Flowerscopy()
                print("after function call",root.playlist)
                app.root.transition = SlideTransition(direction = 'left')
                #app.root.current = "Level"
                app.root.previous = "DefaultSlips"
                app.root.Change_Screen("Level")
        Label:

        MDRectangleFlatIconButton:
            text: "Animals"
            icon: "elephant"
            size_hint: 0.7,4.0
            pos_hint:{"center_x":0.5}
            on_release:
                root.AnimalsCopy()
                app.root.transition = SlideTransition(direction = 'left')
                #app.root.current = "Level"
                app.root.previous = "DefaultSlips"
                app.root.Change_Screen("Level")
        Label:

        MDRectangleFlatIconButton:
            text: "Cartoons"
            icon: "emoticon-cool"
            size_hint: 0.7,4.0
            pos_hint:{"center_x":0.5}
            on_release:
                root.CartoonCopy()
                app.root.transition = SlideTransition(direction = 'left')
                #app.root.current = "Level"
                app.root.previous = "DefaultSlips"
                app.root.Change_Screen("Level")
        Label:

        MDRectangleFlatIconButton:
            text: "Fruits"
            icon: "fruit-cherries"
            size_hint: 0.7,4.0
            pos_hint:{"center_x":0.5}
            on_release:
                root.FruitsCopy()
                app.root.transition = SlideTransition(direction = 'left')
                #app.root.current = "Level"
                app.root.previous = "DefaultSlips"
                app.root.Change_Screen("Level")
        Label:

        MDRectangleFlatIconButton:
            text: "Cars"
            icon: "car-estate"
            size_hint: 0.7,4.0
            pos_hint:{"center_x":0.5}
            on_release:
                root.CarsCopy()
                app.root.transition = SlideTransition(direction = 'left')
                #app.root.current = "Level"
                app.root.previous = "DefaultSlips"
                app.root.Change_Screen("Level")
        Label:

        MDRectangleFlatIconButton:
            text: "Go Back"
            icon: "keyboard-backspace"
            size_hint: 0.7,4.0
            pos_hint:{"center_x":0.5}
            on_release:
                app.root.transition = SlideTransition(direction = "right")
                app.root.current = "StartOptions"

<difficulty>:
    name:"Level"
    canvas:
        Color:
            rgba: 0,0,0,1
        Rectangle:
            pos: self.pos
            size: self.size
    FloatLayout:
        pos_hint:{"top":1}
        size_hint: 1,0.3
        
        MDLabel:
            text:"Select Difficulty Level"
            theme_text_color:"Custom"
            text_color: 0,0,1,1
            halign:"center"
            font_style:"Caption"
            #font_size: 25
    
    BoxLayout:
        orientation:"vertical"
        canvas:    
        pos_hint : {"center_x": 0.5,"top":0.7}
        size_hint: 0.4,0.4
        MDRectangleFlatButton:
            text: "Easy"
            size_hint: 0.7,1.5
            pos_hint:{"center_x":0.5}
            on_release:
                root.easy()
                print("root.count",root.count)
                app.root.transition = SlideTransition(direction = "left")
                app.root.previous = "Level"
                app.root.Change_Screen("PlayScreen")
        Label:
                 
        Label:
        
        MDRectangleFlatButton:
            text: "Hard"
            size_hint: 0.7,1.5
            pos_hint:{"center_x":0.5}
            on_release:
                root.hard()
                print("root.count",root.count)
                app.root.transition = SlideTransition(direction = "left")
                #app.root.current = "Challenge"
                app.root.previous = "Level"
                app.root.Change_Screen("Challenge")
 
<Difficulty_custom>:
    name:"CLevel"
    canvas:
        Color:
            rgba: 0,0,0,1
        Rectangle:
            pos: self.pos
            size: self.size
    FloatLayout:
        pos_hint:{"top":1}
        size_hint: 1,0.3

        MDLabel:
            text:"Select Difficulty Level"
            theme_text_color:"Custom"
            text_color: 0,0,1,1
            halign:"center"
            font_style:"Caption"
            #font_size: 25
            
    BoxLayout:
        orientation:"vertical"
        canvas:    
        pos_hint : {"center_x": 0.5,"top":0.7}
        size_hint: 0.4,0.4
        MDRectangleFlatButton:
            text: "Easy"
            size_hint: 0.7,1.5
            pos_hint:{"center_x":0.5}
            on_release:
                root.easy()
                print("root.count",root.count)
                app.root.transition = SlideTransition(direction = "left")
                app.root.previous = "CLevel"
                app.root.Change_Screen("Customscreen")
        Label:
                 
        Label:
        
        MDRectangleFlatButton:
            text: "Hard"
            size_hint: 0.7,1.5
            pos_hint:{"center_x":0.5}
            on_release:
                root.hard()
                print("root.count",root.count)
                app.root.transition = SlideTransition(direction = "left")
                #app.root.current = "Challengec"
                app.root.previous = "CLevel"
                app.root.Change_Screen("Challengec")
       
<Challenge>:
    name:"Challenge"
    FloatLayout:
        canvas.before:
            Rectangle:
                size: self.size
                pos: self.pos
                source:"challenge.png"
        MDRectangleFlatIconButton:
            text:"Let's Go !!"
            icon:"arrow-right-bold"
            size_hint:0.4,0.1
            pos_hint:{"center_x":0.5,"top":0.2}
            on_release:
                app.root.transition = SlideTransition(direction = "left")
                app.root.current = "PlayScreen"    

<ChallengeC>:
    name:"Challengec"
    FloatLayout:
        canvas.before:
            Rectangle:
                size: self.size
                pos: self.pos
                source:"challenge.png"
        MDRectangleFlatIconButton:
            text:"Let's Go !!"
            icon:"arrow-right-bold"
            size_hint:0.4,0.1
            pos_hint:{"center_x":0.5,"top":0.2}
            on_release:
                app.root.transition = SlideTransition(direction = "left")
                app.root.current = "Customscreen"
                                            
<PlayScreen>:
    name: 'PlayScreen'
    canvas.before:
        Rectangle:
            pos:self.pos
            size:self.size
            source:"Background.jpg"  

    MDToolbar:
        title: "The Paper Game"
        right_action_items: [["video-outline",lambda x: root.VideoAdPopup()],["eye", lambda x: root.sneak_peak() if app.Num>0 else root.VideoAdPopup()],["exit-to-app", lambda x: root.ExitButton()]]
        type:"top"  
        pos_hint:{"top":1}
    
    MDLabel:
        text:"  Sneak Peak : "+str(app.Num)
        pos_hint:{"top":1.35}
        
    GridLayout:
        cols:2
        pos_hint:{"center_x":0.5,"top":0.8}
        size_hint:0.9,0.6
        spacing : 10
        
        Button:
            text: root.player_1[0]
            color : 0,0,0,1
            background_normal :"slip4.png"
            allow_stretch:True
            keep_ratio:False
            on_release:
                root.chosen_slip = root.player_1[0]
                root.pass_slip(root.chosen_slip,root.player_1,root.player_2)
                root.iswinner(root.player_1,"You")
                root.CPU_operate() 
            
        Button:
            text: root.player_1[1]
            color: 0,0,0,1
            background_normal :"slip3.png"
            allow_stretch:True
            keep_ratio:False
            on_release:
                root.chosen_slip = root.player_1[1]
                root.pass_slip(root.chosen_slip,root.player_1,root.player_2)
                root.iswinner(root.player_1,"You")
                root.CPU_operate()
        
        Button:
            text:root.player_1[2]
            color: 0,0,0,1
            background_normal:"slip3.png"
            allow_stretch:True
            keep_ratio:False
            on_release:
                root.chosen_slip = root.player_1[2]
                root.pass_slip(root.chosen_slip,root.player_1,root.player_2)
                root.iswinner(root.player_1,"You")
                root.CPU_operate()
                
        Button:
            text: root.player_1[3]
            color: 0,0,0,1
            background_normal : "slip1.png" 
            allow_stretch:True
            keep_ratio:False  
            on_release:
                root.chosen_slip = root.player_1[3]
                root.pass_slip(root.chosen_slip,root.player_1,root.player_2)
                root.iswinner(root.player_1,"You")
                root.CPU_operate()
            
<Customscreen>:
    name:"Customscreen"
    canvas.before:
        Rectangle:
            pos:self.pos
            size:self.size
            source:"Background.jpg"
            
    MDToolbar:
        title: "The Paper Game"
        right_action_items: [["video-outline",lambda x: root.VideoAdPopup()],["eye", lambda x: root.Sneak_Peak() if app.Num>0 else root.VideoAdPopup()],["exit-to-app", lambda x: root.Exit_Button()]]
        type:"top"  
        pos_hint:{"top":1}
        
    MDLabel:
        text:"  Sneak Peak : "+str(app.Num)
        pos_hint:{"top":1.35}
        
    GridLayout:
        cols:2
        pos_hint:{"center_x":0.5,"top":0.8}
        size_hint:0.9,0.6
        spacing : 10
        
        Button:
            text: root.Player_1[0]
            color : 0,0,0,1
            background_normal :"slip4.png"
            allow_stretch:True
            keep_ratio:False
            on_release:
                root.chose_slip = root.Player_1[0]
                root.Pass_slip(root.chose_slip,root.Player_1,root.Player_2)
                root.Iswinner(root.Player_1,"You")
                root.Default_operate() 
            
        Button:
            text: root.Player_1[1]
            color: 0,0,0,1
            background_normal :"slip3.png"
            allow_stretch:True
            keep_ratio:False
            on_release:
                root.chose_slip = root.Player_1[1]
                root.Pass_slip(root.chose_slip,root.Player_1,root.Player_2)
                root.Iswinner(root.Player_1,"You")
                root.Default_operate()
        
        Button:
            text:root.Player_1[2]
            color: 0,0,0,1
            background_normal:"slip3.png"
            allow_stretch:True
            keep_ratio:False
            on_release:
                root.chose_slip = root.Player_1[2]
                root.Pass_slip(root.chose_slip,root.Player_1,root.Player_2)
                root.Iswinner(root.Player_1,"You")
                root.Default_operate()
        
        Button:
            text: root.Player_1[3]
            color: 0,0,0,1
            background_normal : "slip1.png" 
            allow_stretch:True
            keep_ratio:False  
            on_release:
                root.chose_slip = root.Player_1[3]
                root.Pass_slip(root.chose_slip,root.Player_1,root.Player_2)
                root.Iswinner(root.Player_1,"You")
                root.Default_operate()      
'''
)

#Main App Class
class SlipsApp(MDApp):

    # These are our Admob Ad IDs I kept these secrets.
    APP = "ca-app-pub-XXXXXXXXXXXXXXXXXXXXXXXX" 
    BANNER = "ca-app-pub-XXXXXXXXXXXXXXXXXXXXXXXX"
    INTERSTITIAL = "ca-app-pub-XXXXXXXXXXXXXXXXXXXXXXXX"
    REWARDED_VIDEO = "ca-app-pub-XXXXXXXXXXXXXXXXXXXXXXXX"
    TEST_DEVICE_ID = "XXXXXXXXXXXXXXXXXXXXXXXX"
    # Creating Ad Instance
    ads = KivMob(APP)
    #Number oF Rewards(SneakPeak)
    Num = NumericProperty(1)
    
    def __init__(self, *args,**kwargs):
        self.theme_cls.theme_style = "Dark"
        super().__init__(**kwargs)
        self.reward = Rewards_Handler(self)
        print("Slipsapp init",self)

    #Build Function
    def build(self):
        # Loading Ads
        self.ads.add_test_device(self.TEST_DEVICE_ID)
        self.ads.new_banner(self.BANNER, False)
        self.ads.new_interstitial(self.INTERSTITIAL)
        self.ads.request_banner()
        self.ads.set_rewarded_ad_listener(self.reward)
        self.ads.load_rewarded_ad(self.REWARDED_VIDEO)
        self.ads.show_banner()
        return intro()

    @staticmethod
    def decrement(element):
        element.reward.decrementReward()
        print("decrement reward element",element)

    def load_video(self):
        self.ads.load_rewarded_ad(self.REWARDED_VIDEO)

#Class For Handling Rewards Callback Functions
class Rewards_Handler(RewardedListenerInterface):
    def __init__(self,other):
        self.game = other

    #Overriding Rewards Callback Functions
    def on_rewarded(self, reward_name, reward_amount):
        self.game.Num += 1
        print("User Given 1 reward ",self.game.Num)
        print("On rewarded self",self)
        print("game object",self.game)

    def on_rewarded_video_ad_failed_to_load(self, error_code):
        if(error_code == 0):
            Error_zero = MDDialog(title = "Load Error!",text = "Something Went Wrong, Please Try Again",size_hint = [1,0.4],auto_dismiss = False,
                                  events_callback = self.callback)
            Error_zero.open()
        elif(error_code == 1):
            Error_One = MDDialog(title="Load Error!",text = "Please Report To the Developer Email -> Akgupta0777@gmail.com",size_hint=[1,0.4],
                                 auto_dismiss = False,events_callback = self.callback)
            Error_One.open()
        elif(error_code == 2):
            Error_Two = MDDialog(title = "Load_Error!",text = "Make Sure You Have Internet Access!",size_hint=[1,0.4],
                                 auto_dismiss = False,events_callback =self.callback)
            Error_Two.open()
        else:
            Error_three = MDDialog(title = "Load Error!",text = "Please Try Again",size_hint = [1,0.4],auto_dismiss = False,
                                   events_callback=self.callback)
            Error_three.open()

    def callback(self,text_of_selection,popup_widget):
        pass

    def on_rewarded_video_ad_started(self):
        SlipsApp().load_video()

    def on_rewarded_video_ad_closed(self):
        print("User Closed the video ")

    def on_rewarded_video_ad_left_application(self):
        pass

    def on_rewarded_video_ad_completed(self):
        self.on_rewarded("Reward","1")

    def decrementReward(self):
        self.game.Num -= 1
        print("Deducted By Rewards_Handler ",self.game.Num)
        print("Decrement reward",self)

if __name__ == "__main__":
    SlipsApp().run()
