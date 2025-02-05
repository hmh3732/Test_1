import pygame

pygame.init() #초기화

#화면 크기
screen_width=480
screen_height=640
screen=pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption('Memory Game')

#FPS
clock=pygame.time.Clock()

#배경 이미지 불러오기
background=pygame.image.load("D:/Python/background.png")

#캐릭터 불러오기
character=pygame.image.load("D:/Python/chracter.png")
character_size=character.get_rect().size #이미지의 크기로 구해옴
character_width=character_size[0]
character_height=character_size[1]
character_x_pos=(screen_width/2)-(character_width/2) #화면 가로의 절반 크기에 해당하는 곳에 위치
character_y_pos=screen_height-character_height #화면 세로 크기 가장 아래에 위치

#이동 좌표
to_x=0
to_y=0

#이동속도
character_speed=0.6

#적 캐릭터
enemy=pygame.image.load("D:/Python/enemy.png")
enemy_size=enemy.get_rect().size #이미지의 크기로 구해옴
enemy_width=enemy_size[0]
enemy_height=enemy_size[1]
enemy_x_pos=(screen_width/2)-(enemy_width/2) #화면 가로의 절반 크기에 해당하는 곳에 위치
enemy_y_pos=(screen_height/2)-(enemy_height/2) #화면 세로 크기 가장 아래에 위치

#폰트 정의
game_font=pygame.font.Font(None,40) #폰트 객체 생성(폰트,크기)

#총 시간
total_time=10

#시간 계산
start_ticks=pygame.time.get_ticks() #현재 tick을 받아옴

#이벤트 루프
running=True #게임 진행 중
while running:
    dt=clock.tick(60) #게임화면 초당 프레임 수
    
    #print("fps : "+str(clock.get_fps()))
    for event in pygame.event.get():
        if event.type==pygame.QUIT: #게임 강제 종료?
            running=False #게임 진행 중이 아님
            
        if event.type==pygame.KEYDOWN: #키가 눌러졌는지 확인
            if event.key==pygame.K_LEFT: #왼쪽 이동키
                to_x-=character_speed
            elif event.key==pygame.K_RIGHT: #오른쪽 이동
                to_x+=character_speed
            elif event.key==pygame.K_UP: #위로 이동
                to_y-=character_speed
            elif event.key==pygame.K_DOWN: #아래로 이동
                to_y+=character_speed
                
        if event.type==pygame.KEYUP: #방향키를 떼면 멈춤
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                to_x=0
            elif event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                to_y=0
                
    character_x_pos+=to_x*dt
    character_y_pos+=to_y*dt
    
    #가로 경계값 처리
    if character_x_pos<0:
        character_x_pos=0
    elif character_x_pos>screen_width-character_width:
        character_x_pos=screen_width-character_width
    
    #세로 경계값 처리
    if character_y_pos<0:
        character_y_pos=0
    elif character_y_pos>screen_height-character_height:
        character_y_pos=screen_height-character_height
        
    #충돌처리
    character_rect = character.get_rect()
    character_rect.left=character_x_pos
    character_rect.top=character_y_pos
    
    enemy_rect=enemy.get_rect()
    enemy_rect.left=enemy_x_pos
    enemy_rect.top=enemy_y_pos
    
    #충돌체크
    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running=False
    
            
    screen.blit(background,(0,0)) #배경그리기
    screen.blit(character,(character_x_pos, character_y_pos)) #캐릭터 그리기
    screen.blit(enemy,(enemy_x_pos,enemy_y_pos)) #적 그리기
   
   #경과 시간 계산
    elapsed_time = (pygame.time.get_ticks()-start_ticks) / 1000
    timer = game_font.render("Time: " + str(int(total_time - elapsed_time)), True, (255, 255, 255))
   #출력할 글자, True, 글자 색상
    screen.blit(timer,(10,10))
   
   #시간이 0이하면 게임 종료
    if total_time-elapsed_time<=0:
       print("타임아웃")
       running=False
   
    pygame.display.update() #게임화면 다시 그리기
    
    
#잠시 대기
pygame.time.delay(2000) # 2초 대기
    
#게임 종료
pygame.quit()