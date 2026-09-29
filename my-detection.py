import jetson_inference
import jetson_utils
from jetson_inference import detectNet
from jetson_utils import videoSource, videoOutput
net = detectNet("ssd-mobilenet-v2", threshold=0.5)
camera = videoSource("/dev/video0") # '/dev/video0' for V4L2


# 创建显示窗口
display = videoOutput("display://0") # 'my_video.mp4' for file

while display.IsStreaming():
	img = camera.Capture()
	if img is None: # 捕获超时
		continue

	# 进行检测
	detections = net.Detect(img)

	# 打印检测结果到终端，方便你记录数据！
	print(detections)

	# 渲染画面
	display.Render(img)
	display.SetStatus("Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))

