{\rtf1\ansi\ansicpg936\cocoartf2870
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # ==========================================\
# Assignment 1: Python Basics\
# File: assignment_one_yourname.py\
# ==========================================\
\
# ------------------------------------------\
# 1. Simple Calculator\
# ------------------------------------------\
print("=== Task 1: Simple Calculator ===")\
\
# \uc0\u25552 \u31034 \u36755 \u20837 \u31532 \u19968 \u20010 \u25968 \u23383 \
num1 = float(input("Enter the first number: "))\
\
# \uc0\u25552 \u31034 \u36755 \u20837 \u31532 \u20108 \u20010 \u25968 \u23383 \
num2 = float(input("Enter the second number: "))\
\
# \uc0\u36873 \u25321 \u36816 \u31639 \u31526 \
operator = input("Choose an operator (+, -, *, /): ")\
\
# \uc0\u26681 \u25454 \u36816 \u31639 \u31526 \u36827 \u34892 \u35745 \u31639 \u24182 \u26174 \u31034 \u28165 \u26224 \u30340 \u32467 \u26524 \
if operator == '+':\
    result = num1 + num2\
    print(f"Result: \{num1\} + \{num2\} = \{result\}")\
elif operator == '-':\
    result = num1 - num2\
    print(f"Result: \{num1\} - \{num2\} = \{result\}")\
elif operator == '*':\
    result = num1 * num2\
    print(f"Result: \{num1\} * \{num2\} = \{result\}")\
elif operator == '/':\
    # \uc0\u38450 \u27490 \u38500 \u25968 \u20026  0 \u23548 \u33268 \u25253 \u38169 \
    if num2 == 0:\
        print("Error: Cannot divide by zero.")\
    else:\
        result = num1 / num2\
        print(f"Result: \{num1\} / \{num2\} = \{result\}")\
else:\
    print("Error: Invalid operator. Please choose +, -, *, or /.")\
\
\
# \uc0\u25171 \u21360 \u20998 \u21106 \u32447 \u65292 \u21306 \u20998 \u20004 \u20010 \u20219 \u21153 \
print("\\n" + "=" * 40 + "\\n")\
\
\
# ------------------------------------------\
# 2. QA Bot\
# ------------------------------------------\
print("=== Task 2: QA Bot ===")\
print("Bot: Hi! Ask me a question, or type 'exit' to quit.")\
\
# \uc0\u20351 \u29992 \u26080 \u38480 \u24490 \u29615 \u35753 \u26426 \u22120 \u20154 \u21487 \u20197 \u25345 \u32493 \u23545 \u35805 \
while True:\
    # \uc0\u25509 \u25910 \u29992 \u25143 \u38382 \u39064 \u24182 \u36716 \u20026 \u23567 \u20889 \u65292 \u26041 \u20415 \u21305 \u37197 \
    question = input("You: ").lower()\
\
    # \uc0\u36864 \u20986 \u26426 \u21046 \
    if question == 'exit':\
        print("Bot: Goodbye!")\
        break\
\
    # \uc0\u20351 \u29992  if / elif / else \u21305 \u37197 \u20851 \u38190 \u35789 \u65288 \u25903 \u25345 \u33267 \u23569  5 \u20010 \u65289 \
    if "hello" in question:\
        print("Bot: Hello! How can I help you today?")\
    elif "python" in question:\
        print("Bot: Python is a powerful and easy-to-learn programming language.")\
    elif "jetson" in question:\
        print("Bot: Jetson is a series of embedded computing boards from NVIDIA, great for AI projects.")\
    elif "ai" in question:\
        print("Bot: AI stands for Artificial Intelligence. It's everywhere these days!")\
    elif "name" in question:\
        print("Bot: I am a simple Python QA Bot built for Assignment 1.")\
    else:\
        print("Bot: Sorry, I don't understand. Try asking about: hello, python, jetson, ai, or name.")}