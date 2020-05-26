#import re

text = "X-DSPAM-Confidence:    0.8475";

index = text.find(":")
num_text = text[index+1:]
num = float(num_text.lstrip())
print(num)
