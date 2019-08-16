# image_classification
To start the training , run this command
python train_vgg.py --dataset dataset --model output/smallvggnet.model --label-bin output/smallvggnet_lb.pickle --plot output/smallvggnet_plot.png

To classify an image using our trained network, run this command
python predict.py --image usd.jpg --model output/smallvggnet.model --label-bin output/smallvggnet_lb.pickle --width 64 --height 64
