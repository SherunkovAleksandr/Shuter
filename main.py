from pygame import*                             #подключение библиотек
from random import randint
class GameSprite(sprite.Sprite):                                        #классы для создания спрайтов и стен
    def init (self,player_image,player_x,player_y,player_speed):
        super(). init ()
        self.image=transform.scale(image.load(player_image),(50,50))
        self.speed=player_speed
        self.rect=self.image.get_rect()
        self.rect.x=player_x
        self.rect.y=player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
    
class Player(GameSprite):
    def update(self):
        keys=key.get_pressed()
        if keys[K_LEFT] and self.rect.x>5:
            self.rect.x-=self.speed
        if keys[K_RIGHT] and self.rect.x<win_width-80:
            self.rect.x+=self.speed
        if keys[K_UP] and self.rect.y>5:
            self.rect.y-=self.speed
        if keys[K_DOWN] and self.rect.y<win_height-80:
            self.rect.y+=self.speed
    def fire(self):
        bullet=Bullet2('bullet.jpg',self.rect.centerx,self.rect.top,-17)
        bullets.add(bullet)
    def fire2(self):
        bullet=Bullet3('bullet.jpg',self.rect.centerx,self.rect.top,17)
        bullets.add(bullet)

    

class Bullet(GameSprite):
    def update(self):
        self.rect.x+=self.speed
        if self.rect.x>=570:
            self.kill()
class Bullet2(GameSprite):
    def update(self):
        self.rect.y+=self.speed
        if self.rect.y<0:
            self.kill()          
class Bullet3(GameSprite):
    def update(self):
        self.rect.y+=self.speed
        if self.rect.y>700:
            self.kill()  
class Enemy_1(GameSprite):
    def update(self):
        if self.rect.y<=100:
            self.direction='right'
        if self.rect.y>=win_width-300:
            self.direction='left'
        
        if self.direction=='left':
            self.rect.y-=self.speed
        else:
            self.rect.y+=self.speed
    def fire_1(self):
        bullet=Bullet('bullet.jpg',self.rect.centerx,self.rect.top,17)
        bullets.add(bullet)
        
class Enemy_2(GameSprite):
    def update(self):
        if self.rect.y<=100:
            self.direction='right'
        if self.rect.y>=win_width-500:
            self.direction='left'
        
        if self.direction=='left':
            self.rect.y-=self.speed
        else:
            self.rect.y+=self.speed
    def fire_2(self):
        bullet=Bullet('bullet.jpg',self.rect.centerx,self.rect.top,17)
        bullets.add(bullet)

class Enemy_3(GameSprite):
    def update(self):
        if self.rect.x<=110:
            self.direction='right'
        if self.rect.x>=win_width-500:
            self.direction='left'
        
        if self.direction=='left':
            self.rect.x-=self.speed
        else:
            self.rect.x+=self.speed
    def fire_3(self):
        bullet=Bullet('bullet.jpg',self.rect.centerx,self.rect.top,17)
        bullets.add(bullet)

    

class Wall(sprite.Sprite):
    def init(self,color_1,color_2,color_3,wall_x,wall_y,wall_width,wall_height):
        super().init()
        self.color_1=color_1
        self.color_2=color_2
        self.color_3=color_3
        self.width=wall_width
        self.height=wall_height
        self.image=Surface((self.width,self.height))
        self.image.fill((color_1,color_2,color_3))
        self.rect=self.image.get_rect()
        self.rect.x=wall_x
        self.rect.y=wall_y
    def draw_wall(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

win_width=700
win_height=700
game=True
finish=False
FPS=60
clock=time.Clock()

font.init()
font=font.Font(None,70)
win=font.render('YOU WIN',True,(255,25,0))
lose=font.render('YOU LOSE',True,(180,0,0))

window=display.set_mode((700,700))              #игровое поле
display.set_caption('main.py')
background=transform.scale(image.load('fon.jpg'),(700,700))

'''6'''

player=Player('player.png',50,650,4)              #создание игрока
monster_1=Enemy_1('monster.png',50,100,2)        #создание монстров
monster_2=Enemy_2('monster.png',650,50,2)     
monster_3=Enemy_3('monster.png',650,450,2)            

wall_1=Wall(51,47,47,100,100,100,200)                  #создание стен
wall_2=Wall(51,47,47,300,300,400,100)
wall_3=Wall(51,47,47,300,0,100,200)
wall_4=Wall(51,47,47,500,100,100,200)
wall_5=Wall(51,47,47,0,500,100,100)
wall_6=Wall(51,47,47,200,500,100,200)
wall_7=Wall(51,47,47,400,600,100,100)
wall_8=Wall(51,47,47,400,500,200,100)
bullets = sprite.Group()
score=1
while game:
    for e in event.get():
        if e.type==QUIT:
            game=False
        elif e.type == KEYDOWN:
            if e.key == K_UP or e.key == K_DOWN or e.key == K_LEFT or e.key == K_RIGHT:
                monster_1.fire_1()
                monster_2.fire_2()
                monster_3.fire_3()
            if e.key == K_w:
                player.fire()  
            if e.key == K_s:
                player.fire2()
                      

                
            
    if finish !=True:
        window.blit(background,(0,0))                                    #игровой цикл
        if sprite.collide_rect(player, wall_1) or sprite.collide_rect(player, wall_2) or sprite.collide_rect(player, wall_3) or sprite.collide_rect(player, wall_4) or sprite.collide_rect(player, wall_5) or sprite.collide_rect(player, wall_6) or sprite.collide_rect(player, wall_7) or sprite.collide_rect(player, wall_8):
            player.rect.x=50
            player.rect.y=650
        if sprite.collide_rect(player, monster_1) or sprite.collide_rect(player, monster_2) or sprite.collide_rect(player, monster_3):
            player.rect.x=50
            player.rect.y=650
        if sprite.spritecollide(monster_1, bullets, True) or sprite.spritecollide(monster_2, bullets, True) or sprite.spritecollide(monster_3, bullets, True):
            monster_1.kill()

        player.update()
        monster_1.update()
        monster_2.update()
        monster_3.update()
        bullets.update()
        bullets.draw(window)


        player.reset()
        monster_1.reset()
        monster_2.reset()
        monster_3.reset()

        
        monster_1.fire_2()  #
        monster_1.fire_3()

        wall_1.draw_wall()
        wall_2.draw_wall()
        wall_3.draw_wall()
        wall_4.draw_wall()
        wall_5.draw_wall()
        wall_6.draw_wall()
        wall_7.draw_wall()
        wall_8.draw_wall()
    
    clock.tick(FPS)

    display.update()
