text = "X-DSPAM-Confidence:    0.8475"
x = text.find("0")
code = float(text[x : ])
print(code)
