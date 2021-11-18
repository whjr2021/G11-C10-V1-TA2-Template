# Import "pygame" module and initialize it
import pygame
pygame.init() 

# Create a game screen and set its title 
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Car Racing Game")

# Create a variable "carx" to track car position along x-axis and assign initial value a 140
carx = 140
# Create a variable "cary" to track car position along y-axis and assign initial value a 450
cary = 450
# TA2-Step 1: Create a variable "bgy" to track y position of the background and name it as "bgy". Assign the value 0.


# Game loop
carryOn = True
while carryOn:
    # Display the background image
    baImg_file = "road.png"
    bgImg = pygame.image.load(baImg_file).convert_alpha()
    bgImg_scaled = pygame.transform.smoothscale(bgImg,(650,600))
    screen.blit(bgImg_scaled,(0,0))
    
    # Update the position of yellow car image based on user input and then display it
    # Load the yellow car image and scale it
    yellow_car_file = "yellow_car.png"
    yellow_car = pygame.image.load(yellow_car_file).convert_alpha()
    yellow_car_scaled = pygame.transform.smoothscale(yellow_car,(230,150))
    
    # Check for the event type
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False              
    
        # Check for the user pressing Up, Down, Right, Left arrow keys and 
        # increment or decrement the "carx" and "cary" varaibles by 10 based on user input
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                cary -= 10
                # TA2-Step 2: Decrement "bgy" by 10 units

            if event.key == pygame.K_DOWN:
                cary += 10
                # TA2-Step 2: Increment "bgy" by 10 units

            if event.key == pygame.K_RIGHT:
                carx += 10
            if event.key == pygame.K_LEFT:
                carx -= 10
    
    # TA2-Step 3: Reset car and background positions
    # Check if "cary" is close to upper screen boundary at cary <= 20

        # Reset background's y location to zero

        # Reset car's y location to 450

        
    # Display yellow car image upon updating "carx" and "cary" variable values 
    screen.blit(yellow_car_scaled,(carx, cary))
           
    # Update the contents of the display
    pygame.display.flip()
# On the occurence of "pygame.QUIT" event close the game screen.
pygame.quit()