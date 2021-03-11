import cv2
from PIL import Image
import numpy as np
import os
import paddlehub as hub
from moviepy.editor import *
from tqdm import tqdm

# Config
# 原始视频地址
original_video_path = './1.mp4'
# 提取视频图像的存放地址
original_video_img_path = './original_video_img/'
# 合成视频存放地址
img2video_path = './2.mp4'
# 添加声音后的视频最终输出地址
output_video_path = './3.mp4'

# 从视频提取图片
def video2img(video_path, out_path):
    cap = cv2.VideoCapture(video_path)
    i=1
    while True:
        ret, frame = cap.read()
        if frame is None:
            break
        else:
            cv2.imwrite(out_path + str(i) + ".jpg", frame)
            i+=1
    return


# 把图片转动漫并合成视频
def ani2video(img_path, org_video_path, out_path, model):
    # 获取图片总数
    file_list = os.listdir(img_path)
    img_num = len(file_list)

    # 查看原始视频的参数
    cap = cv2.VideoCapture(org_video_path)
    ret, frame = cap.read()
    # 任选一张图片查看高度和宽度
    result = model.style_transfer(images=[cv2.imread(os.path.join(img_path,file_list[0]))])
    height = result[0].shape[0]
    width = result[0].shape[1]

    fps = cap.get(cv2.CAP_PROP_FPS)  # 返回视频的fps--帧率

    # 把参数用到我们要创建的视频上
    video = cv2.VideoWriter(out_path, cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), fps, (width, height))  # 创建视频流对象
    """
    参数1 即将保存的文件路径
    参数2 VideoWriter_fourcc为视频编解码器 cv2.VideoWriter_fourcc('m', 'p', '4', 'v') 文件名后缀为.mp4
    参数3 为帧播放速率
    参数4 (width,height)为视频帧大小
    """
    for i in tqdm(range(img_num)):
        f_name = str(i + 1) + '.jpg'
        item = os.path.join(img_path, f_name)
        result = model.style_transfer(images=[cv2.imread(item)]) # 转换动漫风格
        video.write(result[0])  # 把图片写进视频
    video.release()  # 释放

# 从原始视频上提取声音合成到新生成的视频上
def sound2video(org_video_path, new_video_path, out_video_path):
    # 读取原始视频
    video_o = VideoFileClip(org_video_path)
    # 获取原始视频的音频部分
    audio_o = video_o.audio

    # 读取新生成视频
    video_clip = VideoFileClip(new_video_path)
    # 指向新生成视频的音频部分
    video_clip2 = video_clip.set_audio(audio_o)
    # 修改音频部分并输出最终视频
    video_clip2.write_videofile(out_video_path)

# 第一步：视频->图像
if not os.path.exists(original_video_img_path):
    os.mkdir(original_video_img_path)
video2img(video_path=original_video_path, out_path=original_video_img_path)


# 第二步：转换为动漫效果并合成视频

# 根据自己喜好选择风格：
## 今敏:'animegan_v2_paprika_98'
## 新海诚:'animegan_v2_shinkai_53'
## 宫崎骏:'animegan_v2_hayao_99'
model = hub.Module(name='animegan_v2_hayao_99', use_gpu=True) 
ani2video(img_path=original_video_img_path, org_video_path=original_video_path, out_path=img2video_path, model=model)


# 第三步：加上原始音频
if not os.path.exists(output_video_path):
    sound2video(org_video_path=original_video_path, new_video_path=img2video_path, out_video_path=output_video_path)
else:
    print('最终视频已存在，请查看输出路径')
