# Variables for wave animation
wave_offset = 0
wave_speed = 2

bird_x = 0
bird_y = 100
bird_speed = 3

def setup():
    size(800, 600)

def draw():
    global wave_offset, bird_x

    background(135, 206, 235) 
    
  
    fill(255, 204, 0)  # Yellow color
    noStroke()
    ellipse(100, 100, 80, 80)  # Sun
    
  
    fill(0, 102, 204)  # Ocean color
    rect(0, height / 2, width, height / 2)  # Ocean
    
  
    fill(194, 178, 128)  # Sand color
    rect(0, height / 2 + 50, width, height / 2 - 50)  # Sand
    
   
    draw_waves(wave_offset)


    wave_offset += wave_speed
    if wave_offset > width:  # Reset offset when it goes off screen
        wave_offset = 0
   
    draw_bird(bird_x, bird_y)

   
    bird_x += bird_speed
    if bird_x > width:  
        bird_x = -50 

def draw_waves(offset):
    fill(255)  
    noStroke()
    for i in range(0, width, 40):
        
        ellipse(i + offset, height / 2 + 50, 60, 20)  # Draw wave

def draw_bird(x, y):
    fill(0)  
    ellipse(x, y, 20, 10) 
    triangle(x - 10, y, x, y - 10, x, y + 10)
