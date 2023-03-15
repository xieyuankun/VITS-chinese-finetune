

# 导入必要的库
import os

# 原始文本文件路径
input_file = './input.txt'

# 存储音素文本的文件路径
output_file = 'output.txt'

# 定义音素转换函数
def chinese_cleaners1(text):
    from pypinyin import Style, pinyin
    phones = [phone[0] for phone in pinyin(text, style=Style.TONE3)]
    return ' '.join(phones)

# 读取原始文本文件并逐行转化为音素文本
with open(input_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    texts = [line.strip().split(' ', maxsplit=1)[1] for line in lines]
    # 遍历每一行文本并将其转化为音素文本
    with open(output_file, 'w', encoding='utf-8') as f_out:
        for i, line in enumerate(texts):
            # 调用音素转换函数
            phone_text = chinese_cleaners1(line.strip())
            print(phone_text)
            # 构建音频文件路径
            wav_path = f'./test/csmsc/{i+1}.wav'

            # 将音频文件路径和音素文本写入到输出文件中
            f_out.write(f'{wav_path}|{phone_text}\n')