import imageio, os


GIF = []
file_dir = "output/chicago"
filenames = os.listdir(file_dir)
filenames = sorted(filenames)
for filename in filenames:
    GIF.append(imageio.imread(os.path.join(file_dir, filename)))
imageio.mimsave(os.path.join(file_dir, "result.gif"), GIF, duration=0.1)
