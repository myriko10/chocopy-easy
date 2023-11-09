import pygame
import main

IMAGEDICT = {'bird': pygame.image.load('../../images/bird.png'),
			'calrun1': pygame.image.load('../../images/callot_horse_run1.png'),
			'calrun1': pygame.image.load('../../images/callot_horse_run2.png'),
			'cloud': pygame.image.load('../../images/cloud.png'),
			'red': pygame.image.load('../../images/flower_red.png'),
	    	'white': pygame.image.load('../../images/flower_white.png'),
	    	'yellow': pygame.image.load('../../images/flower_yellow.png'),
			'home': pygame.image.load('../../images/home.png'),
			'run1': pygame.image.load('../../images/horse_run1.png'),
	    	'run2': pygame.image.load('../../images/horse_run2.png'),
			'smile': pygame.image.load('../../images/horse_smile.png'),
			'stop': pygame.image.load('../../images/horse_stop.png'),
			'walk1': pygame.image.load('../../images/horse_walk1.png'),
			'walk2': pygame.image.load('../../images/horse_walk2.png'),
	    	'mole': pygame.image.load('../../images/mole.png'),
	    	'title': pygame.image.load('../../images/title_horse_goes_home.png'),
	    	'town': pygame.image.load('../../images/town.png'),
	    	#'crun1R': pygame.transform.scale(pygame.image.load('images/callot_horse_run1.png'), (int(main.WIDTH*0.8), int(main.HEIGHT*0.8))),
	    	#'crun2R': pygame.transform.scale(pygame.image.load('images/callot_horse_run2.png'), (int(main.WIDTH*0.8), int(main.HEIGHT*0.8)))
	    		}
	#IMAGEDICT['crun1L'] = pygame.transform.flip(IMAGEDICT['crun1R'], True, False)
	#IMAGEDICT['crun2L'] = pygame.transform.flip(IMAGEDICT['crun2R'], True, False)