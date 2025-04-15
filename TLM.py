import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

#입력 데이터
L = np.array([5,10,20,40,80,160]) # L(um)
R_T = np.array([0.55,0.63,0.73,1.15,1.56,2.76])
W=200 #Width(um)

#Liner pitting
fit = np.polyfit(L,R_T,1)
slope = fit[0]
intercept = fit[1]

#계산
Rs = slope * W #Sheet resistance
Rc = intercept / 2 #Contact resistance
LT = (Rc*W)/Rs #Transfer length(um)
rho_c = Rc * (LT*W)

#x절편, y절편 계산
x_intercept = -intercept /slope #x절편(-2LT)
y_intercept = intercept #y절편(2Rc)

#외삽용 데이터 생성
L_extrapolated = np.linspace(-2 * abs(x_intercept), max(L), 500) #x 데이터 확장
R_T_extrapolated = slope * L_extrapolated + intercept #외삽된 y 데이터

#결과 출력
print(f"sheet resistance(Rs) : {Rs:.4f}")
print(f"contact resistance(Rc) : {Rc:.4f}")
print(f"transfer length(LT) : {LT:.4f}")
print(f"specific contact resistivity(pc) : {rho_c:.4f}")

#그래프 그리기
plt.figure(figsize=(8,6))
plt.plot(L,R_T,'ro',label = 'mesured data') # 측정 데이터
plt.plot(L_extrapolated,R_T_extrapolated,'b-',label = 'Linear Fid (Extrapolated)') #외삽된 선
plt.scatter(0,y_intercept,color='g',label=f'2Rc = {y_intercept:.4f}',zorder=5) # y 절편 점
plt.scatter(x_intercept,0,color='purple',label=f'-2LT = {x_intercept:.4f}',zorder=5) # x 절편 점
plt.axhline(y=0,color='k',linestyle='--',linewidth=0.8) # x-axis
plt.axhline(x=0,color='k',linestyle='--',linewidth=0.8) # y-axis
plt.xlabel('contact spacing L')
plt.ylabel('Total resistance R_T')
plt.title('Resistance Vs. contact spacing')
plt.legend
plt.grid(True)
plt.show