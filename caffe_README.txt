Train on different data set:
1. Go to: /usr/lib/caffe/examples/imagenet

2. Add path to "create_imagenet.sh", change the name(!!!) of the output files as needed

3. Add path to "make_imagenet_mean.sh", change the name(!!!) of the output files as needed

4. Go to: "/usr/lib/caffe/models/bvlc_reference_caffenet"

5. Modify "solver.prototxt" and "train_val.prototxt" to change the net structure

6. Run the following cmd to train:
	"./build/tools/caffe train --solver=models/bvlc_reference_caffenet/solver.prototxt"

7. You are all set!
