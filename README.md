
# This code is slightly modified on the [wac81/vits_chinese](https://github.com/wac81/vits_chinese)
## Inference from biaobei

1. You can get pre-trained model and put the G in ./logs/woman_csmsc/G*.pth
2. `python infer.py`

## Retrain a basic model
1. Copy **16000hz** biaobei datasets to ./test/csmsc
2. You can switch english or chinese by modify `chinese_mode = True`
in ./text/__init__.py
2. Prepare the text like ./test/woman_csmsc.txt.2.cleaned.
3. Run  `python3 train.py -c configs/woman_csmsc.json -m woman_csmsc`

## Finetune
If you need a pre-trained model, please download it from [Baidu Cloud Drive](https://pan.baidu.com/s/1xUz5TEi5aBiIhbh0gXTiSw?pwd=VITS) with the password 'VITS'. 
I provided a fine-tuned pre-trained model for someone, which can be found in the download link XXXG_40000.pth. Please note that if fine-tuning, both G and D checkpoints are required. Although the loss has decreased from 100k to 160k in G checkpoints, I personally think there is not much difference in sound quality.

The fine-tuning steps are as follows:

1. Please put the G and D checkpoints in ./logs/woman_csmsc. Both 100k and 160k checkpoints are acceptable.

2. Prepare your fine-tuning dataset, which can be prepared using previous mockingbird methods. Prepare a good text file similar to ./input.txt.
3. Convert input.txt to phonemes in the style of output.txt using txt2phoneme.
4. Put the audio files in ./test/csmsc/ and copy the contents of output.txt to ./test/woman_csmsc.txt.2.cleaned.
5. Run`python3 train.py -c configs/woman_csmsc.json -m woman_csmsc`to start fine-tuning.












