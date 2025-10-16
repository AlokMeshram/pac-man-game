import pygame
import numpy as np
import os

# Initialize Pygame mixer
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)

# Create sounds directory
os.makedirs('sounds', exist_ok=True)

def create_sound_array(frequency, duration, sample_rate=22050):
    """Create a simple sound array"""
    n_samples = int(duration * sample_rate)
    buf = np.zeros((n_samples, 2), dtype=np.int16)
    max_sample = 2 ** (16 - 1) - 1
    
    for i in range(n_samples):
        t = float(i) / sample_rate
        # Create a sine wave with envelope
        value = int(max_sample * 0.3 * np.sin(2.0 * np.pi * frequency * t) * np.exp(-t * 5))
        buf[i][0] = value
        buf[i][1] = value
    
    return buf

def create_eat_ghost_sound():
    """Create sound for eating ghost - rising pitch"""
    sample_rate = 22050
    duration = 0.3
    n_samples = int(duration * sample_rate)
    buf = np.zeros((n_samples, 2), dtype=np.int16)
    max_sample = 2 ** (16 - 1) - 1
    
    for i in range(n_samples):
        t = float(i) / sample_rate
        # Rising frequency from 400 to 800 Hz
        freq = 400 + (400 * t / duration)
        value = int(max_sample * 0.3 * np.sin(2.0 * np.pi * freq * t) * np.exp(-t * 8))
        buf[i][0] = value
        buf[i][1] = value
    
    sound = pygame.sndarray.make_sound(buf)
    pygame.mixer.Sound.set_volume(sound, 0.5)
    return sound

def create_death_sound():
    """Create sound for pac-man death - falling pitch"""
    sample_rate = 22050
    duration = 0.5
    n_samples = int(duration * sample_rate)
    buf = np.zeros((n_samples, 2), dtype=np.int16)
    max_sample = 2 ** (16 - 1) - 1
    
    for i in range(n_samples):
        t = float(i) / sample_rate
        # Falling frequency from 600 to 200 Hz
        freq = 600 - (400 * t / duration)
        value = int(max_sample * 0.3 * np.sin(2.0 * np.pi * freq * t) * (1 - t / duration))
        buf[i][0] = value
        buf[i][1] = value
    
    sound = pygame.sndarray.make_sound(buf)
    pygame.mixer.Sound.set_volume(sound, 0.5)
    return sound

def create_power_pellet_sound():
    """Create sound for eating power pellet"""
    buf = create_sound_array(500, 0.15)
    sound = pygame.sndarray.make_sound(buf)
    pygame.mixer.Sound.set_volume(sound, 0.3)
    return sound

def create_eat_dot_sound():
    """Create sound for eating dots"""
    buf = create_sound_array(800, 0.05)
    sound = pygame.sndarray.make_sound(buf)
    pygame.mixer.Sound.set_volume(sound, 0.2)
    return sound

# Create all sounds and return them
print("Creating sound effects...")
sounds = {
    'eat_dot': create_eat_dot_sound(),
    'power_pellet': create_power_pellet_sound(),
    'eat_ghost': create_eat_ghost_sound(),
    'death': create_death_sound()
}
print("Sound effects created successfully!")

