import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 300
CELL_SIZE = 20
MAZE_WIDTH = 30
MAZE_HEIGHT = 15

# Colors
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PINK = (255, 192, 203)
CYAN = (0, 255, 255)
ORANGE = (255, 165, 0)

# Simplified maze layout (1 = wall, 0 = empty, 2 = dot, 3 = power pellet)
MAZE = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,3,2,2,2,2,2,2,2,2,2,2,2,2,1,1,2,2,2,2,2,2,2,2,2,2,2,2,3,1],
    [1,2,1,1,1,2,1,1,1,1,1,1,2,2,1,1,2,2,1,1,1,1,1,1,2,1,1,1,2,1],
    [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
    [1,2,1,1,1,2,1,1,2,1,1,1,1,1,1,1,1,1,1,1,2,1,1,2,1,1,1,2,1,1],
    [1,2,2,2,2,2,1,1,2,2,2,2,2,1,1,1,1,2,2,2,2,2,1,1,2,2,2,2,2,1],
    [1,1,1,1,1,2,1,1,1,1,1,1,2,1,0,0,1,2,1,1,1,1,1,1,2,1,1,1,1,1],
    [1,2,2,2,2,2,2,2,2,2,2,2,2,1,0,0,1,2,2,2,2,2,2,2,2,2,2,2,2,1],
    [1,2,1,1,1,2,1,1,1,1,1,1,2,1,0,0,1,2,1,1,1,1,1,1,2,1,1,1,2,1],
    [1,2,2,2,2,2,1,1,2,2,2,2,2,1,1,1,1,2,2,2,2,2,1,1,2,2,2,2,2,1],
    [1,2,1,1,1,2,1,1,2,1,1,1,1,1,1,1,1,1,1,1,2,1,1,2,1,1,1,2,1,1],
    [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
    [1,2,1,1,1,2,1,1,1,1,1,1,2,2,1,1,2,2,1,1,1,1,1,1,2,1,1,1,2,1],
    [1,3,2,2,2,2,2,2,2,2,2,2,2,2,1,1,2,2,2,2,2,2,2,2,2,2,2,2,3,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

class PacMan:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
        self.direction = 0  # 0: right, 1: down, 2: left, 3: up
        self.mouth_open = True
        self.mouth_timer = 0
        self.speed = 0.15
        
    def update(self):
        # Animate mouth
        self.mouth_timer += 1
        if self.mouth_timer >= 8:
            self.mouth_open = not self.mouth_open
            self.mouth_timer = 0
    
    def can_move(self, x, y):
        # Check if the position is valid (not a wall and within bounds)
        grid_x = int(round(x))
        grid_y = int(round(y))
        
        if grid_x < 0 or grid_x >= MAZE_WIDTH or grid_y < 0 or grid_y >= MAZE_HEIGHT:
            return False
        
        return MAZE[grid_y][grid_x] != 1
    
    def move(self, dx, dy):
        new_x = self.x + dx
        new_y = self.y + dy
        
        # Check if the new position is valid
        if self.can_move(new_x, new_y):
            self.x = new_x
            self.y = new_y
            
            # Update direction for mouth animation
            if dx > 0:
                self.direction = 0  # right
            elif dx < 0:
                self.direction = 2  # left
            elif dy > 0:
                self.direction = 1  # down
            elif dy < 0:
                self.direction = 3  # up
            
            # Snap to grid when close to center
            if abs(self.x - round(self.x)) < 0.1:
                self.x = round(self.x)
            if abs(self.y - round(self.y)) < 0.1:
                self.y = round(self.y)
    
    def draw(self, screen):
        center_x = int(self.x * CELL_SIZE + CELL_SIZE // 2)
        center_y = int(self.y * CELL_SIZE + CELL_SIZE // 2)
        radius = CELL_SIZE // 2 - 2
        
        if self.mouth_open:
            # Draw Pac-Man with mouth open
            start_angle = 0
            end_angle = 0
            
            if self.direction == 0:  # right
                start_angle = math.pi / 6
                end_angle = -math.pi / 6
            elif self.direction == 1:  # down
                start_angle = math.pi / 6 + math.pi / 2
                end_angle = -math.pi / 6 + math.pi / 2
            elif self.direction == 2:  # left
                start_angle = math.pi / 6 + math.pi
                end_angle = -math.pi / 6 + math.pi
            elif self.direction == 3:  # up
                start_angle = math.pi / 6 - math.pi / 2
                end_angle = -math.pi / 6 - math.pi / 2
            
            # Draw the arc (Pac-Man with mouth)
            points = [(center_x, center_y)]
            for angle in [i * 0.1 for i in range(int(end_angle * 10), int(start_angle * 10) + 1)]:
                x = center_x + int(radius * math.cos(angle))
                y = center_y + int(radius * math.sin(angle))
                points.append((x, y))
            
            if len(points) > 2:
                pygame.draw.polygon(screen, YELLOW, points)
        else:
            # Draw full circle when mouth is closed
            pygame.draw.circle(screen, YELLOW, (center_x, center_y), radius)

class Ghost:
    def __init__(self, x, y, color):
        self.x = float(x)
        self.y = float(y)
        self.original_color = color
        self.color = color
        self.direction = 0  # 0: right, 1: down, 2: left, 3: up
        self.speed = 0.08
        self.vulnerable = False
        self.vulnerable_timer = 0
        self.move_timer = 0
        
    def update(self, pacman_x, pacman_y, maze):
        # Update vulnerability
        if self.vulnerable:
            self.vulnerable_timer -= 1
            if self.vulnerable_timer <= 0:
                self.vulnerable = False
                self.color = self.original_color
                self.speed = 0.08
            else:
                # Flash when vulnerability is about to end
                if self.vulnerable_timer < 120 and self.vulnerable_timer % 20 < 10:
                    self.color = WHITE
                else:
                    self.color = (0, 0, 150)  # Dark blue when vulnerable
        
        # Move every few frames (faster movement)
        self.move_timer += 1
        if self.move_timer >= 8:  # Move every 8 frames (faster)
            self.move_timer = 0
            self.ai_move(pacman_x, pacman_y, maze)
    
    def make_vulnerable(self):
        self.vulnerable = True
        self.vulnerable_timer = 300  # 5 seconds at 60 FPS
        self.color = (0, 0, 150)  # Dark blue
        self.speed = 0.04  # Slower when vulnerable
    
    def can_move(self, x, y, maze):
        grid_x = int(round(x))
        grid_y = int(round(y))
        
        if grid_x < 0 or grid_x >= MAZE_WIDTH or grid_y < 0 or grid_y >= MAZE_HEIGHT:
            return False
        
        # Allow movement in empty spaces (0) and dot spaces (2,3), block walls (1)
        return maze[grid_y][grid_x] != 1
    
    def ai_move(self, pacman_x, pacman_y, maze):
        import random
        
        # Possible directions: right, down, left, up
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        valid_moves = []
        
        # Find all valid moves
        for i, (dx, dy) in enumerate(directions):
            new_x = self.x + dx * self.speed * 5  # Check further ahead
            new_y = self.y + dy * self.speed * 5
            if self.can_move(new_x, new_y, maze):
                valid_moves.append((i, dx, dy))
        
        if not valid_moves:
            # If no moves available, try smaller steps
            for i, (dx, dy) in enumerate(directions):
                new_x = self.x + dx * 0.5
                new_y = self.y + dy * 0.5
                if self.can_move(new_x, new_y, maze):
                    valid_moves.append((i, dx, dy))
        
        if not valid_moves:
            return
        
        # Choose the best move
        chosen_move = None
        
        if self.vulnerable:
            # When vulnerable, try to avoid Pac-Man
            best_move = None
            max_distance = -1
            
            for direction, dx, dy in valid_moves:
                new_x = self.x + dx * self.speed * 3
                new_y = self.y + dy * self.speed * 3
                distance = abs(new_x - pacman_x) + abs(new_y - pacman_y)
                
                if distance > max_distance:
                    max_distance = distance
                    best_move = (direction, dx, dy)
            
            chosen_move = best_move
        else:
            # When not vulnerable, chase Pac-Man with some randomness
            if random.random() < 0.6:  # 60% chance to chase
                best_move = None
                min_distance = float('inf')
                
                for direction, dx, dy in valid_moves:
                    new_x = self.x + dx * self.speed * 3
                    new_y = self.y + dy * self.speed * 3
                    distance = abs(new_x - pacman_x) + abs(new_y - pacman_y)
                    
                    if distance < min_distance:
                        min_distance = distance
                        best_move = (direction, dx, dy)
                
                chosen_move = best_move
            else:
                # 40% chance to move randomly
                chosen_move = random.choice(valid_moves)
        
        # Execute the chosen move
        if chosen_move:
            direction, dx, dy = chosen_move
            self.direction = direction
            new_x = self.x + dx * self.speed
            new_y = self.y + dy * self.speed
            if self.can_move(new_x, new_y, maze):
                self.x = new_x
                self.y = new_y
            else:
                # If the chosen move fails, try any valid move
                for direction, dx, dy in valid_moves:
                    new_x = self.x + dx * self.speed
                    new_y = self.y + dy * self.speed
                    if self.can_move(new_x, new_y, maze):
                        self.x = new_x
                        self.y = new_y
                        self.direction = direction
                        break
    
    def draw(self, screen):
        center_x = int(self.x * CELL_SIZE + CELL_SIZE // 2)
        center_y = int(self.y * CELL_SIZE + CELL_SIZE // 2)
        radius = CELL_SIZE // 2 - 2
        
        # Draw ghost body (rectangle with rounded top)
        rect_height = radius + 5
        pygame.draw.rect(screen, self.color, 
                        (center_x - radius, center_y - radius, 
                         radius * 2, rect_height))
        pygame.draw.circle(screen, self.color, (center_x, center_y - radius // 2), radius)
        
        # Draw eyes
        eye_size = 3
        pygame.draw.circle(screen, WHITE, (center_x - 5, center_y - 5), eye_size)
        pygame.draw.circle(screen, WHITE, (center_x + 5, center_y - 5), eye_size)
        
        if self.vulnerable and not (self.vulnerable_timer < 120 and self.vulnerable_timer % 20 < 10):
            # When vulnerable, draw white pupils
            pygame.draw.circle(screen, WHITE, (center_x - 5, center_y - 5), 1)
            pygame.draw.circle(screen, WHITE, (center_x + 5, center_y - 5), 1)
        else:
            # Normal black pupils
            pygame.draw.circle(screen, BLACK, (center_x - 5, center_y - 5), 2)
            pygame.draw.circle(screen, BLACK, (center_x + 5, center_y - 5), 2)

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Pac-Man Game")
        self.clock = pygame.time.Clock()
        
        # Initialize game objects
        self.pacman = PacMan(1, 1)
        self.ghosts = [
            Ghost(12, 7, RED),
            Ghost(17, 7, PINK),
            Ghost(12, 8, CYAN),
            Ghost(17, 8, ORANGE)
        ]
        
        self.score = 0
        self.font = pygame.font.Font(None, 36)
        self.game_over = False
        self.power_mode = False
        self.power_timer = 0
        
        # Copy maze for dot management
        self.maze = [row[:] for row in MAZE]
    
    def handle_input(self):
        keys = pygame.key.get_pressed()
        
        # Only allow one direction at a time for more accurate movement
        if keys[pygame.K_RIGHT] and not any([keys[pygame.K_LEFT], keys[pygame.K_UP], keys[pygame.K_DOWN]]):
            self.pacman.move(self.pacman.speed, 0)
        elif keys[pygame.K_LEFT] and not any([keys[pygame.K_RIGHT], keys[pygame.K_UP], keys[pygame.K_DOWN]]):
            self.pacman.move(-self.pacman.speed, 0)
        elif keys[pygame.K_DOWN] and not any([keys[pygame.K_LEFT], keys[pygame.K_RIGHT], keys[pygame.K_UP]]):
            self.pacman.move(0, self.pacman.speed)
        elif keys[pygame.K_UP] and not any([keys[pygame.K_LEFT], keys[pygame.K_RIGHT], keys[pygame.K_DOWN]]):
            self.pacman.move(0, -self.pacman.speed)
    
    def check_dot_collection(self):
        pac_x = int(round(self.pacman.x))
        pac_y = int(round(self.pacman.y))
        
        if (0 <= pac_x < MAZE_WIDTH and 0 <= pac_y < MAZE_HEIGHT):
            # Check if Pac-Man is close enough to the center of the cell
            if (abs(self.pacman.x - pac_x) < 0.3 and abs(self.pacman.y - pac_y) < 0.3):
                if self.maze[pac_y][pac_x] == 2:  # Regular dot
                    self.maze[pac_y][pac_x] = 0
                    self.score += 10
                elif self.maze[pac_y][pac_x] == 3:  # Power pellet
                    self.maze[pac_y][pac_x] = 0
                    self.score += 50
                    self.activate_power_mode()
    
    def activate_power_mode(self):
        self.power_mode = True
        self.power_timer = 300  # 5 seconds at 60 FPS
        for ghost in self.ghosts:
            ghost.make_vulnerable()
    
    def check_ghost_collisions(self):
        pac_x = self.pacman.x
        pac_y = self.pacman.y
        
        for ghost in self.ghosts:
            distance = abs(pac_x - ghost.x) + abs(pac_y - ghost.y)
            if distance < 0.5:  # Collision detected
                if ghost.vulnerable:
                    # Eat the ghost
                    self.score += 200
                    # Reset ghost to main corridor
                    ghost.x = 14.5
                    ghost.y = 7.0
                    ghost.vulnerable = False
                    ghost.color = ghost.original_color
                    ghost.speed = 0.08
                else:
                    # Game over
                    self.game_over = True
                    return
    
    def update_power_mode(self):
        if self.power_mode:
            self.power_timer -= 1
            if self.power_timer <= 0:
                self.power_mode = False
    
    def draw_maze(self):
        for y in range(len(self.maze)):
            for x in range(len(self.maze[y])):
                rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                
                if self.maze[y][x] == 1:  # Wall
                    pygame.draw.rect(self.screen, BLUE, rect)
                elif self.maze[y][x] == 2:  # Dot
                    center_x = x * CELL_SIZE + CELL_SIZE // 2
                    center_y = y * CELL_SIZE + CELL_SIZE // 2
                    pygame.draw.circle(self.screen, WHITE, (center_x, center_y), 3)
                elif self.maze[y][x] == 3:  # Power pellet
                    center_x = x * CELL_SIZE + CELL_SIZE // 2
                    center_y = y * CELL_SIZE + CELL_SIZE // 2
                    pygame.draw.circle(self.screen, YELLOW, (center_x, center_y), 8)
    
    def draw_ui(self):
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (10, 10))
        
        # Power mode indicator
        if self.power_mode:
            power_text = pygame.font.Font(None, 24).render(f"POWER MODE: {self.power_timer // 60 + 1}s", True, YELLOW)
            self.screen.blit(power_text, (10, 40))
        
        # Game over screen
        if self.game_over:
            game_over_text = self.font.render("GAME OVER!", True, RED)
            restart_text = pygame.font.Font(None, 24).render("Press R to restart or ESC to quit", True, WHITE)
            self.screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 80, SCREEN_HEIGHT // 2 - 20))
            self.screen.blit(restart_text, (SCREEN_WIDTH // 2 - 120, SCREEN_HEIGHT // 2 + 10))
        
        # Instructions
        instructions = [
            "Arrow keys to move",
            "Eat dots and power pellets!",
            "Avoid ghosts (or eat them!)"
        ]
        
        for i, instruction in enumerate(instructions):
            text = pygame.font.Font(None, 20).render(instruction, True, WHITE)
            self.screen.blit(text, (SCREEN_WIDTH - 180, 10 + i * 22))
    
    def restart_game(self):
        self.pacman = PacMan(1, 1)
        self.ghosts = [
            Ghost(12, 7, RED),
            Ghost(17, 7, PINK),
            Ghost(12, 8, CYAN),
            Ghost(17, 8, ORANGE)
        ]
        self.score = 0
        self.game_over = False
        self.power_mode = False
        self.power_timer = 0
        self.maze = [row[:] for row in MAZE]
    
    def run(self):
        running = True
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if self.game_over:
                        if event.key == pygame.K_r:
                            self.restart_game()
                        elif event.key == pygame.K_ESCAPE:
                            running = False
            
            if not self.game_over:
                # Handle input
                self.handle_input()
                
                # Update game objects
                self.pacman.update()
                self.check_dot_collection()
                self.update_power_mode()
                
                # Update ghosts with AI
                for ghost in self.ghosts:
                    ghost.update(self.pacman.x, self.pacman.y, self.maze)
                
                # Check collisions
                self.check_ghost_collisions()
            
            # Draw everything
            self.screen.fill(BLACK)
            self.draw_maze()
            
            # Draw game objects
            if not self.game_over:
                self.pacman.draw(self.screen)
            for ghost in self.ghosts:
                ghost.draw(self.screen)
            
            self.draw_ui()
            
            pygame.display.flip()
            self.clock.tick(60)
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()