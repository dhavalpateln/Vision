import cv2
import numpy

class ImageProcessor:

	def __init__(self, path, type):
		self.path = path
		print("in class")
		if type == "video":
			self.videoProcess()
		else:
			self.imageProcess()
			
	def imageProcess(self):
		print("in image")
		return
	
	def videoProcess(self):
		print("in video")
		cap = cv2.VideoCapture(self.path)

		while(cap.isOpened()):
			ret, frame = cap.read()

			gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
			cv2.imshow('original',frame)
			cv2.imshow('frame',gray)
			cv2.imshow('oCanny', self.cannyEdge(frame))
			cv2.imshow('gCanny', self.cannyEdge(gray))
			if cv2.waitKey(1) & 0xFF == ord('q'):
				break

		cap.release()
		cv2.destroyAllWindows()
	
	def cannyEdge(self, frame):
		edge = cv2.Canny(frame, 100, 100)
		return edge
def main():
	start = ImageProcessor('C:\\Users\\Dhaval\\Documents\\GitHub\\Vision\\asd.avi', "video")
	
if __name__ == "__main__":
	main()