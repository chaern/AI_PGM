"""
벽돌깨기 (Breakout) 게임
=========================
필요 라이브러리: pygame
설치 방법: pip install pygame

조작법:
- 좌/우 화살표 키 또는 마우스로 패들 이동
- 스페이스바로 게임 시작 / 재시작
- ESC로 종료
"""

import pygame
import random
import sys

# ----------------------------
# 초기 설정
# ----------------------------
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("벽돌깨기")

clock = pygame.time.Clock()
FPS = 60

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (10, 10, 15)
RED = (231, 76, 60)
ORANGE = (230, 126, 34)
YELLOW = (241, 196, 15)
GREEN = (46, 204, 113)
BLUE = (52, 152, 219)
PURPLE = (155, 89, 182)
GRAY = (149, 165, 166)

BRICK_COLORS = [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE]

font_large = pygame.font.SysFont("malgungothic", 48)
font_medium = pygame.font.SysFont("malgungothic", 32)
font_small = pygame.font.SysFont("malgungothic", 22)


# ----------------------------
# 패들 클래스
# ----------------------------
class Paddle:
    def __init__(self):
        self.width = 100
        self.height = 15
        self.x = SCREEN_WIDTH // 2 - self.width // 2
        self.y = SCREEN_HEIGHT - 40
        self.speed = 8
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def move(self, dx):
        self.rect.x += dx
        self.rect.x = max(0, min(SCREEN_WIDTH - self.width, self.rect.x))

    def set_x(self, x):
        self.rect.x = x - self.width // 2
        self.rect.x = max(0, min(SCREEN_WIDTH - self.width, self.rect.x))

    def draw(self, surface):
        pygame.draw.rect(surface, BLUE, self.rect, border_radius=6)
        pygame.draw.rect(surface, WHITE, self.rect, width=2, border_radius=6)


# ----------------------------
# 공 클래스
# ----------------------------
class Ball:
    def __init__(self, paddle):
        self.radius = 9
        self.paddle = paddle
        self.reset()

    def reset(self):
        self.x = self.paddle.rect.centerx
        self.y = self.paddle.rect.top - self.radius - 1
        self.speed = 5.5
        angle_choices = [-1, -0.7, -0.4, 0.4, 0.7, 1]
        self.dx = random.choice(angle_choices) * self.speed
        self.dy = -self.speed
        self.launched = False

    def update(self):
        if not self.launched:
            self.x = self.paddle.rect.centerx
            self.y = self.paddle.rect.top - self.radius - 1
            return

        self.x += self.dx
        self.y += self.dy

        # 벽 충돌
        if self.x - self.radius <= 0:
            self.x = self.radius
            self.dx *= -1
        elif self.x + self.radius >= SCREEN_WIDTH:
            self.x = SCREEN_WIDTH - self.radius
            self.dx *= -1

        if self.y - self.radius <= 0:
            self.y = self.radius
            self.dy *= -1

    def get_rect(self):
        return pygame.Rect(self.x - self.radius, self.y - self.radius,
                            self.radius * 2, self.radius * 2)

    def draw(self, surface):
        pygame.draw.circle(surface, WHITE, (int(self.x), int(self.y)), self.radius)


# ----------------------------
# 벽돌 클래스
# ----------------------------
class Brick:
    def __init__(self, x, y, width, height, color, points):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.points = points
        self.alive = True

    def draw(self, surface):
        if self.alive:
            pygame.draw.rect(surface, self.color, self.rect, border_radius=4)
            pygame.draw.rect(surface, BLACK, self.rect, width=2, border_radius=4)


def create_bricks():
    bricks = []
    rows = 6
    cols = 10
    padding = 6
    brick_width = (SCREEN_WIDTH - padding * (cols + 1)) // cols
    brick_height = 25
    top_offset = 60

    for row in range(rows):
        for col in range(cols):
            x = padding + col * (brick_width + padding)
            y = top_offset + row * (brick_height + padding)
            color = BRICK_COLORS[row % len(BRICK_COLORS)]
            points = (rows - row) * 10
            bricks.append(Brick(x, y, brick_width, brick_height, color, points))
    return bricks


