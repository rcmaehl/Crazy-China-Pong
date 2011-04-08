#!/usr/bin/env python
"""
    Copyright (C) 2011  Smart Viking (smartestviking@gmail.com)

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import sys, pygame
from pygame.locals import *
pygame.init() and pygame.display.set_caption('Crazy China Pong - 1.0.0.0 Beta 12')

def main():
    score = 0
    clock = pygame.time.Clock()

    size = width, height = 600,400
    screen = pygame.display.set_mode(size)
    gun = pygame.image.load("data/gun.png")
    bg = pygame.image.load("data/bg.png")
    guy = pygame.image.load("data/guy.png")
    guy2 = pygame.image.load("data/guy2.png")
    finished = pygame.image.load("data/finished.png")

    farmer = guy2
    gunh = 125.5
    guyh = 200
    guyw = 280
    east = 1
    guydirs = 0.2
    guyspeed = 0
    gunspeed = 4
    scorespeed = 0.01
    font = pygame.font.Font(None, 17)

    while 1:
        score += scorespeed
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                sys.exit()
        keystate = pygame.key.get_pressed()
        if gunh > 300  or gunh < 0:
            gunh = gunh-(4*(gunh/abs(gunh)))
        if keystate[pygame.K_UP]:
		gunh -= gunspeed
	if keystate[pygame.K_DOWN]:
		gunh += gunspeed
        if guyh < -10 or guyh > 370:
            guydirs = guydirs - (guydirs*2)
        guyh = guyh + guydirs
        if east:
            farmer = guy2
            guyw += guyspeed
            if guyw > 560:
                east = 0
        else:
            farmer = guy
            guyw -= guyspeed
            if guyw < 32 and guyh > gunh-40 and guyh < gunh+100 and guyw > 8:
                east = 1
                guydirs = guydirs- (gunh-(guyh+20)+50)/50.0
        if guyw < 0:
            screen.blit(finished,(0,0)) and pygame.display.update()
            while 2:
                for event in pygame.event.get():
                	if event.type == KEYDOWN and event.key == K_SPACE:
                        	main()
			if event.type == pygame.QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
				sys.exit()
        screen.blit(bg,(0,0))
        text = font.render("Score:  "+str(int(score))+"   "+"Speed: "+str(int(guyspeed)), True, (255, 255, 255), (159, 182, 205))
        screen.blit(text, (50,10))

        screen.blit(farmer,(guyw,guyh))
        screen.blit(gun,(30,gunh))

	pygame.display.update()
        clock.tick(100)

	if score < 1000:
		guyspeed = 2*score/60
		scorespeed = 0.02*(guyspeed/3)
		if 2*score/60 < 4 and 0.02*(guyspeed/3) < 0.04:
			guyspeed = 4
			scorespeed = 0.04
		if guyspeed >= 22:
			guyspeed = 22
main()
