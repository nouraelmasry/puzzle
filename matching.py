#######################what we want to do 
        ## levels of game from simple to more difficult 
        ##winning message by each level 
###############what we are doing now is understand what is object and classes and how to use it 


################question we want to ask our TA
    # should we learn oop ? and if not what to do if we meet in our tutorials they use it? how can we use what we learned to do 
######################sources 
    ### https://youtu.be/FfWpgLFMI7w   ----pygame tutorial 1 
    ###  https://youtu.be/Xpvf9lwRERU  ---pygame tutorial 2 
    ### https://youtu.be/cqopVpEWvCc   ---- classes and objects codzilla 
    ###https://youtu.be/wfcWRAxRVBA    ---- classes and object part one 
    ### https://youtu.be/WOwi0h_-dfA   ---- classes and object part two 
    ### https://youtu.be/JeznW_7DlB0   ---- oop for beginner 


import pygame as p
## pygame is a collection of a different modules 
p.init( )  # kda ae hAGA hst5dmha hekon m3molha initialize msh lazm kolma agi anadi module mo3en 23m init 

##################classes 
     # al classes de haga ana bst5dmha 34an a5tr3 data type gdeda t3mli al ana 3aizo  w 23ml initialize llfunction 
class matching :
    def __init__(self) -> None:
        self.level = 1 
        self.level_complete = False #lma ybd2 al l3ba msh hekon complte 
    def update(self):
        self.draw()
    def draw(self):
        pass 




##screen window 
screen = p.display.set_mode ([800,600])  ## hna da 3ord al shasha 34an lw mt3mltsh htft7 b3ord msh mo7dd 
# kda al code 7aslo run bs mogrd ma ft7 2fl w b al tali m7taga 25leh y2fl lma 22olo 
title = p.display.set_caption('Matching game ')
game_icon = p.image.load('e.png')
p.display.set_icon(game_icon)
##screen colour 
light_green = [204,255,153]
screen.fill(light_green)
p.display.flip()
  #################search on colout to RGB  
    ######RGB - red , green , blue
            # screen.fill(0,150,0)  #مش هيشتغل مفروض اعمل update 
        # p.display.update()
        ## higher num is 255 
        # pure green 129 will be light green 



game= matching()

#Game loop 
# while True :
#     pass   ## kda 3omri ma h3rf 23m exit l brnameg msh h3rf 25rog 34an mfesh quit

running_time = True 
while running_time:
    for i in p.event.get():   # event da module gwa pygame ae 7ds be7sl 3la 7sb fhmna l7d delw2ty 
        if i.type  == p.QUIT:
            running_time = False ## ae event he7sl gwa al l3ba he5osh 3la al loop da lw l2ah msh = Quit hefdl sh8al 
            game.update(p.event.get())
            p.quit()

    ## kda at3ml an al shasha t2fl lma hdos close l2n fe al awl al condition true f htfdl sh8ala bs lma ados 3la quit al condition hekon false w t2fl
    ## gwa al loop b2a 34an tsht8l continously
  
