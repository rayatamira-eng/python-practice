import math
import pygame

# ---------------- Salary program ----------------
Basic_Salary = 32000
Bonus = 4500
Allowance = 2000
Tax_deduction = 3200
Insurance_deduction = 800
Loan_deduction = 1500
Gross_Salary = Basic_Salary + Bonus + Allowance
Total_deduction = Tax_deduction + Insurance_deduction + Loan_deduction
Net_Salary = Gross_Salary - Total_deduction
Savings = 10000
Remaining_Salary = Net_Salary - Savings

print("••••••••••••••••••••••••••••••••")
print("Basic_Salary=", Basic_Salary)
print("Bonus=", Bonus)
print("Allowance=", Allowance)
print("Tax_deduction=", Tax_deduction)
print("Insurance_deduction=", Insurance_deduction)
print("Loan_deduction=", Loan_deduction)
print("Gross_Salary=", Gross_Salary)
print("Total_deduction=", Total_deduction)
print("Net_Salary=", Net_Salary)
print("Savings=", Savings)
print("Remaining_Salary=", Remaining_Salary)
print("•••••••••••••••••••••••••••••••")

# ---------------- Rotating "Love You" heart ----------------
pygame.init()
W, H = 800, 800
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("heart")
clock = pygame.time.Clock()

STEP = 6                      # rotation step in degrees (pre-rendered for speed)
ANGLES = 360 // STEP
# (scale, font size, color) -> outer big heart to small inner hearts
LAYERS = [
    (21, 11, (255, 200, 40)),   # layer 1: golden yellow
    (14, 9, (255, 215, 0)),     # layer 2: golden yellow
    (7, 8, (139, 90, 43)),      # layer 3: brown
]


def heart_point(t, scale):
    x = 16 * math.sin(t) ** 3
    y = 13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)
    return W / 2 + x * scale, H / 2 - y * scale - 20


# Pre-render the rotated text for each layer
layer_surfaces = []
for scale, size, color in LAYERS:
    font = pygame.font.SysFont("arial", size, bold=True)
    base = font.render("LOVE YOU", True, color)
    layer_surfaces.append([pygame.transform.rotate(base, a * STEP) for a in range(ANGLES)])

frame = 0
running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    for li, (scale, size, color) in enumerate(LAYERS):
        for i in range(170):
            t = i / 170 * 2 * math.pi
            x, y = heart_point(t, scale)
            # dynamic rotation: each text spins; alternate layers spin opposite ways
            direction = 1 if li % 2 == 0 else -1
            idx = (frame * direction) % ANGLES
            surf = layer_surfaces[li][idx]
            screen.blit(surf, surf.get_rect(center=(x, y)))

    pygame.display.flip()
    frame += 1
    clock.tick(24)

pygame.quit()
