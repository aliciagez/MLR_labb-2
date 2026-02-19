# MLR_labb-2
Labb 2 maskininlärnings ramverk


Backround: 
Like last time i usw ubuntu with wsl in order to avoid windows since pytorch dont have wheel for the latets update. I use a script to check what kind of device and to see if cuda is avalible. 

Loading data: 
There was alot of good information on the dataset CIFAR-10 on the offical documentations on pytorch and so that was helpfull on how to load the data without physiclay put the data in the project 
which i almost did. i used the dataloader and torch vision to load the dataset. Using the dataloader allaowed me to not have to spell out the x and y and to customize the batches which will be need
later on in the experimetns. Apparenlty accorsing to chat gpt the dataloade is suppoes to the the convertion to floats and such atomaticly too. 

Model: 
I created a model with paramets as varibels so they can be change when 
experimenten with the model, bath size, hiddes layes and such. I did a base model in model.py what will be used in the experiment notebook 
with diffrent hyperparameters. I did a simpel model in order to keep it simpel for myself and i added a flatten function in the model it slef since chatgpt said it was 
better than doing the flattening in the dataset.py. The amount of data in the cifar-10 is 3 x 32 x 32 = 3072. I made the model an calleble object so i can use it to experiment. 
I added hidden layer at 128 as default for the first experiment since according to chatgpt it was a standars numer to start with. 

Train: 
For the traning i wanted to be able to change the hyperparamets as i experimented so i wanted to make the traning and the, model for that matter, to be calleble functions that can be reused. So i did the optermizes at ciritaions in one functiuon and the rest of the traning loop in anotherl. 

