import pygame 
#(나도 코딩님의 파이게임 강의 영상을 참고하였습니다.)

pygame.init() # 초기화 (반드시 해야합니다.)

screen_width = 480 #가로
screen_height = 640 #세로
screen = pygame.display.set_mode((screen_width, screen_height))

#타이틀 설정
pygame.display.set_caption("서준이의 기모띠")# 게임 이름


#FPS
clock = pygame.time.Clock()


#배경 이미지
background = pygame.image.load("D:/python workspace/pygame_basic/background.png")

#스프라이트 불러오기
charater = pygame.image.load("D:\python workspace\pygame_basic\charater.png")
charater_size = charater.get_rect().size #이미지 크기 구해옴
charater_width = charater_size[0]
charater_height = charater_size[1]
charater_x_pos = (screen_width / 2) - (charater_width / 2) #화면 가로의 절반 크기 해당하는 곳에 위치
charater_y_pos = screen_height - charater_height # 화면 세로크기 가장 아래에 해당하는 위치



# 이동 할 좌표
to_x = 0
to_y = 0


#이동속도
charater_speed = 0.6


# 적 enemy 캐릭터
enemy = pygame.image.load("D:\python workspace\pygame_basic\enemy.png")
enemy_size = enemy.get_rect().size #이미지 크기 구해옴
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = (screen_width / 2) - (enemy_width / 2) #화면 가로의 절반 크기 해당하는 곳에 위치
enemy_y_pos = (screen_height / 2) - (enemy_height / 2) # 화면 세로크기 가장 아래에 해당하는 위치


# 폰트 정의
game_font = pygame.font.Font(None, 40)

#총 시간
total_time = 10

#시작 시간정보
start_ticks = pygame.time.get_ticks() # 시작 tick 을 받아옴





#이벤트 루프
running = True # 게임이 진행중인가? 
while running:
    dt = clock.tick(60) #초당 프레임 수 입니다.

    # print("fps : " + str(clock.get_fps())) 1초동안에 프레임 표시

    for event in pygame.event.get(): #어떤 이벤트가 발생?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생?
            running = False # 게임이 진행중이 아님

        if event.type == pygame.KEYDOWN: #키가 눌러졌는가?
            if event.key == pygame.K_LEFT:
                to_x -= charater_speed #to_x = to+x - 5
            elif event.key == pygame.K_RIGHT:
                to_x += charater_speed
            elif event.key == pygame.K_UP:
                to_y -= charater_speed
            elif event.key == pygame.K_DOWN:
                to_y += charater_speed

        if event.type == pygame.KEYUP: #때면 멈춤 
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    # 3. 게임 캐릭터 위치 정의
    charater_x_pos += to_x * dt
    charater_y_pos += to_y * dt

    #가로 경계값 처리
    if charater_x_pos < 0:
        charater_x_pos = 0
    elif charater_x_pos > screen_width - charater_width:
        charater_x_pos = screen_width - charater_width 

    #세로 경계값 처리
    if charater_y_pos < 0:
        charater_y_pos = 0
    elif charater_y_pos > screen_height - charater_height:
        charater_y_pos = screen_height - charater_height
    
    #충돌처리 를 위한 rect 정보 업데이트
    charater_rect = charater.get_rect()
    charater_rect.left = charater_x_pos
    charater_rect.top = charater_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌 체크
    if charater_rect.colliderect(enemy_rect):
        print("서준이는 죽은!")
        running = False
    
    
    screen.blit(background, (0, 0)) #배경 그리기
    screen.blit(charater, (charater_x_pos, charater_y_pos)) #캐릭터 그리기
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) #적 그리기




    # 타이머 집어 넣기
    #경과시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 
    #경과 시간을 1000으로 나눠서 초로 표시
    

    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255))
    # 출력할 글자, True, 글자 색상
    screen.blit(timer, (10, 10))

    #만약 시간이 0 이하면 게임 종료

    if total_time - elapsed_time <= 0:
        print ("타임아웃")
        running = False


    pygame.display.update() # 게임 화면 다시 그리기!

#잠시 대기
pygame.time.delay(2000) # 2초 대기
    
  
#종료
pygame.quit()
