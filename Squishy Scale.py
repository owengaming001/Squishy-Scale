#Loads pygame
#If it can't, it will attempt to install pygame for you
try:
	import pygame
except:
	from os import system
	system("pip install pygame")
	import pygame

#Imports the os.walk function for file scraping
from os import walk

#Scrapes everything in the "Input" folder
Files = []
for (dirpath, dirnames, filenames) in walk("Input"):
	Files.extend(filenames)
	break

#Keeps only the ".png" files
Files=[File for File in Files if File.endswith(".png")]

#Load the "Pixel" and "Glow" images
PixelImage=pygame.image.load("Pixel.png")
GlowImage=pygame.image.load("Glow.png")

#Does the actual upscaling
def Upscale(Surface):
	#Makes a new surface for the upscale to be put onto
	BigSurface=pygame.Surface((Surface.get_width()*PixelImage.get_width(),Surface.get_height()*PixelImage.get_height()))

	#Pixel Pass
	#Iterates over every pixel in the source image, and adds the "Pixel" image to the big image
	for x in range(Surface.get_width()):
		for y in range(Surface.get_height()):
			X=x*PixelImage.get_width()
			Y=y*PixelImage.get_height()
			PixelImage2=PixelImage.copy()
			PixelImage2.fill(Surface.get_at((x,y)))
			PixelImage2.blit(PixelImage,(0,0),special_flags=pygame.BLEND_MULT)
			BigSurface.blit(PixelImage2,(X,Y))

	#Calculates the offset for the glow
	Offset=[GlowImage.get_width()-PixelImage.get_width(),GlowImage.get_height()-PixelImage.get_height()]
	Offset=[(Offset[0]/2),int(Offset[1]/2)]

	#Glow Pass
	#Adds the glow for each pixel
	for x in range(Surface.get_width()):
		for y in range(Surface.get_height()):
			X=x*PixelImage.get_width()
			Y=y*PixelImage.get_height()
			PixelImage2=GlowImage.copy()
			PixelImage2.fill(Surface.get_at((x,y)))
			PixelImage2.blit(GlowImage,(0,0),special_flags=pygame.BLEND_MULT)
			BigSurface.blit(PixelImage2,(X-6,Y-6),special_flags=pygame.BLEND_ADD)

	#Function returns the upscaled image
	return BigSurface

#Takes a filename, opens it from the "Input" Folder and saves it to the "Output" folder
def LoadScaleSave(Filename):
	#Loads the image
	Image=pygame.image.load(f"Input/{Filename}")

	#Upscales the image
	Image=Upscale(Image)

	#Saves the image
	pygame.image.save(Image,f"Output/{Filename}")

#If this file is being run directly, then convert all the files
if __name__=="__main__":
	for File in Files:
		LoadScaleSave(File)