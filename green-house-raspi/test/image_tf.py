from device.camera.sprout_detect import sprout_detect

IMAGE_SEED = '/home/pi/green-house-control/test/img_seed.jpg'
IMAGE_SPROUT = '/home/pi/green-house-control/test/img_sprout.jpg'

def run():
    try:
        print(sprout_detect.detect(IMAGE_SEED))
        print(sprout_detect.detect(IMAGE_SPROUT))
    except Exception as e:
        print("Error")
        print(e)


if __name__ == '__main__':
    run()
