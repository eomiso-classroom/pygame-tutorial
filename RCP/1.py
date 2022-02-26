import pygame as pg

pg.init()
screen = pg.display.set_mode((600, 600))

background_img = pg.image.load("background.png")

rock = pg.image.load("rock.png")
rock = pg.transform.scale(rock, (150, 150))

scissors = pg.image.load("scissors.png")
scissors = pg.transform.scale(scissors, (150, 150))

paper = pg.image.load("paper.png")
paper = pg.transform.scale(paper, (150, 150))

# 화면에 이미지 그리기
screen.blit(background_img, background_img.get_rect())

running = True
while running:
    
    scissors_pos = screen.blit(scissors, (50, 100)) # 가위 객체
    rock_pos = screen.blit(rock, (200, 100)) # 바위 객체
    paper_pos = screen.blit(paper, (350, 100)) # 보 객체
    
    # 외부 이벤트 감지하기
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
            ### (1) 마우스로 가위 이미지를 클릭했을 때, "가위 클릭"을 출력해 주세요.
            if scissors_pos.collidepoint(pg.mouse.get_pos()):
                print("가위 클릭")
            
            
            ### (2) 마우스로 바위 이미지를 클릭했을 때, "바위 클릭"을 출력해 주세요.
            elif rock_pos.collidepoint(pg.mouse.get_pos()):
                print("바위 클릭")
            
            ### (3) 마우스로 보 이미지를 클릭했을 때, "보 클릭"을 출력해 주세요.
            elif paper_pos.collidepoint(pg.mouse.get_pos()):
                print("보 클릭")
            
            ### (4) 배경화면 이미지를 클릭했을 때, "배경화면 클릭"을 출력해 주세요.
            else:
                print("배경화면 클릭")
            
            
    pg.display.update()

