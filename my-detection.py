import jetson.inference
import jetson.utils

net = jetson.inference.detectNet("ssd-mobilenet-v2", threshold=0.5)
camera = jetson.utils.videoSource("/home/nvidia/jetson-inference/examples/detect.jpeg") 
display = jetson.utils.videoOutput("display://0")
while display.IsStreaming():
	img = camera.Capture()
	if img is None:
		continue
	detections = net.Detect(img)
	print(detections)
	display.Render(img)
	display.SetStatus("Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))