# ----------------------------
# 게임 상태
# ----------------------------
class Game:
    def __init__(self):
        self.reset()

    def reset(self):
        self.paddle = Paddle()
        self.ball = Ball(self.paddle)
        self.bricks = create_bricks()
        self.score = 0
        self.lives = 3
        self.state = "ready"  # ready, playing, gameover, win

    def handle_collisions(self):
        ball_rect = self.ball.get_rect()

        # 패들 충돌
        if ball_rect.colliderect(self.paddle.rect) and self.ball.dy > 0:
            offset = (self.ball.x - self.paddle.rect.centerx) / (self.paddle.width / 2)
            offset = max(-1, min(1, offset))
            speed = (self.ball.dx ** 2 + self.ball.dy ** 2) ** 0.5
            self.ball.dx = offset * speed
            self.ball.dy = -abs(self.ball.dy)
            # 속도 보정 (최소 속도 유지)
            norm = (self.ball.dx ** 2 + self.ball.dy ** 2) ** 0.5
            if norm > 0:
                self.ball.dx = self.ball.dx / norm * speed
                self.ball.dy = self.ball.dy / norm * speed

        # 벽돌 충돌
        for brick in self.bricks:
            if brick.alive and ball_rect.colliderect(brick.rect):
                brick.alive = False
                self.score += brick.points

                # 충돌 방향 판단 (간단한 방식)
                overlap_left = ball_rect.right - brick.rect.left
                overlap_right = brick.rect.right - ball_rect.left
                overlap_top = ball_rect.bottom - brick.rect.top
                overlap_bottom = brick.rect.bottom - ball_rect.top

                min_overlap = min(overlap_left, overlap_right, overlap_top, overlap_bottom)
                if min_overlap in (overlap_left, overlap_right):
                    self.ball.dx *= -1
                else:
                    self.ball.dy *= -1
                break

        # 바닥에 떨어짐
        if self.ball.y - self.ball.radius > SCREEN_HEIGHT:
            self.lives -= 1
            if self.lives <= 0:
                self.state = "gameover"
            else:
                self.ball.reset()
                self.state = "ready"

        # 승리 조건
        if all(not b.alive for b in self.bricks):
            self.state = "win"

    def update(self):
        if self.state == "playing":
            self.ball.update()
            self.handle_collisions()
        elif self.state == "ready":
            self.ball.x = self.paddle.rect.centerx
            self.ball.y = self.paddle.rect.top - self.ball.radius - 1

    def draw(self, surface):
        surface.fill(BLACK)

        for brick in self.bricks:
            brick.draw(surface)

        self.paddle.draw(surface)
        self.ball.draw(surface)

        # 점수 및 목숨 표시
        score_text = font_small.render(f"점수: {self.score}", True, WHITE)
        surface.blit(score_text, (10, 10))

        lives_text = font_small.render(f"목숨: {self.lives}", True, WHITE)
        surface.blit(lives_text, (SCREEN_WIDTH - 110, 10))

        if self.state == "ready":
            msg = font_medium.render("스페이스바를 눌러 시작", True, YELLOW)
            surface.blit(msg, msg.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)))
        elif self.state == "gameover":
            msg = font_large.render("게임 오버", True, RED)
            sub = font_small.render("스페이스바를 눌러 재시작", True, WHITE)
            surface.blit(msg, msg.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 20)))
            surface.blit(sub, sub.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 30)))
        elif self.state == "win":
            msg = font_large.render("승리!", True, GREEN)
            sub = font_small.render("스페이스바를 눌러 재시작", True, WHITE)
            surface.blit(msg, msg.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 20)))
            surface.blit(sub, sub.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 30)))


# ----------------------------
# 메인 루프
# ----------------------------
def main():
    game = Game()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_SPACE:
                    if game.state == "ready":
                        game.state = "playing"
                        game.ball.launched = True
                    elif game.state in ("gameover", "win"):
                        game.reset()

        # 키보드 입력 (패들 이동)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            game.paddle.move(-game.paddle.speed)
        if keys[pygame.K_RIGHT]:
            game.paddle.move(game.paddle.speed)

        # 마우스로도 패들 이동 가능
        mouse_x, _ = pygame.mouse.get_pos()
        if pygame.mouse.get_focused():
            pass  # 마우스 이동은 원하면 아래 주석 해제
            # game.paddle.set_x(mouse_x)

        game.update()
        game.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
