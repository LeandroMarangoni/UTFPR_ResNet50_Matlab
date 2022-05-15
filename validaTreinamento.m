I = imread( "Sem título.jpg" );
I = imresize(I, [224 224]);
[YPred,probs] = classify(trainedNetwork_2,I);
imshow(I)
label = YPred;
if probs <= 0.8 | string(label) == "Não Reconhecido"  
    title("Não reconhecido")
else
    title(string(label) + ", " + num2str(100*max(probs),3) + "%")
end
