import pygame
import random

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Acid Rain")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

    #이미지
background = pygame.image.load(
    "C:\\Users\\82104\\OneDrive\\바탕 화면\\PythonWorkspace\\pygame_basic\\background.png"
)
character = pygame.image.load(
    "C:\\Users\\82104\\OneDrive\\바탕 화면\\PythonWorkspace\\pygame_basic\\character.png"
)
acid_rain = pygame.image.load(
    "C:\\Users\\82104\\OneDrive\\바탕 화면\\PythonWorkspace\\pygame_basic\\acid_rain.png"
)

    #캐릭터
character_rect = character.get_rect()
character_rect.centerx = screen_width // 2
character_rect.bottom = screen_height
character_speed = 10
to_x = 0

    #산성비
acid_rain_rect = acid_rain.get_rect()
acid_rain_width = acid_rain_rect.width

acid_rains = []
acid_rain_count = 3

for _ in range(acid_rain_count):
    acid_rains.append({
        "x": random.randint(0, screen_width - acid_rain_width),
        "y": random.randint(-300, 0),
        "speed": random.randint(7, 12)
    })


hit_count = 0
stage = 1
MAX_RAIN_COUNT = 7  #산성비 7개가 맥스

running = True
while running:
    dt = clock.tick(60)

    #이벤트 적용
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                to_x = -character_speed
            elif event.key == pygame.K_d:
                to_x = character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                to_x = 0

    #캐릭터 이동
    character_rect.x += to_x
    if character_rect.left < 0:
        character_rect.left = 0

    if character_rect.right > screen_width:
        character_rect.right = screen_width

    #산성비
    for rain in acid_rains:
        rain["y"] += rain["speed"]

        if rain["y"] > screen_height:
            rain["y"] = random.randint(-300, 0)
            rain["x"] = random.randint(0, screen_width - acid_rain_width)
            hit_count += 1

        rain_rect = acid_rain.get_rect(topleft=(rain["x"], rain["y"]))

        if character_rect.colliderect(rain_rect):       ##dict를 썼다길래 코드 전체를 5분 봄 rect인데 무지성으로 탭 눌러서 그런가바ㅅㅂ
            print("대머리가 되었다")
            running = False

    #단계 처리
    next_stage_hit = stage * 15

    if hit_count >= next_stage_hit:
        stage += 1

        # 1-5단계 : 개수 증가
        if stage <= 5:      #여기 왜 충돌처리 안먹힘; 자고일어나서 조금 만졋는데 됨ㄷㄷㄷㄷ 왜 되지
            acid_rains.append({
                "x": random.randint(0, screen_width - acid_rain_width),
                "y": random.randint(-300, 0),
                "speed": random.randint(9,13)
            })

        # 6단계 이후 :속도 증가
        else:
            for rain in acid_rains:
                rain["speed"] += 1

        # 갯수 제한
        if len(acid_rains) > MAX_RAIN_COUNT:
            acid_rains = acid_rains[:MAX_RAIN_COUNT]

        print(f"{stage}단계 진입")

    #그리기
    screen.blit(background, (0, 0))
    screen.blit(character, character_rect)

    for rain in acid_rains:
        screen.blit(acid_rain, (rain["x"], rain["y"]))

    # 단계 표시
    stage_text = font.render(f"STAGE {stage}", True, (0, 0, 0))
    screen.blit(stage_text, (10, 10))

    pygame.display.update()

pygame.quit()       #ㅅㅂ판정개같네ㅅㅂ!!!!!!!!11 5단계의 벽을 못넘겟다ㅁㅁ
