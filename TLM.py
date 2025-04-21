import numpy as np
import matplotlib.pyplot as plt

# 입력 데이터
L = np.array([5*1e-6, 10*1e-6, 20*1e-6, 40*1e-6, 80*1e-6, 160*1e-6])  # L (μm)
R_T = np.array([0.55, 0.63, 0.73, 1.15, 1.56, 2.76])  # Total resistance (Ω)
W = 200*1e-6  # width (μm)

# 선형 피팅
fit = np.polyfit(L, R_T, 1)
slope = fit[0]
intercept = fit[1]

# 계산
Rs = slope * W  # Sheet resistance (Ω/sq)
Rc = intercept / 2  # Contact resistance (Ω)
LT = (Rc*W)/Rs  # Transfer length (μm)
rho_c = (Rc * (LT *W))*1e4  # Specific contact resistivity (Ω·cm²)

# x-절편 및 y-절편 계산
x_intercept = -intercept / slope  # x-절편 (-2LT)
y_intercept = intercept  # y-절편 (2Rc)

# 외삽용 데이터 생성
L_extrapolated = np.linspace(-2 * abs(x_intercept), max(L), 500)  # x 데이터 확장
R_T_extrapolated = slope * L_extrapolated + intercept  # 외삽된 y 데이터

# 결과 출력(Rs,Rc,LT,pc 값)
print(f"Sheet Resistance (Rs): {Rs:.4f} Ω/sq")
print(f"Contact Resistance (Rc): {Rc:.4f} Ω")
print(f"Transfer Length (LT): {LT:.4e} m ")
print(f"Specific Contact Resistivity (ρc): {rho_c:.4e} Ω·cm²")


# 그래프 그리기
plt.figure(figsize=(8, 6))
plt.plot(L, R_T, 'ro', label='Measured Data')  # 측정 데이터
plt.plot(L_extrapolated, R_T_extrapolated, 'b--', label='Linear Fit (Extrapolated)')  # 외삽된 선
plt.scatter(0, y_intercept, color='g', label=f'2Rc = {y_intercept:.4f} Ω', zorder=5)  # y-절편 점
plt.scatter(x_intercept, 0, color='purple', label=f'-2LT = {x_intercept:.4e} ', zorder=5)  # x-절편 점
plt.axhline(y=0, color='k', linestyle='-', linewidth=0.8)  # x-axis
plt.axvline(x=0, color='k', linestyle='-', linewidth=0.8)  # y-axis
plt.xlabel('Length L (m)')
plt.ylabel('Total Resistance R_T (Ω)')
plt.title('Resistance vs. Length')
plt.legend()
plt.grid(True)
plt.show()