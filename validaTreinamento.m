I = imread( "images (1).jfif" );
I = imresize(I, [224 224]);
[YPred,probs] = classify(trainedNetwork_3,I);
imshow(I)
label = YPred;
title(string(label) + ", " + num2str(100*max(probs),3) + "%")