N = int(input())
S = str(input())
flg = "Takahashi"
 
for i in range(0, len(S)):
  
  if(S[i] == "0"):
    if(flg == "Takahashi"):
       flg = "Aoki"
    elif(flg == "Aoki"):
       flg = "Takahashi"
  
  elif(S[i] == "1"):
    break